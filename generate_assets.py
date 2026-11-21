#!/usr/bin/env python3
"""
AUDIO & ASSET GENERATION ENGINE
Project: "Semiconductors — The New Oil of the Future"
Authors: Dr. Theodore Voss & Dr. Caleb Sterling

Generates high-fidelity procedural audio assets:
1. ambient_lab.wav: Subtle cleanroom airflow and electromagnetic lab drone
2. bg_music.wav: Cinematic ambient sci-fi intellectual musical loop
3. ui_click.wav: High-tech responsive tactile interface click
4. scene_transition.wav: Smooth futuristic acoustic whoosh & frequency sweep
5. calc_complete.wav: Harmonic dual-tone engineering calculation chime
6. processor_hum.wav: Microprocessor high-speed computational resonance
"""

import os
import math
import wave
import struct

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
AUDIO_DIR = os.path.join(PROJECT_ROOT, 'static', 'audio')
os.makedirs(AUDIO_DIR, exist_ok=True)

SAMPLE_RATE = 44100

def write_wav(filename, samples, sample_rate=SAMPLE_RATE, channels=2):
    filepath = os.path.join(AUDIO_DIR, filename)
    with wave.open(filepath, 'w') as wav:
        wav.setnchannels(channels)
        wav.setsampwidth(2) # 16-bit
        wav.setframerate(sample_rate)
        # Convert float (-1.0 to 1.0) to 16-bit PCM (-32768 to 32767)
        packed_frames = bytearray()
        for s in samples:
            if isinstance(s, (tuple, list)):
                l_val = int(max(-1.0, min(1.0, float(s[0]))) * 32767)
                r_val = int(max(-1.0, min(1.0, float(s[1]))) * 32767)
                if channels == 1:
                    packed_frames += struct.pack('<h', int((l_val + r_val) / 2))
                else:
                    packed_frames += struct.pack('<hh', l_val, r_val)
            else:
                val = max(-1.0, min(1.0, float(s)))
                pcm_val = int(val * 32767)
                if channels == 1:
                    packed_frames += struct.pack('<h', pcm_val)
                else:
                    packed_frames += struct.pack('<hh', pcm_val, pcm_val)
        wav.writeframes(packed_frames)
    print(f"[AUDIO] Generated {filepath} ({len(samples)/sample_rate:.2f}s)")

def generate_ambient_lab():
    # 15 seconds loopable subtle cleanroom airflow + 60Hz hum + gentle harmonic resonances
    duration = 15.0
    num_samples = int(duration * SAMPLE_RATE)
    samples = []
    
    # White noise base with low-pass filtered characteristic
    noise_state = 0.0
    for i in range(num_samples):
        t = i / SAMPLE_RATE
        # Cleanroom low hum (60Hz + 120Hz + 180Hz)
        hum = 0.08 * math.sin(2 * math.pi * 60 * t) + \
              0.03 * math.sin(2 * math.pi * 120 * t) + \
              0.015 * math.sin(2 * math.pi * 180 * t)
        
        # Subtle harmonic air resonator (850Hz modulated slowly)
        res_freq = 780 + 30 * math.sin(2 * math.pi * 0.2 * t)
        res = 0.012 * math.sin(2 * math.pi * res_freq * t)
        
        # Soft pink-ish airflow noise
        raw_noise = (math.sin(i * 12.9898) * 43758.5453) % 1.0 - 0.5
        noise_state = 0.95 * noise_state + 0.05 * raw_noise
        airflow = noise_state * 0.04
        
        # Gentle stereo spread
        left = (hum + airflow + res) * 0.6
        right = (hum + airflow - res * 0.8) * 0.6
        samples.append((left, right))
    
    write_wav("ambient_lab.wav", samples)

