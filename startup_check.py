#!/usr/bin/env python3
"""
startup_check.py
================
Pre-flight verification and startup logger for:
"SEMICONDUCTORS — THE NEW OIL OF THE FUTURE"
An Academic Presentation & Computational Microelectronics Suite.

Performs:
1. Environment and working directory verification
2. Python executable and version detection
3. Scientific dependency verification (Flask, NumPy, Matplotlib, Pandas)
4. Port 5000 availability & duplicate server instance detection
5. Precomputed asset & MATLAB/Python numerical results verification
6. Comprehensive logging to startup.log
"""

import os
import sys
import socket
import json
import time
import urllib.request
import urllib.error
import importlib.metadata
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, 'startup.log')
RESULTS_DIR = os.path.join(BASE_DIR, 'results')
DATA_DIR = os.path.join(BASE_DIR, 'data')
STATIC_DIR = os.path.join(BASE_DIR, 'static')

# Ensure localhost bypasses any system proxies
os.environ['NO_PROXY'] = 'localhost,127.0.0.1'
os.environ['no_proxy'] = 'localhost,127.0.0.1'


def log(msg, to_console=True):
    """Write message to startup.log and optionally to console."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {msg}"
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(line + "\n")
    if to_console:
        print(msg)


def init_log():
    """Initialize startup.log with session header."""
    with open(LOG_FILE, 'w', encoding='utf-8') as f:
        f.write("=" * 76 + "\n")
        f.write(" SEMICONDUCTORS — THE NEW OIL OF THE FUTURE\n")
        f.write(" STARTUP DIAGNOSTICS & EXECUTION LOG\n")
        f.write(f" Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 76 + "\n\n")


def check_port_5000():
    """
    Check if port 5000 is open.
    Returns:
      ('free', None) if port is available.
      ('our_server', data) if port 5000 is already hosting our presentation.
      ('occupied', info) if port is occupied by another process.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.6)
    try:
        s.bind(('127.0.0.1', 5000))
        s.close()
        return ('free', None)
    except OSError:
        # Port is in use. Test if it is already our Flask app
        s.close()
        try:
            proxy_handler = urllib.request.ProxyHandler({})
            opener = urllib.request.build_opener(proxy_handler)
            req = opener.open('http://127.0.0.1:5000/api/health', timeout=1.0)
            if req.status == 200:
                data = json.loads(req.read().decode('utf-8'))
                if "Semiconductors" in data.get("project", ""):
                    return ('our_server', data)
        except Exception:
            pass
        return ('occupied', 'Port 5000 is bound by another local process.')


def check_dependencies():
    """Verify required Python packages."""
    core_deps = {
        'flask': 'Flask',
        'numpy': 'NumPy',
        'matplotlib': 'Matplotlib',
        'pandas': 'Pandas'
    }
    missing = []
    versions = {}
    for mod, display in core_deps.items():
        try:
            __import__(mod)
            try:
                v = importlib.metadata.version(mod)
            except Exception:
                v = 'Installed'
            versions[display] = v
        except ImportError:
            missing.append(mod)

    return missing, versions


def verify_precomputed_results():
    """Check if MATLAB/Python results exist, run runner if missing."""
    json_path = os.path.join(DATA_DIR, 'semiconductor_data.json')
    csv_path = os.path.join(DATA_DIR, 'semiconductor_results.csv')
    required_plots = [
        'plot1_diode_iv.png',
        'plot2_mosfet_output.png',
        'plot3_cmos_power.png',
        'plot4_yield_model.png',
        'plot5_moores_law.png'
    ]
    missing_assets = False
    if not os.path.exists(json_path) or not os.path.exists(csv_path):
        missing_assets = True
    for p in required_plots:
        if not os.path.exists(os.path.join(RESULTS_DIR, p)):
            missing_assets = True

    if missing_assets:
        log("Precomputed computational results missing. Generating via matlab_runner.py...")
        from matlab_runner import main as run_computations
        run_computations()
        log("Computational results generated successfully.")
    else:
        log("Precomputed results and scientific plots verified.")

    # Also verify audio assets
    required_audio = [
        'bg_music.wav',
        'ambient_lab.wav',
        'ui_click.wav',
        'scene_transition.wav',
        'calc_complete.wav',
        'processor_hum.wav'
    ]
    audio_missing = any(not os.path.exists(os.path.join(STATIC_DIR, 'audio', a)) for a in required_audio)
    if audio_missing:
        log("Audio assets missing. Generating procedural audio via generate_assets.py...")
        from generate_assets import main as run_audio_gen
        run_audio_gen()
        log("Audio assets generated successfully.")
    else:
        log("Audio assets verified.")

    # Also verify vector graphics
    required_svgs = [
        'energy_bands.svg',
        'silicon_lattice.svg',
        'pn_junction.svg',
        'mosfet_structure.svg',
        'wafer_fab_pipeline.svg',
        'future_tech_stack.svg'
    ]
    svg_missing = any(not os.path.exists(os.path.join(STATIC_DIR, 'images', s)) for s in required_svgs)
    if svg_missing:
        log("Vector SVGs missing. Generating diagrams via generate_svgs.py...")
        from generate_svgs import main as run_svg_gen
        run_svg_gen()
        log("Vector SVGs generated successfully.")
    else:
        log("Scientific vector diagrams verified.")


def main():
    init_log()
    log(f"Project Directory: {BASE_DIR}")
    log(f"Python Executable: {sys.executable}")
    log(f"Python Version: {sys.version.split()[0]} ({sys.platform})")

    # 1. Check Dependencies
    missing_deps, dep_versions = check_dependencies()
    log("Dependency verification results:")
    for name, ver in dep_versions.items():
        log(f"  - {name}: {ver}")
    
    if missing_deps:
        log(f"[WARNING] Missing required dependencies: {', '.join(missing_deps)}")
        # Exit with code 10 to instruct batch to run pip install
        sys.exit(10)

    # 2. Check Port 5000 and duplicate instances
    port_status, port_info = check_port_5000()
    if port_status == 'free':
        log("Port 5000 Availability: Available (127.0.0.1:5000 is free)")
    elif port_status == 'our_server':
        log("Port 5000 Status: Presentation server is ALREADY ACTIVE and responding on http://127.0.0.1:5000/.")
        log("Avoiding duplicate server instance. Opening browser to active session...")
        import webbrowser
        webbrowser.open('http://127.0.0.1:5000/')
        log("Browser opened to existing active server.")
        # Exit code 2 indicates server is already running and browser is opened
        sys.exit(2)
    else:
        log(f"[WARNING] Port 5000 is occupied: {port_info}")

    # 3. Verify Precomputed Results & Assets
    verify_precomputed_results()

    log("Pre-flight checks passed successfully. Ready to launch Flask.")
    sys.exit(0)


if __name__ == '__main__':
    main()
