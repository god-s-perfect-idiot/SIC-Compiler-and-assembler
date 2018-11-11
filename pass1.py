temp=[]
symtab = open("symtab","w")
symtab.write("")
symtab.close
symtab = open("symtab","a")
f = open("instruction")
opt = open("optab")
intm=open("intermediate","w")
intm.write("")
intm.close
intm= open("intermediate","a")
locctr=0
optab = opt.read()
optab=optab.split()
count = len(open("instruction").readlines(  ))
a=f.readline()
a=a.split("#")
if "\n" in a[0]:
	a[0]=a[0][:-1]
b=a[0].split("\t")
if(b[1]=="START"):
	intm.write(str(locctr)+"\t"+a[0]+"\n")
for i in range(count-1):
	a=f.readline()
	a=a.split("#")
	if "\n" in a[0]:
		a[0]=a[0][:-1]
	b=a[0].split("\t")
	s=len(b)
	if(b[1] in optab):
		if(b[0]!=""):
			symtab.write(b[0]+"\t"+str(locctr)+"\n")
		if(s==3):
			intm.write(str(locctr)+"\t"+b[1]+"\t"+b[2]+"\n")	
		elif(s==2):
			intm.write(str(locctr)+"\t"+b[1]+"\n")	
		locctr+=3
	elif(b[1]=="WORD"):
		intm.write(str(locctr)+"\t"+b[1]+"\t"+b[2]+"\n")
		symtab.write(b[0]+"\t"+str(locctr)+"\n")
		locctr+=3
	elif(b[1]=="RESW"):
		intm.write(str(locctr)+"\t"+b[1]+"\t"+b[2]+"\n")
		symtab.write(b[0]+"\t"+str(locctr)+"\n")
		locctr+=int(b[2])*3
	elif(b[1]=="BYTE"):
		slen=len(b[3])
		intm.write(str(locctr)+"\t"+b[1]+"\t"+b[2]+"\t"+b[3]+"\n")
		symtab.write(b[0]+"\t"+str(locctr)+"\n")	
		if(b[2]=="X"):
			slen=int(round(slen/2))
		locctr+=slen
	elif(b[1]=="RESB"):
		intm.write(str(locctr)+"\t"+b[1]+"\t"+b[2]+"\n")	
		symtab.write(b[0]+"\t"+str(locctr)+"\n")	
		locctr+=int(b[2])
	elif(b[1]=="END"):
		intm.write(str(locctr)+"\t"+b[1]+"\t"+b[2]+"\n")		
		break;		
