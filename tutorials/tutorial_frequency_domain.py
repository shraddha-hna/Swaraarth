import scipy
import librosa
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import numpy as np

file_path = "/home/shraddha/Documents/Recurse/Swaraarth/audio/Swarmalika_Kaafi.wav"
#Load Audio
Sa_output, sr = librosa.load(file_path, sr=44100)

#Compute FFT of the audio and noise
ft = scipy.fft.fft(Sa_output)
magnitude = np.absolute(ft)
frequencies = np.linspace(0, sr, len(magnitude))

#Plot Frequency Domain Signal
plt.figure()
plt.plot(frequencies, magnitude)
plt.xlabel("frequency")
plt.ylabel("magnitude")
plt.show()