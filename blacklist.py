#!/usr/bin/env python3
import sys, os

blacklist = ".blklst"

def add_to_blacklist(files):
	with open(blacklist, "a") as fd:
		for file in files:
			fd.write("\n" + file)	

def main():
	args = sys.argv
	files = []
	
	for i in range(1, len(args)):
		files.append(os.path.abspath(args[i]))

	add_to_blacklist(files)	
	
main()
