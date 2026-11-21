/**
 * DIALOGUE, SPEECH SYNTHESIS & TIMELINE DATA
 * Project: "Semiconductors — The New Oil of the Future"
 * Characters: Dr. Theodore Voss & Dr. Caleb Sterling
 * Total Timeline: Exactly 165.0 seconds (7 Scenes)
 */

const PRESENTATION_TIMELINE = {
  totalDuration: 165.0,
  scenes: [
    {
      id: 1,
      title: "THE INVISIBLE POWER RUNNING THE WORLD",
      subtitle: "The Foundation of the Modern Technological Era",
      start: 0.0,
      end: 22.0,
      duration: 22.0,
      bgVisual: "scene1-world-microprocessor"
    },
    {
      id: 2,
      title: "THE SCIENCE INSIDE A SEMICONDUCTOR",
      subtitle: "Energy Bands, Crystal Lattices & Controlled Doping",
      start: 22.0,
      end: 44.0,
      duration: 22.0,
      bgVisual: "scene2-solid-state-physics"
    },
    {
      id: 3,
      title: "FROM TRANSISTORS TO MICROPROCESSORS",
      subtitle: "PN Junctions, MOSFET Inversion & CMOS Scaling",
      start: 44.0,
      end: 68.0,
      duration: 24.0,
      bgVisual: "scene3-transistor-revolution"
    },
    {
      id: 4,
      title: "HOW A CHIP IS ACTUALLY MANUFACTURED",
      subtitle: "EUV Lithography, Cleanroom Precision & Yield Dynamics",
      start: 68.0,
      end: 93.0,
      duration: 25.0,
      bgVisual: "scene4-wafer-fabrication"
    },
    {
      id: 5,
      title: "MATLAB: THE MATHEMATICS INSIDE MICROELECTRONICS",
      subtitle: "Numerical Modeling, Diode, MOSFET & CMOS Power Analysis",
      start: 93.0,
      end: 120.0,
      duration: 27.0,
      bgVisual: "scene5-matlab-dashboard"
    },
    {
      id: 6,
      title: "THE FUTURE OF SEMICONDUCTOR TECHNOLOGY",
      subtitle: "3D Chiplets, Wide-Bandgap GaN/SiC & Advanced Packaging",
      start: 120.0,
      end: 145.0,
      duration: 25.0,
      bgVisual: "scene6-future-horizons"
    },
    {
      id: 7,
      title: "THE NEXT INDUSTRIAL REVOLUTION",
      subtitle: "The Tiny Technology Powering a Planetary Transformation",
      start: 145.0,
      end: 165.0,
      duration: 20.0,
      bgVisual: "scene7-global-network"
    }
  ],

  dialogues: [
    // SCENE 1 (0:00 - 0:22)
    {
      id: "d1_1",
      sceneId: 1,
      speaker: "theodore",
      start: 0.8,
      end: 7.5,
      gesture: "gesture-explain",
      text: "Look around this laboratory, Caleb. Beneath every smartphone, cloud data center, electric vehicle, and satellite orbit lies a microscopic architecture of silicon. Semiconductors have quietly become the bedrock of human civilization."
    },
    {
      id: "d1_2",
      sceneId: 1,
      speaker: "caleb",
      start: 8.0,
      end: 14.2,
      gesture: "gesture-think",
      text: "It is astonishing how components measured in nanometers hold such geopolitical weight. Why has silicon surpassed traditional commodities in strategic value?"
    },
    {
      id: "d1_3",
      sceneId: 1,
      speaker: "theodore",
      start: 14.6,
      end: 21.6,
      gesture: "gesture-point",
      text: "Because just as crude oil powered the mechanical engines of the industrial age, semiconductors power the computational intelligence of our digital age. Not as a combustible fuel, but as the indispensable catalyst of global power."
    },

    // SCENE 2 (0:22 - 0:44)
    {
      id: "d2_1",
      sceneId: 2,
      speaker: "theodore",
      start: 22.8,
      end: 29.5,
      gesture: "gesture-explain",
      text: "To understand why, we look into solid-state physics. Unlike metals with overlapping bands or insulators with vast bandgaps, silicon possesses a moderate forbidden gap of approximately 1.12 electron-volts at room temperature."
    },
    {
      id: "d2_2",
      sceneId: 2,
      speaker: "caleb",
      start: 30.0,
      end: 36.2,
      gesture: "gesture-datapad",
      text: "And in pure intrinsic silicon, thermal excitation alone yields few mobile carriers. But by introducing a mere handful of dopant atoms per million, conductivity increases by many orders of magnitude!"
    },
    {
      id: "d2_3",
      sceneId: 2,
      speaker: "theodore",
      start: 36.7,
      end: 43.5,
      gesture: "gesture-point",
      text: "Precisely. Pentavalent donors like phosphorus inject free conduction electrons for N-type silicon, while trivalent acceptors like boron create mobile valence holes in P-type material, establishing the physical foundation of modern electronics."
    },

    // SCENE 3 (0:44 - 1:08)
    {
      id: "d3_1",
      sceneId: 3,
      speaker: "theodore",
      start: 44.8,
      end: 51.5,
      gesture: "gesture-explain",
      text: "When P-type and N-type silicon meet, they form a PN junction diode. The resulting built-in potential barrier allows current to surge forward under positive bias while blocking reverse conduction."
    },
    {
      id: "d3_2",
      sceneId: 3,
      speaker: "caleb",
      start: 52.0,
      end: 59.2,
      gesture: "gesture-point",
      text: "And by adding a dielectric gate atop this channel, we achieve the MOSFET. Applying a threshold gate voltage inverts the surface, creating an ultrafast electronic switch that dissipates virtually zero static power in complementary CMOS configurations."
    },
    {
      id: "d3_3",
      sceneId: 3,
      speaker: "theodore",
      start: 59.7,
      end: 67.4,
      gesture: "gesture-explain",
      text: "From individual switches to boolean logic gates, arithmetic units, and multi-core processors. Today, a single thumbnail-sized die integrates tens of billions of synchronized nanometer switches, executing trillions of operations per second."
    },

    // SCENE 4 (1:08 - 1:33)
    {
      id: "d4_1",
      sceneId: 4,
      speaker: "caleb",
      start: 68.8,
      end: 76.5,
      gesture: "gesture-think",
      text: "Yet the sheer difficulty of fabricating these chips is mind-boggling. Why does building a leading-edge fabrication facility require upwards of twenty billion dollars?"
    },
    {
      id: "d4_2",
      sceneId: 4,
      speaker: "theodore",
      start: 77.0,
      end: 85.0,
      gesture: "gesture-explain",
      text: "Because chip manufacturing is the most complex engineering feat on Earth. We slice cylindrical monocrystalline ingots into mirror-polished 300-millimeter wafers, transported inside ISO Class 1 cleanrooms with fewer than ten microscopic particles per cubic meter."
    },
    {
      id: "d4_3",
      sceneId: 4,
      speaker: "theodore",
      start: 85.5,
      end: 92.4,
      gesture: "gesture-point",
      text: "Inside giant EUV scanners, 13.5-nanometer extreme ultraviolet light projects circuit blueprints through photomasks. Over three months and a thousand automated steps of plasma etching, ion bombardment, and copper planarization, microscopic architectures emerge."
    },

    // SCENE 5 (1:33 - 2:00)
    {
      id: "d5_1",
      sceneId: 5,
      speaker: "caleb",
      start: 93.8,
      end: 100.8,
      gesture: "gesture-datapad",
      text: "Here on our engineering workstation, we utilize MATLAB and computational modeling to simulate every physical and electrical characteristic before silicon ever enters the fab."
    },
    {
      id: "d5_2",
      sceneId: 5,
      speaker: "theodore",
      start: 101.3,
      end: 109.5,
      gesture: "gesture-point",
      text: "Our script, SemiconductorAnalysis, numerically evaluates the Shockley diode equation with exponential precision, and computes long-channel MOSFET drain current across both linear and saturation regimes."
    },
    {
      id: "d5_3",
      sceneId: 5,
      speaker: "caleb",
      start: 110.0,
      end: 119.4,
      gesture: "gesture-explain",
      text: "We also model CMOS dynamic switching power scaling quadratically with supply voltage, as well as Poisson wafer yield curves. Notice how larger die areas cause exponential yield loss, driving the industry toward modular chiplet paradigms."
    },

    // SCENE 6 (2:00 - 2:25)
    {
      id: "d6_1",
      sceneId: 6,
      speaker: "theodore",
      start: 120.8,
      end: 128.5,
      gesture: "gesture-explain",
      text: "As physical gate lengths approach atomic limits, the future of microelectronics no longer relies solely on traditional geometric scaling. We are entering the 'More than Moore' era of architectural innovation."
    },
    {
      id: "d6_2",
      sceneId: 6,
      speaker: "caleb",
      start: 129.0,
      end: 136.8,
      gesture: "gesture-point",
      text: "Advanced 3D packaging and through-silicon vias now allow us to stack compute dies and high-bandwidth memory vertically. Simultaneously, wide-bandgap materials like gallium nitride and silicon carbide revolutionize electric vehicles and high-power grids."
    },
    {
      id: "d6_3",
      sceneId: 6,
      speaker: "theodore",
      start: 137.3,
      end: 144.5,
      gesture: "gesture-explain",
      text: "Furthermore, research in silicon photonics and neuromorphic accelerators promises light-speed interconnects and brain-inspired computing, while global foundries secure resilient, sustainable supply chains."
    },

    // SCENE 7 (2:25 - 2:45)
    {
      id: "d7_1",
      sceneId: 7,
      speaker: "caleb",
      start: 145.8,
      end: 153.5,
      gesture: "gesture-point",
      text: "From quantum mechanical bandgaps to planetary-scale AI clusters, semiconductors represent the most remarkable convergence of science, mathematics, and manufacturing ever achieved."
    },
    {
      id: "d7_2",
      sceneId: 7,
      speaker: "theodore",
      start: 154.0,
      end: 163.5,
      gesture: "gesture-explain",
      text: "Oil powered the machines of the industrial age. Semiconductors power the intelligence of the digital age. And the next revolution will be built from the smallest structures we can engineer."
    }
  ]
};