def generate_bg_music():
    # 24-second seamless ambient intellectual progression
    # Soft chords in D minor (D - F - A - C), Bb maj7, G minor, A minor
    # Warm analog synth pad + soft sub bass + subtle high frequency crystal pulse
    duration = 24.0
    num_samples = int(duration * SAMPLE_RATE)
    samples = []
    
    # Chord progression timings (6 seconds each)
    # Chord 1: Dm9 (D3=146.83, F3=174.61, A3=220.00, C4=261.63, E4=329.63)
    # Chord 2: Bb_maj7 (Bb2=116.54, D3=146.83, F3=174.61, A3=220.00)
    # Chord 3: Gm7 (G2=98.00, Bb2=116.54, D3=146.83, F3=174.61)
    # Chord 4: Asus4-A (A2=110.00, D3=146.83, E3=164.81, G3=196.00)
    
    chords = [
        [146.83, 174.61, 220.00, 261.63, 329.63], # Dm9
        [116.54, 146.83, 174.61, 220.00, 293.66], # Bb maj7
        [98.00,  116.54, 146.83, 174.61, 220.00], # Gm9
        [110.00, 146.83, 164.81, 220.00, 277.18]  # A7sus4 -> A
    ]
    
    for i in range(num_samples):
        t = i / SAMPLE_RATE
        chord_idx = int(t / 6.0) % 4
        chord_t = t % 6.0
        active_chord = chords[chord_idx]
        
        # Warm pad envelope
        env = math.sin(math.pi * (chord_t / 6.0)) ** 0.6
        
        val_l = 0.0
        val_r = 0.0
        
        # Sub bass
        bass_freq = active_chord[0] * 0.5
        bass = 0.12 * math.sin(2 * math.pi * bass_freq * t) * env
        val_l += bass
        val_r += bass
        
        # Pad notes with soft chorus/detuning
        for n_idx, freq in enumerate(active_chord):
            # Left slightly detuned lower, right slightly detuned higher
            p_l = math.sin(2 * math.pi * (freq * 0.998) * t) + 0.3 * math.sin(4 * math.pi * freq * t)
            p_r = math.sin(2 * math.pi * (freq * 1.002) * t) + 0.3 * math.sin(4 * math.pi * freq * t)
            weight = 0.04 / (1.0 + n_idx * 0.2)
            val_l += p_l * weight * env
            val_r += p_r * weight * env
            
        # Subtle crystalline pulse every 1.5 seconds
        pulse_t = t % 1.5
        pulse_env = math.exp(-pulse_t * 6.0)
        pulse_freq = active_chord[-1] * 2.0
        crystal = 0.025 * math.sin(2 * math.pi * pulse_freq * t) * pulse_env
        val_l += crystal * 0.7
        val_r += crystal * 0.3
        
        # Final mix scaling (ambient volume background - never overpowers dialogue)
        master_vol = 0.18
        samples.append((val_l * master_vol, val_r * master_vol))
        
    write_wav("bg_music.wav", samples)

def generate_ui_click():
    duration = 0.06
    num_samples = int(duration * SAMPLE_RATE)
    samples = []
    for i in range(num_samples):
        t = i / SAMPLE_RATE
        env = math.exp(-t * 90.0)
        sig = (math.sin(2 * math.pi * 2400 * t) + 0.5 * math.sin(2 * math.pi * 4800 * t)) * env
        samples.append(sig * 0.25)
    write_wav("ui_click.wav", samples, channels=1)

def generate_scene_transition():
    duration = 1.2
    num_samples = int(duration * SAMPLE_RATE)
    samples = []
    for i in range(num_samples):
        t = i / SAMPLE_RATE
        # Envelope: rise and fall
        env = math.sin(math.pi * (t / duration)) ** 1.5
        # Pitch sweep from 220Hz to 660Hz then settling
        freq = 220.0 + 440.0 * (t / duration)
        sine = math.sin(2 * math.pi * freq * t)
        shimmer = math.sin(2 * math.pi * (freq * 2.5) * t) * 0.3
        val = (sine + shimmer) * env * 0.2
        # Panning sweep left to right
        pan = t / duration
        samples.append((val * (1.0 - pan), val * pan))
    write_wav("scene_transition.wav", samples)

def generate_calc_complete():
    # Two-tone ascending chime (880Hz -> 1320Hz)
    duration = 0.8
    num_samples = int(duration * SAMPLE_RATE)
    samples = []
    for i in range(num_samples):
        t = i / SAMPLE_RATE
        if t < 0.25:
            env = math.exp(-t * 12.0)
            sig = (math.sin(2 * math.pi * 880 * t) + 0.3 * math.sin(2 * math.pi * 1760 * t)) * env
        else:
            t2 = t - 0.25
            env = math.exp(-t2 * 8.0)
            sig = (math.sin(2 * math.pi * 1320 * t) + 0.4 * math.sin(2 * math.pi * 2640 * t)) * env
        samples.append(sig * 0.28)
    write_wav("calc_complete.wav", samples, channels=1)

def generate_processor_hum():
    duration = 2.0
    num_samples = int(duration * SAMPLE_RATE)
    samples = []
    for i in range(num_samples):
        t = i / SAMPLE_RATE
        env = math.sin(math.pi * (t / duration))
        # Digital high frequency micro-pulses (1.2kHz + 3.6kHz modulated)
        pulse = math.sin(2 * math.pi * 1200 * t) * (1.0 + 0.5 * math.sin(2 * math.pi * 40 * t))
        val = pulse * env * 0.15
        samples.append((val * 0.6, val * 0.8))
    write_wav("processor_hum.wav", samples)

def main():
    print("Generating procedural audio assets...")
    generate_ambient_lab()
    generate_bg_music()
    generate_ui_click()
    generate_scene_transition()
    generate_calc_complete()
    generate_processor_hum()
    print("All audio assets successfully generated in static/audio/!")

if __name__ == '__main__':
    main()
