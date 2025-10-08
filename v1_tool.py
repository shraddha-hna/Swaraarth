import librosa
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

y, sr = librosa.load('output_Sa.wav', sr=44100)
D = librosa.stft(y)
frequencies = librosa.fft_frequencies(sr=44100)
times = librosa.frames_to_time(np.arange(D.shape[1]), sr=44100)
print(len(frequencies))
print(D.shape)
#strength = librosa.onset.onset_strength(y=y)
#print(strength)
#print(D[0][:])

#fig = go.Figure()
#fig.add_trace(go.scatter(x=frequencies, y=times, mode='lines'))
#fig.show()