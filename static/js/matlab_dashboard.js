/**
 * MATLAB ENGINEERING RESULTS & INTERACTIVE DASHBOARD CONTROLLER
 * Project: "Semiconductors — The New Oil of the Future"
 * Authors: Dr. Theodore Voss & Dr. Caleb Sterling
 */

class MatlabDashboard {
  constructor() {
    this.modal = document.getElementById('matlab-modal');
    this.data = null;
    this.activeTab = 'tab-exp1';
    this.isLoaded = false;
  }

  init() {
    this.loadData();
    this.bindEvents();
    this.initCalculators();
    console.log('[DASHBOARD] MATLAB engineering dashboard initialized.');
  }

  loadData() {
    fetch('data/semiconductor_data.json')
      .then(res => res.json())
      .then(data => {
        this.data = data;
        this.isLoaded = true;
        this.updateMetadata(data.metadata);
        console.log('[DASHBOARD] Semiconductor engineering data loaded.');
      })
      .catch(err => {
        console.warn('[DASHBOARD] Using embedded local engineering dataset:', err);
        this.isLoaded = true;
      });
  }

  updateMetadata(meta) {
    if (!meta) return;
    const engineEl = document.getElementById('dash-engine-status');
    const thermalEl = document.getElementById('dash-thermal-vt');
    if (engineEl) engineEl.textContent = meta.engine || 'MATLAB 2024 / Certified Python Engine';
    if (thermalEl && meta.thermal_voltage_V) {
      thermalEl.textContent = `${(meta.thermal_voltage_V * 1000).toFixed(2)} mV (${meta.temperature_K} K)`;
    }
  }

  bindEvents() {
    // Open/Close buttons
    const openBtn = document.getElementById('btn-open-matlab');
    const closeBtn = document.getElementById('btn-close-matlab');
    if (openBtn) {
      openBtn.addEventListener('click', () => this.open());
    }
    if (closeBtn) {
      closeBtn.addEventListener('click', () => this.close());
    }

    // Tab buttons
    const tabButtons = document.querySelectorAll('.dash-tab-btn');
    tabButtons.forEach(btn => {
      btn.addEventListener('click', (e) => {
        tabButtons.forEach(b => b.classList.remove('active'));
        document.querySelectorAll('.dash-tab-content').forEach(c => c.classList.remove('active'));
        
        btn.classList.add('active');
        const tabTarget = btn.getAttribute('data-tab');
        const contentEl = document.getElementById(tabTarget);
        if (contentEl) contentEl.classList.add('active');
        this.activeTab = tabTarget;
        if (window.soundEngine) window.soundEngine.playClick();
      });
    });
  }

  open() {
    if (!this.modal) return;
    this.modal.classList.add('active');
    if (window.soundEngine) {
      window.soundEngine.playCalcChime();
    }
  }

  close() {
    if (!this.modal) return;
    this.modal.classList.remove('active');
    if (window.soundEngine) window.soundEngine.playClick();
  }

