#!/usr/bin/env python
import os
import sys

blacklistPath = '.blklst' # SET ME!

for arg in sys.argv[1:]:
    if argv[0] == '-':
        options.append(arg)
    else:
        filesToldToDelete.append(arg)

filesSafeToDelete = filesToldToDelete
with open(blacklistPath, 'r') as blacklist:
    for line in blacklist.readlines():
        if line == '' or line[0] == '#':
            continue
        else:
            for file in filesToldToDelete:
                if os.abspath(file) == line:
                    print('Cannot rm ' + file + ': file or directory is'
                        + ' blacklisted')
                    filesSafeToDelete.remove(file)

if len(filesSafeToDelete) == 0:
    sys.exit()

safeRm = 'rm ' + ' '.join(options) + ' '.join(filesSafeToDelete)
os.system(safeRm)
