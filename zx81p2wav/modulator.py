import math


class Modulator:

    def __init__(self, samplerate=22050):
        self.samplerate = samplerate
        self.waveform = bytes()

        num_samples = round(9 * 300e-6 * self.samplerate)
        template = [0] * num_samples
        phi = 2. * math.pi * 3333. / self.samplerate
        for t in range(num_samples):
            template[t] = 128 + round(127 * math.sin(t * phi))
        self.template = bytes(template)

    def silence(self, duration):
        self.waveform += b'\x80' * (round(duration * self.samplerate))

    def write_bytes(self, data):
        for b in data:
            self.write_byte(b)

    def write_byte(self, byte):
        for _ in range(8):
            self.write_bit(byte & 0x80 != 0)
            byte <<= 1

    def write_bit(self, bit):
        periods = 9 if bit else 4
        num_samples = round(periods * 300e-6 * self.samplerate)
        self.waveform += self.template[:num_samples] + \
            b'\x80' * round(1300e-6*self.samplerate)
