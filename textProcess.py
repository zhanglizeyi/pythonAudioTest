import sys
import hashTable
import string, os
import re
from collections import Counter

#tokens = []

# This point is to modify the file and mapping out all the puncuations from file
def analyzer(ifile):
	global tokens


	file = open(ifile, "r")
	file = file.read();
	tokens = [e.lower() for e in map(string.strip, re.split("(\W+)",file)) if len(e) > 0 and not re.match("\W", e)]
	#print tokens

def storeHash(tokens):
	



if __name__ == "__main__":
	print "Input file path:"
	ifile = raw_input("Which file? : ");
	analyzer(ifile)
