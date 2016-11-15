#!/usr/bin/python

import sys
import string, os
import re
import csv
import numpy
import collections

#tokens = []

# This point is to modify the file and mapping out all the puncuations from file
def analyzer(ifile):
	global tokens
	global hashT
	hashT = dict()

	file = open(ifile, "r")
	file = file.read();
	#This is to filter out puncuation in the text, should not worry about in input 
	tokens = [e.lower() for e in map(string.strip, re.split("(\W+)",file)) if len(e) > 0 and not re.match("\W", e)]

	#iterate key and value to hash table with duplicate words/values
	hashT = [(key, value) for key,value in enumerate(tokens)]
	

	#declear one list track values 
	#counter is frequency of words appear
	temp = dict()
	counter = 0
	
	for key, value in hashT:
		counter = 1
		for a,b in hashT:
			if b == value:
				temp[key] = (value, counter)
				dict(temp)  
				counter += 1

	#temp.sort()
	# print temp
	print temp
	#rank of 
	# for value, freq in temp.items():
		# for v, f in temp.items():
			#implement a sort here
			# if freq > f:
			# 	print "> " + str(freq)
			# elif freq == f:
			# 	print "=="
			# else:
			# 	print  "< " + str(f)
			
			

if __name__ == "__main__":
	print "Input file path:"
	ifile = raw_input("Which file? : ");
	analyzer(ifile)
