import symmtab
lst2=symmtab.lst1()
#print lst2
lst3=symmtab.lstt2()
#print lst3
lst4=symmtab.lstt3()
#print lst4
reg=symmtab.regdata()
#print reg
section=symmtab.section()
datasec=symmtab.datasec()
op=symmtab.opc()
add1=symmtab.add1()
mm=symmtab.inter()
symlst=[]
symm={}
gh=[]
lstf=[]
r=0
def objcode(symlist,gh,lstf):
	ou=open("objcode.txt",'w')
	ou.write("\n----------------Symbol table--------------\n")
	for i in symlist:
		ou.write('\n')
		#print i
		for j in i:
			ou.write(str(j)+'\t\t')

	ou.write("\n----------------Literal table--------------\n")
	for i in gh:
		ou.write('\n')
		for j in i:
			ou.write(str(j)+'\t\t')
	
	ou.write("\n--------------lst file--------------\n")
	for i in lstf:
		ou.write('\n')
		for j in i:
			ou.write(str(j)+'\t\t')





def interm(fp):
 fp2=open("intermediate.asm","rw")
 var=[]
 u=0
 fpp=fp.readlines()
 for i in fpp:
  jp=i.split()
  fp2.write('\n')
  for j in range(0,len(jp)):
	 if jp[j]=='dd' or jp[j]=='dw' or jp[j]=='db' or jp[j]=='resd' or jp[j]=='resw':
	    if jp[0] in gh:
		print gh[1]
           	fp2.write(gh[1]+jp[1]+jp[2])
 	 elif jp[j] in mm:
	    ans=mm[jp[j]]
            fp2.write(ans+' ')
         elif (len(jp[j].split(','))<3):
             el=jp[j].split(',')
             for m in range (0,len(el)):
              if el[m] in mm:
               ans=mm[el[m]]
	       if m==(len(el))-1:
                 fp2.write(ans+' ')
               else:
                 fp2.write(ans+',')
              elif el[m] in var:
               for ii in range(0,len(var)):
                   if(el[m]==var[ii]):
	            p=ii
	#	    print "p::::",p
                    fp2.write("var"+str(p)+' ')
	      else:
	       ans=el[m]
               fp2.write(ans+' ')
         elif jp[j]  in var:
               for ii in range(0,len(var)):
                   if(jp[j]==var[ii]):
                    p=ii
         #           print "p::::",p
                    fp2.write("var"+str(p)+' ')
         else:
          fp2.write(jp[j]+' ')












def sthex(j):
	for pp in range(len(j)):
           k=list(j[pp])
        #   print k
           arr1=[]
           arr2=[]
           l1=[]
           for i in k:
               x=ord(i)
               arr1.append(x)
               q=hex(ord(i))
               arr2.append(q)
           for i in arr2:
                p=i[2:]
                l1.append(p)
           pl="".join(l1)
	   return pl
def inttohex(n):
	dd=int(n)
	ddd=hex(dd)
	return(ddd)
def lstmain(r,lstf,symm,mp):
	address=00000
	fp=open("add.asm",'r')
	fp1=fp.readlines()
	for i in range(r,len(fp1)):
	 if i==r:
			lstf.append(["           ",'main:'])
		        mp.write("\t"+"\t\t"+fp1[i])
