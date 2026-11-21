#!/usr/bin/env python3
"""
VECTOR GRAPHICS & SCIENTIFIC DIAGRAM GENERATOR
Project: "Semiconductors — The New Oil of the Future"
Authors: Dr. Theodore Voss & Dr. Caleb Sterling

Generates modular, high-resolution scientific SVG vector diagrams for the 7 scenes:
- energy_bands.svg: Conductor, Semiconductor, Insulator comparison
- silicon_lattice.svg: Silicon crystal, covalent bonds, P/N doping
- pn_junction.svg: Depletion region, built-in potential, bias states
- mosfet_structure.svg: Gate, oxide, source, drain, channel inversion
- wafer_fab_pipeline.svg: Cleanroom 6-stage fabrication flow
- future_tech_stack.svg: 3D Chiplets, GaN/SiC, Photonic, Quantum
"""

import os

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(PROJECT_ROOT, 'static', 'images')
os.makedirs(IMAGE_DIR, exist_ok=True)

def generate_energy_bands():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="metalGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#0284c7" stop-opacity="0.8"/>
    </linearGradient>
    <linearGradient id="semiGradCond" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#00f5d4" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#059669" stop-opacity="0.7"/>
    </linearGradient>
    <linearGradient id="semiGradVal" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#d97706" stop-opacity="0.9"/>
    </linearGradient>
    <linearGradient id="insulGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ef4444" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#b91c1c" stop-opacity="0.9"/>
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <rect width="800" height="450" fill="#080e1e" rx="12"/>
  
  <!-- Title -->
  <text x="400" y="38" text-anchor="middle" fill="#f8fafc" font-family="'Segoe UI', sans-serif" font-size="20" font-weight="bold">
    ELECTRONIC BAND STRUCTURE COMPARISON
  </text>
  <text x="400" y="62" text-anchor="middle" fill="#94a3b8" font-family="'Segoe UI', sans-serif" font-size="13">
    Valence Band, Conduction Band, and Energy Bandgap (Eg)
  </text>

  <!-- COLUMN 1: METAL / CONDUCTOR -->
  <g transform="translate(60, 90)">
    <rect width="180" height="300" fill="#0f172a" stroke="#334155" stroke-width="1.5" rx="8"/>
    <text x="90" y="32" text-anchor="middle" fill="#38bdf8" font-family="'Segoe UI', sans-serif" font-size="16" font-weight="bold">CONDUCTOR</text>
    <text x="90" y="50" text-anchor="middle" fill="#64748b" font-family="'Segoe UI', sans-serif" font-size="11">(Copper / Aluminum)</text>
    
    <!-- Overlapping bands -->
    <rect x="25" y="80" width="130" height="180" fill="url(#metalGrad)" rx="4"/>
    <text x="90" y="165" text-anchor="middle" fill="#081022" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="bold">OVERLAPPING BANDS</text>
    <text x="90" y="185" text-anchor="middle" fill="#081022" font-family="'Segoe UI', sans-serif" font-size="11">Zero Forbidden Gap</text>
    <text x="90" y="280" text-anchor="middle" fill="#38bdf8" font-family="'Segoe UI', sans-serif" font-size="14" font-weight="bold">Eg = 0 eV</text>
  </g>

  <!-- COLUMN 2: SEMICONDUCTOR -->
  <g transform="translate(310, 90)">
    <rect width="180" height="300" fill="#0f172a" stroke="#00f5d4" stroke-width="2" rx="8" filter="url(#glow)"/>
    <rect width="180" height="300" fill="#0f172a" stroke="#00f5d4" stroke-width="1.5" rx="8"/>
    <text x="90" y="32" text-anchor="middle" fill="#00f5d4" font-family="'Segoe UI', sans-serif" font-size="16" font-weight="bold">SEMICONDUCTOR</text>
    <text x="90" y="50" text-anchor="middle" fill="#64748b" font-family="'Segoe UI', sans-serif" font-size="11">(Silicon: Eg ≈ 1.12 eV)</text>
    
    <!-- Conduction Band -->
    <rect x="25" y="75" width="130" height="65" fill="url(#semiGradCond)" rx="4"/>
    <text x="90" y="105" text-anchor="middle" fill="#042f2e" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="bold">CONDUCTION BAND</text>
    <text x="90" y="122" text-anchor="middle" fill="#042f2e" font-family="'Segoe UI', sans-serif" font-size="10">Empty at 0K / Free e⁻ at 300K</text>

    <!-- Energy Gap -->
    <line x1="90" y1="145" x2="90" y2="195" stroke="#f8fafc" stroke-width="1.5" stroke-dasharray="3,3"/>
    <polygon points="90,142 86,149 94,149" fill="#f8fafc"/>
    <polygon points="90,198 86,191 94,191" fill="#f8fafc"/>
    <text x="90" y="174" text-anchor="middle" fill="#f8fafc" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="bold">Eg ≈ 1.12 eV</text>

    <!-- Valence Band -->
    <rect x="25" y="200" width="130" height="65" fill="url(#semiGradVal)" rx="4"/>
    <text x="90" y="230" text-anchor="middle" fill="#451a03" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="bold">VALENCE BAND</text>
    <text x="90" y="247" text-anchor="middle" fill="#451a03" font-family="'Segoe UI', sans-serif" font-size="10">Covalent Bond Electrons</text>
    <text x="90" y="284" text-anchor="middle" fill="#00f5d4" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="bold">Moderate Bandgap</text>
  </g>

  <!-- COLUMN 3: INSULATOR -->
  <g transform="translate(560, 90)">
    <rect width="180" height="300" fill="#0f172a" stroke="#334155" stroke-width="1.5" rx="8"/>
    <text x="90" y="32" text-anchor="middle" fill="#ef4444" font-family="'Segoe UI', sans-serif" font-size="16" font-weight="bold">INSULATOR</text>
    <text x="90" y="50" text-anchor="middle" fill="#64748b" font-family="'Segoe UI', sans-serif" font-size="11">(SiO2 / Diamond)</text>
    
    <!-- Conduction Band -->
    <rect x="25" y="70" width="130" height="40" fill="#475569" rx="4"/>
    <text x="90" y="94" text-anchor="middle" fill="#94a3b8" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="bold">EMPTY CONDUCTION</text>

    <!-- Wide Gap -->
    <line x1="90" y1="115" x2="90" y2="225" stroke="#ef4444" stroke-width="1.5"/>
    <polygon points="90,113 86,120 94,120" fill="#ef4444"/>
    <polygon points="90,227 86,220 94,220" fill="#ef4444"/>
    <text x="90" y="174" text-anchor="middle" fill="#ef4444" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="bold">Eg &gt; 5.0 eV</text>
    <text x="90" y="190" text-anchor="middle" fill="#94a3b8" font-family="'Segoe UI', sans-serif" font-size="10">Very Wide Gap</text>

    <!-- Valence Band -->
    <rect x="25" y="230" width="130" height="45" fill="url(#insulGrad)" rx="4"/>
    <text x="90" y="258" text-anchor="middle" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="bold">FULL VALENCE</text>
    <text x="90" y="285" text-anchor="middle" fill="#ef4444" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="bold">Negligible Conduction</text>
  </g>
