import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
from scipy.signal import stft
import scipy

# Load audio file
file_path = "output_Sa.wav"
sample_rate, data = wav.read(file_path)

# If stereo, take one channel
if len(data.shape) > 1:
    data = data[:, 0]

# Normalize if integer type
if np.issubdtype(data.dtype, np.integer):
    data = data / np.iinfo(data.dtype).max

sos = scipy.signal.butter(4, 50, btype='highpass', fs=sample_rate, output='sos')  # cutoff freq 50 Hz
y_filtered = scipy.signal.sosfilt(sos, data)

# Compute STFT
f, t, Zxx = stft(y_filtered, fs=sample_rate, nperseg=2048, noverlap=1024)
magnitude = np.abs(Zxx)

# Find dominant frequency at each time frame
dominant_freqs = f[np.argmax(magnitude, axis=0)]

# Group into note segments (tolerance = 5 Hz)
tolerance = 5
notes = []
start_time = t[0]
current_freq = dominant_freqs[0]

for i in range(1, len(dominant_freqs)):
    if abs(dominant_freqs[i] - current_freq) > tolerance:
        # Note ended, save it
        notes.append((current_freq, start_time, t[i]))
        # Start new note
        start_time = t[i]
        current_freq = dominant_freqs[i]

# Append last note
notes.append((current_freq, start_time, t[-1]))

# Print detected notes
for freq, start, end in notes:
    print(f"Note: {freq:.2f} Hz, Start: {start:.2f}s, End: {end:.2f}s")

# Optional: plot spectrogram
plt.figure(figsize=(12, 6))
plt.pcolormesh(t, f, 20*np.log10(magnitude + 1e-6), shading='gouraud')
plt.title("Spectrogram (Time vs Frequency)")
plt.ylabel("Frequency [Hz]")
plt.xlabel("Time [s]")
plt.colorbar(label="Amplitude (dB)")
plt.ylim(0, 2000)  # limit to 2kHz for clarity
plt.show()
