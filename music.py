import os.path
import os
import sys
import time
ans="/media/g-drive/b2/songs"
ans2="/media/g-drive/b2/isongs"
l=[]
def filelsit(dirname):#list files in direc
	return os.listdir(dirname)
def printtr(dirname,lfile=[]):
		for i in lfile:#recursiely check for each file in direc dirname
			i=dirname+"/"+i
			if(os.path.isdir(i)==True):#if file is direc
					printtr(i,filelsit(i))
			else:
				i=i.lower()
				l.append(i)

printtr(ans,filelsit(ans))
printtr(ans2,filelsit(ans2))
while(1):
   try:
	t=raw_input("enter filename ")
	for i in l:
		if t in i:
			print i
   except KeyboardInterrupt:
	    print "keyboard interupt"
	    os.system('clear')
	    break






