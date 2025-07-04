"""FSK Decoder"""
import wave
import numpy as np
from scipy.fftpack import fft


def load_wav(file_path):
    """
    Loads a WAV file and returns the audio signal and frame rate.
    :param file_path: Path to the WAV file
    :return: Tuple of (signal, frame_rate)
    """
    try:
        wav = wave.open(file_path, 'rb')
        frame_rate = wav.getframerate()
        n_frames = wav.getnframes()
        signal = wav.readframes(n_frames)
        signal = np.frombuffer(signal, dtype=np.int16)
        wav.close()
        return signal, frame_rate
    except FileNotFoundError:
        print(
            f"Error : File not found '{file_path}'.")
        return None, None


# Baud rate confirmed to be 10 after visual analysis
def decode_fsk(signal, frame_rate, baud_rate=10):
    """
    Decode FSK signal into bits.
    :param signal: Audio signal
    :param frame_rate: Frame rate of the audio signal
    :param baud_rate: Baud rate for decoding
    :return: Decoded bits as a string
    """
    f0, f1 = 1200, 2400  # Frequencies of '0' and '1' in Hz from visual analysis in Sonic Visualiser
    bit_duration = 1 / baud_rate  # Bitrate in seconds
    samples_per_bit = int(bit_duration * frame_rate)

    bits = ""
    for i in range(0, len(signal), samples_per_bit):
        segment = signal[i:i + samples_per_bit]
        spectrum = np.abs(fft(segment))
        freqs = np.fft.fftfreq(len(segment), 1 / frame_rate)
        peak_freq = freqs[np.argmax(spectrum[:len(freqs) // 2])]
        if abs(peak_freq - f0) < abs(peak_freq - f1):
            bits += "0"
        else:
            bits += "1"

    print(f"Bits read: {bits}")
    return bits


def bits_to_text(bits):
    """
    Convert a string of bits to text.
    :param bits: String of bits
    :return: Decoded text
    """
    try:
        text = ""
        for i in range(0, len(bits), 8):
            byte = bits[i:i + 8]
            if len(byte) == 8:
                char = chr(int(byte, 2))
                if char.isprintable():
                    text += char
                else:
                    text += '?'
        return text
    except ValueError:
        print("Error decoding bits to text.")
        return ""


def main(wav_path, baud_rate=100):
    """ entry point """
    signal, frame_rate = load_wav(wav_path)
    if signal is not None and frame_rate is not None:
        decoded_bits = decode_fsk(signal, frame_rate, baud_rate)
        if decoded_bits:
            text = bits_to_text(decoded_bits)
            print("Texte décodé :", text)
        else:
            print("Impossible de décoder les bits.")
    else:
        print("Impossible de charger le fichier audio.")


if __name__ == "__main__":
    FILE = "fsk_zer0ne/fsk_zer0ne.wav"
    # Baud rate confirmé à 10 après analyse visuelle
    main(FILE, baud_rate=10)
