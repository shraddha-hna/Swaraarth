from pynput import keyboard
import threading
import pyaudio
import wave

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
WAVE_OUTPUT_FILENAME = "output_Sa.wav"

recording_event = threading.Event()
stop_event = threading.Event()
frames = []
listener = None  # will hold the reference to the listener object

def record_audio():
    global frames
    frames = []
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    print("Recording started. Press 's' to stop.")
    while not stop_event.is_set():
        data = stream.read(CHUNK)
        frames.append(data)
    print("Finished recording.")
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    stop_event.clear()
    recording_event.clear()
    # Stop the listener after saving file
    if listener is not None:
        listener.stop()

def on_press(key):
    global listener
    try:
        if key.char == 'b' and not recording_event.is_set():
            recording_event.set()
            stop_event.clear()
            t = threading.Thread(target=record_audio)
            t.start()
        elif key.char == 's' and recording_event.is_set():
            stop_event.set()
    except AttributeError:
        if key == keyboard.Key.esc:
            if listener is not None:
                listener.stop()

def main():
    global listener
    print("Welcome to Swaraarth.")
    print("Press 'b' to start recording. Press 's' to stop recording. (Program will auto-exit after save.)")
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()

if __name__ == "__main__":
    main()


