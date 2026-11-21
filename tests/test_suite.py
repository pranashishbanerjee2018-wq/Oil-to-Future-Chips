#!/usr/bin/env python3
"""
AUTOMATED VERIFICATION & TEST SUITE
Project: "Semiconductors — The New Oil of the Future"
Authors: Dr. Theodore Voss & Dr. Caleb Sterling
"""

import os
import sys
import json
import csv
import unittest

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

class TestSemiconductorProject(unittest.TestCase):

    def test_01_required_files_exist(self):
        """Verify all critical files and directories exist."""
        required_files = [
            "index.html",
            "README.md",
            ".nojekyll",
            "app.py",
            "start.bat",
            "startup_check.py",
            "startup.log",
            "requirements.txt",
            "generate_assets.py",
            "generate_svgs.py",
            "matlab_runner.py",
            "SemiconductorAnalysis.m",
            os.path.join("data", "semiconductor_data.json"),
            os.path.join("data", "semiconductor_results.csv"),
            os.path.join("results", "plot1_diode_iv.png"),
            os.path.join("results", "plot2_mosfet_output.png"),
            os.path.join("results", "plot3_cmos_power.png"),
            os.path.join("results", "plot4_yield_model.png"),
            os.path.join("results", "plot5_moores_law.png"),
            os.path.join("static", "css", "main.css"),
            os.path.join("static", "css", "characters.css"),
            os.path.join("static", "css", "scenes.css"),
            os.path.join("static", "css", "dashboard.css"),
            os.path.join("static", "js", "app.js"),
            os.path.join("static", "js", "characters.js"),
            os.path.join("static", "js", "dialogue.js"),
            os.path.join("static", "js", "timeline.js"),
            os.path.join("static", "js", "audio.js"),
            os.path.join("static", "js", "matlab_dashboard.js"),
            os.path.join("static", "js", "scene_visuals.js"),
            os.path.join("static", "audio", "bg_music.wav"),
            os.path.join("static", "audio", "ambient_lab.wav"),
            os.path.join("static", "images", "energy_bands.svg"),
            os.path.join("static", "images", "silicon_lattice.svg"),
            os.path.join("static", "images", "pn_junction.svg"),
            os.path.join("static", "images", "mosfet_structure.svg"),
            os.path.join("static", "images", "wafer_fab_pipeline.svg"),
            os.path.join("static", "images", "future_tech_stack.svg")
        ]
        for rel_path in required_files:
            full_path = os.path.join(PROJECT_ROOT, rel_path)
            self.assertTrue(os.path.exists(full_path), f"Missing required file: {rel_path}")

    def test_02_timeline_and_seven_scenes(self):
        """Verify timeline is exactly 165 seconds and has exactly 7 scenes."""
        dialogue_js = os.path.join(PROJECT_ROOT, "static", "js", "dialogue.js")
        with open(dialogue_js, "r", encoding="utf-8") as f:
            content = f.read()

        # Parse PRESENTATION_TIMELINE JSON slice or inspect values
        self.assertIn("totalDuration: 165.0", content)
        self.assertIn('title: "THE INVISIBLE POWER RUNNING THE WORLD"', content)
        self.assertIn('title: "THE SCIENCE INSIDE A SEMICONDUCTOR"', content)
        self.assertIn('title: "FROM TRANSISTORS TO MICROPROCESSORS"', content)
        self.assertIn('title: "HOW A CHIP IS ACTUALLY MANUFACTURED"', content)
        self.assertIn('title: "MATLAB: THE MATHEMATICS INSIDE MICROELECTRONICS"', content)
        self.assertIn('title: "THE FUTURE OF SEMICONDUCTOR TECHNOLOGY"', content)
        self.assertIn('title: "THE NEXT INDUSTRIAL REVOLUTION"', content)

    def test_03_character_identities(self):
        """Verify new character identities and ensure no previous names are used."""
        forbidden_names = [
            "Adrian Reynolds", "Ethan Carter", "Nathaniel Brooks", "Julian Hayes",
            "Sebastian Clarke", "Oliver Bennett", "Alexander Whitmore", "Vincent Hale"
        ]
        for root, _, files in os.walk(PROJECT_ROOT):
            for file in files:
                if file.endswith(('.js', '.html', '.py', '.m', '.md')) and file != 'test_suite.py':
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        txt = f.read()
                        for forbidden in forbidden_names:
                            self.assertNotIn(forbidden, txt, f"Found forbidden name {forbidden} in {file}")

        # Ensure correct characters are present
        char_js = os.path.join(PROJECT_ROOT, "static", "js", "characters.js")
        with open(char_js, "r", encoding="utf-8") as f:
            char_content = f.read()
            self.assertIn("Dr. Theodore Voss", char_content)
            self.assertIn("Dr. Caleb Sterling", char_content)
            # Verify 5 visemes
            for viseme in ['REST', 'OPEN', 'ROUND', 'WIDE', 'MID']:
                self.assertIn(f"viseme-{viseme}", char_content)

    def test_04_matlab_data_and_physics_accuracy(self):
        """Verify scientific computations, physical constants and CSV/JSON output."""
        data_json = os.path.join(PROJECT_ROOT, "data", "semiconductor_data.json")
        with open(data_json, "r", encoding="utf-8") as f:
            data = json.load(f)

        meta = data.get("metadata", {})
        self.assertAlmostEqual(meta.get("temperature_K"), 300.0, places=1)
        self.assertAlmostEqual(meta.get("thermal_voltage_V"), 0.02585, places=3)

        # Diode parameters
        d_data = data.get("experiment1_diode", {})
        self.assertEqual(d_data.get("turn_on_knee_V"), 0.70)
        self.assertAlmostEqual(d_data.get("I_s_A"), 1.0e-14)

        # MOSFET parameters
        m_data = data.get("experiment2_mosfet", {})
        self.assertEqual(m_data.get("V_TH_V"), 0.40)
        self.assertEqual(m_data.get("W_over_L"), 20.0)

        # CSV checks
        csv_path = os.path.join(PROJECT_ROOT, "data", "semiconductor_results.csv")
        with open(csv_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = {r["Metric"]: r for r in reader}
            self.assertIn("Thermal_Voltage_300K", rows)
            self.assertIn("Diode_TurnOn_Knee", rows)
            self.assertIn("MOSFET_VTH", rows)
            self.assertIn("CMOS_Power_1V_3GHz", rows)
            self.assertIn("Modern_Max_Transistors", rows)

    def test_05_flask_app_routes(self):
        """Test Flask server routes and API calculation endpoints."""
        from app import app
        client = app.test_client()

        # Health endpoint
        res = client.get('/api/health')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data["total_duration_sec"], 165.0)
        self.assertEqual(data["scenes_count"], 7)

        # Calculate diode endpoint
        res = client.post('/api/calculate', json={"experiment": "diode", "vd": 0.70})
        self.assertEqual(res.status_code, 200)
        calc_res = res.get_json()
        self.assertIn("I_D_mA", calc_res)
        self.assertGreater(calc_res["I_D_mA"], 0.1)

        # Calculate MOSFET endpoint
        res = client.post('/api/calculate', json={"experiment": "mosfet", "vgs": 1.2, "vds": 1.0})
        self.assertEqual(res.status_code, 200)
        mos_res = res.get_json()
        self.assertEqual(mos_res["region"], "Saturation")

        # Static assets served
        res = client.get('/results/plot1_diode_iv.png')
        self.assertEqual(res.status_code, 200)
        self.assertGreater(len(res.data), 1000)

if __name__ == '__main__':
    unittest.main()
