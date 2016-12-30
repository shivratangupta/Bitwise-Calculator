from Tkinter import*
root=Tk()
root.minsize(700,400)
frame=Frame(root)
bottomframe=Frame(root)

L1=Label(root, text="Number1", bg="white", border=1, height=2, width=10)
L1.grid(row=0)
L1.place(x=50, y=50)

L2=Label(root, text="Number2", bg="white", border=1, height=2, width=10)
L2.grid(row=0)
L2.place(x=400, y=50)

E1=Entry(root, bg="white", bd=9)
E1.grid(row=0, column=1)
E1.place(x=150, y=50)
m=str(E1.get())

E2=Entry(root, bg="white", bd=9)
E2.grid(row=0, column=1)
E2.place(x=500, y=50)
n=str(E1.get())

var=IntVar()
R1=Radiobutton(root, text="AND", bg="white", variable=var, value=1)
R1.grid(row=1, column=1)
R1.place(x=50, y=120)

R2=Radiobutton(root, text="NOT", bg="white", variable=var, value=2)
R2.grid(row=2, column=1)
R2.place(x=50, y=150)

R3=Radiobutton(root, text="OR", bg="white", variable=var, value=3)
R3.grid(row=1, column=1)
R3.place(x=350, y=120)

R4=Radiobutton(root, text="XOR", bg="white", variable=var, value=4)
R4.grid(row=2, column=1)
R4.place(x=350, y=150)

def explanation():
    exp=Tk()
    exp.minsize(700,400)
    expframe=Frame(exp)

    def binary(e):
        a=int(e)
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

    L3=Label(exp, text="Number1", bg="white", border=1, height=2, width=10)
    L3.grid(row=0)
    L3.place(x=50, y=50) 

    L4=Label(exp, text="Number2", bg="white", border=1, height=2, width=10)
    L4.grid(row=1)
    L4.place(x=50, y=100)

    label2=Label(exp, bg="white", border=1, height=2, width=10)
    label2.config(text=str(E1.get()))
    label2.place(x=150, y=50)

    label3=Label(exp, bg="white", border=1, height=2, width=10)
    label3.config(text=str(E2.get()))
    label3.place(x=150,y=100)

    L5=Label(exp, text="Binary:", bg="white", border=1, height=2, width=10)
    L5.grid(row=0)
    L5.place(x=400, y=50) 

    L6=Label(exp, text="Binary:", bg="white", border=1, height=2, width=10)
    L6.grid(row=1)
    L6.place(x=400, y=100)

    y=binary(str(E1.get()))
    label4=Label(exp, bg="white", border=1, height=2, width=10)
    label4.config(text=y)
    label4.place(x=500, y=50)

    z=binary(str(E2.get()))
    label5=Label(exp, bg="white", border=1, height=2, width=10)
    label5.config(text=z)
    label5.place(x=500, y=100)

    L7=Label(exp, bg="white", border=1, height=2, width=10)
    if(str(var.get())=='1'):
        L7.config(text="AND")

    if(str(var.get())=='2'):
        L7.config(text="NOT")

    if(str(var.get())=='3'):
        L7.config(text="OR")

    if(str(var.get())=='4'):
        L7.config(text="XOR")

    L7.place(x=400, y=200)

    def bitwise(p,q):
        if(str(var.get())=='1'):
            x=p&q

        if(str(var.get())=='2'):
            x=~p

        if(str(var.get())=='3'):
            x=p|q

        if(str(var.get())=='4'):
            x=p^q
        return x

    w=bitwise(int(str(E1.get())),int(str(E2.get())))
    l=binary(w)
    label6=Label(exp, bg="white", border=1, height=2, width=15)
    label6.config(text=l)
    label6.place(x=500, y=200)

    L8=Label(exp, text="Decimal Result", bg="white", border=1, height=2, width=15)
    L8.grid(row=1)
    L8.place(x=200, y=300)

    label7=Label(exp, bg="white", border=1, height=2, width=10)
    label7.config(text=w)
    label7.place(x=350, y=300)
    
    exp.mainloop()

label=Label(root, bg="white", border=1, height=2, width=10)
label.place(x=150, y=250)

B2=Button(root, text ="Explanation", bg="skyblue", command=explanation)
B2.grid(row=3, column=1)
B2.place(x=400, y=200)

def bitwise(p,q):
    if(str(var.get())=='1'):
        x=p&q

    if(str(var.get())=='2'):
        x=~p

    if(str(var.get())=='3'):
        x=p|q

    if(str(var.get())=='4'):
        x=p^q
    return x

def result():
    w=bitwise(int(str(E1.get())),int(str(E2.get())))
    label.config(text=w)

B1=Button(root, text ="Result", bg="skyblue", command=result)
B1.grid(row=3, column=1)
B1.place(x=200, y=200)

L9=Label(root, text="Result is:", bg="white", border=1, height=2, width=10)
L9.grid(row=0)
L9.place(x=50, y=250)

root.mainloop()
