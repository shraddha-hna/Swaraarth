import scipy
import librosa
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import numpy as np

#Load Audio and Noise
Sa_output, sr = librosa.load("Sagar_alankara.wav", sr=44100)
#noise, sr = librosa.load("noise.wav")

#Compute FFT of the audio and noise
ft = scipy.fft.fft(Sa_output)
#ft_noise = scipy.fft.fft(noise)


magnitude = np.absolute(ft)
frequencies = np.linspace(0, sr, len(magnitude))

#Plot Frequency Domain Signal
plt.figure()
plt.plot(frequencies[0:5000], magnitude[0:5000])
plt.xlabel("frequency")
plt.ylabel("magnitude")
plt.show()