/**
 * RESEARCHER CHARACTER RIG & 2D VECTOR ANIMATION ENGINE
 * Project: "Semiconductors — The New Oil of the Future"
 * Lead Characters: Dr. Theodore Voss & Dr. Caleb Sterling
 */

class CharacterSystem {
  constructor() {
    this.theodoreEl = document.getElementById('char-theodore');
    this.calebEl = document.getElementById('char-caleb');
    this.currentSpeaker = null;
    this.lipSyncInterval = null;
    this.blinkTimers = { theodore: null, caleb: null };
    this.visemes = ['REST', 'OPEN', 'ROUND', 'WIDE', 'MID'];
  }

  init() {
    this.renderTheodore();
    this.renderCaleb();
    this.startBlinking('theodore');
    this.startBlinking('caleb');
    this.setGesture('theodore', 'gesture-rest');
    this.setGesture('caleb', 'gesture-rest');
    console.log('[CHARACTERS] Dr. Theodore Voss & Dr. Caleb Sterling initialized.');
  }

  renderTheodore() {
    if (!this.theodoreEl) return;
    this.theodoreEl.innerHTML = `
      <div class="character-badge">
        <span class="badge-status"></span>
        <span class="badge-name">Dr. Theodore Voss</span>
        <div class="badge-role">Senior Semiconductor Scientist</div>
      </div>
      <svg class="character-svg" viewBox="0 0 320 540" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <linearGradient id="suitGradTheo" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#2a3240"/>
            <stop offset="50%" stop-color="#1f2530"/>
            <stop offset="100%" stop-color="#151a22"/>
          </linearGradient>
          <linearGradient id="skinTheo" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#f8cfb4"/>
            <stop offset="100%" stop-color="#e8b99c"/>
          </linearGradient>
          <linearGradient id="hairTheo" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#332d2a"/>
            <stop offset="60%" stop-color="#211e1c"/>
            <stop offset="100%" stop-color="#181514"/>
          </linearGradient>
          <filter id="shadowFilter" x="-10%" y="-10%" width="120%" height="120%">
            <feDropShadow dx="0" dy="4" stdDeviation="4" flood-opacity="0.3"/>
          </filter>
        </defs>

        <!-- Torso & Clothing (Dark Charcoal Research Suit) -->
        <g class="char-torso-group" id="theo-torso">
          <!-- Legs / Lower Body -->
          <rect x="95" y="380" width="55" height="160" fill="#151a22" rx="4"/>
          <rect x="170" y="380" width="55" height="160" fill="#151a22" rx="4"/>

          <!-- Suit Jacket Body -->
          <path d="M 75 220 L 245 220 L 255 390 L 65 390 Z" fill="url(#suitGradTheo)" filter="url(#shadowFilter)"/>
          
          <!-- Crisp White Shirt & Charcoal Tie -->
          <polygon points="160,220 140,290 180,290" fill="#f8fafc"/>
          <!-- Tie -->
          <polygon points="158,235 162,235 166,310 160,330 154,310" fill="#0f172a"/>

          <!-- Lapels -->
          <path d="M 120 220 L 160 330 L 140 330 L 95 220 Z" fill="#2d3748"/>
          <path d="M 200 220 L 160 330 L 180 330 L 225 220 Z" fill="#2d3748"/>

          <!-- Lab Access Badge Pin -->
          <rect x="95" y="270" width="32" height="42" fill="#0f172a" stroke="#00f5d4" stroke-width="1.2" rx="2"/>
          <rect x="99" y="274" width="24" height="12" fill="#0284c7" rx="1"/>
          <line x1="99" y1="292" x2="123" y2="292" stroke="#94a3b8" stroke-width="2"/>
          <line x1="99" y1="298" x2="117" y2="298" stroke="#64748b" stroke-width="1.5"/>

          <!-- Arms -->
          <g class="char-arm-left" id="theo-arm-l">
            <path d="M 75 230 Q 50 310 70 380 Q 75 390 85 385 Q 75 315 95 240 Z" fill="#1f2530"/>
            <!-- Hand -->
            <ellipse cx="73" cy="385" rx="12" ry="14" fill="url(#skinTheo)"/>
          </g>

          <g class="char-arm-right" id="theo-arm-r">
            <path d="M 245 230 Q 270 310 250 380 Q 245 390 235 385 Q 245 315 225 240 Z" fill="#1f2530"/>
            <!-- Hand -->
            <ellipse cx="247" cy="385" rx="12" ry="14" fill="url(#skinTheo)"/>
          </g>
        </g>

        <!-- Head Group (Senior Scientist, Glasses, Styled Hair) -->
        <g class="char-head-group" id="theo-head" transform="translate(0, 0)">
          <!-- Neck -->
          <rect x="145" y="180" width="30" height="45" fill="url(#skinTheo)" rx="2"/>

          <!-- Head Base / Face -->
          <ellipse cx="160" cy="145" rx="46" ry="56" fill="url(#skinTheo)" filter="url(#shadowFilter)"/>

          <!-- Ears -->
          <ellipse cx="113" cy="148" rx="8" ry="14" fill="#e8b99c"/>
          <ellipse cx="207" cy="148" rx="8" ry="14" fill="#e8b99c"/>

          <!-- Neatly Parted Mature Dark Hair -->
          <path d="M 112 135 C 108 85, 150 72, 195 82 C 215 88, 218 115, 214 138 C 205 105, 185 95, 155 98 C 128 100, 118 115, 112 135 Z" fill="url(#hairTheo)"/>
          <!-- Subtle silver temple highlight -->
          <path d="M 114 130 C 112 120, 118 112, 124 116" stroke="#94a3b8" stroke-width="1.2" fill="none" opacity="0.6"/>

          <!-- Eyebrows (Distinguished, Analytical) -->
          <path d="M 130 126 Q 142 122 152 125" stroke="#211e1c" stroke-width="3" stroke-linecap="round" fill="none"/>
          <path d="M 168 125 Q 178 122 190 126" stroke="#211e1c" stroke-width="3" stroke-linecap="round" fill="none"/>

          <!-- Eyes & Blinking Eyelids -->
          <!-- Left Eye -->
          <g class="char-eye" id="theo-eye-l">
            <ellipse cx="142" cy="136" rx="7" ry="5" fill="#ffffff"/>
            <circle cx="143" cy="136" r="3.2" fill="#3b2b20"/>
            <circle cx="144" cy="135" r="1.2" fill="#ffffff"/>
            <!-- Eyelid for Blinking -->
            <rect class="eyelid-top" x="133" y="129" width="18" height="13" fill="#e8b99c" style="transform: scaleY(0);"/>
          </g>

          <!-- Right Eye -->
          <g class="char-eye" id="theo-eye-r">
            <ellipse cx="178" cy="136" rx="7" ry="5" fill="#ffffff"/>
            <circle cx="177" cy="136" r="3.2" fill="#3b2b20"/>
            <circle cx="178" cy="135" r="1.2" fill="#ffffff"/>
            <rect class="eyelid-top" x="169" y="129" width="18" height="13" fill="#e8b99c" style="transform: scaleY(0);"/>
          </g>

          <!-- Titanium Eyeglasses -->
          <g class="char-glasses">
            <rect x="131" y="127" width="22" height="17" fill="none" stroke="#94a3b8" stroke-width="1.8" rx="3"/>
            <rect x="167" y="127" width="22" height="17" fill="none" stroke="#94a3b8" stroke-width="1.8" rx="3"/>
            <line x1="153" y1="135" x2="167" y2="135" stroke="#94a3b8" stroke-width="1.8"/>
            <line x1="113" y1="135" x2="131" y2="135" stroke="#94a3b8" stroke-width="1.5"/>
            <line x1="189" y1="135" x2="207" y2="135" stroke="#94a3b8" stroke-width="1.5"/>
          </g>

          <!-- Nose -->
          <path d="M 160 135 L 157 155 L 164 156" stroke="#d49a7a" stroke-width="2" fill="none" stroke-linecap="round"/>

          <!-- MOUTH VISEMES CONTAINER -->
          <g class="char-mouth" id="theo-mouth" transform="translate(160, 172)">
            <!-- 1. REST (Neutral Closed Line) -->
            <g class="viseme viseme-REST active" id="theo-v-REST">
              <path d="M -14 0 Q 0 2 14 0" stroke="#a3543e" stroke-width="2.5" stroke-linecap="round" fill="none"/>
            </g>
            <!-- 2. OPEN (Aa, Ah, Wide Vowels) -->
            <g class="viseme viseme-OPEN" id="theo-v-OPEN">
              <ellipse cx="0" cy="3" rx="11" ry="8" fill="#4a1515" stroke="#a3543e" stroke-width="1.5"/>
              <path d="M -7 -1 Q 0 1 7 -1" stroke="#f8fafc" stroke-width="2.5" fill="none"/>
              <ellipse cx="0" cy="7" rx="6" ry="3" fill="#cf5d5d"/>
            </g>
            <!-- 3. ROUND (Oh, Oo, W) -->
            <g class="viseme viseme-ROUND" id="theo-v-ROUND">
              <ellipse cx="0" cy="2" rx="7" ry="8" fill="#4a1515" stroke="#a3543e" stroke-width="1.5"/>
              <circle cx="0" cy="2" r="3.5" fill="#300a0a"/>
            </g>
            <!-- 4. WIDE (Ee, Ay, Smile) -->
            <g class="viseme viseme-WIDE" id="theo-v-WIDE">
              <path d="M -15 -1 Q 0 4 15 -1 Q 0 8 -15 -1 Z" fill="#4a1515" stroke="#a3543e" stroke-width="1.5"/>
              <line x1="-11" y1="1" x2="11" y2="1" stroke="#ffffff" stroke-width="2"/>
            </g>
            <!-- 5. MID (Consonants, M, P, L, Conversation) -->
            <g class="viseme viseme-MID" id="theo-v-MID">
              <path d="M -12 0 Q 0 3 12 0 Q 0 5 -12 0 Z" fill="#4a1515" stroke="#a3543e" stroke-width="1.5"/>
              <line x1="-8" y1="1" x2="8" y2="1" stroke="#f8fafc" stroke-width="1.5"/>
            </g>
          </g>
        </g>
      </svg>
    `;
  }

