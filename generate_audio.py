import numpy as np
import wave

def generate_sine_wave(filename, duration=5, freq=440, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    audio = 0.5 * np.sin(2 * np.pi * freq * t)
    audio = (audio * 32767).astype(np.int16)

    with wave.open(filename, 'w') as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(sample_rate)
        f.writeframes(audio.tobytes())

    print(f"[INFO] 5-second audio file '{filename}' generated successfully.")

generate_sine_wave("input.wav")