</svg>'''
    with open(os.path.join(IMAGE_DIR, 'energy_bands.svg'), 'w', encoding='utf-8') as f:
        f.write(svg)
    print("[SVG] Generated energy_bands.svg")

def generate_silicon_lattice():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <radialGradient id="atomSi" cx="35%" cy="35%" r="65%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </radialGradient>
    <radialGradient id="atomDonor" cx="35%" cy="35%" r="65%">
      <stop offset="0%" stop-color="#4ade80"/>
      <stop offset="100%" stop-color="#16a34a"/>
    </radialGradient>
    <radialGradient id="atomAcceptor" cx="35%" cy="35%" r="65%">
      <stop offset="0%" stop-color="#fb923c"/>
      <stop offset="100%" stop-color="#ea580c"/>
    </radialGradient>
    <filter id="glowE" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <rect width="800" height="450" fill="#080e1e" rx="12"/>
  
  <text x="400" y="38" text-anchor="middle" fill="#f8fafc" font-family="'Segoe UI', sans-serif" font-size="20" font-weight="bold">
    SILICON CRYSTAL LATTICE &amp; DOPING FUNDAMENTALS
  </text>
  <text x="400" y="62" text-anchor="middle" fill="#94a3b8" font-family="'Segoe UI', sans-serif" font-size="13">
    Intrinsic Covalent Bonds vs. Extrinsic N-Type (Phosphorus) and P-Type (Boron) Doping
  </text>

  <!-- LEFT PANEL: INTRINSIC SILICON -->
  <g transform="translate(40, 85)">
    <rect width="340" height="330" fill="#0f172a" stroke="#1e293b" stroke-width="1.5" rx="8"/>
    <text x="170" y="28" text-anchor="middle" fill="#38bdf8" font-family="'Segoe UI', sans-serif" font-size="15" font-weight="bold">INTRINSIC SILICON (Pure Diamond Cubic)</text>
    
    <!-- Covalent bond lines -->
    <line x1="85" y1="100" x2="170" y2="100" stroke="#334155" stroke-width="4"/>
    <line x1="170" y1="100" x2="255" y2="100" stroke="#334155" stroke-width="4"/>
    <line x1="85" y1="185" x2="170" y2="185" stroke="#334155" stroke-width="4"/>
    <line x1="170" y1="185" x2="255" y2="185" stroke="#334155" stroke-width="4"/>
    <line x1="85" y1="270" x2="170" y2="270" stroke="#334155" stroke-width="4"/>
    <line x1="170" y1="270" x2="255" y2="270" stroke="#334155" stroke-width="4"/>

    <line x1="85" y1="100" x2="85" y2="185" stroke="#334155" stroke-width="4"/>
    <line x1="85" y1="185" x2="85" y2="270" stroke="#334155" stroke-width="4"/>
    <line x1="170" y1="100" x2="170" y2="185" stroke="#334155" stroke-width="4"/>
    <line x1="170" y1="185" x2="170" y2="270" stroke="#334155" stroke-width="4"/>
    <line x1="255" y1="100" x2="255" y2="185" stroke="#334155" stroke-width="4"/>
    <line x1="255" y1="185" x2="255" y2="270" stroke="#334155" stroke-width="4"/>

    <!-- Atoms Si (4 valence electrons each) -->
    <!-- Row 1 -->
    <circle cx="85" cy="100" r="22" fill="url(#atomSi)"/>
    <text x="85" y="106" text-anchor="middle" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="bold">Si</text>
    <circle cx="170" cy="100" r="22" fill="url(#atomSi)"/>
    <text x="170" y="106" text-anchor="middle" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="bold">Si</text>
    <circle cx="255" cy="100" r="22" fill="url(#atomSi)"/>
    <text x="255" y="106" text-anchor="middle" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="bold">Si</text>

    <!-- Row 2 -->
    <circle cx="85" cy="185" r="22" fill="url(#atomSi)"/>
    <text x="85" y="191" text-anchor="middle" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="bold">Si</text>
    <circle cx="170" cy="185" r="22" fill="url(#atomSi)"/>
    <text x="170" y="191" text-anchor="middle" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="bold">Si</text>
    <circle cx="255" cy="185" r="22" fill="url(#atomSi)"/>
    <text x="255" y="191" text-anchor="middle" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="bold">Si</text>

    <!-- Row 3 -->
    <circle cx="85" cy="270" r="22" fill="url(#atomSi)"/>
    <text x="85" y="276" text-anchor="middle" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="bold">Si</text>
    <circle cx="170" cy="270" r="22" fill="url(#atomSi)"/>
    <text x="170" y="276" text-anchor="middle" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="bold">Si</text>
    <circle cx="255" cy="270" r="22" fill="url(#atomSi)"/>
    <text x="255" y="276" text-anchor="middle" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="bold">Si</text>

    <text x="170" y="315" text-anchor="middle" fill="#94a3b8" font-family="'Segoe UI', sans-serif" font-size="11">Each Si shares 4 valence electrons; tightly bound at low T</text>
  </g>

  <!-- RIGHT PANEL: EXTRINSIC DOPED SILICON -->
  <g transform="translate(420, 85)">
    <rect width="340" height="330" fill="#0f172a" stroke="#00f5d4" stroke-width="1.5" rx="8"/>
    <text x="170" y="28" text-anchor="middle" fill="#00f5d4" font-family="'Segoe UI', sans-serif" font-size="15" font-weight="bold">EXTRINSIC DOPING (N-Type Donor: P)</text>

    <!-- Covalent bond lines -->
    <line x1="85" y1="100" x2="170" y2="100" stroke="#334155" stroke-width="4"/>
    <line x1="170" y1="100" x2="255" y2="100" stroke="#334155" stroke-width="4"/>
    <line x1="85" y1="185" x2="170" y2="185" stroke="#334155" stroke-width="4"/>
    <line x1="170" y1="185" x2="255" y2="185" stroke="#334155" stroke-width="4"/>
    <line x1="85" y1="270" x2="170" y2="270" stroke="#334155" stroke-width="4"/>
    <line x1="170" y1="270" x2="255" y2="270" stroke="#334155" stroke-width="4"/>

    <line x1="85" y1="100" x2="85" y2="185" stroke="#334155" stroke-width="4"/>
    <line x1="85" y1="185" x2="85" y2="270" stroke="#334155" stroke-width="4"/>
    <line x1="170" y1="100" x2="170" y2="185" stroke="#334155" stroke-width="4"/>
    <line x1="170" y1="185" x2="170" y2="270" stroke="#334155" stroke-width="4"/>
    <line x1="255" y1="100" x2="255" y2="185" stroke="#334155" stroke-width="4"/>
    <line x1="255" y1="185" x2="255" y2="270" stroke="#334155" stroke-width="4"/>

    <!-- Outer Si atoms -->
    <circle cx="85" cy="100" r="22" fill="url(#atomSi)"/>
    <text x="85" y="106" text-anchor="middle" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="bold">Si</text>
    <circle cx="170" cy="100" r="22" fill="url(#atomSi)"/>
    <text x="170" y="106" text-anchor="middle" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="bold">Si</text>
    <circle cx="255" cy="100" r="22" fill="url(#atomSi)"/>
    <text x="255" y="106" text-anchor="middle" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="bold">Si</text>

    <circle cx="85" cy="185" r="22" fill="url(#atomSi)"/>
    <text x="85" y="191" text-anchor="middle" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="bold">Si</text>
    
    <!-- CENTRAL PHOSPHORUS DONOR (Group V: 5 valence electrons) -->
    <circle cx="170" cy="185" r="24" fill="url(#atomDonor)" filter="url(#glowE)"/>
    <text x="170" y="191" text-anchor="middle" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="14" font-weight="bold">P⁺</text>

    <circle cx="255" cy="185" r="22" fill="url(#atomSi)"/>
    <text x="255" y="191" text-anchor="middle" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="bold">Si</text>

    <circle cx="85" cy="270" r="22" fill="url(#atomSi)"/>
    <text x="85" y="276" text-anchor="middle" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="bold">Si</text>
    <circle cx="170" cy="270" r="22" fill="url(#atomSi)"/>
    <text x="170" y="276" text-anchor="middle" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="bold">Si</text>
    <circle cx="255" cy="270" r="22" fill="url(#atomSi)"/>
    <text x="255" y="276" text-anchor="middle" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="bold">Si</text>

    <!-- FREE DELOCALIZED CONDUCTION ELECTRON -->
    <circle cx="205" cy="155" r="8" fill="#facc15" filter="url(#glowE)"/>
    <text x="205" y="159" text-anchor="middle" fill="#713f12" font-family="'Segoe UI', sans-serif" font-size="10" font-weight="bold">e⁻</text>
    <path d="M 205 155 Q 230 140, 220 120" stroke="#facc15" stroke-width="1.5" stroke-dasharray="3,2" fill="none"/>

    <text x="170" y="315" text-anchor="middle" fill="#00f5d4" font-family="'Segoe UI', sans-serif" font-size="11">5th valence electron enters conduction band with ~0.045 eV</text>
  </g>
</svg>'''
    with open(os.path.join(IMAGE_DIR, 'silicon_lattice.svg'), 'w', encoding='utf-8') as f:
        f.write(svg)
    print("[SVG] Generated silicon_lattice.svg")

