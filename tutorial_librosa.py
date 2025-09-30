
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # interactive backend

# Load audio (automatically converts to float32)
y, sr = librosa.load('output_alankara.wav')

# Compute onset envelope
onset_env = librosa.onset.onset_strength(y=y, sr=sr)

# Detect onsets (in frames)
onset_frames = librosa.onset.onset_detect(onset_envelope=onset_env, sr=sr)

# Convert frame indices to time (seconds)
onset_times = librosa.frames_to_time(onset_frames, sr=sr)

onset_strengths = onset_env[onset_frames]

# Print onset times and their strengths
for t, s in zip(onset_times, onset_strengths):
    print(f"Onset at {t:.3f} sec has strength {s:.3f}")

print("Detected note start times (seconds):", onset_times)
# Plot waveform and detected onsets
plt.figure(figsize=(12, 4))
librosa.display.waveshow(y, sr=sr, alpha=0.6)
plt.vlines(onset_times, ymin=-1, ymax=1, color='r', linestyle='--', label='Onsets')
plt.title("Detected Note Onsets")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.show()
