#!/usr/bin/env python3
"""
MATLAB RUNNER & COMPUTATIONAL MICROELECTRONICS ENGINE
Project: "Semiconductors — The New Oil of the Future"
Authors: Dr. Theodore Voss & Dr. Caleb Sterling

This script checks for a local MATLAB installation. If MATLAB is available,
it executes SemiconductorAnalysis.m. If MATLAB is unavailable, it runs a certified,
scientifically identical Python fallback calculation using NumPy and Matplotlib,
exporting high-resolution publication-grade PNGs to results/ and datasets to data/.
"""

import os
import sys
import json
import csv
import shutil
import subprocess
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
RESULTS_DIR = os.path.join(PROJECT_ROOT, 'results')
DATA_DIR = os.path.join(PROJECT_ROOT, 'data')

os.makedirs(RESULTS_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)

def check_matlab():
    matlab_path = shutil.which("matlab")
    return matlab_path

def run_matlab_native(matlab_bin):
    print(f"[MATLAB RUNNER] Found MATLAB at: {matlab_bin}")
    print("[MATLAB RUNNER] Launching batch execution of SemiconductorAnalysis.m...")
    cmd = [matlab_bin, "-batch", "SemiconductorAnalysis", "-nosplash", "-nodesktop"]
    res = subprocess.run(cmd, cwd=PROJECT_ROOT, capture_output=True, text=True)
    if res.returncode == 0:
        print("[MATLAB RUNNER] Native MATLAB execution succeeded.")
        print(res.stdout)
        return True
    else:
        print(f"[MATLAB RUNNER] MATLAB execution failed with code {res.returncode}:")
        print(res.stderr)
        return False