  initCalculators() {
    // -------------------------------------------------------------
    // CALCULATOR 1: Diode Shockley Equation
    // I_D = I_S * [exp(q*V_D / (n*k*T)) - 1]
    // -------------------------------------------------------------
    const vdSlider = document.getElementById('calc-vd-slider');
    const vdVal = document.getElementById('calc-vd-val');
    const diodeOut = document.getElementById('calc-diode-out');
    const diodeStatus = document.getElementById('calc-diode-status');

    const updateDiode = () => {
      if (!vdSlider) return;
      const vd = parseFloat(vdSlider.value);
      if (vdVal) vdVal.textContent = `${vd.toFixed(2)} V`;
      
      const Is = 1e-14;
      const n = 1.05;
      const Vt = 0.02585;
      const arg = Math.min(vd / (n * Vt), 40.0);
      const I_amps = Is * (Math.exp(arg) - 1.0);
      const I_mA = I_amps * 1e3;

      if (diodeOut) {
        if (Math.abs(I_mA) < 1e-3) {
          diodeOut.textContent = `${(I_amps * 1e9).toFixed(3)} nA`;
        } else {
          diodeOut.textContent = `${I_mA.toFixed(3)} mA`;
        }
      }

      if (diodeStatus) {
        if (vd < 0) {
          diodeStatus.textContent = 'Reverse Bias (Saturation Current ~ -10 fA)';
          diodeStatus.style.color = '#94a3b8';
        } else if (vd < 0.65) {
          diodeStatus.textContent = 'Sub-Threshold / Weak Conduction';
          diodeStatus.style.color = '#fbbf24';
        } else {
          diodeStatus.textContent = 'Active Forward Conduction (Exponential Regime)';
          diodeStatus.style.color = '#34d399';
        }
      }
    };

    if (vdSlider) {
      vdSlider.addEventListener('input', updateDiode);
      updateDiode();
    }

    // -------------------------------------------------------------
    // CALCULATOR 2: MOSFET
    // -------------------------------------------------------------
    const vgsSlider = document.getElementById('calc-vgs-slider');
    const vdsSlider = document.getElementById('calc-vds-slider');
    const vgsVal = document.getElementById('calc-vgs-val');
    const vdsVal = document.getElementById('calc-vds-val');
    const mosfetOut = document.getElementById('calc-mosfet-out');
    const mosfetRegion = document.getElementById('calc-mosfet-region');

    const updateMosfet = () => {
      if (!vgsSlider || !vdsSlider) return;
      const vgs = parseFloat(vgsSlider.value);
      const vds = parseFloat(vdsSlider.value);
      if (vgsVal) vgsVal.textContent = `${vgs.toFixed(2)} V`;
      if (vdsVal) vdsVal.textContent = `${vds.toFixed(2)} V`;

      const Vth = 0.40;
      const W_L = 20.0;
      const k_prime = 450 * (3.9 * 8.854e-14 / 3e-7); // ~5.18e-4 A/V2
      const V_ov = Math.max(0, vgs - Vth);
      let Id = 0;
      let region = 'Cutoff (V_GS < V_TH)';

      if (vgs <= Vth) {
        Id = 0;
        region = 'Cutoff (Channel Not Inverted)';
      } else if (vds < V_ov) {
        // Linear
        Id = k_prime * W_L * (V_ov * vds - 0.5 * vds * vds);
        region = `Linear / Triode (V_DS < V_OV = ${V_ov.toFixed(2)} V)`;
      } else {
        // Saturation
        const lambda = 0.04;
        Id = 0.5 * k_prime * W_L * (V_ov * V_ov) * (1.0 + lambda * (vds - V_ov));
        region = `Saturation / Pinch-Off (V_DS ≥ V_OV = ${V_ov.toFixed(2)} V)`;
      }

      const Id_mA = Id * 1e3;
      if (mosfetOut) mosfetOut.textContent = `${Id_mA.toFixed(3)} mA`;
      if (mosfetRegion) {
        mosfetRegion.textContent = region;
        mosfetRegion.style.color = (vgs <= Vth) ? '#f87171' : (vds < V_ov ? '#38bdf8' : '#34d399');
      }
    };

    if (vgsSlider && vdsSlider) {
      vgsSlider.addEventListener('input', updateMosfet);
      vdsSlider.addEventListener('input', updateMosfet);
      updateMosfet();
    }

    // -------------------------------------------------------------
    // CALCULATOR 3: CMOS Dynamic Power P = alpha * C * V^2 * f
    // -------------------------------------------------------------
    const vddSlider = document.getElementById('calc-vdd-slider');
    const freqSlider = document.getElementById('calc-freq-slider');
    const vddVal = document.getElementById('calc-vdd-val');
    const freqVal = document.getElementById('calc-freq-val');
    const powerOut = document.getElementById('calc-power-out');

    const updatePower = () => {
      if (!vddSlider || !freqSlider) return;
      const vdd = parseFloat(vddSlider.value);
      const freq = parseFloat(freqSlider.value); // GHz
      if (vddVal) vddVal.textContent = `${vdd.toFixed(2)} V`;
      if (freqVal) freqVal.textContent = `${freq.toFixed(1)} GHz`;

      const alpha = 0.15;
      const C_eff = 2.5e-9; // 2.5 nF
      const f_hz = freq * 1e9;
      const P_dyn = alpha * C_eff * (vdd * vdd) * f_hz;

      if (powerOut) {
        powerOut.textContent = `${P_dyn.toFixed(3)} W`;
      }
    };

    if (vddSlider && freqSlider) {
      vddSlider.addEventListener('input', updatePower);
      freqSlider.addEventListener('input', updatePower);
      updatePower();
    }

    // -------------------------------------------------------------
    // CALCULATOR 4: Wafer Yield Y = exp(-D0 * A)
    // -------------------------------------------------------------
    const areaSlider = document.getElementById('calc-area-slider');
    const d0Slider = document.getElementById('calc-d0-slider');
    const areaVal = document.getElementById('calc-area-val');
    const d0Val = document.getElementById('calc-d0-val');
    const yieldOut = document.getElementById('calc-yield-out');
    const diesOut = document.getElementById('calc-dies-out');

    const updateYield = () => {
      if (!areaSlider || !d0Slider) return;
      const area_mm2 = parseFloat(areaSlider.value);
      const d0 = parseFloat(d0Slider.value);
      if (areaVal) areaVal.textContent = `${area_mm2.toFixed(0)} mm²`;
      if (d0Val) d0Val.textContent = `${d0.toFixed(2)} def/cm²`;

      const area_cm2 = area_mm2 / 100.0;
      const Y_poisson = Math.exp(-d0 * area_cm2) * 100.0;
      
      // 300mm wafer gross die estimation
      // Gross Dies = (pi * R^2 / A) - (pi * 2R / sqrt(2*A))
      const R_mm = 150.0;
      const grossDies = Math.floor((Math.PI * R_mm * R_mm / area_mm2) - (Math.PI * 2 * R_mm / Math.sqrt(2 * area_mm2)));
      const netDies = Math.floor(grossDies * (Y_poisson / 100.0));

      if (yieldOut) {
        yieldOut.textContent = `${Y_poisson.toFixed(1)}%`;
        yieldOut.style.color = (Y_poisson > 75) ? '#34d399' : (Y_poisson > 40 ? '#fbbf24' : '#f87171');
      }
      if (diesOut) {
        diesOut.textContent = `~${netDies} Good Dies / 300mm Wafer (Gross: ${grossDies})`;
      }
    };

    if (areaSlider && d0Slider) {
      areaSlider.addEventListener('input', updateYield);
      d0Slider.addEventListener('input', updateYield);
      updateYield();
    }
  }
}

window.matlabDashboard = new MatlabDashboard();
