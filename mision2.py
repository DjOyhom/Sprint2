import re
import sys

f = open(sys.argv[1], "r")
s = []

for i in f:
    a = i.split("\t")
    if len(a[1]) > 5:
        s.append(a[0] + "-" + a[1] + "-" + a[2])

def burbuja(A):
    for i in range(1,len(A)):
        for j in range(0,len(A)-i):
            if(A[j+1] < A[j]):
                aux=A[j]
                A[j]=A[j+1]
                A[j+1]=aux
    print(A)
 
burbuja(s)