/**
 * SPEECH SYNTHESIS ENGINE
 * Handles browser voice enumeration, distinct male voice assignment, and speech playback.
 */
class SpeechManager {
  constructor() {
    this.voices = [];
    this.theodoreVoice = null;
    this.calebVoice = null;
    this.isMuted = false;
    this.speechAvailable = ('speechSynthesis' in window);
    this.currentUtterance = null;
  }

  init(callback) {
    if (!this.speechAvailable) {
      console.warn('[SPEECH] Web Speech API not supported in this browser. Fallback timer active.');
      if (callback) callback();
      return;
    }

    const loadVoices = () => {
      this.voices = window.speechSynthesis.getVoices();
      if (this.voices.length > 0) {
        this.assignDistinctVoices();
        console.log('[SPEECH] Voices loaded:', this.voices.length);
        console.log(`[SPEECH] Theodore: ${this.theodoreVoice ? this.theodoreVoice.name : 'Default'} | Caleb: ${this.calebVoice ? this.calebVoice.name : 'Default'}`);
        if (callback) callback();
      }
    };

    loadVoices();
    if (window.speechSynthesis.onvoiceschanged !== undefined) {
      window.speechSynthesis.onvoiceschanged = loadVoices;
    }
  }

  assignDistinctVoices() {
    // Look for high-quality male voices
    const maleNames = ['David', 'Guy', 'George', 'Daniel', 'James', 'Mark', 'Alex', 'Fred', 'Oliver'];
    const englishVoices = this.voices.filter(v => v.lang && v.lang.startsWith('en'));
    const pool = englishVoices.length > 0 ? englishVoices : this.voices;

    // Candidates for Theodore (Mature, deep, authoritative)
    const theoCandidates = pool.filter(v => 
      /david|guy|daniel|george|uk english male|natural.*male/i.test(v.name)
    );

    // Candidates for Caleb (Younger, energetic, clear)
    const calebCandidates = pool.filter(v => 
      /mark|alex|fred|james|us english male|natural.*young/i.test(v.name)
    );

    this.theodoreVoice = theoCandidates.length > 0 ? theoCandidates[0] : (pool[0] || null);

    // Ensure Caleb doesn't pick the identical voice object if multiple exist
    const diffVoices = pool.filter(v => v !== this.theodoreVoice);
    if (calebCandidates.length > 0 && calebCandidates[0] !== this.theodoreVoice) {
      this.calebVoice = calebCandidates[0];
    } else if (diffVoices.length > 0) {
      this.calebVoice = diffVoices[0];
    } else {
      this.calebVoice = this.theodoreVoice;
    }
  }

