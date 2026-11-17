
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="320" viewBox="0 0 1200 320">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#071a2b"/>
      <stop offset="55%" stop-color="#102d45"/>
      <stop offset="100%" stop-color="#090e20"/>
    </linearGradient>
    <linearGradient id="mountain" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#315b83"/>
      <stop offset="100%" stop-color="#101d35"/>
    </linearGradient>
    <radialGradient id="sun">
      <stop offset="0%" stop-color="#ffb4a2" stop-opacity=".9"/>
      <stop offset="100%" stop-color="#ff668c" stop-opacity="0"/>
    </radialGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="12"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="1200" height="320" fill="url(#bg)"/>

  <!-- Stars -->
  <g fill="#b9dfff">
    <circle cx="90" cy="48" r="1.5"/>
    <circle cx="260" cy="75" r="1"/>
    <circle cx="470" cy="35" r="1.5"/>
    <circle cx="720" cy="55" r="1"/>
    <circle cx="960" cy="42" r="1.5"/>
    <circle cx="1110" cy="100" r="1"/>
    <circle cx="850" cy="125" r="1"/>
    <circle cx="350" cy="125" r="1"/>
  </g>

  <!-- Glowing moon -->
  <circle cx="970" cy="115" r="95" fill="#ff668c" opacity=".12" filter="url(#glow)"/>
  <circle cx="970" cy="115" r="63" fill="#ff9eaa" opacity=".75"/>

  <!-- Mount Fuji -->
  <path d="M570 275 L780 95 L990 275 Z" fill="url(#mountain)"/>
  <path d="M780 95 L750 130 L780 119 L805 140 L780 95 Z" fill="#d8e7f5" opacity=".9"/>

  <!-- Distant mountains -->
  <path d="M400 275 L620 155 L810 275 Z" fill="#172e49"/>
  <path d="M850 275 L1030 175 L1200 275 Z" fill="#152a43"/>

  <!-- Tokyo skyline -->
  <g fill="#081525" opacity=".95">
    <rect x="0" y="215" width="80" height="105"/>
    <rect x="90" y="185" width="65" height="135"/>
    <rect x="165" y="225" width="90" height="95"/>
    <rect x="260" y="170" width="65" height="150"/>
    <rect x="335" y="210" width="80" height="110"/>
    <rect x="1040" y="195" width="75" height="125"/>
    <rect x="1125" y="225" width="75" height="95"/>
  </g>

  <!-- Building lights -->
  <g fill="#58baff" opacity=".7">
    <path d="M105 205h5v6h-5z M120 205h5v6h-5z M105 225h5v6h-5z M120 225h5v6h-5z"/>
    <path d="M275 190h5v7h-5z M295 190h5v7h-5z M275 210h5v7h-5z"/>
    <path d="M1060 215h5v6h-5z M1080 215h5v6h-5z M1060 235h5v6h-5z"/>
  </g>

  <!-- Horizon -->
  <path d="M0 276 Q300 265 600 278 T1200 276" fill="none" stroke="#4da9e9" stroke-opacity=".5"/>

  <!-- Moving sakura petals -->
  <g fill="#ffb5cf" opacity=".8">
    <ellipse cx="150" cy="60" rx="5" ry="3">
      <animate attributeName="cy" values="60;290;60" dur="12s" repeatCount="indefinite"/>
      <animate attributeName="cx" values="150;280;150" dur="12s" repeatCount="indefinite"/>
      <animateTransform attributeName="transform" type="rotate" from="0 150 60" to="360 150 60" dur="6s" repeatCount="indefinite"/>
    </ellipse>
    <ellipse cx="420" cy="90" rx="5" ry="3">
      <animate attributeName="cy" values="90;300;90" dur="15s" repeatCount="indefinite"/>
      <animate attributeName="cx" values="420;540;420" dur="15s" repeatCount="indefinite"/>
    </ellipse>
    <ellipse cx="1100" cy="40" rx="5" ry="3">
      <animate attributeName="cy" values="40;290;40" dur="13s" repeatCount="indefinite"/>
      <animate attributeName="cx" values="1100;930;1100" dur="13s" repeatCount="indefinite"/>
    </ellipse>
    <ellipse cx="700" cy="25" rx="4" ry="3">
      <animate attributeName="cy" values="25;300;25" dur="17s" repeatCount="indefinite"/>
    </ellipse>
  </g>

  <!-- Subtle horizontal glow -->
  <path d="M0 290 Q600 260 1200 290" stroke="#299bff" stroke-width="2" opacity=".5" fill="none">
    <animate attributeName="opacity" values=".2;.8;.2" dur="5s" repeatCount="indefinite"/>
  </path>

  <!-- Text -->
  <text x="60" y="155" fill="#ffffff" font-family="Arial, sans-serif" font-size="43" font-weight="bold">
    Vaibhav Sharma
  </text>
  <text x="62" y="198" fill="#b9dfff" font-family="Arial, sans-serif" font-size="19">
    Python • Backend • Full Stack • AI/GenAI
  </text>

  <rect x="62" y="218" width="330" height="5" rx="3" fill="#2f81f7">
    <animate attributeName="width" values="100;330;100" dur="5s" repeatCount="indefinite"/>
  </rect>
</svg>
