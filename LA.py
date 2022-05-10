f=open(“/Users/dhruvupadhyay/Downloads/test.c")
key=[‘int’,'float','string','include','stdio.h','char','break','if','else','switch','return', ‘void','while','struct','for']
iden=[]
sp={"(",")","{","}",";","&","#","$",'"',",","\n"}
spec=["%d","%f","%c","%s"]
num="012345678910"
n=[]
k=[]
o=[]
l=[]
io=['scanf','printf']
op="+-%*=/^><"
dl=[]
F=[]
for lines in f:
words=lines.split(" ")
for i in range(len(words)):
if words[i] in key:
k.append(words[i])
elif words[i] in io:
l.append(words[i])
elif words[i] in op:
o.append(words[i])
elif words[i] in sp:
dl.append(words[i])
elif words[i] in spec:
F.append(words[i])
elif words[i] in num:
n.append(words[i])
else:
iden.append(words[i])

print("Keywords: ")
print(set(k))
print("Input/Output: ")
print(set(l))
print("Operators: ")
print(set(o))
print("Special Symbols: ")
print(set(dl))
print("Identifiers: " )
print(set(iden))
print("Format Specifier:")
print(set(F))
print("Constants:")
print(set(n))

test.c
#include <stdio.h>
int main ( ) {
int a , b , sum ;
scanf ( " %d %d " , & a , & b ) ;
sum = a + b ;
printf ( " %d " , sum ) ;
return 0 ;
}
