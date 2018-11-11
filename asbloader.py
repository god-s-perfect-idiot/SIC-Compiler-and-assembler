with open("objectcode") as f, open("memory","w") as op:	
	def readnew():
		s=f.readline()
		s=s.split("^")
		return s
	s=readnew()
	k = len(open("objectcode").readline(  ))
	loc = 0
	for i in range(k):
		if(s[0]=="H"):
			loc=int(s[1],16)
		s=readnew()
		elif(s[0]=="T"):
			p = len(s)
			for i in range(3,p):
				t="0"*6+str(hex(loc))[2:]
				t=t[-6:]
				op.write(t+"\t"+":"+"\t"+s[i]+"\n")
				loc+=len(s[i])
