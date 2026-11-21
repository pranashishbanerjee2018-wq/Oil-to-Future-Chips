#!/usr/bin/env python3
"""
INTEGRATION TEST: LIVE SERVER PROBING & STARTUP VERIFICATION
"""

import time
import subprocess
import requests
import sys
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_FILE = os.path.join(PROJECT_ROOT, "startup.log")

def test_startup_check():
    print("[TEST 1] Running startup_check.py...")
    res = subprocess.run([sys.executable, "startup_check.py"], cwd=PROJECT_ROOT, capture_output=True, text=True)
    print("  -> Return code:", res.returncode)
    print("  -> Output summary:", res.stdout.strip().splitlines()[-1] if res.stdout else "No output")
    assert res.returncode == 0
    assert os.path.exists(LOG_FILE)
    print("  -> startup.log exists and verified.")

def test_flask():
    print("\n[TEST 2] Starting Flask server with NO_BROWSER=1...")
    env = os.environ.copy()
    env['NO_BROWSER'] = '1'
    env['NO_PROXY'] = 'localhost,127.0.0.1'
    
    proc = subprocess.Popen([sys.executable, 'app.py'], cwd=PROJECT_ROOT, env=env)
    session = requests.Session()
    session.trust_env = False
    
    try:
        time.sleep(2.5)
        # Health
        r = session.get("http://127.0.0.1:5000/api/health", timeout=5)
        print("  -> /api/health:", r.status_code, r.json()["project"])
        assert r.status_code == 200

        # Root
        r = session.get("http://127.0.0.1:5000/", timeout=5)
        print("  -> / (root index):", r.status_code, f"{len(r.text)} bytes")
        assert r.status_code == 200
        assert "Dr. Theodore Voss" in r.text
        assert "Dr. Caleb Sterling" in r.text

        # Results Plot
        r = session.get("http://127.0.0.1:5000/results/plot1_diode_iv.png", timeout=5)
        print("  -> /results/plot1_diode_iv.png:", r.status_code, f"{len(r.content)} bytes")
        assert r.status_code == 200

        # Data JSON
        r = session.get("http://127.0.0.1:5000/api/data", timeout=5)
        print("  -> /api/data:", r.status_code, "Metadata keys:", list(r.json()["metadata"].keys()))
        assert r.status_code == 200

        # Calculation API
        r = session.post("http://127.0.0.1:5000/api/calculate", json={"experiment": "power", "vdd": 1.2, "freq_ghz": 3.5})
        print("  -> /api/calculate (power):", r.status_code, r.json())
        assert r.status_code == 200

        print("[TEST 2] Flask tests passed!")
    finally:
        proc.kill()
        proc.wait()

def test_static():
    print("\n[TEST 3] Starting Static HTTP server (python -m http.server 8000)...")
    proc = subprocess.Popen([sys.executable, '-m', 'http.server', '8000'], cwd=PROJECT_ROOT)
    session = requests.Session()
    session.trust_env = False

    try:
        time.sleep(2.0)
        # Root index.html
        r = session.get("http://127.0.0.1:8000/index.html", timeout=5)
        print("  -> Static /index.html:", r.status_code, f"{len(r.text)} bytes")
        assert r.status_code == 200

        # Plot via static
        r = session.get("http://127.0.0.1:8000/results/plot2_mosfet_output.png", timeout=5)
        print("  -> Static /results/plot2_mosfet_output.png:", r.status_code, f"{len(r.content)} bytes")
        assert r.status_code == 200

        # SVG via static
        r = session.get("http://127.0.0.1:8000/static/images/energy_bands.svg", timeout=5)
        print("  -> Static /static/images/energy_bands.svg:", r.status_code, f"{len(r.content)} bytes")
        assert r.status_code == 200

        print("[TEST 3] Static HTTP server tests passed!")
    finally:
        proc.kill()
        proc.wait()

if __name__ == '__main__':
    test_startup_check()
    test_flask()
    test_static()
    print("\n[ALL STARTUP REPAIR & INTEGRATION TESTS PASSED 100%!]")