  renderCaleb() {
    if (!this.calebEl) return;
    this.calebEl.innerHTML = `
      <div class="character-badge">
        <span class="badge-status"></span>
        <span class="badge-name">Dr. Caleb Sterling</span>
        <div class="badge-role">Microelectronics &amp; Computational Systems</div>
      </div>
      <svg class="character-svg" viewBox="0 0 320 540" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <linearGradient id="shirtGradCaleb" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#1e3a8a"/>
            <stop offset="60%" stop-color="#172554"/>
            <stop offset="100%" stop-color="#0f172a"/>
          </linearGradient>
          <linearGradient id="skinCaleb" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#fcd5bc"/>
            <stop offset="100%" stop-color="#f0bf9e"/>
          </linearGradient>
          <linearGradient id="hairCaleb" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#2d221c"/>
            <stop offset="70%" stop-color="#1c1613"/>
            <stop offset="100%" stop-color="#120e0c"/>
          </linearGradient>
        </defs>

        <!-- Torso & Clothing (Deep-Blue Smart-Casual Button-Down) -->
        <g class="char-torso-group" id="caleb-torso">
          <!-- Pants / Trousers -->
          <rect x="95" y="380" width="55" height="160" fill="#262e3d" rx="4"/>
          <rect x="170" y="380" width="55" height="160" fill="#262e3d" rx="4"/>

          <!-- Deep Blue Shirt -->
          <path d="M 75 220 L 245 220 L 255 390 L 65 390 Z" fill="url(#shirtGradCaleb)" filter="url(#shadowFilter)"/>
          
          <!-- Collar & Buttons -->
          <polygon points="160,225 140,250 180,250" fill="#1e3a8a" stroke="#2563eb" stroke-width="1"/>
          <!-- Button placket -->
          <line x1="160" y1="250" x2="160" y2="390" stroke="#1d4ed8" stroke-width="3"/>
          <circle cx="160" cy="275" r="2.5" fill="#93c5fd"/>
          <circle cx="160" cy="305" r="2.5" fill="#93c5fd"/>
          <circle cx="160" cy="335" r="2.5" fill="#93c5fd"/>
          <circle cx="160" cy="365" r="2.5" fill="#93c5fd"/>

          <!-- Smart Watch on Left Wrist -->
          <rect x="63" y="365" width="16" height="8" fill="#00f5d4" rx="2" opacity="0.8"/>

          <!-- Arms -->
          <g class="char-arm-left" id="caleb-arm-l">
            <path d="M 75 230 Q 55 310 70 380 Q 75 390 85 385 Q 80 315 95 240 Z" fill="#172554"/>
            <!-- Rolled cuff -->
            <rect x="62" y="355" width="22" height="10" fill="#1e40af" rx="2"/>
            <ellipse cx="73" cy="385" rx="12" ry="14" fill="url(#skinCaleb)"/>
          </g>

          <g class="char-arm-right" id="caleb-arm-r">
            <path d="M 245 230 Q 265 310 250 380 Q 245 390 235 385 Q 240 315 225 240 Z" fill="#172554"/>
            <rect x="236" y="355" width="22" height="10" fill="#1e40af" rx="2"/>
            <ellipse cx="247" cy="385" rx="12" ry="14" fill="url(#skinCaleb)"/>
          </g>
        </g>

        <!-- Head Group (Younger Researcher, Energetic, Textured Hair) -->
        <g class="char-head-group" id="caleb-head">
          <!-- Neck -->
          <rect x="145" y="180" width="30" height="45" fill="url(#skinCaleb)" rx="2"/>

          <!-- Face (Slightly leaner, youthful) -->
          <ellipse cx="160" cy="145" rx="44" ry="54" fill="url(#skinCaleb)" filter="url(#shadowFilter)"/>

          <!-- Ears -->
          <ellipse cx="114" cy="148" rx="8" ry="13" fill="#f0bf9e"/>
          <ellipse cx="206" cy="148" rx="8" ry="13" fill="#f0bf9e"/>

          <!-- Modern Textured Dark Hair -->
          <path d="M 114 135 C 108 90, 140 70, 195 76 C 216 82, 220 108, 214 135 C 205 105, 185 96, 160 98 C 135 100, 122 118, 114 135 Z" fill="url(#hairCaleb)"/>
          <path d="M 140 82 Q 155 68 175 74 Q 165 84 150 82 Z" fill="#2d221c"/>
          <path d="M 165 74 Q 185 66 198 78 Q 185 86 170 82 Z" fill="#3a2e27"/>

          <!-- Eyebrows (Curious, expressive) -->
          <path d="M 132 124 Q 143 118 153 122" stroke="#1c1613" stroke-width="2.8" stroke-linecap="round" fill="none"/>
          <path d="M 167 122 Q 177 118 188 124" stroke="#1c1613" stroke-width="2.8" stroke-linecap="round" fill="none"/>

          <!-- Eyes (Clear, enthusiastic) -->
          <g class="char-eye" id="caleb-eye-l">
            <ellipse cx="142" cy="135" rx="7.5" ry="5.5" fill="#ffffff"/>
            <circle cx="143" cy="135" r="3.4" fill="#2b2d42"/>
            <circle cx="144" cy="133.5" r="1.3" fill="#ffffff"/>
            <rect class="eyelid-top" x="133" y="128" width="18" height="14" fill="#f0bf9e" style="transform: scaleY(0);"/>
          </g>

          <g class="char-eye" id="caleb-eye-r">
            <ellipse cx="178" cy="135" rx="7.5" ry="5.5" fill="#ffffff"/>
            <circle cx="177" cy="135" r="3.4" fill="#2b2d42"/>
            <circle cx="178" cy="133.5" r="1.3" fill="#ffffff"/>
            <rect class="eyelid-top" x="169" y="128" width="18" height="14" fill="#f0bf9e" style="transform: scaleY(0);"/>
          </g>

          <!-- Nose -->
          <path d="M 160 134 L 158 153 L 165 154" stroke="#db9c7a" stroke-width="2" fill="none" stroke-linecap="round"/>

          <!-- MOUTH VISEMES CONTAINER -->
          <g class="char-mouth" id="caleb-mouth" transform="translate(160, 172)">
            <!-- 1. REST -->
            <g class="viseme viseme-REST active" id="caleb-v-REST">
              <path d="M -13 0 Q 0 3 13 0" stroke="#ad5742" stroke-width="2.5" stroke-linecap="round" fill="none"/>
            </g>
            <!-- 2. OPEN -->
            <g class="viseme viseme-OPEN" id="caleb-v-OPEN">
              <ellipse cx="0" cy="3" rx="10" ry="7.5" fill="#4a1515" stroke="#ad5742" stroke-width="1.5"/>
              <path d="M -6 -1 Q 0 1 6 -1" stroke="#f8fafc" stroke-width="2.5" fill="none"/>
              <ellipse cx="0" cy="6.5" rx="5" ry="3" fill="#d96a6a"/>
            </g>
            <!-- 3. ROUND -->
            <g class="viseme viseme-ROUND" id="caleb-v-ROUND">
              <ellipse cx="0" cy="2" rx="6.5" ry="7.5" fill="#4a1515" stroke="#ad5742" stroke-width="1.5"/>
              <circle cx="0" cy="2" r="3.2" fill="#2d0808"/>
            </g>
            <!-- 4. WIDE -->
            <g class="viseme viseme-WIDE" id="caleb-v-WIDE">
              <path d="M -14 -1 Q 0 4 14 -1 Q 0 8 -14 -1 Z" fill="#4a1515" stroke="#ad5742" stroke-width="1.5"/>
              <line x1="-10" y1="1" x2="10" y2="1" stroke="#ffffff" stroke-width="2"/>
            </g>
            <!-- 5. MID -->
            <g class="viseme viseme-MID" id="caleb-v-MID">
              <path d="M -11 0 Q 0 3.5 11 0 Q 0 5 -11 0 Z" fill="#4a1515" stroke="#ad5742" stroke-width="1.5"/>
              <line x1="-7" y1="1" x2="7" y2="1" stroke="#f8fafc" stroke-width="1.5"/>
            </g>
          </g>
        </g>
      </svg>
    `;
  }