def generate_pn_and_mosfet():
    # PN Junction SVG
    svg_pn = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" width="100%" height="100%">
  <defs>
    <linearGradient id="pGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#3b82f6" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#1d4ed8" stop-opacity="0.9"/>
    </linearGradient>
    <linearGradient id="nGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#059669" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#10b981" stop-opacity="0.8"/>
    </linearGradient>
    <linearGradient id="depGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="50%" stop-color="#334155"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
  </defs>

  <rect width="800" height="420" fill="#080e1e" rx="12"/>
  <text x="400" y="36" text-anchor="middle" fill="#f8fafc" font-family="'Segoe UI', sans-serif" font-size="18" font-weight="bold">
    PN JUNCTION DIODE: EQUILIBRIUM &amp; DEPLETION REGION
  </text>
  <text x="400" y="58" text-anchor="middle" fill="#94a3b8" font-family="'Segoe UI', sans-serif" font-size="12">
    Built-in Potential Vbi, Space Charge Layer, and Forward vs. Reverse Bias
  </text>

  <!-- P-REGION -->
  <rect x="80" y="80" width="240" height="220" fill="url(#pGrad)" rx="6"/>
  <text x="200" y="115" text-anchor="middle" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="18" font-weight="bold">P - TYPE</text>
  <text x="200" y="135" text-anchor="middle" fill="#bfdbfe" font-family="'Segoe UI', sans-serif" font-size="12">Majority: Holes (h⁺)</text>

  <!-- Holes -->
  <g fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="bold">
    <circle cx="120" cy="170" r="12" fill="#60a5fa"/><text x="120" y="174" text-anchor="middle" fill="#0c4a6e">h⁺</text>
    <circle cx="170" cy="190" r="12" fill="#60a5fa"/><text x="170" y="194" text-anchor="middle" fill="#0c4a6e">h⁺</text>
    <circle cx="130" cy="240" r="12" fill="#60a5fa"/><text x="130" y="244" text-anchor="middle" fill="#0c4a6e">h⁺</text>
    <circle cx="210" cy="230" r="12" fill="#60a5fa"/><text x="210" y="234" text-anchor="middle" fill="#0c4a6e">h⁺</text>
  </g>

  <!-- DEPLETION REGION -->
  <rect x="320" y="80" width="160" height="220" fill="url(#depGrad)" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4,4"/>
  <text x="400" y="105" text-anchor="middle" fill="#f59e0b" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="bold">DEPLETION ZONE</text>
  <text x="400" y="122" text-anchor="middle" fill="#cbd5e1" font-family="'Segoe UI', sans-serif" font-size="10">Space-Charge Layer</text>

  <!-- Fixed Acceptor Ions (-) and Donor Ions (+) -->
  <g fill="#f87171">
    <circle cx="355" cy="160" r="14" fill="#991b1b" stroke="#f87171" stroke-width="1.5"/>
    <text x="355" y="165" text-anchor="middle" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="14" font-weight="bold">-</text>
    <circle cx="355" cy="220" r="14" fill="#991b1b" stroke="#f87171" stroke-width="1.5"/>
    <text x="355" y="225" text-anchor="middle" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="14" font-weight="bold">-</text>
  </g>
  <g fill="#4ade80">
    <circle cx="445" cy="160" r="14" fill="#166534" stroke="#4ade80" stroke-width="1.5"/>
    <text x="445" y="165" text-anchor="middle" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="14" font-weight="bold">+</text>
    <circle cx="445" cy="220" r="14" fill="#166534" stroke="#4ade80" stroke-width="1.5"/>
    <text x="445" y="225" text-anchor="middle" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="14" font-weight="bold">+</text>
  </g>

  <!-- Built-in Electric Field Arrow -->
  <line x1="440" y1="270" x2="360" y2="270" stroke="#38bdf8" stroke-width="3" marker-end="url(#arrow)"/>
  <polygon points="360,270 372,265 372,275" fill="#38bdf8"/>
  <text x="400" y="262" text-anchor="middle" fill="#38bdf8" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="bold">Electric Field E</text>

  <!-- N-REGION -->
  <rect x="480" y="80" width="240" height="220" fill="url(#nGrad)" rx="6"/>
  <text x="600" y="115" text-anchor="middle" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="18" font-weight="bold">N - TYPE</text>
  <text x="600" y="135" text-anchor="middle" fill="#d1fae5" font-family="'Segoe UI', sans-serif" font-size="12">Majority: Electrons (e⁻)</text>

  <!-- Electrons -->
  <g fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="bold">
    <circle cx="560" cy="170" r="12" fill="#34d399"/><text x="560" y="174" text-anchor="middle" fill="#064e3b">e⁻</text>
    <circle cx="630" cy="190" r="12" fill="#34d399"/><text x="630" y="194" text-anchor="middle" fill="#064e3b">e⁻</text>
    <circle cx="570" cy="240" r="12" fill="#34d399"/><text x="570" y="244" text-anchor="middle" fill="#064e3b">e⁻</text>
    <circle cx="650" cy="230" r="12" fill="#34d399"/><text x="650" y="234" text-anchor="middle" fill="#064e3b">e⁻</text>
  </g>

  <!-- Bottom Annotation Bar -->
  <rect x="80" y="325" width="640" height="65" fill="#0f172a" stroke="#334155" rx="6"/>
  <text x="400" y="348" text-anchor="middle" fill="#38bdf8" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="bold">
    FORWARD BIAS (V &gt; 0): Depletion narrows, massive diffusion current flows (I ∝ exp(qV/nkT))
  </text>
  <text x="400" y="372" text-anchor="middle" fill="#94a3b8" font-family="'Segoe UI', sans-serif" font-size="12">
    REVERSE BIAS (V &lt; 0): Depletion widens, negligible saturation current -Is flows
  </text>
