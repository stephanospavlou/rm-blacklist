#!/usr/bin/env python3

import os, sys

blacklist = ".blklst"

def check_against_blacklist(files):
	with open(blacklist, "r") as fd:
		lines = fd.readlines()
		lines = [line.rstrip() for line in lines]

	for file in files:
		for line in lines:
			if line[0] != '#' and os.path.abspath(file) == line:
				print("Cannot rm " + file + ": file is blacklisted")
				files.remove(file)
			
def main():
	files = []
	args = []
	for i in range(1, len(sys.argv)):
		if '-' == sys.argv[i][0]:
			args.append(sys.argv[i])
		else:
			files.append(sys.argv[i])	

	check_against_blacklist(files)

	if len(files) == 0:
		quit()	

	cmd = "rm"
	for arg in args: 
		cmd = cmd + " " + arg 

	for file in files:
		cmd = cmd + " " + file

	os.system(cmd)

main()
