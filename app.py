#!/usr/bin/env python3
"""
app.py
======
Local Flask Application for:
"SEMICONDUCTORS — THE NEW OIL OF THE FUTURE"
An Academic Presentation & Computational Microelectronics Suite.

Lead Researchers:
- Dr. Theodore Voss (Senior Semiconductor Research Scientist)
- Dr. Caleb Sterling (Microelectronics & Computational Systems Researcher)
"""

import os
import sys
import json
import time
import socket
import threading
import webbrowser
import traceback
import subprocess
import urllib.request
from datetime import datetime
from flask import Flask, render_template, send_from_directory, jsonify, request
import numpy as np

# Ensure localhost bypasses any system proxies
os.environ['NO_PROXY'] = 'localhost,127.0.0.1'
os.environ['no_proxy'] = 'localhost,127.0.0.1'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESULTS_DIR = os.path.join(BASE_DIR, 'results')
DATA_DIR = os.path.join(BASE_DIR, 'data')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
LOG_FILE = os.path.join(BASE_DIR, 'startup.log')

app = Flask(__name__,
            static_folder=STATIC_DIR,
            template_folder=TEMPLATES_DIR)


def append_startup_log(msg):
    """Append a message to startup.log."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {msg}"
    try:
        with open(LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(line + "\n")
    except Exception:
        pass


@app.route('/')
def index():
    """Serves the master presentation interface."""
    if os.path.exists(os.path.join(TEMPLATES_DIR, 'index.html')):
        return render_template('index.html')
    return send_from_directory(BASE_DIR, 'index.html')


@app.route('/results/<path:filename>')
def serve_results(filename):
    """Serves generated plots from results/."""
    return send_from_directory(RESULTS_DIR, filename)


@app.route('/data/<path:filename>')
def serve_data(filename):
    """Serves raw data and experiment tables from data/."""
    return send_from_directory(DATA_DIR, filename)


@app.route('/api/health', methods=['GET'])
def health():
    """System diagnostics and verification endpoint."""
    return jsonify({
        "status": "healthy",
        "project": "Semiconductors — The New Oil of the Future",
        "total_duration_sec": 165.0,
        "scenes_count": 7,
        "characters": [
            {"id": "theodore", "name": "Dr. Theodore Voss", "role": "Senior Semiconductor Research Scientist", "age": 38},
            {"id": "caleb", "name": "Dr. Caleb Sterling", "role": "Microelectronics & Computational Systems Researcher", "age": 29}
        ],
        "matlab_script": "SemiconductorAnalysis.m",
        "results_generated": os.path.exists(os.path.join(DATA_DIR, 'semiconductor_data.json'))
    })


@app.route('/api/data', methods=['GET'])
def get_data():
    """Returns the full semiconductor experiments JSON results."""
    json_path = os.path.join(DATA_DIR, 'semiconductor_data.json')
    if os.path.exists(json_path):
        with open(json_path, 'r', encoding='utf-8') as f:
            return jsonify(json.load(f))
    return jsonify({"error": "Dataset not found"}), 404


@app.route('/api/calculate', methods=['POST'])
def calculate_api():
    """Live scientific computation endpoint."""
    req = request.get_json(force=True) or {}
    exp_type = req.get('experiment', 'diode')

    if exp_type == 'diode':
        vd = float(req.get('vd', 0.70))
        Is = 1.0e-14
        n = 1.05
        Vt = 0.02585
        arg = min(vd / (n * Vt), 45.0)
        Id = Is * (np.exp(arg) - 1.0)
        return jsonify({
            "experiment": "diode",
            "V_D_V": vd,
            "I_D_A": float(Id),
            "I_D_mA": float(Id * 1e3)
        })

    elif exp_type == 'mosfet':
        vgs = float(req.get('vgs', 1.2))
        vds = float(req.get('vds', 1.0))
        Vth = 0.40
        W_L = 20.0
        k_prime = 5.18e-4
        V_ov = max(0.0, vgs - Vth)
        if vgs <= Vth:
            Id = 0.0
            region = "Cutoff"
        elif vds < V_ov:
            Id = k_prime * W_L * (V_ov * vds - 0.5 * (vds**2))
            region = "Linear"
        else:
            lambda_param = 0.04
            Id = 0.5 * k_prime * W_L * (V_ov**2) * (1.0 + lambda_param * (vds - V_ov))
            region = "Saturation"
        return jsonify({
            "experiment": "mosfet",
            "region": region,
            "I_D_mA": float(Id * 1e3)
        })

    elif exp_type == 'power':
        vdd = float(req.get('vdd', 1.0))
        freq_ghz = float(req.get('freq_ghz', 3.0))
        alpha = 0.15
        C_eff = 2.5e-9
        P_dyn = alpha * C_eff * (vdd**2) * (freq_ghz * 1e9)
        return jsonify({
            "experiment": "power",
            "P_dyn_W": float(P_dyn)
        })

    elif exp_type == 'yield':
        area_mm2 = float(req.get('area_mm2', 150.0))
        d0 = float(req.get('d0', 0.08))
        A_cm2 = area_mm2 / 100.0
        Y_poisson = np.exp(-d0 * A_cm2) * 100.0
        return jsonify({
            "experiment": "yield",
            "yield_pct": float(Y_poisson)
        })

    return jsonify({"error": "Unknown experiment type"}), 400


@app.route('/api/run-matlab', methods=['GET', 'POST'])
def trigger_matlab_computation():
    """Triggers execution of matlab_runner.py (native MATLAB or verified Python fallback)."""
    runner_script = os.path.join(BASE_DIR, 'matlab_runner.py')
    try:
        proc = subprocess.run([sys.executable, runner_script], capture_output=True, text=True, check=True)
        return jsonify({
            "status": "success",
            "message": "Computational suite completed successfully.",
            "output": proc.stdout
        })
    except subprocess.CalledProcessError as e:
        return jsonify({
            "status": "error",
            "message": f"Computation failed: {e.stderr}"
        }), 500


def wait_and_open_browser(port=5000, timeout=12.0):
    """
    Poller running in a background thread.
    Waits until the Flask server successfully serves http://127.0.0.1:port/
    before launching the browser, preventing blank screens or connection errors.
    """
    url = f"http://127.0.0.1:{port}/"
    start_time = time.time()
    opened = False

    proxy_handler = urllib.request.ProxyHandler({})
    opener = urllib.request.build_opener(proxy_handler)

    while time.time() - start_time < timeout:
        time.sleep(0.3)
        try:
            with opener.open(f"http://127.0.0.1:{port}/api/health", timeout=1.0) as resp:
                if resp.status == 200:
                    append_startup_log(f"Server Startup Status: Operational (HTTP 200 confirmed at {url})")
                    print(f"\n[Startup] Presentation server ready. Launching browser to {url} ...")
                    webbrowser.open(url)
                    opened = True
                    append_startup_log(f"Browser Launch Status: Successfully opened {url} in default browser.")
                    break
        except Exception:
            continue

    if not opened:
        append_startup_log(f"Browser Launch Status: Timed out waiting for server at {url}")
        print(f"\n[Startup Warning] Server took longer than {timeout}s to respond. Please navigate to {url} manually.")


def start_server():
    """Starts the Flask presentation server with logging and error handling."""
    host = '127.0.0.1'
    port = int(os.environ.get('PORT', 5000))
    
    append_startup_log(f"Flask Startup Command: python app.py (Host: {host}, Port: {port})")

    # Start browser readiness poller thread (suppressible with NO_BROWSER=1)
    if os.environ.get('NO_BROWSER', '0') != '1':
        browser_thread = threading.Thread(target=wait_and_open_browser, args=(port,), daemon=True)
        browser_thread.start()

    print("========================================================================")
    print(" SEMICONDUCTORS — THE NEW OIL OF THE FUTURE")
    print(" An Academic Presentation & Computational Microelectronics Suite")
    print(f" Serving at: http://{host}:{port}/")
    print(f" Local address: http://localhost:{port}/")
    print(" Press Ctrl+C in this console window to terminate the server.")
    print("========================================================================")

    try:
        app.run(host=host, port=port, debug=False)
    except OSError as e:
        err_msg = f"Port {port} binding error: {e}"
        print(f"\n[FATAL ERROR] {err_msg}")
        append_startup_log(f"[FATAL ERROR] {err_msg}")
        append_startup_log(traceback.format_exc())
        sys.exit(1)
    except Exception as e:
        err_msg = f"Unexpected Flask exception: {e}"
        print(f"\n[FATAL ERROR] {err_msg}")
        append_startup_log(f"[FATAL ERROR] {err_msg}")
        append_startup_log(traceback.format_exc())
        sys.exit(1)


if __name__ == '__main__':
    start_server()
