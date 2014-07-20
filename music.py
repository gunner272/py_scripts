import os.path
import os
import sys
import time

songlist = []

def filelsit(dirname):#list files in direc
	return os.listdir(dirname)


def printtr(dirname, lfile = []):
		for i in lfile:
			i = dirname+"/"+i
			if (os.path.isdir(i) == True):##recursively check for each file in direc dirname
			    printtr(i, filelsit(i))
			else:
			    i = i.lower()
			    songlist.append(i)


for direc in sys.argv[1::]:
	printtr(direc, filelsit(direc))


while(1):
   try:
	t = raw_input("enter songname ")
	for i in songlist:
		if t in i:
			print i
   except KeyboardInterrupt:
	    print "\nBye"
	    time.sleep(1)
	    os.system('clear')
	    break