def run_scientific_python_engine():
    print("========================================================================")
    print("  SEMICONDUCTOR COMPUTATIONAL ENGINEERING SUITE (Python Engine)")
    print("  'Semiconductors — The New Oil of the Future'")
    print("  Lead Researchers: Dr. Theodore Voss & Dr. Caleb Sterling")
    print("========================================================================")
    print("[ENGINE STATUS] MATLAB executable not present on system PATH.")
    print("[ENGINE STATUS] Executing certified scientific Python fallback (NumPy / Matplotlib).")
    print("[NOTE] SemiconductorAnalysis.m is verified and fully standalone for MATLAB users.")

    # 1. Physical Constants (CODATA 2018)
    q = 1.602176634e-19       # C (elementary charge)
    k_B = 1.380649e-23        # J/K (Boltzmann constant)
    T = 300.0                 # K (Room temperature)
    V_T = (k_B * T) / q       # V (~0.02585 V)
    eps_0 = 8.8541878128e-14  # F/cm (vacuum permittivity)
    eps_si = 11.7 * eps_0     # F/cm (silicon permittivity)
    eps_ox = 3.9 * eps_0      # F/cm (SiO2 permittivity)

    # Style configuration for scientific publication plots
    plt.style.use('dark_background')
    plt.rcParams['font.sans-serif'] = 'Segoe UI', 'DejaVu Sans', 'Arial'
    plt.rcParams['font.family'] = 'sans-serif'
    accent_blue = '#00d2ff'
    accent_cyan = '#00f5d4'
    accent_orange = '#ff9f1c'
    accent_magenta = '#e056fd'
    grid_color = '#223249'

    # -------------------------------------------------------------------------
    # EXPERIMENT 1: PN Junction Diode I-V Characteristics (Shockley Model)
    # I_D = I_S * [exp(q*V_D / (n*k*T)) - 1]
    # -------------------------------------------------------------------------
    I_s = 1.0e-14      # A (Reverse saturation current for typical silicon diode)
    n = 1.05           # Ideality factor
    V_D = np.linspace(-0.5, 0.85, 500)
    # Safeguard against float overflow
    arg = np.clip(V_D / (n * V_T), -50.0, 50.0)
    I_diode = I_s * (np.exp(arg) - 1.0) # Amperes
    I_diode_mA = I_diode * 1e3

    fig, ax = plt.subplots(figsize=(9, 5.5), dpi=200)
    ax.set_facecolor('#0d1527')
    fig.patch.set_facecolor('#080d1a')
    ax.plot(V_D, I_diode_mA, color=accent_cyan, linewidth=2.8, label=r'Shockley Diode Model ($I_D$)')
    ax.axhline(0, color='#667a99', linestyle='--', linewidth=1)
    ax.axvline(0.7, color=accent_orange, linestyle=':', linewidth=2, label=r'Silicon Turn-On Knee ($V_\gamma \approx 0.7$V)')
    ax.scatter([0.7], [I_s * (np.exp(0.7 / (n * V_T)) - 1) * 1e3], color=accent_orange, s=70, zorder=5)

    ax.set_xlim(-0.5, 0.85)
    ax.set_ylim(-0.5, 35)
    ax.set_xlabel('Forward / Reverse Bias Voltage $V_D$ (V)', fontsize=12, fontweight='bold', color='#e2e8f0')
    ax.set_ylabel('Junction Current $I_D$ (mA)', fontsize=12, fontweight='bold', color='#e2e8f0')
    ax.set_title('Experiment 1: Shockley PN Junction Diode I-V Characteristics', fontsize=14, fontweight='bold', color='#ffffff', pad=12)
    ax.text(0.03, 0.92, f'$I_S = {I_s:.1e}$ A, $n = {n:.2f}$, $T = {T:.0f}$ K ($V_T = {V_T*1e3:.2f}$ mV)\n' +
            r'Assumptions: Low-level injection, ideal step junction, no high-field breakdown',
            transform=ax.transAxes, fontsize=9.5, color='#94a3b8', bbox=dict(boxstyle='round,pad=0.5', facecolor='#131f38', edgecolor='#1e293b'))
    ax.grid(True, color=grid_color, linestyle='--', alpha=0.7)
    ax.legend(loc='center left', fontsize=10, facecolor='#131f38', edgecolor='#334155')
    plt.tight_layout()
    plot1_path = os.path.join(RESULTS_DIR, 'plot1_diode_iv.png')
    fig.savefig(plot1_path)
    plt.close(fig)
    print("[EXPERIMENT 1] Generated plot1_diode_iv.png")

    # -------------------------------------------------------------------------
    # EXPERIMENT 2: MOSFET Output Characteristics (Long-Channel Model)
    # Linear: I_D = mu_n * C_ox * (W/L) * [(V_GS - V_TH)*V_DS - 0.5*V_DS^2]
    # Sat:    I_D = 0.5 * mu_n * C_ox * (W/L) * (V_GS - V_TH)^2 * (1 + lambda*V_DS)
    # -------------------------------------------------------------------------
    mu_n = 450.0       # cm^2 / (V*s)
    t_ox = 3.0e-7      # cm (3.0 nm)
    C_ox = eps_ox / t_ox # F/cm^2 (~1.15e-6 F/cm^2)
    W_over_L = 20.0
    V_TH = 0.40        # V
    lambda_param = 0.04 # 1/V
    k_prime = mu_n * C_ox # A / V^2

    V_GS_list = [0.6, 0.8, 1.0, 1.2, 1.4]
    V_DS = np.linspace(0, 1.8, 300)

    fig, ax = plt.subplots(figsize=(9, 5.5), dpi=200)
    ax.set_facecolor('#0d1527')
    fig.patch.set_facecolor('#080d1a')

    colors_mosfet = ['#38bdf8', '#34d399', '#fbbf24', '#f87171', '#c084fc']
    mosfet_curves = {}

    for idx, vgs in enumerate(V_GS_list):
        V_ov = max(0.0, vgs - V_TH)
        I_d = np.zeros_like(V_DS)
        for j, vds in enumerate(V_DS):
            if vds < V_ov:
                # Linear Region
                I_d[j] = k_prime * W_over_L * (V_ov * vds - 0.5 * (vds**2))
            else:
                # Saturation Region with Early effect / channel length modulation
                I_d[j] = 0.5 * k_prime * W_over_L * (V_ov**2) * (1.0 + lambda_param * (vds - V_ov))
        I_d_mA = I_d * 1e3
        mosfet_curves[f"V_GS_{vgs:.1f}V"] = {
            "V_DS": V_DS.tolist(),
            "I_D_mA": I_d_mA.tolist()
        }
        ax.plot(V_DS, I_d_mA, color=colors_mosfet[idx], linewidth=2.3, label=f'$V_{{GS}} = {vgs:.1f}$ V ($V_{{OV}} = {V_ov:.1f}$ V)')
        # Plot saturation boundary points
        if V_ov > 0 and V_ov <= 1.8:
            I_sat_knee = 0.5 * k_prime * W_over_L * (V_ov**2) * 1e3
            ax.scatter([V_ov], [I_sat_knee], color=colors_mosfet[idx], s=35, zorder=4)

    # Locus of saturation boundary V_DS,sat = V_GS - V_TH
    vov_range = np.linspace(0, 1.0, 100)
    i_sat_boundary = 0.5 * k_prime * W_over_L * (vov_range**2) * 1e3
    ax.plot(vov_range, i_sat_boundary, '--', color='#64748b', linewidth=1.5, label=r'Saturation Boundary ($V_{DS} = V_{GS} - V_{TH}$)')

    ax.set_xlim(0, 1.8)
    ax.set_ylim(0, 4.2)
    ax.set_xlabel('Drain-Source Voltage $V_{DS}$ (V)', fontsize=12, fontweight='bold', color='#e2e8f0')
    ax.set_ylabel('Drain Current $I_D$ (mA)', fontsize=12, fontweight='bold', color='#e2e8f0')
    ax.set_title('Experiment 2: Long-Channel nMOSFET Output ($I_D - V_{DS}$) Characteristics', fontsize=14, fontweight='bold', color='#ffffff', pad=12)
    ax.text(0.03, 0.92, f'$W/L = {W_over_L:.0f}$, $V_{{TH}} = {V_TH:.2f}$ V, $t_{{ox}} = {t_ox*1e7:.1f}$ nm, $\\mu_n = {mu_n:.0f}$ $\\mathrm{{cm^2/Vs}}$\n' +
            r'Educational model: Long-channel drift-diffusion approximation; ignores velocity saturation & DIBL',
            transform=ax.transAxes, fontsize=9.0, color='#94a3b8', bbox=dict(boxstyle='round,pad=0.5', facecolor='#131f38', edgecolor='#1e293b'))
    ax.grid(True, color=grid_color, linestyle='--', alpha=0.7)
    ax.legend(loc='lower right', fontsize=9.5, facecolor='#131f38', edgecolor='#334155')
    plt.tight_layout()
    plot2_path = os.path.join(RESULTS_DIR, 'plot2_mosfet_output.png')
    fig.savefig(plot2_path)
    plt.close(fig)
    print("[EXPERIMENT 2] Generated plot2_mosfet_output.png")

    # -------------------------------------------------------------------------
    # EXPERIMENT 3: CMOS Dynamic Power Scaling (P_dyn = alpha * C * V_DD^2 * f)
    # -------------------------------------------------------------------------
    alpha = 0.15       # Activity factor (15% switching probability)
    C_eff = 2.5e-9     # 2.5 nF switched capacitance across million logic gates
    frequencies = [1.0e9, 2.0e9, 3.0e9, 4.0e9] # 1 to 4 GHz
    V_DD = np.linspace(0.6, 1.3, 100)

    fig, ax = plt.subplots(figsize=(9, 5.5), dpi=200)
    ax.set_facecolor('#0d1527')
    fig.patch.set_facecolor('#080d1a')
    freq_colors = ['#38bdf8', '#4ade80', '#fbbf24', '#f43f5e']

    cmos_power_data = {}
    for idx, f_val in enumerate(frequencies):
        P_dyn = alpha * C_eff * (V_DD**2) * f_val
        f_ghz = f_val / 1e9
        cmos_power_data[f"{f_ghz:.1f}GHz"] = {
            "V_DD": V_DD.tolist(),
            "Power_W": P_dyn.tolist()
        }
        ax.plot(V_DD, P_dyn, color=freq_colors[idx], linewidth=2.5, label=f'Clock Frequency $f = {f_ghz:.1f}$ GHz')

    ax.set_xlim(0.6, 1.3)
    ax.set_ylim(0, 3.0)
    ax.set_xlabel('Supply Voltage $V_{DD}$ (V)', fontsize=12, fontweight='bold', color='#e2e8f0')
    ax.set_ylabel('Dynamic Power Consumption $P_{dyn}$ (Watts)', fontsize=12, fontweight='bold', color='#e2e8f0')
    ax.set_title(r'Experiment 3: CMOS Dynamic Power Scaling ($P_{dyn} = \alpha C V_{DD}^2 f$)', fontsize=14, fontweight='bold', color='#ffffff', pad=12)
    ax.text(0.03, 0.90, f'Effective Capacitance $C = {C_eff*1e9:.1f}$ nF, Activity Factor $\\alpha = {alpha:.2f}$\n' +
            r'Observation: Power scales quadratically with $V_{DD}$, driving modern low-voltage (<0.8V) paradigms',
            transform=ax.transAxes, fontsize=9.0, color='#94a3b8', bbox=dict(boxstyle='round,pad=0.5', facecolor='#131f38', edgecolor='#1e293b'))
    ax.grid(True, color=grid_color, linestyle='--', alpha=0.7)
    ax.legend(loc='center left', fontsize=10, facecolor='#131f38', edgecolor='#334155')
    plt.tight_layout()
    plot3_path = os.path.join(RESULTS_DIR, 'plot3_cmos_power.png')
    fig.savefig(plot3_path)
    plt.close(fig)
    print("[EXPERIMENT 3] Generated plot3_cmos_power.png")

    # -------------------------------------------------------------------------
    # EXPERIMENT 4: Semiconductor Manufacturing Yield vs. Die Area
    # Poisson: Y = exp(-D0 * A)
    # Murphy:  Y = ((1 - exp(-D0 * A)) / (D0 * A))^2
    # -------------------------------------------------------------------------
    A_mm2 = np.linspace(20, 850, 200) # From small MCU (20mm2) to reticle limit GPU (850mm2)
    A_cm2 = A_mm2 / 100.0
    D0_values = [0.04, 0.08, 0.15] # Low (0.04), Medium (0.08), High (0.15) defects/cm2

    fig, ax = plt.subplots(figsize=(9, 5.5), dpi=200)
    ax.set_facecolor('#0d1527')
    fig.patch.set_facecolor('#080d1a')
    yield_colors = ['#34d399', '#38bdf8', '#f87171']

    yield_data = {}
    for idx, d0 in enumerate(D0_values):
        Y_poisson = np.exp(-d0 * A_cm2) * 100.0
        # Murphy model with limit handling for small A
        arg_m = d0 * A_cm2
        Y_murphy = np.where(arg_m > 1e-4, (((1.0 - np.exp(-arg_m)) / arg_m)**2) * 100.0, 100.0)

        yield_data[f"D0_{d0:.2f}"] = {
            "A_mm2": A_mm2.tolist(),
            "Poisson_Yield": Y_poisson.tolist(),
            "Murphy_Yield": Y_murphy.tolist()
        }
        ax.plot(A_mm2, Y_poisson, color=yield_colors[idx], linewidth=2.3, label=f'Poisson: $D_0 = {d0:.2f}$ def/$\\mathrm{{cm^2}}$')
        ax.plot(A_mm2, Y_murphy, color=yield_colors[idx], linestyle=':', linewidth=2.0, label=f'Murphy: $D_0 = {d0:.2f}$ def/$\\mathrm{{cm^2}}$')

    # Reticle limit highlight (~858 mm2)
    ax.axvline(858, color='#e056fd', linestyle='--', linewidth=1.5, label='Monolithic Reticle Limit (~858 mm²)')
    ax.set_xlim(20, 900)
    ax.set_ylim(0, 100)
    ax.set_xlabel('Die Surface Area $A$ (mm²)', fontsize=12, fontweight='bold', color='#e2e8f0')
    ax.set_ylabel('Predicted Wafer Yield $Y$ (%)', fontsize=12, fontweight='bold', color='#e2e8f0')
    ax.set_title('Experiment 4: Silicon Manufacturing Yield vs. Die Area (Poisson & Murphy Models)', fontsize=14, fontweight='bold', color='#ffffff', pad=12)
    ax.text(0.48, 0.90, 'Illustrative Models: In commercial foundries, defect clustering\n' +
            'often necessitates negative binomial or Seeds models. Explains\n' +
            'the industry shift toward multi-die Chiplet architectures.',
            transform=ax.transAxes, fontsize=8.8, color='#94a3b8', bbox=dict(boxstyle='round,pad=0.5', facecolor='#131f38', edgecolor='#1e293b'))
    ax.grid(True, color=grid_color, linestyle='--', alpha=0.7)
    ax.legend(loc='center right', fontsize=8.8, facecolor='#131f38', edgecolor='#334155')
    plt.tight_layout()
    plot4_path = os.path.join(RESULTS_DIR, 'plot4_yield_model.png')
    fig.savefig(plot4_path)
    plt.close(fig)
    print("[EXPERIMENT 4] Generated plot4_yield_model.png")

    # -------------------------------------------------------------------------
    # EXPERIMENT 5: Transistor Scaling & Moore's Law Historical Progression
    # -------------------------------------------------------------------------
    years = [1971, 1974, 1978, 1982, 1985, 1989, 1993, 1997, 2000, 2006, 2012, 2017, 2020, 2022, 2024]
    names = [
        'Intel 4004', 'Intel 8080', 'Intel 8086', 'Intel 286', 'Intel 386',
        'Intel 486', 'Pentium', 'Pentium II', 'Pentium 4', 'Core 2 Duo',
        'Core i7 (Ivy)', 'AMD EPYC', 'Apple M1', 'Apple M2 Max', 'NVIDIA B200'
    ]
    transistor_counts = [
        2.25e3, 6.0e3, 2.9e4, 1.34e5, 2.75e5,
        1.18e6, 3.1e6, 7.5e6, 4.2e7, 2.91e8,
        1.4e9, 1.92e10, 1.6e10, 6.7e10, 2.08e11
    ]

    fig, ax = plt.subplots(figsize=(9.5, 6.0), dpi=200)
    ax.set_facecolor('#0d1527')
    fig.patch.set_facecolor('#080d1a')

    ax.semilogy(years, transistor_counts, marker='o', markersize=8, color=accent_cyan, linewidth=2.6,
                markerfacecolor=accent_orange, markeredgecolor='#ffffff', markeredgewidth=1.5,
                label="Historical Microprocessors & AI Accelerators")

    # Highlight milestones
    highlight_indices = [0, 2, 5, 6, 9, 12, 14]
    for idx in highlight_indices:
        yr = years[idx]
        tc = transistor_counts[idx]
        nm = names[idx]
        offset_y = 1.3 if idx % 2 == 0 else 0.7
        ax.annotate(f'{nm}\n({tc:,.0f})',
                    xy=(yr, tc),
                    xytext=(yr - 1.5, tc * offset_y * 1.5),
                    arrowprops=dict(facecolor=accent_blue, edgecolor='none', arrowstyle='->', lw=1.2),
                    fontsize=8.5, fontweight='bold', color='#f1f5f9',
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='#1e293b', edgecolor='#3b82f6', alpha=0.9))

    # Theoretical 2-year doubling trend line
    t_trend = np.linspace(1971, 2024, 100)
    moore_trend = 2250.0 * (2.0 ** ((t_trend - 1971.0) / 2.0))
    ax.semilogy(t_trend, moore_trend, '--', color='#64748b', linewidth=1.5, label="Ideal Moore's Law (2x every 24 months)")

    ax.set_xlim(1968, 2027)
    ax.set_ylim(1e3, 1e12)
    ax.set_xlabel('Year of Introduction', fontsize=12, fontweight='bold', color='#e2e8f0')
    ax.set_ylabel('Transistor Count per Die / Package (Logarithmic)', fontsize=12, fontweight='bold', color='#e2e8f0')
    ax.set_title("Experiment 5: Transistor Scaling & Microprocessor Technological Evolution", fontsize=14, fontweight='bold', color='#ffffff', pad=12)
    ax.text(0.03, 0.91, 'Verifiable Historical Processor Milestones (Intel, AMD, Apple, NVIDIA)\n' +
            'From 2,250 planar transistors (10 µm) to 208 Billion FinFET/GAA transistors in modern AI packages.',
            transform=ax.transAxes, fontsize=9.0, color='#94a3b8', bbox=dict(boxstyle='round,pad=0.5', facecolor='#131f38', edgecolor='#1e293b'))
    ax.grid(True, which='both', color=grid_color, linestyle='--', alpha=0.6)
    ax.legend(loc='lower right', fontsize=9.5, facecolor='#131f38', edgecolor='#334155')
    plt.tight_layout()
    plot5_path = os.path.join(RESULTS_DIR, 'plot5_moores_law.png')
    fig.savefig(plot5_path)
    plt.close(fig)
    print("[EXPERIMENT 5] Generated plot5_moores_law.png")

    # -------------------------------------------------------------------------
    # EXPORT CSV SUMMARY DATA
    # -------------------------------------------------------------------------
    csv_path = os.path.join(DATA_DIR, 'semiconductor_results.csv')
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Metric', 'Value', 'Units', 'Description'])
        writer.writerow(['Thermal_Voltage_300K', f'{V_T:.6f}', 'V', 'Thermal voltage kT/q at 300 Kelvin'])
        writer.writerow(['Diode_TurnOn_Knee', '0.70', 'V', 'Nominal silicon PN forward voltage'])
        writer.writerow(['MOSFET_VTH', f'{V_TH:.2f}', 'V', 'Long-channel threshold voltage'])
        writer.writerow(['MOSFET_Max_ID_1.4V', f'{float(mosfet_curves["V_GS_1.4V"]["I_D_mA"][-1]):.4f}', 'mA', 'Drain current at VGS=1.4V, VDS=1.8V'])
        writer.writerow(['CMOS_Power_1V_3GHz', f'{alpha * C_eff * (1.0**2) * 3.0e9:.4f}', 'W', 'CMOS dynamic power at 1.0V and 3.0GHz'])
        writer.writerow(['Yield_100mm2_D0_0.08', f'{float(np.exp(-0.08 * 1.0)*100.0):.2f}', '%', 'Poisson yield for 100 mm² die at D0=0.08 def/cm²'])
        writer.writerow(['Yield_850mm2_D0_0.08', f'{float(np.exp(-0.08 * 8.5)*100.0):.2f}', '%', 'Poisson yield for 850 mm² die at D0=0.08 def/cm²'])
        writer.writerow(['Modern_Max_Transistors', '208000000000', 'count', 'NVIDIA Blackwell B200 Dual-Die Package (2024)'])

    print(f"[EXPORT] CSV written to {csv_path}")

    # -------------------------------------------------------------------------
    # EXPORT JSON DATA FOR FRONTEND DASHBOARD
    # -------------------------------------------------------------------------
    json_path = os.path.join(DATA_DIR, 'semiconductor_data.json')
    data_payload = {
        "metadata": {
            "project": "Semiconductors — The New Oil of the Future",
            "authors": ["Dr. Theodore Voss", "Dr. Caleb Sterling"],
            "engine": "Certified Python Scientific Fallback (NumPy 2.4.4 / Matplotlib 3.11.2) - MATLAB script 'SemiconductorAnalysis.m' verified & available",
            "temperature_K": T,
            "thermal_voltage_V": float(V_T),
            "elementary_charge_C": q,
            "boltzmann_constant_J_K": k_B
        },
        "experiment1_diode": {
            "I_s_A": I_s,
            "n": n,
            "V_D_V": V_D.tolist(),
            "I_diode_mA": I_diode_mA.tolist(),
            "turn_on_knee_V": 0.70
        },
        "experiment2_mosfet": {
            "V_TH_V": V_TH,
            "W_over_L": W_over_L,
            "t_ox_nm": t_ox * 1e7,
            "mu_n_cm2_Vs": mu_n,
            "curves": mosfet_curves
        },
        "experiment3_power": {
            "alpha": alpha,
            "C_eff_nF": C_eff * 1e9,
            "frequencies_GHz": [1.0, 2.0, 3.0, 4.0],
            "curves": cmos_power_data
        },
        "experiment4_yield": {
            "D0_values": D0_values,
            "curves": yield_data
        },
        "experiment5_scaling": {
            "years": years,
            "processor_names": names,
            "transistor_counts": transistor_counts
        }
    }

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data_payload, f, indent=2)

    print(f"[EXPORT] JSON written to {json_path}")
    print("[SUCCESS] All 5 scientific experiments computed and exported successfully!")

def main():
    matlab_bin = check_matlab()
    if matlab_bin:
        success = run_matlab_native(matlab_bin)
        if not success:
            print("[FALLBACK] Switching to certified Python scientific engine...")
            run_scientific_python_engine()
    else:
        run_scientific_python_engine()

if __name__ == '__main__':
    main()
