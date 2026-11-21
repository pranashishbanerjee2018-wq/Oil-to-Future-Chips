/**
 * SCENE VISUALS & ANIMATED SCIENTIFIC BACKDROPS
 * Project: "Semiconductors — The New Oil of the Future"
 * Authors: Dr. Theodore Voss & Dr. Caleb Sterling
 */

class SceneVisualsManager {
  constructor() {
    this.stageEl = document.getElementById('scene-visuals-stage');
    this.activeSceneId = 1;
    this.canvas = null;
    this.ctx = null;
    this.animFrameId = null;
    this.circuitNodes = [];
  }

  init() {
    this.initCanvas();
    this.renderScene(1);
    console.log('[SCENE VISUALS] Scientific visual staging initialized.');
  }

  initCanvas() {
    this.canvas = document.getElementById('circuit-canvas');
    if (!this.canvas) return;
    this.ctx = this.canvas.getContext('2d');
    this.resizeCanvas();
    window.addEventListener('resize', () => this.resizeCanvas());

    // Generate circuit network particles
    this.circuitNodes = [];
    const count = 35;
    for (let i = 0; i < count; i++) {
      this.circuitNodes.push({
        x: Math.random() * this.canvas.width,
        y: Math.random() * this.canvas.height,
        vx: (Math.random() - 0.5) * 0.8,
        vy: (Math.random() - 0.5) * 0.8,
        radius: 1.5 + Math.random() * 2,
        pulse: Math.random() * Math.PI
      });
    }

    this.startCanvasAnimation();
  }

  resizeCanvas() {
    if (!this.canvas) return;
    this.canvas.width = window.innerWidth;
    this.canvas.height = window.innerHeight;
  }

  startCanvasAnimation() {
    const loop = () => {
      this.drawCircuits();
      this.animFrameId = requestAnimationFrame(loop);
    };
    this.animFrameId = requestAnimationFrame(loop);
  }

  drawCircuits() {
    if (!this.ctx || !this.canvas) return;
    const w = this.canvas.width;
    const h = this.canvas.height;
    this.ctx.clearRect(0, 0, w, h);

    // Subtle dark lab ambient
    this.ctx.fillStyle = 'rgba(8, 14, 30, 0.2)';
    this.ctx.fillRect(0, 0, w, h);

    // Connect close nodes with electric cyan lines
    for (let i = 0; i < this.circuitNodes.length; i++) {
      const p1 = this.circuitNodes[i];
      p1.x += p1.vx;
      p1.y += p1.vy;
      p1.pulse += 0.03;

      if (p1.x < 0 || p1.x > w) p1.vx *= -1;
      if (p1.y < 0 || p1.y > h) p1.vy *= -1;

      for (let j = i + 1; j < this.circuitNodes.length; j++) {
        const p2 = this.circuitNodes[j];
        const dist = Math.hypot(p1.x - p2.x, p1.y - p2.y);
        if (dist < 140) {
          const alpha = (1 - dist / 140) * 0.25;
          this.ctx.strokeStyle = `rgba(0, 245, 212, ${alpha})`;
          this.ctx.lineWidth = 1;
          this.ctx.beginPath();
          // Orthogonal circuit trace angle
          const midX = (p1.x + p2.x) / 2;
          this.ctx.moveTo(p1.x, p1.y);
          this.ctx.lineTo(midX, p1.y);
          this.ctx.lineTo(midX, p2.y);
          this.ctx.lineTo(p2.x, p2.y);
          this.ctx.stroke();
        }
      }

      // Draw node point
      const glow = (Math.sin(p1.pulse) + 1) / 2;
      this.ctx.fillStyle = `rgba(56, 189, 248, ${0.4 + glow * 0.5})`;
      this.ctx.beginPath();
      this.ctx.arc(p1.x, p1.y, p1.radius, 0, Math.PI * 2);
      this.ctx.fill();
    }
  }

