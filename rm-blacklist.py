#!/usr/bin/env python
import os
import sys

blacklistPath = '.blklst' # SET ME!

options = []
filesToldToDelete = []
for arg in sys.argv[1:]:
    if arg[0] == '-':
        options.append(arg)
    else:
        filesToldToDelete.append(arg)

filesSafeToDelete = filesToldToDelete
with open(blacklistPath, 'r') as blacklist:
    for line in blacklist.readlines():
        if line == '' or lstrip(line)[0] == '#':
            continue
        else:
            for file in filesToldToDelete:
                fileAbsPath = os.path.abspath(file)
                if fileAbsPath in line:
                    if os.path.isdir(fileAbsPath):
                        print('Cannot rm directory ' + file + ' because either'
                            + ' it or its contents are blacklisted')
                    else:
                        print('Cannot rm ' + file + ': file is blacklisted')


if len(filesSafeToDelete) == 0:
    sys.exit()

safeRm = 'rm ' + ' '.join(options) + ' ' + ' '.join(filesSafeToDelete)
os.system(safeRm)
