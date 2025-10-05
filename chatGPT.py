import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import sys
from scipy.fft import fft, fftfreq
np.set_printoptions(threshold=sys.maxsize)

# Load the audio file
file_path = "output_Sa.wav"
sample_rate, data = wav.read(file_path)

# If stereo, take one channel
if len(data.shape) > 1:
    data = data[:, 0]

# Normalize data to range [-1, 1] if it's integer type
if np.issubdtype(data.dtype, np.integer):
    data = data / np.iinfo(data.dtype).max

# Perform FFT
N = len(data)
yf = fft(data)
xf = fftfreq(N, 1 / sample_rate)

# Only take positive frequencies
idx = np.where(xf >= 0)
xf = xf[idx]
yf = np.abs(yf[idx])

print(yf)

# Find dominant frequencies
threshold = np.max(yf) * 0.1   # only keep frequencies with >10% of max amplitude
dominant_freqs = xf[yf > threshold]
#print(dominant_freqs)

# Plot spectrum
plt.figure(figsize=(12, 6))
plt.plot(xf, yf)
plt.title("Frequency Spectrum of Audio Signal")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.xlim(0, 5000)  # Show up to 5 kHz for clarity
plt.show()

# Print top dominant frequencies
print(dominant_freqs[:20])
