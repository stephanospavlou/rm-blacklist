#!/usr/bin/env python3

import os, sys

blacklist = ".blklst"

def check_against_blacklist(files):
	with open(blacklist, "r") as fd:
		for file in files:
			if file in fd.read():
				print("Cannot rm "+file+": file is blacklisted")
				files.remove(file)
		
def parse_args(args):
	files = []
	for i in range(1, len(sys.argv)):
		if "-" not in sys.argv[i]:
			files.append(sys.argv[i])

	return files
		
def main(args):
	files = parse_args(args)
	check_against_blacklist(files)

	cmd = "rm "
	for file in files: 
		cmd = cmd + file

	os.system(cmd)
	
	print(files)

main(sys.argv)
