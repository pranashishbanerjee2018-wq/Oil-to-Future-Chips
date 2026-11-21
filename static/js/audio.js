/**
 * AUDIO CONTROLLER & PROCEDURAL SOUND DESIGN ENGINE
 * Project: "Semiconductors — The New Oil of the Future"
 * Authors: Dr. Theodore Voss & Dr. Caleb Sterling
 */

class SoundEngine {
  constructor() {
    this.isMuted = false;
    this.audioCtx = null;
    this.bgMusic = null;
    this.ambientLab = null;
    this.soundEffects = {};
    this.audioInitialized = false;
  }

  init() {
    if (this.audioInitialized) return;

    try {
      const AudioContext = window.AudioContext || window.webkitAudioContext;
      if (AudioContext) {
        this.audioCtx = new AudioContext();
      }
    } catch (e) {
      console.warn('[AUDIO] AudioContext initialization deferred until user interaction.');
    }

    // Audio file sources
    this.bgMusic = new Audio('static/audio/bg_music.wav');
    this.bgMusic.loop = true;
    this.bgMusic.volume = 0.16; // Balanced: never overpowers speech

    this.ambientLab = new Audio('static/audio/ambient_lab.wav');
    this.ambientLab.loop = true;
    this.ambientLab.volume = 0.08;

    this.soundEffects = {
      click: new Audio('static/audio/ui_click.wav'),
      transition: new Audio('static/audio/scene_transition.wav'),
      calc: new Audio('static/audio/calc_complete.wav'),
      processor: new Audio('static/audio/processor_hum.wav')
    };

    // Set volumes for SFX
    if (this.soundEffects.click) this.soundEffects.click.volume = 0.3;
    if (this.soundEffects.transition) this.soundEffects.transition.volume = 0.35;
    if (this.soundEffects.calc) this.soundEffects.calc.volume = 0.4;
    if (this.soundEffects.processor) this.soundEffects.processor.volume = 0.25;

    this.audioInitialized = true;
    console.log('[AUDIO] Audio system initialized with balanced mixing levels.');
  }

  resumeContext() {
    if (this.audioCtx && this.audioCtx.state === 'suspended') {
      this.audioCtx.resume();
    }
  }

  startBackgroundAudio() {
    this.init();
    this.resumeContext();
    if (this.isMuted) return;

    if (this.bgMusic) {
      this.bgMusic.play().catch(e => console.log('[AUDIO] Autoplay blocked, awaiting user click:', e));
    }
    if (this.ambientLab) {
      this.ambientLab.play().catch(e => console.log('[AUDIO] Ambient play blocked:', e));
    }
  }

  pauseBackgroundAudio() {
    if (this.bgMusic) this.bgMusic.pause();
    if (this.ambientLab) this.ambientLab.pause();
  }

  playClick() {
    if (this.isMuted) return;
    try {
      if (this.soundEffects.click) {
        this.soundEffects.click.currentTime = 0;
        this.soundEffects.click.play().catch(() => this.synthClick());
      } else {
        this.synthClick();
      }
    } catch (e) {
      this.synthClick();
    }
  }

  playTransition() {
    if (this.isMuted) return;
    try {
      if (this.soundEffects.transition) {
        this.soundEffects.transition.currentTime = 0;
        this.soundEffects.transition.play().catch(() => this.synthTransition());
      } else {
        this.synthTransition();
      }
    } catch (e) {
      this.synthTransition();
    }
  }

  playCalcChime() {
    if (this.isMuted) return;
    try {
      if (this.soundEffects.calc) {
        this.soundEffects.calc.currentTime = 0;
        this.soundEffects.calc.play().catch(() => this.synthChime());
      } else {
        this.synthChime();
      }
    } catch (e) {
      this.synthChime();
    }
  }

  toggleMute() {
    this.isMuted = !this.isMuted;
    if (window.speechManager) {
      window.speechManager.isMuted = this.isMuted;
    }
    if (this.isMuted) {
      this.pauseBackgroundAudio();
    } else {
      this.startBackgroundAudio();
    }
    return this.isMuted;
  }

  // Web Audio procedural synthesizer fallback
  synthClick() {
    if (!this.audioCtx || this.isMuted) return;
    try {
      const osc = this.audioCtx.createOscillator();
      const gain = this.audioCtx.createGain();
      osc.type = 'sine';
      osc.frequency.setValueAtTime(1800, this.audioCtx.currentTime);
      gain.gain.setValueAtTime(0.12, this.audioCtx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, this.audioCtx.currentTime + 0.05);
      osc.connect(gain);
      gain.connect(this.audioCtx.destination);
      osc.start();
      osc.stop(this.audioCtx.currentTime + 0.05);
    } catch (e) {}
  }

  synthChime() {
    if (!this.audioCtx || this.isMuted) return;
    try {
      const now = this.audioCtx.currentTime;
      [880, 1320].forEach((freq, idx) => {
        const osc = this.audioCtx.createOscillator();
        const gain = this.audioCtx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(freq, now + idx * 0.15);
        gain.gain.setValueAtTime(0.15, now + idx * 0.15);
        gain.gain.exponentialRampToValueAtTime(0.001, now + idx * 0.15 + 0.4);
        osc.connect(gain);
        gain.connect(this.audioCtx.destination);
        osc.start(now + idx * 0.15);
        osc.stop(now + idx * 0.15 + 0.4);
      });
    } catch (e) {}
  }

  synthTransition() {
    if (!this.audioCtx || this.isMuted) return;
    try {
      const now = this.audioCtx.currentTime;
      const osc = this.audioCtx.createOscillator();
      const gain = this.audioCtx.createGain();
      osc.type = 'sine';
      osc.frequency.setValueAtTime(260, now);
      osc.frequency.exponentialRampToValueAtTime(680, now + 0.5);
      gain.gain.setValueAtTime(0.1, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.6);
      osc.connect(gain);
      gain.connect(this.audioCtx.destination);
      osc.start(now);
      osc.stop(now + 0.6);
    } catch (e) {}
  }
}

window.soundEngine = new SoundEngine();