#	print lstf
	 else:
		jj=fp1[i].split()
	#	print jj
		for j in range(0,len(jj)):
		 if jj[j]=='mov':
		  if len(jj)>1:
		   jjj=jj[1].split(',')
		   eee=jjj[1].split('dword[')
		  # print eee
		   if jjj[0] and jjj[1] in reg:
			el=reg[jjj[0]]
			el1=reg[jjj[1]]
			el2=str(el1)+str(el)
			el3=inttohex(el2)
			el4='89'+el3[3:]
			address0=intohex(address)
 			lstf.append([str(address0[2:].zfill(8)),el4,fp1[i]])
		        mp.write(str(address0[2:].zfill(8))+"\t"+el4+"\t\t\t"+fp1[i])
			address+=len(el4)/2
		#	print fp1[i]
		   elif jjj[0] and jjj[1].isdigit():
			el=reg[jjj[0]]
		#	print el
			el2=(inttohex(8+int(el,2))).upper()
			#print el2
			el1=inttohex(jjj[1])
			el3='B'+el2[2:]+el1[2:]
			address0=inttohex(address)
			lstf.append([str(address0[2:].zfill(8)),el3,fp1[i]])
		        mp.write(str(address0[2:].zfill(8))+"\t"+el3+"\t\t\t"+fp1[i])
			address+=len(el3)/2
		   elif jjj[0] in reg and jjj[1] in symm:
			el1=symm[jjj[1]]
			el2=(inttohex(8+int(el1,2))).upper()
			el3='B'+el2[2:]+'['+str(el1)+']'
			address0=inttohex(address)
			lstf.append([str(address0[2:].zfill(8)),el3,fp1[i]])
		        mp.write(str(address0[2:].zfill(8))+"\t"+el3+"\t\t\t"+fp1[i])
			address+=len(el3)/2
		   elif len(eee)>1:
			if jjj[0]=='eax' and eee[1][:-1].isdigit():
				el1=inttohex(int(eee[1][:-1])).upper()
				el2='A1'+str(format('{0:02b}'.format(int(el1[2:]))))
				address0=inttohex(address)
				lstf.append([str(address0[2:].zfill(8)),el2,fp1[i]])
		        	mp.write(str(address0[2:].zfill(8))+"\t"+el2+"\t\t\t"+fp1[i])
				address+=len(el3)/2
			if jjj[0] in reg and jjj[0]!='eax' and eee[1][:-1].isdigit():
				el1=inttohex(int(eee[1][:-1])).upper()
				el2=inttohex(int(reg[jjj[0]]))
				el3='8B'+str(format('{0:02b}'.format(int(el1[2:]))))+str(el1)
				lstf.append([str(address0[2:].zfill(8)),el3,fp1[i]])
				address0=inttohex(address)
		        	mp.write(str(address0[2:].zfill(8))+"\t"+el3+"\t\t\t"+fp1[i])
				address+=len(el3)/2
			if jjj[0]=='eax' and eee[1][:-1] in reg:
				el=int(reg[eee[1][:-1]])
				el1=inttohex(el)
				el2='A1'+str(format('{0:02b}'.format(int(el1[2:]))))
				address0=inttohex(address)
				lstf.append([str(address0[2:].zfill(8)),el2,fp1[i]])
		        	mp.write(str(address0[2:].zfill(8))+"\t"+el2+"\t\t\t"+fp1[i])
				address+=len(el3)/2
			if jjj[0] in reg and jjj[0]!='eax' and eee[1][:-1] in reg:
				el1=int(reg[eee[1][:-1]])
				el2=int(reg[jjj[0]])
				el4=str(inttohex(el2))
				el5=str(inttohex(el1))
				el3='8B'+el5[2:]+el4[2:]
				address0=inttohex(address)
				lstf.append([str(address0[2:].zfill(8)),el3,fp1[i]])
		        	mp.write(str(address0[2:].zfill(8))+"\t"+el3+"\t\t\t"+fp1[i])
				address+=len(el3)/2
			if jjj[0] in reg and eee[1][:-1] in symm:
				el1=symm[eee[1][:-1]]
				el2=int(reg[jjj[0]])
				el4=inttohex(el2)
				el3='8B'+str(el1)+str(el2)
				address0=inttohex(address)
				lstf.append([str(address0[2:].zfill(8)),el3,fp1[i]])
		        	mp.write(str(address0[2:].zfill(8))+"\t"+el3+"\t\t\t"+fp1[i])
				address+=len(el3)/2
		 elif jj[j] in op:
		   #   print jj[0]
		      #print symm
		      if jj[0]=='call':
				if jj[1] not in symm:
					#print jj[1]				
					el1=op[jj[0]]
					el2="[00000000]"
					el3=str(el1)+str(el2)
					address0=inttohex(address)
					lstf.append([str(address0[2:].zfill(8)),el3,fp1[i]])
					mp.write(str(address0[2:].zfill(8))+"\t"+el3+"\t\t"+fp1[i])
					address+=len(el3)/2
						
		      if jj[1] in symm:
		    #		print jj[0]
				el1=op[jj[0]]
				el2=[000000000]
				el3=str(el1)+str(el2)
				address0=inttohex(address)
				lstf.append([str(address0[2:].zfill(8)),el3,fp1[i]])
				mp.write(str(address0[2:].zfill(8))+"\t"+el3+"\t\t\t"+fp1[i])
				address+=len(el3)/2
		      jjj=jj[1].split(',')
		 #   print jj[0]
		      if(len(jjj)>1):
			
		#	print jjj[1]
			if jjj[0] and jjj[1] in reg:
					el1=op[jj[0]]
					el2=int((reg[jjj[1]]+reg[jjj[1]]),2)
					el4=inttohex(el2)
				        el3='31'+el4[2:]
					address0=inttohex(address)
					lstf.append([str(address0[2:].zfill(8)),str(el3),fp1[i]])
					mp.write(str(address0[2:].zfill(8))+"\t"+str(el3)+"\t\t\t"+fp1[i])
					#print address
					address+=len(str(el3))/2
			if jj[0]=='cmp':
				if jjj[0] in reg and jjj[1].isdigit():
					el1=op[jj[0]]
					el2=inttohex(int(reg[jjj[0]],2))
					el=inttohex(jjj[1])
					el3=str(el1)+str(format('{0:02b}'.format(int(el1[2:]))))+str(format('{0:02b}'.format(int(el1[2:]))))
					address0=inttohex(address)
					lstf.append([str(address0[2:].zfill(8)),el3,fp1[i]])
					mp.write(str(address0[2:].zfill(8))+"\t"+el3+"\t\t\t"+fp1[i])
					#print address
					address+=len(el3)/2
		      if jj[0]=="inc" or jj[0]=="dec":
				el1=op[jj[0]]
			#	print el1
				el2=int(reg[jj[1]],2)
				el3=str(int(el1)+int(el2))
			#	print el3
				address0=inttohex(address)
				lstf.append([str(address0[2:].zfill(8)),el3,fp1[i]])
				mp.write(str(address0[2:].zfill(8))+"\t"+el3+"\t\t\t"+fp1[i])
				#print address
				address+=len(el3)/2

		if jj[0]=='add':
                  if len(jj)>1:
                   jjj=jj[1].split(',')
                   if jjj[0] and jjj[1] in reg:
                        el=reg[jjj[0]]
                        el1=reg[jjj[1]]
                        el2=int((reg[jjj[1]]+reg[jjj[1]]),2)
                        el3=inttohex(el2)
                        el4='01'+str(el3[3:])
			address0=inttohex(address)
                        lstf.append([str(address0[2:].zfill(8)),el4,fp1[i]])
			mp.write(str(address0[2:].zfill(8))+"\t"+el4+"\t\t\t"+fp1[i])
                        address+=len(el4)/2

                #       print fp1[i]
                   elif jjj[0] in reg and jjj[1].isdigit():
                        el=int(add1[jjj[0]])
                        #print el
			#print symm
                        el2=inttohex(el)
                        #print el2
                        el1=inttohex(jjj[1])
                        el3='83'+str(el2[2:])+str(el1[2:])
			address0=inttohex(address)
                        lstf.append([str(address0[2:].zfill(8)),el3,fp1[i]])
			mp.write(str(address0[2:].zfill(8))+"\t"+el3+"\t\t\t"+fp1[i])
                        address+=len(el3)/2
                   elif jjj[0] in reg and jjj[1] in symm:
                        el1=symm[jjj[1]]
                        el2=(inttohex(8+int(el,2))).upper()
                        el3='B'+el2[2:]+'['+str(el1)+']'
			address0=inttohex(address)
                        lstf.append([str(address0[2:].zfill(8)),el3,fp1[i]])
			mp.write(str(address0[2:].zfill(8))+"\t"+el3+"\t\t\t"+fp1[i])
                        address+=len(el3)/2

	     	  elif len(eee)>1:
                        if jjj[0] in reg and eee[1][:-1].isdigit():
                                el1=inttohex(eee[1][:-1]).upper()
                                el2=int(reg[jjj[0]])
				el4=inttohex(el2)
                                el3='03'+str(el1[2:])+el4[2:]
				address0=inttohex(address)
                                lstf.append([str(address0[2:].zfill(8)),el3,fp1[i]])
				mp.write(str(address0[2:].zfill(8))+"\t"+el3+"\t\t\t"+fp1[i])
                                address+=len(el3)/2
                        if jjj[0] in reg and eee[1][:-1] in reg:
                                el1=reg[eee[1][:-1]]
                                el2=int(reg[jjj[0]])
				el4=inttohex(el2)
                                el3='03'+str(el1[2:])+el4[2:]
				address0=inttohex(address)
                                lstf.append([str(address0[2:].zfill(8)),el3,fp1[i]])
				mp.write(str(address0[2:].zfill(8))+"\t"+el3+"\t\t\t"+fp1[i])
                                address+=len(el3)/2
                        if jjj[0] in reg and eee[1][:-1] in symm:
                                el1=symm[eee[1][:-1]]
                                el2=int(reg[jjj[0]])
				el4=inttohex(el2)
                                el3='03'+str(el1[2:])+el4[2:]
				address0=inttohex(address)
                                lstf.append([str(address0[2:].zfill(8)),el3,fp1[i]])
				mp.write(str(address0[2:].zfill(8))+"\t"+el3+"\t\t\t"+fp1[i])
                                address+=len(el3)/2
                                address+=len(el3)/2
			
	return lstf