</svg>'''
    with open(os.path.join(IMAGE_DIR, 'pn_junction.svg'), 'w', encoding='utf-8') as f:
        f.write(svg_pn)
    print("[SVG] Generated pn_junction.svg")

    # MOSFET SVG
    svg_mosfet = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 440" width="100%" height="100%">
  <defs>
    <linearGradient id="gateGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#a855f7"/>
      <stop offset="100%" stop-color="#7e22ce"/>
    </linearGradient>
    <linearGradient id="subGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="800" height="440" fill="#080e1e" rx="12"/>
  <text x="400" y="36" text-anchor="middle" fill="#f8fafc" font-family="'Segoe UI', sans-serif" font-size="18" font-weight="bold">
    nMOSFET CROSS-SECTION &amp; CHANNEL INVERSION
  </text>
  <text x="400" y="58" text-anchor="middle" fill="#94a3b8" font-family="'Segoe UI', sans-serif" font-size="12">
    Gate, Thin Oxide Dielectric (tox), Source, Drain, and Inversion Layer
  </text>

  <!-- P-Substrate -->
  <rect x="80" y="160" width="640" height="190" fill="url(#subGrad)" stroke="#334155" stroke-width="2" rx="4"/>
  <text x="400" y="310" text-anchor="middle" fill="#64748b" font-family="'Segoe UI', sans-serif" font-size="16" font-weight="bold">P-TYPE SILICON SUBSTRATE (Bulk)</text>

  <!-- Source N+ Well -->
  <rect x="120" y="160" width="140" height="75" fill="#0284c7" stroke="#38bdf8" stroke-width="2" rx="4"/>
  <text x="190" y="205" text-anchor="middle" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="16" font-weight="bold">SOURCE (N⁺)</text>

  <!-- Drain N+ Well -->
  <rect x="540" y="160" width="140" height="75" fill="#0284c7" stroke="#38bdf8" stroke-width="2" rx="4"/>
  <text x="610" y="205" text-anchor="middle" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="16" font-weight="bold">DRAIN (N⁺)</text>

  <!-- Inversion Channel (Yellow Glow) -->
  <rect x="260" y="160" width="280" height="16" fill="#facc15" opacity="0.9"/>
  <text x="400" y="173" text-anchor="middle" fill="#713f12" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="bold">INVERSION CHANNEL (e⁻ accumulation layer)</text>

  <!-- Gate Oxide SiO2 -->
  <rect x="250" y="142" width="300" height="18" fill="#14b8a6" stroke="#5eead4" stroke-width="1.5"/>
  <text x="400" y="155" text-anchor="middle" fill="#042f2e" font-family="'Segoe UI', sans-serif" font-size="10" font-weight="bold">GATE OXIDE DIELECTRIC (SiO2, tox ≈ 1.5 - 3 nm)</text>

  <!-- Polysilicon / Metal Gate -->
  <rect x="270" y="90" width="260" height="52" fill="url(#gateGrad)" stroke="#c084fc" stroke-width="2" rx="4"/>
  <text x="400" y="122" text-anchor="middle" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="15" font-weight="bold">GATE ELECTRODE (V_GS)</text>

  <!-- Terminals -->
  <line x1="190" y1="160" x2="190" y2="80" stroke="#f8fafc" stroke-width="3"/>
  <text x="190" y="72" text-anchor="middle" fill="#f8fafc" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="bold">SOURCE</text>

  <line x1="400" y1="90" x2="400" y2="75" stroke="#c084fc" stroke-width="3"/>

  <line x1="610" y1="160" x2="610" y2="80" stroke="#f8fafc" stroke-width="3"/>
  <text x="610" y="72" text-anchor="middle" fill="#f8fafc" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="bold">DRAIN (V_DS)</text>

  <!-- Channel Length Annotation -->
  <line x1="260" y1="195" x2="540" y2="195" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="3,3"/>
  <polygon points="260,195 268,191 268,199" fill="#94a3b8"/>
  <polygon points="540,195 532,191 532,199" fill="#94a3b8"/>
  <text x="400" y="215" text-anchor="middle" fill="#94a3b8" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="bold">Channel Length (L)</text>

  <!-- Formula Summary -->
  <rect x="80" y="365" width="640" height="55" fill="#0f172a" stroke="#334155" rx="6"/>
  <text x="400" y="388" text-anchor="middle" fill="#38bdf8" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="bold">
    Linear Region (VDS &lt; VGS - VTH): ID = μn Cox (W/L) [(VGS - VTH)VDS - VDS²/2]
  </text>
  <text x="400" y="408" text-anchor="middle" fill="#a855f7" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="bold">
    Saturation Region (VDS ≥ VGS - VTH): ID = 1/2 μn Cox (W/L) (VGS - VTH)²
  </text>
</svg>'''
    with open(os.path.join(IMAGE_DIR, 'mosfet_structure.svg'), 'w', encoding='utf-8') as f:
        f.write(svg_mosfet)
    print("[SVG] Generated mosfet_structure.svg")