  speak(dialogue, onStart, onEnd) {
    if (this.isMuted || !this.speechAvailable || !window.speechSynthesis) {
      if (onStart) onStart();
      const textDuration = (dialogue.end - dialogue.start) * 1000;
      setTimeout(() => {
        if (onEnd) onEnd();
      }, textDuration);
      return;
    }

    // Cancel any previous utterance
    window.speechSynthesis.cancel();

    const utterance = new SpeechSynthesisUtterance(dialogue.text);

    if (dialogue.speaker === 'theodore') {
      utterance.voice = this.theodoreVoice;
      utterance.rate = 0.94;
      utterance.pitch = 0.84; // Deeper, mature resonance
    } else {
      utterance.voice = this.calebVoice;
      utterance.rate = 1.04;
      utterance.pitch = 1.14; // Higher, younger, energetic resonance
    }

    utterance.onstart = () => {
      this.currentUtterance = utterance;
      if (onStart) onStart();
    };

    utterance.onend = () => {
      this.currentUtterance = null;
      if (onEnd) onEnd();
    };

    utterance.onerror = (e) => {
      console.warn('[SPEECH ERROR]', e);
      this.currentUtterance = null;
      if (onEnd) onEnd();
    };

    try {
      window.speechSynthesis.speak(utterance);
    } catch (err) {
      console.error('[SPEECH EXCEPTION]', err);
      if (onStart) onStart();
      setTimeout(onEnd, (dialogue.end - dialogue.start) * 1000);
    }
  }

  cancel() {
    if (this.speechAvailable && window.speechSynthesis) {
      window.speechSynthesis.cancel();
      this.currentUtterance = null;
    }
  }
}

window.PRESENTATION_TIMELINE = PRESENTATION_TIMELINE;
window.speechManager = new SpeechManager();
