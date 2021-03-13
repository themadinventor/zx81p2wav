import argparse
import zx81p2wav
from zx81p2wav.modulator import Modulator
import wave


def convert(pfile, wavfile):
    # prepend empty filename
    data = b'\x80' + pfile.read()

    modulator = Modulator()

    modulator.silence(0.2)
    modulator.write_bytes(data)
    modulator.silence(0.05)

    wav = wave.open(wavfile, 'wb')
    wav.setnchannels(1)
    wav.setsampwidth(1)
    wav.setframerate(modulator.samplerate)
    wav.writeframes(modulator.waveform)


def main():
    parser = argparse.ArgumentParser(
            description='zx81p2wav %s' % zx81p2wav.__version__,
            prog='zx81p2wav',
            epilog='Website: https://github.com/themadinventor/zx81p2wav')

    parser.add_argument(
            'pfile',
            help='Input P-file'
            )

    parser.add_argument(
            'wavfile',
            help='Output wave-file'
            )

    args = parser.parse_args()

    with open(args.pfile, 'rb') as pfile:
        with open(args.wavfile, 'wb') as wavfile:
            convert(pfile, wavfile)