def generate_fabrication_pipeline():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 450" width="100%" height="100%">
  <rect width="900" height="450" fill="#080e1e" rx="12"/>
  <text x="450" y="36" text-anchor="middle" fill="#f8fafc" font-family="'Segoe UI', sans-serif" font-size="20" font-weight="bold">
    SEMICONDUCTOR CLEANROOM FABRICATION PIPELINE
  </text>
  <text x="450" y="58" text-anchor="middle" fill="#94a3b8" font-family="'Segoe UI', sans-serif" font-size="13">
    From Single-Crystal Ingot to Nanometer Photolithography, Etching, Metallization &amp; Packaging
  </text>

  <!-- 6 Step Cards -->
  <!-- Step 1: Crystal & Wafering -->
  <g transform="translate(30, 85)">
    <rect width="125" height="280" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5" rx="8"/>
    <circle cx="62" cy="35" r="18" fill="#0284c7"/>
    <text x="62" y="40" text-anchor="middle" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="14" font-weight="bold">1</text>
    <text x="62" y="75" text-anchor="middle" fill="#38bdf8" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="bold">INGOT &amp; WAFER</text>
    <!-- Visual icon: Ingot & Slice -->
    <rect x="42" y="100" width="40" height="60" rx="6" fill="#475569"/>
    <ellipse cx="62" cy="180" rx="35" ry="12" fill="#00f5d4" opacity="0.8"/>
    <text x="62" y="215" text-anchor="middle" fill="#cbd5e1" font-family="'Segoe UI', sans-serif" font-size="11">Czochralski single crystal pulled &amp; sliced to 300mm mirror disc</text>
  </g>

  <!-- Step 2: Spin Coat Photoresist -->
  <g transform="translate(175, 85)">
    <rect width="125" height="280" fill="#0f172a" stroke="#334155" stroke-width="1.5" rx="8"/>
    <circle cx="62" cy="35" r="18" fill="#334155"/>
    <text x="62" y="40" text-anchor="middle" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="14" font-weight="bold">2</text>
    <text x="62" y="75" text-anchor="middle" fill="#f8fafc" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="bold">PHOTORESIST</text>
    <rect x="25" y="110" width="75" height="15" fill="#f59e0b" rx="2"/>
    <rect x="25" y="127" width="75" height="20" fill="#00f5d4" opacity="0.7" rx="2"/>
    <text x="62" y="215" text-anchor="middle" fill="#cbd5e1" font-family="'Segoe UI', sans-serif" font-size="11">Light-sensitive polymer spun uniformly across the spinning wafer</text>
  </g>

  <!-- Step 3: EUV Lithography -->
  <g transform="translate(320, 85)">
    <rect width="125" height="280" fill="#0f172a" stroke="#a855f7" stroke-width="2" rx="8"/>
    <circle cx="62" cy="35" r="18" fill="#9333ea"/>
    <text x="62" y="40" text-anchor="middle" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="14" font-weight="bold">3</text>
    <text x="62" y="75" text-anchor="middle" fill="#c084fc" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="bold">EUV STEPPER</text>
    <!-- Mask and light beam -->
    <rect x="35" y="100" width="55" height="10" fill="#e2e8f0"/>
    <polygon points="40,112 85,112 95,160 30,160" fill="#c084fc" opacity="0.4"/>
    <rect x="25" y="160" width="75" height="15" fill="#f59e0b" rx="2"/>
    <text x="62" y="215" text-anchor="middle" fill="#cbd5e1" font-family="'Segoe UI', sans-serif" font-size="11">13.5 nm Extreme Ultraviolet light projects sub-micron mask patterns</text>
  </g>

  <!-- Step 4: Etch & Implantation -->
  <g transform="translate(465, 85)">
    <rect width="125" height="280" fill="#0f172a" stroke="#334155" stroke-width="1.5" rx="8"/>
    <circle cx="62" cy="35" r="18" fill="#334155"/>
    <text x="62" y="40" text-anchor="middle" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="14" font-weight="bold">4</text>
    <text x="62" y="75" text-anchor="middle" fill="#f8fafc" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="bold">ETCH &amp; IMPLANT</text>
    <!-- Ion beams -->
    <line x1="45" y1="105" x2="45" y2="155" stroke="#ef4444" stroke-width="2"/>
    <line x1="62" y1="105" x2="62" y2="155" stroke="#ef4444" stroke-width="2"/>
    <line x1="80" y1="105" x2="80" y2="155" stroke="#ef4444" stroke-width="2"/>
    <rect x="25" y="155" width="75" height="20" fill="#00f5d4" opacity="0.6" rx="2"/>
    <text x="62" y="215" text-anchor="middle" fill="#cbd5e1" font-family="'Segoe UI', sans-serif" font-size="11">Plasma RIE dry etching and high-energy ion beam dopant implantation</text>
  </g>

  <!-- Step 5: Metal & CMP -->
  <g transform="translate(610, 85)">
    <rect width="125" height="280" fill="#0f172a" stroke="#334155" stroke-width="1.5" rx="8"/>
    <circle cx="62" cy="35" r="18" fill="#334155"/>
    <text x="62" y="40" text-anchor="middle" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="14" font-weight="bold">5</text>
    <text x="62" y="75" text-anchor="middle" fill="#f8fafc" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="bold">INTERCONNECTS</text>
    <!-- Multi metal layers -->
    <line x1="30" y1="115" x2="95" y2="115" stroke="#f59e0b" stroke-width="3"/>
    <line x1="30" y1="135" x2="95" y2="135" stroke="#38bdf8" stroke-width="3"/>
    <line x1="30" y1="155" x2="95" y2="155" stroke="#f59e0b" stroke-width="3"/>
    <text x="62" y="215" text-anchor="middle" fill="#cbd5e1" font-family="'Segoe UI', sans-serif" font-size="11">Up to 15+ Copper metallization layers planarized with CMP</text>
  </g>

  <!-- Step 6: Test & Packaging -->
  <g transform="translate(755, 85)">
    <rect width="125" height="280" fill="#0f172a" stroke="#10b981" stroke-width="1.5" rx="8"/>
    <circle cx="62" cy="35" r="18" fill="#059669"/>
    <text x="62" y="40" text-anchor="middle" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="14" font-weight="bold">6</text>
    <text x="62" y="75" text-anchor="middle" fill="#34d399" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="bold">PACKAGING</text>
    <!-- Packaged Chip -->
    <rect x="35" y="110" width="55" height="55" fill="#1e293b" stroke="#34d399" stroke-width="2" rx="4"/>
    <rect x="47" y="122" width="31" height="31" fill="#0f172a" stroke="#64748b"/>
    <text x="62" y="215" text-anchor="middle" fill="#cbd5e1" font-family="'Segoe UI', sans-serif" font-size="11">Wafer dicing, automated probe test, flip-chip or 2.5D substrate mount</text>
  </g>

  <!-- Cleanroom ISO 1 banner -->
  <rect x="30" y="380" width="850" height="48" fill="#0f172a" stroke="#1e293b" rx="6"/>
  <text x="450" y="402" text-anchor="middle" fill="#00f5d4" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="bold">
    ISO CLASS 1 CLEANROOM SPECIFICATION: &lt; 10 particles per m³ (&gt;0.1 μm)
  </text>
  <text x="450" y="419" text-anchor="middle" fill="#94a3b8" font-family="'Segoe UI', sans-serif" font-size="11">
    Cycle time: 3 to 4 months through over 1,000 discrete automated chemical and physical manufacturing steps
  </text>
