def lst1():
  lst1=["loop","jz","jnz","jmp","call"]
  return lst1
def lstt2():
  lstt2=["dw","db","resb","resw"]
  return lstt2
def lstt3():
  lst3=["dd","resd"]
  return lst3
lst1()
lstt2()
lstt3()

def regdata():
	reg = {"eax" : '000', "ecx" : '001', "edx" : '010', "ebx":"011","ebp" : '100', "esp" : '101',"edi":'110',"esi":'111'}
	return reg
regdata()

def opc():
	op={"xor":'31',"call":'E8',"inc":'40',"dec":'48',"cmp":'83F'}
	return op
opc()

def section():
	sec=[".data",".bss",".text","main:"]
	return sec
section()
def datasec():
	datasec=["dd","db","dw"]
	return datasec
datasec()
def add():
	add={"eax":'c0',"ecx":'c1',"edx":'c2',"ebx":'c3',"esp":'c4',"ebp":'c5',"esi":'c6',"edi":'c7'}
	return add
add()
def add1():
	add1={"eax":'05',"ecx":'0D',"edx":'15',"ebx":'1D',"esp":'25',"ebp":'2D',"esi":'35',"edi":'3D'}
	return add1
add1()
def inter():
	inter={'eax':'000','ecx':'001','edx':'010','ebx':'011','ebp':'100','esi':'101','edi':'111','esp':'101','dword[eax]':'000','dword[ecx]':'001','dword[edx]':'010','dword[ebx]':'011','dword[ebp]':'100','dword[esi]':'101','dword[edi]':'111','dword[esp]':'101'}
	return inter;
inter()

