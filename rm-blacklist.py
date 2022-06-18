#!/usr/bin/env python3
import os, sys

blacklist = ".blklst"

def check_against_blacklist(files):
	with open(blacklist, "r") as fd:
		lines = fd.readlines()
		lines = [line.rstrip() for line in lines]

	# remove comments and ignore lines
  # containing only whitespace
	lines_to_remove = []
	for line in lines:
		if line == '' or line[0] == '#': 
			lines_to_remove.append(line)

	for line in lines_to_remove:
		lines.remove(line)

	files_to_remove = []
	for file in files:
		for line in lines:
			if os.path.abspath(file) == line:
				print("Cannot rm " + file + ": file is blacklisted")
				files_to_remove.append(file)

	for file in files_to_remove:
		files.remove(file)
			
def main():
	files = []
	flags = []
	for i in range(1, len(sys.argv)):
		if '-' == sys.argv[i][0]:
			flags.append(sys.argv[i])
		else:
			files.append(sys.argv[i])	

	check_against_blacklist(files)

	if len(files) == 0:
		quit()	

	cmd = "rm"
	for flag in flags: 
		cmd = cmd + " " + flag 

	for file in files:
		cmd = cmd + " " + file

	os.system(cmd)

main()
