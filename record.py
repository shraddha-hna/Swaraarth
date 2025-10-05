
import pyaudio
import wave
import keyboard
import threading

# Parameters
FORMAT = pyaudio.paInt16  # Audio format (16-bit PCM)
CHANNELS = 1              # Single channel for microphone
RATE = 44100              # Sample rate
CHUNK = 1024              # Block size
RECORD_SECONDS = 20        # Duration of recording
WAVE_OUTPUT_FILENAME = "output_sa.wav"  # Output file

def record_audio():

    # Initialize PyAudio
    p = pyaudio.PyAudio()
    # Open stream
    stream = p.open(format=FORMAT,
		channels=CHANNELS,
		rate=RATE,
		input=True,
		frames_per_buffer=CHUNK)

    print("Recording SA")

    frames = []

    # Start recording
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Finished recording.")

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Save the recorded data as a WAV file
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def listen_for_key():
    keyboard.add_hotkey('b', record_audio())  # Trigger `my_function` when 'a' is pressed
    keyboard.wait()

if __name__ == "__main__":
    # Start the listener in a separate thread
    listener_thread = threading.Thread(target=listen_for_key)
    listener_thread.start()

    # Your main program continues to run from here
    print("Welcome to Swaraarth.")
    print("Press b to record sa and generate your original singing scale.")
    # Example of main program doing other things


import pyaudio
import wave
import keyboard
import threading

# Parameters
FORMAT = pyaudio.paInt16  # Audio format (16-bit PCM)
CHANNELS = 1              # Single channel for microphone
RATE = 44100              # Sample rate
CHUNK = 1024              # Block size
WAVE_OUTPUT_FILENAME = "output_alankara.wav"  # Output file

# Global flag to control recording
is_recording = False

def record_audio():
    global is_recording

    # Initialize PyAudio
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Recording... Press 's' to stop.")

    frames = []
    is_recording = True

    while is_recording:  # keep recording until flag is cleared
        data = stream.read(CHUNK)
        frames.append(data)

    print("Finished recording.")

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Save the recorded data as a WAV file
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def start_recording():
    # Run recording in a separate thread so it doesn’t block
    threading.Thread(target=record_audio).start()

def stop_recording():
    global is_recording
    is_recording = False  # this will break the loop in record_audio()

def listen_for_key():
    keyboard.add_hotkey('b', start_recording)  # press 'b' to start recording
    keyboard.add_hotkey('s', stop_recording)   # press 's' to stop recording
    keyboard.wait()  # wait indefinitely for keys

if __name__ == "__main__":
    # Start the listener in a separate thread
    listener_thread = threading.Thread(target=listen_for_key, daemon=True)
    listener_thread.start()

    print("Welcome to Swaraarth.")
    print("Press 'b' to start recording.")
    print("Press 's' to stop and save recording.")
