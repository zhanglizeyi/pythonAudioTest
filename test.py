"""PyAudio Example: Play a WAVE file."""

import pyaudio
import audiolab, scipy
import wave
import sys

CHUNK = 1024

# if len(sys.argv) < 2:
#     print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
#     sys.exit(-1)
w1 = wave.open("cow2.wav", "rb")
w2 = wave.open("cat_meow2", "rb")

p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(w1.getsampwidth()),
                channels=w1.getnchannels(),
                rate=w1.getframerate(),
                output=True)

data1 = w1.readframes(CHUNK)


while data1 != '':
    stream.write(data1)
    data1 = w1.readframes(CHUNK)

stream.stop_stream()
stream.close()

p.terminate()