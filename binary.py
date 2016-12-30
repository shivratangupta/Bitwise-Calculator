a=input("Enter the number:")
def binary(a):
    b=""
    i=0
    if(a==0):
        b=b+'0'

    elif(a==1):
        b=b+'1'

    else:
        while i<100 and a!=1:
            if(a%2==0):
                a=a/2
                b=b+'0'
            else:
                a=a-1
                a=a/2
                b=b+'1'
            i=i+1
        b=b+'1'

    c=""
    j=len(b)-1

    while j>=0:
        c=c+b[j]
        j=j-1
    d=int(c)
    return d
print binary(a)