  startBlinking(charKey) {
    const blink = () => {
      const eyeL = document.querySelector(`#${charKey === 'theodore' ? 'theo' : 'caleb'}-eye-l .eyelid-top`);
      const eyeR = document.querySelector(`#${charKey === 'theodore' ? 'theo' : 'caleb'}-eye-r .eyelid-top`);
      if (eyeL && eyeR) {
        eyeL.style.transform = 'scaleY(1)';
        eyeR.style.transform = 'scaleY(1)';
        setTimeout(() => {
          eyeL.style.transform = 'scaleY(0)';
          eyeR.style.transform = 'scaleY(0)';
        }, 120);
      }
      // Next blink in 3.0 to 5.5 seconds
      const nextDelay = 3000 + Math.random() * 2500;
      this.blinkTimers[charKey] = setTimeout(blink, nextDelay);
    };
    this.blinkTimers[charKey] = setTimeout(blink, 2000 + Math.random() * 1500);
  }

  setSpeaker(speakerId) {
    this.currentSpeaker = speakerId;
    if (speakerId === 'theodore') {
      this.theodoreEl.classList.add('is-speaking');
      this.theodoreEl.classList.remove('is-listening');
      this.calebEl.classList.add('is-listening');
      this.calebEl.classList.remove('is-speaking');
      this.resetMouth('caleb');
    } else if (speakerId === 'caleb') {
      this.calebEl.classList.add('is-speaking');
      this.calebEl.classList.remove('is-listening');
      this.theodoreEl.classList.add('is-listening');
      this.theodoreEl.classList.remove('is-speaking');
      this.resetMouth('theodore');
    } else {
      this.theodoreEl.classList.remove('is-speaking', 'is-listening');
      this.calebEl.classList.remove('is-speaking', 'is-listening');
      this.resetMouth('theodore');
      this.resetMouth('caleb');
    }
  }

