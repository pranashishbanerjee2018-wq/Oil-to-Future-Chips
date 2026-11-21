/**
 * MASTER PRESENTATION TIMELINE & ORCHESTRATION ENGINE
 * Project: "Semiconductors — The New Oil of the Future"
 * Authors: Dr. Theodore Voss & Dr. Caleb Sterling
 * Total Timeline: Exactly 165.0 seconds (2m 45s) across 7 Scenes
 */

class TimelineController {
  constructor() {
    this.totalDuration = 165.0;
    this.currentTime = 0.0;
    this.isPlaying = false;
    this.playbackRate = 1.0;
    this.currentSceneId = 1;
    this.activeDialogue = null;
    this.playedDialogueIds = new Set();
    this.lastFrameTimestamp = null;
    this.rafId = null;

    // DOM Elements
    this.progressBar = document.getElementById('timeline-progress');
    this.scrubber = document.getElementById('timeline-scrubber');
    this.timeDisplay = document.getElementById('time-display');
    this.sceneTitleEl = document.getElementById('current-scene-title');
    this.sceneSubEl = document.getElementById('current-scene-subtitle');
    this.subtitleTextEl = document.getElementById('subtitle-text');
    this.subtitleSpeakerEl = document.getElementById('subtitle-speaker');
    this.playPauseBtn = document.getElementById('btn-play-pause');
  }

  init() {
    this.bindControls();
    this.updateSceneDisplay(1);
    this.updateProgress(0);
    console.log('[TIMELINE] Master 165-second timeline controller initialized.');
  }

  bindControls() {
    if (this.playPauseBtn) {
      this.playPauseBtn.addEventListener('click', () => this.togglePlayPause());
    }

    const restartBtn = document.getElementById('btn-restart');
    if (restartBtn) {
      restartBtn.addEventListener('click', () => this.restart());
    }

    const prevBtn = document.getElementById('btn-prev-scene');
    if (prevBtn) {
      prevBtn.addEventListener('click', () => this.prevScene());
    }

    const nextBtn = document.getElementById('btn-next-scene');
    if (nextBtn) {
      nextBtn.addEventListener('click', () => this.nextScene());
    }

    // Scrubber click/drag
    if (this.scrubber) {
      this.scrubber.addEventListener('click', (e) => {
        const rect = this.scrubber.getBoundingClientRect();
        const pos = Math.max(0, Math.min(1, (e.clientX - rect.left) / rect.width));
        this.seekTo(pos * this.totalDuration);
      });
    }

    // Keyboard shortcuts
    window.addEventListener('keydown', (e) => {
      if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
      if (e.code === 'Space') {
        e.preventDefault();
        this.togglePlayPause();
      } else if (e.code === 'ArrowRight') {
        this.seekTo(Math.min(this.totalDuration, this.currentTime + 5));
      } else if (e.code === 'ArrowLeft') {
        this.seekTo(Math.max(0, this.currentTime - 5));
      } else if (e.code === 'KeyM') {
        if (window.soundEngine) window.soundEngine.toggleMute();
      } else if (e.code === 'KeyD') {
        if (window.matlabDashboard) window.matlabDashboard.open();
      }
    });

    // Scene Navigation Jump Links
    const scenePills = document.querySelectorAll('.scene-pill');
    scenePills.forEach(pill => {
      pill.addEventListener('click', () => {
        const sid = parseInt(pill.getAttribute('data-scene-id'), 10);
        this.jumpToScene(sid);
      });
    });
  }

  togglePlayPause() {
    if (this.isPlaying) {
      this.pause();
    } else {
      this.play();
    }
  }

  play() {
    if (this.currentTime >= this.totalDuration) {
      this.restart();
      return;
    }

    this.isPlaying = true;
    if (this.playPauseBtn) {
      this.playPauseBtn.innerHTML = '❚❚ PAUSE';
      this.playPauseBtn.classList.add('playing');
    }

    if (window.soundEngine) {
      window.soundEngine.startBackgroundAudio();
    }

    this.lastFrameTimestamp = performance.now();
    this.tick();
    console.log('[TIMELINE] Playback started at', this.currentTime.toFixed(2), 's');
  }

