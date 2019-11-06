
section .data 
a "addition is %d",10,0 
section .text 
global main 
extern printf 
main: 
xor 000,000 
xor 011,011 
xor 010,010 
xor 001,001 
mov 000,20 
mov 010,30 
add 000,011 
push 000 
push a 
call printf 
add 101,8 