  setViseme(charKey, visemeName) {
    const prefix = charKey === 'theodore' ? 'theo-v-' : 'caleb-v-';
    this.visemes.forEach(v => {
      const el = document.getElementById(`${prefix}${v}`);
      if (el) {
        if (v === visemeName) {
          el.classList.add('active');
        } else {
          el.classList.remove('active');
        }
      }
    });
  }

  resetMouth(charKey) {
    this.setViseme(charKey, 'REST');
  }

  startLipSync(charKey) {
    this.stopLipSync();
    let counter = 0;
    const activeVisemes = ['MID', 'OPEN', 'ROUND', 'WIDE', 'MID'];
    this.lipSyncInterval = setInterval(() => {
      // Natural speech viseme rhythm
      const v = activeVisemes[counter % activeVisemes.length];
      this.setViseme(charKey, v);
      counter++;
    }, 140);
  }

  stopLipSync() {
    if (this.lipSyncInterval) {
      clearInterval(this.lipSyncInterval);
      this.lipSyncInterval = null;
    }
    this.resetMouth('theodore');
    this.resetMouth('caleb');
  }

  setGesture(charKey, gestureClass) {
    const el = charKey === 'theodore' ? this.theodoreEl : this.calebEl;
    if (!el) return;
    el.classList.remove('gesture-explain', 'gesture-point', 'gesture-think', 'gesture-datapad', 'gesture-rest');
    el.classList.add(gestureClass);
  }
}

// Global instance
window.characterSystem = new CharacterSystem();