#	for ii in lstf:
#		print ii			
#	print symm
		
	

def secwise(r,mp):
	address=00000
	fp=open("add.asm",'r')
	fp1=fp.readlines()
#	print gh
	oo=0
	for i in range(0,r):
	 jj=fp1[i].split()
		
	 for ii in datasec:
		if jj[1] in ii:
		#	print gh[oo][2]
			oo+=1
			address0=inttohex(address)
			lstf.append([str(address0[2:].zfill(8)),gh[oo][2],fp1[i]])
		        mp.write(str(address0[2:].zfill(8))+"\t"+str(gh[oo][2])+"\t\t\t"+fp1[i])
			ell1=jj[0]
			ell2=address
			symm[ell1]=ell2	
			addres=len(gh[oo][2])/2
			address+=addres
	 if jj[1] not in datasec:
 		# print fp1[i]
		 mp.write("\t"+"\t\t"+fp1[i])
		 lstf.append(["  ","  ",fp1[i]])
		 
	return symm
	return lstf
#	for ll in lstf:
#		print ll

def lst():
	fp=open("add.asm",'r')
	mp=open("mylst.lst",'w')
	fp1=fp.readlines()
	for i in range(len(fp1)):
	 jj=fp1[i].split()
	 if 'main:' in fp1[i]:
	   r=i
	 #  print r
	   secwise(r,mp)	
	 if jj[0]=='extern':
	  ell1=jj[1]
	  ell2=000
	  symm[ell1]=ell2
		
  	 if 'main:' in fp1[i]:
    			 lstmain(i,lstf,symm,mp)
