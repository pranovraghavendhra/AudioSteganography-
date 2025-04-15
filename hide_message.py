import wave

def text_to_bits(text):
    return ''.join(format(ord(i), '08b') for i in text)

def hide_data(audio_path, output_path, message):
    audio = wave.open(audio_path, mode='rb')
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))

    message += '###' 
    bits = text_to_bits(message)

    if len(bits) > len(frame_bytes):
        raise ValueError("Message too long to hide in audio!")

    for i, bit in enumerate(bits):
        frame_bytes[i] = (frame_bytes[i] & 254) | int(bit)

    modified_audio = wave.open(output_path, 'wb')
    modified_audio.setparams(audio.getparams())
    modified_audio.writeframes(bytes(frame_bytes))
    audio.close()
    modified_audio.close()

    print(" Message successfully hidden in 'output.wav'")


msg = input(" Enter the secret message to hide: ")
hide_data("input.wav", "output.wav", msg)
