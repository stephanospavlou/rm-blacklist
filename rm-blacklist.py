#!/usr/bin/env python3
import os, sys

blacklist = ".blklst"

def check_against_blacklist(args: list) -> list:
  with open(blacklist, "r") as file:
    lines = file.readlines()

  new_args = args

  for line in lines:
    line = line.strip()

    if line == "" or line[0] == '#':
      continue
    else:
      for arg in args:
        if os.path.abspath(arg) == line:
          print("Cannot rm " + arg + ": file is blacklisted")
          # there is an inefficiency here:
          # we continue to check args that
          # we have already determined are
          # blacklisted.
          new_args.remove(arg)

  return new_args
          
def main(sys_argv: list):
  args = []
  opts = []

  # separate options from args
  for i in range(1, len(sys_argv)):
    if '-' == sys_argv[i][0]:
      opts.append(sys_argv[i])
    else:
      args.append(sys_argv[i])

  new_args = check_against_blacklist(args)
  # in case all args are blacklisted,
  # just exit. (rm prints an error when
  # given no arguments and that's pretty
  # redundant after rm-blacklist has
  # printed its own)
  if len(new_args) == 0:
    sys.exit()

  com = "rm"
  for opt in opts:
    com = com + " " + opt

  for arg in new_args:
    com = com + " " + arg

  os.system(com)

main(sys.argv)