#	  for j in range(len(jj)):

def mainpart(u,gh,j,llee):
	tt=0
	for i in range(u,len(j)):
	 jj=j[i].split()
#	 print jj
	 if len(jj)>1:
		 if len(jj[1])>1:
			el=jj[1].split(',')
			el1=jj[1].split('dword[')
			el3=jj[1].split("'")
		#	print el1
			if len(el)>1:
				if (el[1]).isdigit():
					llee+=1
					tt+=1
					kk=int(el[1])
					kkk=hex(kk)
					gh.append([i,"lit#"+str(llee),kkk[2:],'\t\t',el[1]])  #str(llee) is used to concat string to str(integer)
			if len(el1)>1:
				el2=(el1[1])[:-1]
				if (el2.isdigit()):
					llee+=1
					tt+=1
					kk=int(el2)
					kkk=hex(kk)
					gh.append([i,"lit#"+str(llee),kkk[2:],'\t\t   ',el2])
				if len(el3)>1:
				#	print el3[1]
					kkk=sthex(el3[1])
					llee+=1
					gh.append([i,"lit#"+str(llee),kkk,'\t\t   ',el3[1]])
					
			if len(el3)>1:
					#print el3[1]
					kkk=sthex(el3[1])
					llee+=1
					gh.append([i,"lit#"+str(llee),kkk,'\t\t   ',el3[1]])
	return(gh)
#	for i in gh:
#		print i
def litt(fq):
  st1=fq.readlines()
