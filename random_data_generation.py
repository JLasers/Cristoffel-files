#!/usr/bin/env python

'''
Open data file and create a new data file with pseudo-random data selected from the original file.
Input file should have rows with columns of format:
  n	 Vs1      Vs2       Vp
  
 WARNING: NOT FINISHED YET
	To be done: 
		-Problem: The output file can contain any number of data points
		-Generalize file locations
'''
from random import randint as rand
import numpy as np

infile = 'c:\Users\John\Documents\Projects\Cristoffel-master\MgO_100_010.out'							#input file
outfile = 'c:\Users\John\Documents\Projects\Cristoffel-master\MgO_100_010_random.dat'			#output file
header = '  n		Vs1 		    Vs2  	     Vp'																						#file header

#setting up some variables
nlines = 91						#number of data  in input file
count = 0							#variable used to determine what row you are on	
step = rand(1,5)				#step size
stop = rand(1,nlines)		#where to stop scanning through, decides where the first data point is
start = False					#whether or not you should begin stepping through the data

#main program
with open(infile) as infile, open(outfile, "w") as outfile:						#open both files
	outfile.write(header)																		#write the header to the outfile
	outfile.write('\n')				
	for row in infile:																				#begin scanning through the file
		count = count + 1
		if count == stop:																			#stop scanning through the file
			start = True
		if start == True:																			#begin stepping through the file and recording
			if count%step == 0:																	#data points in outfile
				outfile.write(row)
				
print 'The deed has been done.'															#fin