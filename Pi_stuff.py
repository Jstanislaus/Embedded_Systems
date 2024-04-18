import pyaudio

def capture_audio():
    CHUNK = 1
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

    print("Capturing audio. Press Ctrl+C to stop.")

    try:
        while True:
            audio_data = stream.read(CHUNK)
            # Process audio data as needed (e.g., save to a file, analyze, etc.)
            # You can replace this print statement with your desired action.
            print("Audio data received:", len(audio_data))
    except KeyboardInterrupt:
        print("Recording stopped by user.")
        stream.stop_stream()
        stream.close()
        p.terminate()

if __name__ == "__main__":
    capture_audio()