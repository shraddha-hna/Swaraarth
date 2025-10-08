import librosa
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal 
import scipy.io.wavfile as wav

file_path = "/home/shraddha/Documents/Recurse/Swaraarth/audio/Swarmalika_Kaafi.wav"
# 1. High-pass filter (removes DC and slow varying offset)
def highpass_filter(data, fs, cutoff=20, order=5):
    sos = signal.butter(order, cutoff, 'hp', fs=fs, output='sos')
    filtered = signal.sosfilt(sos, data)
    return filtered

def amplitude_envelope(signal, frame_size, hop_length):
    amp_env = []
    for i in range(0,len(signal),hop_length):
        ae = max(signal[i:i+frame_size])
        amp_env.append(ae)
    return np.array(amp_env)

#Sa_output, sr = librosa.load('output_Sa.wav', sr=44100)
sr, Sa_output = wav.read(file_path)
Sa_output = Sa_output - np.mean(Sa_output)
Sa_output_filtered = highpass_filter(Sa_output, sr)
FRAME_SIZE = 1024
HOP_LENGTH = 512

#Calculate Amplitude Envelope
ae_Sa = amplitude_envelope(Sa_output_filtered, FRAME_SIZE, HOP_LENGTH)
frames_ae = range(0, ae_Sa.size)
t_ae = librosa.frames_to_time(frames_ae)

#Calculate Root Mean Square
rms_Sa = librosa.feature.rms(y=Sa_output_filtered,frame_length=FRAME_SIZE,hop_length=HOP_LENGTH)[0]
frames_rms = range(len(rms_Sa))
t_rms = librosa.frames_to_time(frames_rms)

#Calculate Zero Crossing Rate
zero_crossing_Sa = librosa.feature.zero_crossing_rate(y=Sa_output_filtered,frame_length=FRAME_SIZE,hop_length=HOP_LENGTH)
frames_zero = range(len(zero_crossing_Sa))
t_zero = librosa.frames_to_time(frames_zero)

plt.figure()

plt.plot(t_ae, ae_Sa, label='amp_env', color='b')
#plt.plot(t_zero, zero_crossing_Sa, label='zero_crossing_Sa', color='r')
# If you want to include rms_Sa, uncomment below:
plt.plot(t_rms, rms_Sa, label='rms', color='g')

plt.title('Sa Signal Analysis')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude / Value')
plt.legend()
plt.grid(True)
plt.show()



#To find sharp increase in the amplitude envelope(onset detection)
#Method 1: Difference derivative
diff_ae = np.diff(ae_Sa)
note_onset_time = t_ae[np.argmax(diff_ae)]
print(note_onset_time)
