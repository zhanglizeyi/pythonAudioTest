import sys
import string, os
import re
from collections import Counter

#tokens = []

# This point is to modify the file and mapping out all the puncuations from file
def analyzer(ifile):
	global tokens

	global hashTable


	file = open(ifile, "r")
	file = file.read();
	tokens = [e.lower() for e in map(string.strip, re.split("(\W+)",file)) if len(e) > 0 and not re.match("\W", e)]
	#tokens = []
	#for i in file:
		#tokens.append([e.lower() for e in map(string.strip, re.split("(\W+)",i)) if len(e) > 0 and not re.match("\W", e)])
		#tokens = [e.lower() for e in map(string.strip, re.split("(\W+)",file)) if len(e) > 0 and not re.match("\W", e)]
	print tokens

#def storeHash(tokens):
	



if __name__ == "__main__":
	#print "Input file path:"
	#ifile = raw_input("Which file you want to process? ");
	analyzer("testTxt1.txt")
	print
	print

	dictionary = {}
	for i in range(10):
		dictionary[i] = chr(ord('a') + i)
	print dictionary

	dictionary = {}
