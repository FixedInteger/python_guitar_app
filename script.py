import numpy as np
import pyaudio

def generate_guitar_sound(frequency, duration=1.0, volume=0.5):
    # Parameters for audio generation
    sample_rate = 44100  # Samples per second
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    
    # Generate a sine wave at the specified frequency
    signal = volume * np.sin(2 * np.pi * frequency * t)
    
    return signal

def play_sound(signal):
    p = pyaudio.PyAudio()

    try:
        stream = p.open(
            format=pyaudio.paFloat32,
            channels=1,
            rate=44100,
            output=True
        )

        stream.start_stream()
        stream.write(signal.tobytes())
        stream.stop_stream()
        stream.close()

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        p.terminate()

if __name__ == "__main__":
    try:
        frequency = float(input("Enter the guitar frequency (in Hz): "))
        duration = float(input("Enter the duration (in seconds): "))
        volume = float(input("Enter the volume (0.0 - 1.0): "))

        sound_signal = generate_guitar_sound(frequency, duration, volume)
        play_sound(sound_signal)
    
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")
