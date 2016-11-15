#!/usr/bin/python

import sys
import string, os
import re
import csv
import collections
import operator
from collections import Counter

#tokens = []

# This point is to modify the file and mapping out all the puncuations from file
def analyzer(ifile):
	global tokens
	#global hashT
	#hashT = dict()

	file = open(ifile, "r")
	file = file.read();
	#This is to filter out puncuation in the text, should not worry about in input 
	tokens = [e.lower() for e in map(string.strip, re.split("(\W+)",file)) if len(e) > 0 and not re.match("\W", e)]

	#print tokens
	print len(tokens)
	#iterate key and value to hash table with duplicate words/values
	#hashT = [(key, value) for key,value in enumerate(tokens)]
	

	#declear one list track values 
	#counter is frequency of words appear
	# temp = dict()
	# counter = 0
	
	# for key, value in hashT:
	# 	counter = 1
	# 	for a,b in hashT:
	# 		if b == value:
	# 			temp[key] = (value, counter)
	# 			dict(temp)  
	# 			counter += 1

	# #temp.sort()
	# print temp
	
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
	#print "Input file path:"
	#ifile = raw_input("Which file you want to process? ");
	analyzer("testTxt1.txt")

	print
	print
	dictionary = {}
	freq = Counter(tokens)
	# counter will return a list  (words, freq) {'test': 10, 'is': 2, ...}

	#print freq
	

	for i in range (len(tokens)):
		dictionary[tokens[i]] = freq[tokens[i]]

	#print dictionary

	sorted_dict = sorted( dictionary.items(), key = lambda x: (-x[1], x[0]))
	#dictionary = 
	newList = sorted_dict

	print sorted_dict
	# sorted --> list of sorted tuples based on the frequency : [('text', 1), ('am', 1), ...]

	print
	print
	print newList[9]

