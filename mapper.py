#!/usr/bin/env python
import sys

stopwords = set(['the', 'and', 'i', 'to', 'of', 'a', 'you', 'if', 'which', 'when', 'my', 'that', 'is', 'not','in', 'me', 'it', 'for', 'with', 'be', 'your', 'this', 'his', ',', '.', '[', ']', '(', ')', '&', '/', '-', '?', '!', '$','%', ';', ':', '`', '~', '*', '^']) 

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip().lower()
   
 # split the line into words; splits on any whitespace
    words = line.split()

    # output tuples (word, 1) in tab-delimited format
    for word in words:
	if word not in stopwords:
        	print '%s\t%s' % (word, "1")
