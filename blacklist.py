#!/usr/bin/env python3
import os, sys

blacklist = ".blklst"

def add_to_blacklist(args: list):
  with open(blacklist, "a") as file:
    for arg in args:
      file.write("\n" + arg)	

def main(sys_argv: list):
  if len(sys_argv) <= 1:
    sys.exit()

  args = []
 
  if sys_argv[1] == "-r":
    recursive_mode = True
    start = 2
  else:
    recursive_mode = False
    start = 1

  for i in range(start, len(sys_argv)):
    args.append(os.path.abspath(sys_argv[i]))
    if recursive_mode == True:
      # recursively add all files
      # and directories to args
      for dirpath, dirnames, filenames in os.walk(sys_argv[i], followlinks=True):
        for d in dirnames:
          args.append(os.path.abspath(os.path.join(dirpath, d)))

        for f in filenames:
          args.append(os.path.abspath(os.path.join(dirpath, f)))

  add_to_blacklist(args)

main(sys.argv)