  pause() {
    this.isPlaying = false;
    if (this.playPauseBtn) {
      this.playPauseBtn.innerHTML = '▶ PLAY';
      this.playPauseBtn.classList.remove('playing');
    }

    if (this.rafId) {
      cancelAnimationFrame(this.rafId);
      this.rafId = null;
    }

    if (window.soundEngine) {
      window.soundEngine.pauseBackgroundAudio();
    }

    if (window.speechManager) {
      window.speechManager.cancel();
    }

    if (window.characterSystem) {
      window.characterSystem.stopLipSync();
      window.characterSystem.setSpeaker(null);
    }

    console.log('[TIMELINE] Playback paused at', this.currentTime.toFixed(2), 's');
  }

  restart() {
    this.pause();
    this.currentTime = 0.0;
    this.playedDialogueIds.clear();
    this.activeDialogue = null;
    this.jumpToScene(1);
    this.updateProgress(0);
    this.updateSubtitles('', '');
    this.play();
  }

  seekTo(timeInSeconds) {
    const wasPlaying = this.isPlaying;
    this.pause();
    this.currentTime = Math.max(0, Math.min(this.totalDuration, timeInSeconds));
    
    // Clear future dialogues from played set
    this.playedDialogueIds.forEach(id => {
      const d = window.PRESENTATION_TIMELINE.dialogues.find(item => item.id === id);
      if (d && d.start > this.currentTime) {
        this.playedDialogueIds.delete(id);
      }
    });

    const scene = this.getSceneForTime(this.currentTime);
    if (scene && scene.id !== this.currentSceneId) {
      this.updateSceneDisplay(scene.id);
    }

    this.updateProgress(this.currentTime);
    if (wasPlaying) {
      this.play();
    }
  }

  jumpToScene(sceneId) {
    const scene = window.PRESENTATION_TIMELINE.scenes.find(s => s.id === sceneId);
    if (scene) {
      this.seekTo(scene.start);
      if (window.soundEngine) window.soundEngine.playTransition();
    }
  }

  prevScene() {
    if (this.currentSceneId > 1) {
      this.jumpToScene(this.currentSceneId - 1);
    } else {
      this.seekTo(0);
    }
  }

  nextScene() {
    if (this.currentSceneId < window.PRESENTATION_TIMELINE.scenes.length) {
      this.jumpToScene(this.currentSceneId + 1);
    }
  }

  getSceneForTime(t) {
    return window.PRESENTATION_TIMELINE.scenes.find(s => t >= s.start && t < s.end) || 
           window.PRESENTATION_TIMELINE.scenes[window.PRESENTATION_TIMELINE.scenes.length - 1];
  }

  tick() {
    if (!this.isPlaying) return;

    const now = performance.now();
    const dt = (now - this.lastFrameTimestamp) / 1000.0;
    this.lastFrameTimestamp = now;

    this.currentTime += dt * this.playbackRate;

    // Check completion
    if (this.currentTime >= this.totalDuration) {
      this.currentTime = this.totalDuration;
      this.updateProgress(this.currentTime);
      this.pause();
      console.log('[TIMELINE] Presentation completed 165 seconds.');
      return;
    }

    // Check Scene boundary
    const currentScene = this.getSceneForTime(this.currentTime);
    if (currentScene && currentScene.id !== this.currentSceneId) {
      this.updateSceneDisplay(currentScene.id);
    }

    // Check dialogues
    this.processDialogues(this.currentTime);

    this.updateProgress(this.currentTime);
    this.rafId = requestAnimationFrame(() => this.tick());
  }