  renderScene(sceneId) {
    this.activeSceneId = sceneId;
    if (!this.stageEl) return;

    let html = '';
    switch (sceneId) {
      case 1:
        html = `
          <div class="scene-visual-container scene-1-visual animate-fade-in">
            <div class="hud-center-chip">
              <div class="microprocessor-glow">
                <div class="die-core">
                  <div class="core-grid"></div>
                  <div class="die-label">SILICON CATALYST</div>
                  <div class="die-sub">100B+ TRANSISTORS</div>
                </div>
                <div class="bus-lines">
                  <span class="bus-line bus-top"></span>
                  <span class="bus-line bus-bottom"></span>
                  <span class="bus-line bus-left"></span>
                  <span class="bus-line bus-right"></span>
                </div>
              </div>
            </div>
            <div class="tech-ecosystem-cards">
              <div class="eco-card"><i class="icon-phone">📱</i> Smartphones</div>
              <div class="eco-card"><i class="icon-server">☁️</i> Data Centers</div>
              <div class="eco-card"><i class="icon-car">⚡</i> Electric Vehicles</div>
              <div class="eco-card"><i class="icon-brain">🤖</i> Artificial Intelligence</div>
              <div class="eco-card"><i class="icon-sat">🛰️</i> Aerospace Systems</div>
            </div>
            <div class="scene-quote-banner">
              "Just as oil powered the industrial age, semiconductors power the computational intelligence of the digital age."
            </div>
          </div>
        `;
        break;

      case 2:
        html = `
          <div class="scene-visual-container scene-2-visual animate-fade-in">
            <div class="diagrams-duo-wrapper">
              <div class="diagram-card">
                <img src="static/images/energy_bands.svg" alt="Energy Bands Structure" class="diagram-img"/>
              </div>
              <div class="diagram-card">
                <img src="static/images/silicon_lattice.svg" alt="Silicon Lattice & Doping" class="diagram-img"/>
              </div>
            </div>
          </div>
        `;
        break;

      case 3:
        html = `
          <div class="scene-visual-container scene-3-visual animate-fade-in">
            <div class="diagrams-duo-wrapper">
              <div class="diagram-card">
                <img src="static/images/pn_junction.svg" alt="PN Junction Diode" class="diagram-img"/>
              </div>
              <div class="diagram-card">
                <img src="static/images/mosfet_structure.svg" alt="nMOSFET Cross Section" class="diagram-img"/>
              </div>
            </div>
          </div>
        `;
        break;

      case 4:
        html = `
          <div class="scene-visual-container scene-4-visual animate-fade-in">
            <div class="diagram-single-wrapper">
              <img src="static/images/wafer_fab_pipeline.svg" alt="Semiconductor Cleanroom Pipeline" class="diagram-img-wide"/>
            </div>
          </div>
        `;
        break;

      case 5:
        html = `
          <div class="scene-visual-container scene-5-visual animate-fade-in">
            <div class="matlab-dashboard-preview">
              <div class="preview-header">
                <span class="preview-title">MATLAB ENGINEERING ANALYSIS: SemiconductorAnalysis.m</span>
                <button class="btn-preview-launch" onclick="window.matlabDashboard.open()">OPEN INTERACTIVE SUITE 📊</button>
              </div>
              <div class="plots-grid-preview">
                <div class="plot-thumb" onclick="window.matlabDashboard.open()">
                  <img src="results/plot1_diode_iv.png" alt="Shockley Diode IV"/>
                  <span class="plot-cap">1. Shockley Diode</span>
                </div>
                <div class="plot-thumb" onclick="window.matlabDashboard.open()">
                  <img src="results/plot2_mosfet_output.png" alt="MOSFET Output"/>
                  <span class="plot-cap">2. MOSFET Output</span>
                </div>
                <div class="plot-thumb" onclick="window.matlabDashboard.open()">
                  <img src="results/plot3_cmos_power.png" alt="CMOS Dynamic Power"/>
                  <span class="plot-cap">3. CMOS Power (P ∝ V²f)</span>
                </div>
                <div class="plot-thumb" onclick="window.matlabDashboard.open()">
                  <img src="results/plot4_yield_model.png" alt="Chip Manufacturing Yield"/>
                  <span class="plot-cap">4. Wafer Yield Models</span>
                </div>
                <div class="plot-thumb" onclick="window.matlabDashboard.open()">
                  <img src="results/plot5_moores_law.png" alt="Moore's Law Scaling"/>
                  <span class="plot-cap">5. Transistor Scaling</span>
                </div>
              </div>
            </div>
          </div>
        `;
        break;

      case 6:
        html = `
          <div class="scene-visual-container scene-6-visual animate-fade-in">
            <div class="diagram-single-wrapper">
              <img src="static/images/future_tech_stack.svg" alt="Next-Gen Semiconductor Technologies" class="diagram-img-wide"/>
            </div>
          </div>
        `;
        break;

      case 7:
        html = `
          <div class="scene-visual-container scene-7-visual animate-fade-in">
            <div class="final-revolution-stage">
              <div class="planetary-network-sphere">
                <div class="sphere-grid"></div>
                <div class="sphere-core-chip"></div>
              </div>
              <div class="final-title-wrapper">
                <h1 class="final-main-title">SEMICONDUCTORS — THE NEW OIL OF THE FUTURE</h1>
                <h2 class="final-subtitle">THE TINY TECHNOLOGY POWERING A MASSIVE REVOLUTION</h2>
                <div class="final-statement">
                  “Oil powered the machines of the industrial age. Semiconductors power the intelligence of the digital age. And the next revolution will be built from the smallest structures we can engineer.”
                </div>
              </div>
            </div>
          </div>
        `;
        break;
    }

    this.stageEl.innerHTML = html;
  }
}

window.sceneVisualsManager = new SceneVisualsManager();
