#!/usr/bin/env python
import os, sys

blacklistPath = ".blklst" # SET ME!

usage = '''Usage: blacklist [options] <file | directory> <file | directory> ...
Options:
\t-h, --help\tdisplay this help and exit
\t-r        \tblacklist directory/directories recursively'''

if len(sys.argv) == 1 or sys.argv[1] == '-h' or sys.argv[1] == '--help':
    print(usage)
    sys.exit()

if sys.argv[1] == '-r':
    recursiveMode = True
    filesToBlacklist = sys.argv[2:]
else:
    recursiveMode = False
    filesToBlacklist = sys.argv[1:]

with open(blacklistPath, "a") as blacklist:
    for file in filesToBlacklist:
        blacklist.write("\n" + os.path.abspath(file))
        if recursiveMode == True:
            for dirPath, dirNames, fileNames in os.walk(file, followlinks=True):
                for dirName in dirNames:
                    blacklist.write("\n" +
                        os.path.abspath(os.path.join(dirPath, dirName)))
                for fileName in fileNames:
                    blacklist.write("\n" +
                        os.path.abspath(os.path.join(dirPath, fileName)))
