import sys
import os
if __name__=="__main__":
	fp=open(sys.argv[1],"r")
	st=fp.readlines()
	l=len(st)
	m=[]
	fn=open("mnt.txt","w")
	fd=open("mdt.txt","w")
	fn.write("Macro name\tno of parameter\tstart\tend\n")
	fd.write("Macro defination\tstart\tend\n")
	for i in range(0,l):
		if '%macro' in st[i]: 
			f=st[i].split()
			n=f[2].split()
			j=i
		if '%endmacro' in st[i]:
			k=i
			fn.write(("%s\t%d\t%d\t%d"%(f[1],len(n),j,i))+os.linesep)
			p=st[1]
			pp=p.split()
			fd.write(("%s\t%d\t%d"%(pp,j,i))+os.linesep)
			for l in range(j+1,k):
				m.append(st[k])
				fd.write("%s"%(st[l])+os.linesep)