</svg>'''
    with open(os.path.join(IMAGE_DIR, 'wafer_fab_pipeline.svg'), 'w', encoding='utf-8') as f:
        f.write(svg)
    print("[SVG] Generated wafer_fab_pipeline.svg")

def generate_future_tech():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 450" width="100%" height="100%">
  <rect width="900" height="450" fill="#080e1e" rx="12"/>
  <text x="450" y="36" text-anchor="middle" fill="#f8fafc" font-family="'Segoe UI', sans-serif" font-size="20" font-weight="bold">
    NEXT-GENERATION SEMICONDUCTOR HORIZONS
  </text>
  <text x="450" y="58" text-anchor="middle" fill="#94a3b8" font-family="'Segoe UI', sans-serif" font-size="13">
    Beyond Traditional Moore's Law: 3D Packaging, Wide-Bandgap, Silicon Photonics, and Neuromorphic Hardware
  </text>

  <!-- Pillar 1: 3D Chiplets & Advanced Packaging -->
  <g transform="translate(40, 85)">
    <rect width="185" height="280" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5" rx="8"/>
    <text x="92" y="30" text-anchor="middle" fill="#38bdf8" font-family="'Segoe UI', sans-serif" font-size="14" font-weight="bold">3D CHIPLETS &amp; TSV</text>
    <rect x="30" y="50" width="125" height="24" fill="#0284c7" rx="3"/>
    <text x="92" y="66" text-anchor="middle" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="bold">Compute Die (3nm)</text>
    
    <rect x="30" y="80" width="125" height="24" fill="#0369a1" rx="3"/>
    <text x="92" y="96" text-anchor="middle" fill="#ffffff" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="bold">HBM3e Memory Stack</text>

    <rect x="20" y="112" width="145" height="15" fill="#f59e0b" rx="2"/>
    <text x="92" y="124" text-anchor="middle" fill="#451a03" font-family="'Segoe UI', sans-serif" font-size="10" font-weight="bold">Silicon Interposer / Bridge</text>

    <text x="92" y="165" text-anchor="middle" fill="#cbd5e1" font-family="'Segoe UI', sans-serif" font-size="11">Deconstructs massive monolithic reticle-limited dies into modular high-yield silicon tiles interconnected via micro-bumps and Through-Silicon Vias.</text>
    <text x="92" y="255" text-anchor="middle" fill="#38bdf8" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="bold">Yield Maximization</text>
  </g>

  <!-- Pillar 2: Wide Bandgap (GaN & SiC) -->
  <g transform="translate(250, 85)">
    <rect width="185" height="280" fill="#0f172a" stroke="#00f5d4" stroke-width="1.5" rx="8"/>
    <text x="92" y="30" text-anchor="middle" fill="#00f5d4" font-family="'Segoe UI', sans-serif" font-size="14" font-weight="bold">WIDE-BANDGAP (GaN/SiC)</text>
    
    <circle cx="92" cy="80" r="32" fill="#065f46" stroke="#00f5d4" stroke-width="2"/>
    <text x="92" y="78" text-anchor="middle" fill="#00f5d4" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="bold">GaN / SiC</text>
    <text x="92" y="93" text-anchor="middle" fill="#99f6e4" font-family="'Segoe UI', sans-serif" font-size="10">Eg &gt; 3.2 eV</text>

    <text x="92" y="150" text-anchor="middle" fill="#cbd5e1" font-family="'Segoe UI', sans-serif" font-size="11">High critical electric breakdown fields (10x Silicon), enabling 99%+ power conversion efficiency in Electric Vehicles, renewable inverters, and AI server power stages.</text>
    <text x="92" y="255" text-anchor="middle" fill="#00f5d4" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="bold">Extreme Power Density</text>
  </g>

  <!-- Pillar 3: Silicon Photonics -->
  <g transform="translate(460, 85)">
    <rect width="185" height="280" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5" rx="8"/>
    <text x="92" y="30" text-anchor="middle" fill="#f59e0b" font-family="'Segoe UI', sans-serif" font-size="14" font-weight="bold">SILICON PHOTONICS</text>

    <!-- Optical waveguides -->
    <path d="M 30 75 Q 92 100, 155 75" stroke="#f59e0b" stroke-width="3" fill="none"/>
    <path d="M 30 90 Q 92 65, 155 90" stroke="#f43f5e" stroke-width="3" fill="none"/>

    <text x="92" y="150" text-anchor="middle" fill="#cbd5e1" font-family="'Segoe UI', sans-serif" font-size="11">Replaces resistive copper traces with on-chip laser waveguides. Provides petabit-per-second bandwidth at sub-picojoule energy per bit for AI cluster fabrics.</text>
    <text x="92" y="255" text-anchor="middle" fill="#f59e0b" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="bold">Light-Speed Interconnects</text>
  </g>

  <!-- Pillar 4: Cryogenic & Neuromorphic -->
  <g transform="translate(670, 85)">
    <rect width="185" height="280" fill="#0f172a" stroke="#c084fc" stroke-width="1.5" rx="8"/>
    <text x="92" y="30" text-anchor="middle" fill="#c084fc" font-family="'Segoe UI', sans-serif" font-size="14" font-weight="bold">NEUROMORPHIC / QUANTUM</text>

    <!-- Quantum Qubit / Synapse -->
    <circle cx="92" cy="78" r="28" fill="#581c87" stroke="#c084fc" stroke-width="2"/>
    <text x="92" y="82" text-anchor="middle" fill="#e9d5ff" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="bold">|ψ⟩ / Synapse</text>

    <text x="92" y="150" text-anchor="middle" fill="#cbd5e1" font-family="'Segoe UI', sans-serif" font-size="11">Spiking event-driven neural architectures and superconducting Josephson junction circuits operating at 15 mK dilution refrigeration temperatures.</text>
    <text x="92" y="255" text-anchor="middle" fill="#c084fc" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="bold">Non-Von Neumann Hardware</text>
  </g>

  <!-- Geopolitical & Supply Chain Footer -->
  <rect x="40" y="380" width="815" height="48" fill="#0f172a" stroke="#1e293b" rx="6"/>
  <text x="447" y="402" text-anchor="middle" fill="#f8fafc" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="bold">
    STRATEGIC ECOSYSTEM: Extreme Capital Intensity ($20B+ per Leading-Edge Giga-Fab)
  </text>
  <text x="447" y="419" text-anchor="middle" fill="#94a3b8" font-family="'Segoe UI', sans-serif" font-size="11">
    Complex global interdependence: High-purity neon gas, ultra-pure water (UPW), polysilicon, EUV optics, EDA software
  </text>
</svg>'''
    with open(os.path.join(IMAGE_DIR, 'future_tech_stack.svg'), 'w', encoding='utf-8') as f:
        f.write(svg)
    print("[SVG] Generated future_tech_stack.svg")

def main():
    print("Generating scientific SVG vector diagrams...")
    generate_energy_bands()
    generate_silicon_lattice()
    generate_pn_and_mosfet()
    generate_fabrication_pipeline()
    generate_future_tech()
    print("All scientific vector SVGs successfully created in static/images/!")

if __name__ == '__main__':
    main()
