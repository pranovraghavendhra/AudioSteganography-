import wave

def extract_data(audio_path):
    audio = wave.open(audio_path, mode='rb')
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))

    extracted_bits = [str(byte & 1) for byte in frame_bytes]
    byte_chunks = [''.join(extracted_bits[i:i+8]) for i in range(0, len(extracted_bits), 8)]
    decoded_message = ''.join([chr(int(byte, 2)) for byte in byte_chunks])

    hidden_message = decoded_message.split('###')[0]
    audio.close()
    return hidden_message

hidden_msg = extract_data("output.wav")
print(" Hidden message extracted:")
print( hidden_msg)
