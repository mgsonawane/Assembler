section .data
a db "addition is %d",10,0
section  .text
global main
extern printf
main: 
	xor eax,eax
	xor ebx,ebx
	xor edx,edx
	xor ecx,ecx
	mov eax,20
	mov edx,30
	add eax,ebx
	push eax
	push a
	call printf
	add esp,8
