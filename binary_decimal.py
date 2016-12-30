a=raw_input("Enter the string:")
b=""
c=0
i=len(a)-1
j=0
while i>=0:
    b=b+a[i]
    i=i-1

while j<len(a):
    c=c+(int(b[j])*(2**j))
    j=j+1

print c
    
