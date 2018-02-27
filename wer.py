#-*- coding: utf-8 -*-
#!/usr/bin/env python

import sys
import os
import numpy as np


'''
	Name: Leonardo Dutra
	Github: github.com/dutraleonardo
	Linkedin: www.linkedin.com/in/dutraleonardo/

	This is my approach to solve the Zoom Media assessment.

	Requirements:
	Numpy

	How to install all requirements:
	pip install -r requirements.txt

	How to run:
	Execute the following coe -> python wer.py <reference_file.txt> <hypothesis_file.txt>
	e.g.: python wer.py Scripted_Benchmark.txt Scripted_Laptop.txt

	ps: I passed all hypothesis and references files to the same directory of wer.py
'''

def distance(r, h):
	# r it's the reference
	# h it's the hypothesis

	dist = np.zeros((len(r)+1)*(len(h)+1), dtype=np.uint8).reshape((len(r)+1, len(h)+1))

	# Creating the matrix
	for i in range(len(r)+1):
	    for j in range(len(h)+1):
	        if i == 0: 
	            dist[0][j] = j
	        elif j == 0: 
	            dist[i][0] = i

	for i in range(1, len(r)+1):
	    for j in range(1, len(h)+1):

	        if r[i-1] == h[j-1]:
	            dist[i][j] = dist[i-1][j-1]
	        else:
	            substitution = dist[i-1][j-1] + 1
	            deletion = dist[i-1][j] + 1
	            insertion = dist[i][j-1] + 1
	            dist[i][j] = min(insertion, deletion, substitution)
	return dist

def get_wer(r, h):
	
	matrix = distance(r, h)	

	result = float(matrix[len(r)][len(h)]) / len(r) * 100
	print("Your Word Error Rate (WER) percentage is: " + str("%.2f" % result) + "%")

if __name__ == '__main__':
    reference_filename = sys.argv[1]
    hypothesis_filename = sys.argv[2]
    r = open(reference_filename, mode='r', errors='ignore').read().split()
    h = open(hypothesis_filename, mode='r', errors='ignore').read().split()
    get_wer(r, h)