"""PyAudio Example: Play a WAVE file."""

import pyaudio
import wave
import sys
from contextlib import closing

CHUNK = 1024

# if len(sys.argv) < 2:
#     print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
#     sys.exit(-1)

# infiles = ["cat_meow2.wav", "cat_meow2.wav", ]
infiles = ["chunk0.wav", "chunk1.wav"]
outfile = "result.wav"

with closing( wave.open( outfile, 'wb' ) ) as output:

	# find sample rate from 1st file:
	with closing( wave.open( infiles[0]) ) as w:
		output.setparams( w.getparams() )

	for infile in infiles:
		with closing ( wave.open( infile )) as w:
			output.writeframes( w.readframes( w.getnframes() ))



#========================================
# data = []
# for infile in infiles:
# 	w = wave.open( infile, 'rb' )
# 	data.append( [ w.getparams(), w.readframes( w.getnframes() ) ] )
# 	w.close()
# output = wave.open( outfile, 'wb' )
# output.setparams( data[0][0] )
# output.writeframes( data[0][1] )
# output.writeframes( data[1][1] )
#output.close()
#========================================

w = wave.open("result.wav", "rb")
p = pyaudio.PyAudio()
stream = p.open( format = p.get_format_from_width( w.getsampwidth() ),
                channels = w.getnchannels(),
                rate = w.getframerate(),
                output = True )
data1 = w.readframes( CHUNK )

while data1 != '':
    stream.write( data1 )
    data1 = w.readframes( CHUNK )

stream.stop_stream()
stream.close()

p.terminate()



