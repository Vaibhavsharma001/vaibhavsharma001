import os
import json
import math
import urllib.request
from datetime import datetime, timedelta, timezone
from collections import defaultdict

USERNAME = "vaibhavsharma001"
TOKEN = os.environ["GH_TOKEN"]

# Last 52 weeks, starting on a Monday
today = datetime.now(timezone.utc).date()
current_monday = today - timedelta(days=today.weekday())
start_date = current_monday - timedelta(weeks=51)

query = """
query($login: String!, $from: DateTime!, $to: DateTime!) {
  user(login: $login) {
    contributionsCollection(from: $from, to: $to) {
      contributionCalendar {
        weeks {
          contributionDays {
            date
            contributionCount
          }
        }
      }
    }
  }
}
"""

variables = {
    "login": USERNAME,
    "from": f"{start_date}T00:00:00Z",
    "to": f"{today}T23:59:59Z"
}

payload = json.dumps({
    "query": query,
    "variables": variables
}).encode("utf-8")

request = urllib.request.Request(
    "https://api.github.com/graphql",
    data=payload,
    headers={
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }
)

with urllib.request.urlopen(request) as response:
    result = json.loads(response.read().decode("utf-8"))

if result.get("errors"):
    raise RuntimeError(result["errors"])

user = result.get("data", {}).get("user")
if not user:
    raise RuntimeError("GitHub user not found.")

weeks = user["contributionsCollection"]["contributionCalendar"]["weeks"]

weekly_counts = defaultdict(int)

for week in weeks:
    for day in week["contributionDays"]:
        date = datetime.strptime(day["date"], "%Y-%m-%d").date()
        monday = date - timedelta(days=date.weekday())
        weekly_counts[monday] += day["contributionCount"]

dates = [start_date + timedelta(weeks=i) for i in range(52)]
values = [weekly_counts[d] for d in dates]

# SVG dimensions
WIDTH, HEIGHT = 900, 260
LEFT, RIGHT = 65, 25
TOP, BOTTOM = 25, 45
PLOT_WIDTH = WIDTH - LEFT - RIGHT
PLOT_HEIGHT = HEIGHT - TOP - BOTTOM

maximum = max(values) if values else 0
step = max(1, math.ceil(maximum / 4))
y_max = step * 4

def x_pos(index):
    return LEFT + index * PLOT_WIDTH / 51

def y_pos(value):
    return TOP + PLOT_HEIGHT - (value / y_max) * PLOT_HEIGHT

points = [(x_pos(i), y_pos(v)) for i, v in enumerate(values)]

# Smooth curve using quadratic segments
path = f"M {points[0][0]:.2f} {points[0][1]:.2f}"
for i in range(1, len(points)):
    x1, y1 = points[i - 1]
    x2, y2 = points[i]
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    path += f" Q {x1:.2f} {y1:.2f} {mx:.2f} {my:.2f}"
path += f" T {points[-1][0]:.2f} {points[-1][1]:.2f}"

area_path = (
    path
    + f" L {points[-1][0]:.2f} {TOP + PLOT_HEIGHT}"
    + f" L {points[0][0]:.2f} {TOP + PLOT_HEIGHT} Z"
)

# Horizontal grid and Y-axis numbers
grid = []
for tick in range(5):
    value = tick * step
    y = y_pos(value)
    grid.append(
        f'<line x1="{LEFT}" y1="{y:.2f}" x2="{WIDTH-RIGHT}" '
        f'y2="{y:.2f}" stroke="#21262d"/>'
    )
    grid.append(
        f'<text x="{LEFT-12}" y="{y+4:.2f}" text-anchor="end" '
        f'fill="#8b949e" font-size="11">{value}</text>'
    )

# Month labels along the X-axis
months = []
for index in [0, 13, 26, 39, 51]:
    label = dates[index].strftime("%b")
    months.append(
        f'<text x="{x_pos(index):.2f}" y="{HEIGHT-15}" '
        f'text-anchor="middle" fill="#8b949e" font-size="11">{label}</text>'
    )

# Small dots on the line
dots = []
for index, (x, y) in enumerate(points):
    dots.append(
        f'<circle cx="{x:.2f}" cy="{y:.2f}" r="2.5" '
        f'fill="#39d353"><title>{dates[index]}: {values[index]} contributions</title></circle>'
    )

svg = f"""<svg xmlns="http://www.w3.org/2000/svg"
width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">
<rect width="100%" height="100%" rx="12" fill="#0d1117"/>
{''.join(grid)}
<path d="{area_path}" fill="#39d353" opacity="0.10"/>
<path d="{path}" fill="none" stroke="#39d353"
stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
{''.join(dots)}
{''.join(months)}
</svg>
"""

with open("contribution-graph.svg", "w", encoding="utf-8") as file:
    file.write(svg)

print("Live contribution graph generated.")
