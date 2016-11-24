import struct
import wave
import pyaudio
import sys
from pydub import AudioSegment

CHUNK = 1024

from pydub import AudioSegment
from pydub.silence import split_on_silence

sound = AudioSegment.from_mp3("sounds/mp3files/161112_002.mp3")
chunks = split_on_silence(sound, 
    # must be silent for at least half a second
    min_silence_len=1000,

    # consider it silent if quieter than -16 dBFS
    silence_thresh=-30
)
for i, chunk in enumerate(chunks):
    chunk.export("sounds/chunks/chunk{0}.wav".format(i), format="wav")

"""convert mp3 files to WAV
sound = AudioSegment.from_mp3("./sounds/mp3files/161112_002.mp3")
sound.export("./sounds/161112_002.wav", format="wav")
wave_file = wave.open("./sounds/161112_002.wav", "r")

for i in range(wave_file.getnframes()):
    # read a single frame and advance to next frame
    current_frame = wave_file.readframes(1)

    # check for silence
    silent = True
    # wave frame samples are stored in little endian**
    # this example works for a single channel 16-bit per sample encoding
    unpacked_signed_value = struct.unpack("<h", current_frame) # *
    if abs(unpacked_signed_value[0]) > 500:
        silent = False

    if silent:
        print "Frame %s is silent." % wave_file.tell()
    else:
        print "Frame %s is not silent." % wave_file.tell()
"""