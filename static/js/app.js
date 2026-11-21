/**
 * MASTER APPLICATION CONTROLLER & UI BINDINGS
 * Project: "Semiconductors — The New Oil of the Future"
 * Authors: Dr. Theodore Voss & Dr. Caleb Sterling
 */

document.addEventListener('DOMContentLoaded', () => {
  console.log('[APP] Booting "Semiconductors — The New Oil of the Future"...');

  // Initialize Subsystems
  if (window.characterSystem) window.characterSystem.init();
  if (window.soundEngine) window.soundEngine.init();
  if (window.sceneVisualsManager) window.sceneVisualsManager.init();
  if (window.matlabDashboard) window.matlabDashboard.init();
  if (window.timelineController) window.timelineController.init();

  // Initialize Speech and assign distinct voices
  if (window.speechManager) {
    window.speechManager.init(() => {
      updateDiagnostics();
    });
  }

  // Bind Global UI Controls
  bindGlobalControls();

  // Diagnostics periodic update
  setInterval(updateDiagnostics, 1000);

  // Auto-hide start splash when user clicks start
  const splashBtn = document.getElementById('btn-splash-start');
  if (splashBtn) {
    splashBtn.addEventListener('click', () => {
      document.getElementById('start-splash').style.display = 'none';
      if (window.soundEngine) window.soundEngine.startBackgroundAudio();
      if (window.timelineController) window.timelineController.play();
    });
  }
});

function bindGlobalControls() {
  // Sound Mute Toggle
  const soundBtn = document.getElementById('btn-toggle-sound');
  if (soundBtn) {
    soundBtn.addEventListener('click', () => {
      const isMuted = window.soundEngine.toggleMute();
      soundBtn.innerHTML = isMuted ? '🔇 SOUND OFF' : '🔊 SOUND ON';
      soundBtn.classList.toggle('muted', isMuted);
    });
  }

  // Subtitles Toggle
  const subBtn = document.getElementById('btn-toggle-subtitles');
  const subContainer = document.getElementById('subtitle-container');
  if (subBtn && subContainer) {
    subBtn.addEventListener('click', () => {
      const isHidden = subContainer.classList.toggle('subs-hidden');
      subBtn.innerHTML = isHidden ? '💬 SUBS OFF' : '💬 SUBS ON';
      if (window.soundEngine) window.soundEngine.playClick();
    });
  }

  // Fullscreen Toggle
  const fsBtn = document.getElementById('btn-toggle-fullscreen');
  if (fsBtn) {
    fsBtn.addEventListener('click', () => {
      if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().catch(err => {
          console.warn('[FULLSCREEN] Error attempting to enable fullscreen:', err);
        });
        fsBtn.innerHTML = '⛶ EXIT FULL';
      } else {
        document.exitFullscreen();
        fsBtn.innerHTML = '⛶ FULLSCREEN';
      }
      if (window.soundEngine) window.soundEngine.playClick();
    });
  }

  // Diagnostics Panel Toggle
  const diagBtn = document.getElementById('btn-toggle-diag');
  const diagPanel = document.getElementById('diagnostics-panel');
  if (diagBtn && diagPanel) {
    diagBtn.addEventListener('click', () => {
      diagPanel.classList.toggle('active');
      if (window.soundEngine) window.soundEngine.playClick();
    });
  }

  const diagClose = document.getElementById('btn-close-diag');
  if (diagClose && diagPanel) {
    diagClose.addEventListener('click', () => {
      diagPanel.classList.remove('active');
      if (window.soundEngine) window.soundEngine.playClick();
    });
  }
}

function updateDiagnostics() {
  const diagTheoVoice = document.getElementById('diag-theo-voice');
  const diagCalebVoice = document.getElementById('diag-caleb-voice');
  const diagTimeline = document.getElementById('diag-timeline-status');
  const diagDialogue = document.getElementById('diag-active-dialogue');
  const diagAudio = document.getElementById('diag-audio-status');

  if (window.speechManager) {
    if (diagTheoVoice) {
      diagTheoVoice.textContent = window.speechManager.theodoreVoice ? window.speechManager.theodoreVoice.name : 'System Default Male';
    }
    if (diagCalebVoice) {
      diagCalebVoice.textContent = window.speechManager.calebVoice ? window.speechManager.calebVoice.name : 'System Default Alternate';
    }
  }

  if (window.timelineController) {
    if (diagTimeline) {
      diagTimeline.textContent = `${window.timelineController.currentTime.toFixed(2)}s / 165.0s (Playing: ${window.timelineController.isPlaying})`;
    }
    if (diagDialogue) {
      diagDialogue.textContent = window.timelineController.activeDialogue ? 
        `[${window.timelineController.activeDialogue.id}] ${window.timelineController.activeDialogue.speaker}` : 'None (Inter-dialogue pause)';
    }
  }

  if (window.soundEngine && diagAudio) {
    diagAudio.textContent = window.soundEngine.isMuted ? 'MUTED' : 'ACTIVE (AudioContext + Procedural Waves)';
  }
}
