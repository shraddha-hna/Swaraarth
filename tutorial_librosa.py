
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import scipy
matplotlib.use('TkAgg')  # interactive backend

scale = []
def calculate_notes(input):
    for i in range(13):
        scale.append(input * (2**(i/12)))
    return scale


# Load audio (automatically converts to float32)
y, sr = librosa.load('output_Sa.wav')

sos = scipy.signal.butter(4, 50, btype='highpass', fs=sr, output='sos')  # cutoff freq 50 Hz
y_filtered = scipy.signal.sosfilt(sos, y)
# Compute onset envelope
onset_env = librosa.onset.onset_strength(y=y_filtered, sr=sr)

# Detect onsets (in frames)
onset_frames = librosa.onset.onset_detect(onset_envelope=onset_env, sr=sr)

# Convert frame indices to time (seconds)
onset_times = librosa.frames_to_time(onset_frames, sr=sr)

onset_strengths = onset_env[onset_frames]

#print(onset_env)

# Print onset times and their strengths
#for t, s in zip(onset_times, onset_strengths):
    #print(f"Onset at {t:.3f} sec has strength {s:.3f}")

#max_onset_frame = np.argsort(onset_env)[-2]

# 2. Find the frame with maximum onset strength
max_onset_frame = np.argmax(onset_env)
max_onset_time = librosa.frames_to_time(max_onset_frame, sr=sr)

#print(f"Maximum onset at frame {max_onset_frame}, time {max_onset_time:.2f} sec")

# 3. Compute STFT around that onset
S = np.abs(librosa.stft(y_filtered, n_fft=2048, hop_length=512))

# Slice the spectrum at that frame
spectrum = S[:, max_onset_frame]

# 4. Find the frequency bin with maximum magnitude
max_bin = np.argmax(spectrum)
freqs = librosa.fft_frequencies(sr=sr, n_fft=2048)
dominant_freq = freqs[max_bin]

print(f"Dominant frequency at max onset: {dominant_freq:.2f} Hz")

print("Detected note start times (seconds):", onset_times)
# Plot waveform and detected onsets
plt.figure(figsize=(12, 4))
librosa.display.waveshow(y_filtered, sr=sr, alpha=0.6)
plt.vlines(onset_times, ymin=-1, ymax=1, color='r', linestyle='--', label='Onsets')
plt.title("Detected Note Onsets")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
#plt.show()
print("The User is singing in this scale:", librosa.hz_to_note(dominant_freq))

# replace the input frequency
scale = calculate_notes(dominant_freq)
print(f"Do: {scale[0]}")
print(f"Re: {scale[2]}")
print(f"Mi: {scale[4]}")
print(f"Fa: {scale[5]}")
print(f"So: {scale[7]}")
print(f"La: {scale[9]}")
print(f"Ti: {scale[11]}")
print(f"Do2: {scale[12]}")
do = scale[0]
dore = scale[1]
re = scale[2]
remi = scale[3]
mi = scale[4]
fa = scale[5]
faso = scale[6]
so = scale[7]
sola = scale[8]
la = scale[9]
lati = scale[10]
ti = scale[11]
do2 = scale[12]
