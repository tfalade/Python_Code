'''
Created on Aug 6, 2015

@author: tfalade
'''

import re
import os

handle1 = open('output.txt', 'w')
emptylist = []
fname = raw_input('Enter file name: ')
try:
    os.path.exists(fname)
    handle = open(fname)
    for line in handle.readlines():
        x = re.findall('^Received:.*\[(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', line)
        if len(x) > 0:
            for item in x:
                emptylist.append(item)
                for lst in emptylist:
                    handle1.writelines(lst)
                    handle1.write('\n')
    handle.close()
    #print(emptylist)
except IOError:
    print('File does not exist')

handle1.write('\n')     
handle1.write('.....................File 2 output...............\n') 
handle1.write('\n')    

bname = raw_input('Enter file name:')
newnote = list()
try:
    os.path.exists(bname)
    fh = open(fname)
    for line in fh:
        if line.startswith('From'): 
            line.rstrip()   
            newline = line.split()
            if len(newline) == 7:
                newnote = newline[1]
                handle1.writelines(newnote)
                handle1.write('\n')
    fh.close()
except IOError:
    print('File does not exist')
    
handle1.close()
    