import librosa
import numpy as np
import matplotlib.pyplot as plt

Sa_output, sr = librosa.load('output_Sa.wav', sr=44100)
FRAME_SIZE = 1024
HOP_LENGTH = 512

def amplitude_envelope(signal, frame_size, hop_length):
    amp_env = []
    for i in range(0,len(signal),hop_length):
        ae = max(signal[i:i+frame_size])
        amp_env.append(ae)
    return np.array(amp_env)

#Calculate Amplitude Envelope
ae_Sa = amplitude_envelope(Sa_output, FRAME_SIZE, HOP_LENGTH)
frames_ae = range(0, ae_Sa.size)
t_ae = librosa.frames_to_time(frames_ae)

#Calculate Root Mean Square
rms_Sa = librosa.feature.rms(y=Sa_output,frame_length=FRAME_SIZE,hop_length=HOP_LENGTH)[0]
frames_rms = range(len(rms_Sa))
t_rms = librosa.frames_to_time(frames_rms)

#Calculate Zero Crossing Rate
zero_crossing_Sa = librosa.feature.zero_crossing_rate(y=Sa_output,frame_length=FRAME_SIZE,hop_length=HOP_LENGTH)
frames_zero = range(len(zero_crossing_Sa))
t_zero = librosa.frames_to_time(frames_zero)

plt.figure()
librosa.display.waveshow(Sa_output)
plt.plot(t_ae, ae_Sa)
plt.plot(t_rms, rms_Sa)
plt.plot(t_zero, zero_crossing_Sa)
plt.title('Sa')
plt.show()