#  print "check",st1
  sq=[]
  pp=[]
  llee=0           # literal no. in main part
  for line in range(0,len(st1)):
   		j=st1[line].split()

                if (len(j)>1):
		   if j[1] in lst3:
			llee+=1
                        p1=j[2:]
                        dr=" ".join(p1)
                        k=list(dr)
                        arr1=[]
                        arr2=[]
                        l1=[]
                        for i in k:
                                x=ord(i)
                                arr1.append(x)
                                q=hex(ord(i))
                                arr2.append(q)
                        for i in arr2:
                                p=i[2:]
                                l1.append(p)
                        pl="".join(l1)
                        gh.append([line,"lit#"+str(llee),pl,j[0]])
		   if j[1] in lst4:
			llee+=1
	                ll=j[2].split(',')
        	        t2=[]
                	p1=j[2:]
	                dr=" ".join(p1)
        	        dq=dr.split(',')
                	arr2=[]
	                l1=[]
        	        for i in dq:
                	   p=int(i)
	                   q=hex(p)
        	           arr2.append(q)
                	for i in arr2:
	                   p=i[2:]
        	           l1.append(p)
	               	   pl="".join(l1)
                	gh.append([line,"lit#"+str(llee),pl,','.join(ll)])

  		if(j[0]=='main:'):
    			 mainpart(line,gh,st1,llee)
   		else:
			continue
  return gh




def symtab(fp):   #fp os filename and line no.

 sp=fp.readlines()
 h=1
 lno=0
 for i in range(len(sp)):
	j=sp[i].split()
        if len(j)>1:
           if lst4[0]==j[1]:
		n=j[0]
		com=j[2].split(',')
	        var1=0	
                var1=len(com)
                if (h==1):
		 n=j[0]
		 symlst.append([n,'4',str(var1),'s','D',0,','.join(com),i])
	  	 man=var1*4
                 h=h+1
                else:
	
                  symlst.append([n,'4',str(var1),'s','D',man,','.join(com),i])
                  man=man+(var1*4)
           elif(lst4[0]==j[0]):
                 n=" "
                 com=j[1].split(',')

                 var1=len(com)
                 if h==1:
                  n=j[0]
                  symlst.append([n,'4',str(var1),'s','D',0,','.join(com),i])
                  man=var1*4
                  h=h+1
      
                 else:

                   symlst.append([n,'4',str(var1),'s','D',man,','.join(com),i])
                   man1=var1*4
		   man=man+man1

           elif(lst3[1]==j[1]):
                  n=j[0]
		 # print n
                  com=' '.join(j)[6:]
                  var1=len(com)
                  n=j[0]
                  man=var1*1
                  symlst.append([n,'1',str(var1),'s','D',man,com,i])
                  man1=var1*1
		  man=man+man1
           elif(lst4[1]==j[1]):
		  n=j[0]
		  com=' '.join(j)[7:]
                  var1=len(com)
		  symlst.append([n,4,str(var1),'s','D',man,com,i])
                  man1=var1*4
		  man=man+man1
           elif(lst3[2]==j[1]):
                  n=j[0]
                  com=' '.join(j)[7:]
                  var1=len(com)
                  symlst.append([n,'1',str(var1),'s','D',man,com,i])
                  man1=var1*2
		  man=man+man1
	   elif(lst3[3]==j[1]):
                  n=j[0]
                  com=' '.join(j)[7:]
		  var1=len(com)
                  symlst.append([n,'1',str(var1),'s','D',man,com,i])
                  man1=var1*1
		  man=man+man1
	   elif j[0]=='global':
		n=j[1]
		symlst.append([n,"    - ","  -  "," -  ","-","- ","-\t\t",i])
      	   elif j[0]=='extern':
		n=j[1]
		symlst.append([n,"- ","- ","- ","- ","- ","-\t\t",i])
		
           elif(j[0] in lst2):
		  n=j[1]
		  symlst.append([n,'-','-','L','D','0','-\t\t',i])
 return symlst
# print lst

def main():
	fp=open("add.asm",'r')
	symtab(fp)#To create symbol table
	fq=open("add.asm",'r')
	
	litt(fq)
	fp=open("add.asm",'r')
	interm(fp)
	lst()
        objcode(symlst,gh,lstf)
#        create_litt()
 #   	create_LST()#TO create lst part
if __name__ == "__main__":
    main()