  updateSceneDisplay(sceneId) {
    this.currentSceneId = sceneId;
    const scene = window.PRESENTATION_TIMELINE.scenes.find(s => s.id === sceneId);
    if (!scene) return;

    if (this.sceneTitleEl) this.sceneTitleEl.textContent = `SCENE ${scene.id} — ${scene.title}`;
    if (this.sceneSubEl) this.sceneSubEl.textContent = scene.subtitle;

    // Update scene navigation pills
    document.querySelectorAll('.scene-pill').forEach(pill => {
      const pid = parseInt(pill.getAttribute('data-scene-id'), 10);
      if (pid === sceneId) {
        pill.classList.add('active');
      } else {
        pill.classList.remove('active');
      }
    });

    // Update visual background
    if (window.sceneVisualsManager) {
      window.sceneVisualsManager.renderScene(sceneId);
    }

    if (window.soundEngine) {
      window.soundEngine.playTransition();
    }
  }

  processDialogues(currentTime) {
    // Find active dialogue
    const matching = window.PRESENTATION_TIMELINE.dialogues.find(
      d => currentTime >= d.start && currentTime < d.end
    );

    if (matching) {
      if (this.activeDialogue !== matching) {
        this.activeDialogue = matching;
        this.startDialogueTurn(matching);
      }
    } else {
      if (this.activeDialogue) {
        this.endDialogueTurn(this.activeDialogue);
        this.activeDialogue = null;
      }
    }
  }

  startDialogueTurn(dialogue) {
    const speakerName = dialogue.speaker === 'theodore' ? 'Dr. Theodore Voss' : 'Dr. Caleb Sterling';
    this.updateSubtitles(speakerName, dialogue.text);

    if (window.characterSystem) {
      window.characterSystem.setSpeaker(dialogue.speaker);
      window.characterSystem.setGesture(dialogue.speaker, dialogue.gesture);
      window.characterSystem.startLipSync(dialogue.speaker);
    }

    // If dialogue hasn't been spoken yet via Web Speech
    if (!this.playedDialogueIds.has(dialogue.id)) {
      this.playedDialogueIds.add(dialogue.id);
      if (window.speechManager) {
        window.speechManager.speak(
          dialogue,
          () => {
            if (window.characterSystem) window.characterSystem.startLipSync(dialogue.speaker);
          },
          () => {
            if (window.characterSystem) window.characterSystem.stopLipSync();
          }
        );
      }
    }
  }

  endDialogueTurn(dialogue) {
    if (window.characterSystem) {
      window.characterSystem.stopLipSync();
      window.characterSystem.setSpeaker(null);
      window.characterSystem.setGesture(dialogue.speaker, 'gesture-rest');
    }
    this.updateSubtitles('', '');
  }

  updateSubtitles(speaker, text) {
    if (!this.subtitleTextEl || !this.subtitleSpeakerEl) return;
    if (text) {
      this.subtitleSpeakerEl.textContent = speaker ? `${speaker}:` : '';
      this.subtitleTextEl.textContent = text;
      document.getElementById('subtitle-container')?.classList.add('visible');
    } else {
      this.subtitleSpeakerEl.textContent = '';
      this.subtitleTextEl.textContent = '';
      document.getElementById('subtitle-container')?.classList.remove('visible');
    }
  }

  updateProgress(t) {
    const pct = (t / this.totalDuration) * 100;
    if (this.progressBar) {
      this.progressBar.style.width = `${pct}%`;
    }

    if (this.timeDisplay) {
      const curM = Math.floor(t / 60);
      const curS = Math.floor(t % 60);
      const totM = Math.floor(this.totalDuration / 60);
      const totS = Math.floor(this.totalDuration % 60);
      this.timeDisplay.textContent = 
        `${String(curM).padStart(2, '0')}:${String(curS).padStart(2, '0')} / ${String(totM).padStart(2, '0')}:${String(totS).padStart(2, '0')}`;
    }
  }
}

window.timelineController = new TimelineController();
