import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
import sys
from scipy.fft import fft, fftfreq, rfft, rfftfreq
import scipy
import librosa
np.set_printoptions(threshold=sys.maxsize)

# Load the audio file
file_path = "output_Sa.wav"
sample_rate, data = wav.read(file_path)


# Normalize data to range [-1, 1] if it's integer type
#if np.issubdtype(data.dtype, np.integer):
#    data = data / np.iinfo(data.dtype).max

#data = data - np.mean(data)
# Design a 4th order Butterworth high-pass filter with cutoff 50 Hz
#sos = scipy.signal.butter(4, 50, btype='highpass', fs=sr, output='sos')

# Apply filter to audio signal
#data = scipy.signal.sosfilt(sos, data)
# Perform FFT
N = len(data)
yf = fft(data)
xf = fftfreq(N, 1 / sample_rate)
print(xf)


#sos = scipy.signal.butter(4, 50, btype='highpass', fs=sample_rate, output='sos')  # cutoff freq 50 Hz
#y_filtered = scipy.signal.sosfilt(sos, yf)
# Take the magnitude of the FFT results
magnitude = np.abs(yf[:N//2])
frequencies = xf[:N//2]
# Find the index of the dominant frequency
dominant_index = np.argmax(magnitude)
dominant_frequency = frequencies[dominant_index]

print(f"Dominant frequency: {dominant_frequency:.2f} Hz")
print(yf[np.argmax(np.abs(xf))])

# Only take positive frequencies
idx = np.where(xf >= 0)
xf = xf[idx]
yf = np.abs(yf[idx])


# Find dominant frequencies
threshold = np.max(yf) * 0.1   # only keep frequencies with >10% of max amplitude
dominant_freqs = xf[yf > threshold]
#print(dominant_freqs)
#onsets = librosa.onset.onset_detect(y=data, sr=sample_rate)



# Plot spectrum
plt.figure(figsize=(12, 6))
plt.plot(xf, yf)
plt.title("Frequency Spectrum of Audio Signal")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.grid(True)
#plt.xlim(0, 5000)  # Show up to 5 kHz for clarity
plt.show()