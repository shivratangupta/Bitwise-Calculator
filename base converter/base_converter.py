from Tkinter import*
root=Tk()
root.minsize(700,400)
frame=Frame(root)

L1=Label(root, text="Enter The Number", bg="white", border=1, height=2, width=20)
L1.grid(row=0)
L1.place(x=50, y=50) 

E1=Entry(root, bg="white", bd=9)
E1.get()
E1.grid(row=0, column=1)
E1.place(x=200, y=50)

L1=Label(root, text="Number To be Converted in", bg="white", border=1, height=2, width=25)
L1.grid(row=0)
L1.place(x=430, y=50)

var1=IntVar()
R1=Radiobutton(root, text="Decimal", variable=var1, bg="white", value=10)
R1.grid(row=1, column=1)
R1.place(x=70, y=120)
#R1.pack(anchor=W)

R2=Radiobutton(root, text="Binary", variable=var1, bg="white", value=2)
R2.grid(row=2, column=1)
R2.place(x=70, y=150)
#R2.pack(anchor=W)

R3=Radiobutton(root, text="Octal", variable=var1, bg="white", value=8)
R3.grid(row=3, column=1)
R3.place(x=70, y=180)
#R3.pack(anchor=W)

R4=Radiobutton(root, text="Hexadecimal", variable=var1, bg="white", value=16)
R4.grid(row=4, column=1)
R4.place(x=70, y=210)
#R4.pack(anchor=W)

var2=IntVar()
R5=Radiobutton(root, text="Decimal", variable=var2, bg="white", value=10)
R5.grid(row=1, column=2)
R5.place(x=450, y=120)
#R5.pack(anchor=W)

R6=Radiobutton(root, text="Binary", variable=var2, bg="white", value=2)
R6.grid(row=2, column=2)
R6.place(x=450, y=150)
#R6.pack(anchor=W)

R7=Radiobutton(root, text="Octal", variable=var2, bg="white", value=8)
R7.grid(row=3, column=2)
R7.place(x=450, y=180)
#R7.pack(anchor=W)

R8=Radiobutton(root, text="Hexadecimal", variable=var2, bg="white", value=16)
R8.grid(row=4, column=2)
R8.place(x=450, y=210)
#R8.pack(anchor=W)

def result():
    abc=Tk()
    abc.minsize(400,400)
    resultframe=Frame(abc)

    def convert(num, type, con):
        if type == 10:
            if con == 2:
                return bin(num)
            if con == 8:
                return oct(num)
            if con == 16:
                return hex(num)
            if con == 10:
                return num
        if type == 2:
            num = int(str(num),2)
            if con == 2:
                return bin(num)
            if con == 8:
                return oct(num)
            if con == 16:
                return hex(num)
            if con == 10:
                return num
        if type == 8:
            num = int(str(num),8)
            if con == 2:
                return bin(num)
            if con == 8:
                return oct(num)
            if con == 16:
                return hex(num)
            if con == 10:
                return num
        if type == 16:
            num = int(str(num),16)
            if con == 2:
                return bin(num)
            if con == 8:
                return oct(num)
            if con == 16:
                return hex(num)
            if con == 10:
                return num

    x=convert(int(str(E1.get())), var1.get(), var2.get())
    
    L2=Label(abc, text="Binary", bg="white", border=1, height=2, width=15)
    L2.grid(row=1)
    L2.place(x=50, y=50)

    L3=Label(abc, text="Octal", bg="white", border=1, height=2, width=15)
    L3.grid(row=1)
    L3.place(x=50, y=100)

    L4=Label(abc, text="Decimal", bg="white", border=1, height=2, width=15)
    L4.grid(row=1)
    L4.place(x=50, y=150)

    L5=Label(abc, text="Hexa Decimal", bg="white", border=1, height=2, width=15)
    L5.grid(row=1)
    L5.place(x=50, y=200)

    label2=Label(abc, bg="white", border=1, height=2, width=10)

    label3=Label(abc, bg="white", border=1, height=2, width=10)

    label4=Label(abc, bg="white", border=1, height=2, width=10)

    label5=Label(abc, bg="white", border=1, height=2, width=10)

    if(str(var1.get())=='10'):
        label2.config(text=x)

    if(str(var1.get())=='2'):
        label3.config(text=x)

    if(str(var1.get())=='8'):
        label4.config(text=x)

    if(str(var1.get())=='16'):
        label5.config(text=x)
    
    #label2.config(text=w)
    label2.place(x=200, y=50)

    #label3.config(text=w)
    label3.place(x=200, y=100)

    #label4.config(text=w)
    label4.place(x=200, y=150)

    #label5.config(text=w)
    label5.place(x=200, y=200)

    abc.mainloop()

def explanation():
    exp=Tk()
    exp.minsize(700,400)
    expframe=Frame(exp)

    def convert(num, type, con):
        if type == 10:
            if con == 2:
                return bin(num)
            if con == 8:
                return oct(num)
            if con == 16:
                return hex(num)
            if con == 10:
                return num
        if type == 2:
            num = int(str(num),2)
            if con == 2:
                return bin(num)
            if con == 8:
                return oct(num)
            if con == 16:
                return hex(num)
            if con == 10:
                return num
        if type == 8:
            num = int(str(num),8)
            if con == 2:
                return bin(num)
            if con == 8:
                return oct(num)
            if con == 16:
                return hex(num)
            if con == 10:
                return num
        if type == 16:
            num = int(str(num),16)
            if con == 2:
                return bin(num)
            if con == 8:
                return oct(num)
            if con == 16:
                return hex(num)
            if con == 10:
                return num

    x=convert(int(str(E1.get())), var1.get(), var2.get())    

    L6=Label(exp, text="Number", bg="white", border=1, height=2, width=10)
    L6.grid(row=0)
    L6.place(x=50, y=50)

    label6=Label(exp, bg="white", border=1, height=2, width=10)
    label6.config(text=str(E1.get()))
    label6.place(x=200, y=50)

    L7=Label(exp, text="Number system this number in", bg="white", border=1, height=2, width=30)
    L7.grid(row=0)
    L7.place(x=50, y=100)

    label7=Label(exp, bg="white", border=1, height=2, width=10)

    if(str(var1.get())=='10'):
        label7.config(text="Decimal")

    if(str(var1.get())=='2'):
        label7.config(text="Binary")

    if(str(var1.get())=='8'):
        label7.config(text="Octal")

    if(str(var1.get())=='16'):
        label7.config(text="Hexadecimal")

    label7.place(x=300, y=100)

    L8=Label(exp, text="Number system to be converted in", bg="white", border=1, height=2, width=30)
    L8.grid(row=0)
    L8.place(x=50, y=150)

    label8=Label(exp, bg="white", border=1, height=2, width=10)
    
    L9=Label(exp, bg="white", border=1, height=2, width=10)

    if(str(var2.get())=='10'):
        L9.config(text="Decimal")
        label8.config(text="Decimal")

    if(str(var2.get())=='2'):
        L9.config(text="Binary")
        label8.config(text="Binary")

    if(str(var2.get())=='8'):
        L9.config(text="Octal")
        label8.config(text="Octal")

    if(str(var2.get())=='16'):
        L9.config(text="Hexadecimal")
        label8.config(text="Hexadecimal")

    label8.place(x=300, y=150)

    L9.place(x=50, y=200)

    label9=Label(exp, bg="white", border=1, height=2, width=10)
    label9.config(text=x)
    label9.place(x=200, y=200)
    
    exp.mainloop()


B1=Button(root, text ="Result", bg="white", command=result)
B1.grid(row=3, column=1)
B1.place(x=200, y=300)
#B1.pack()

B2=Button(root, text ="Explanation", bg="white", command=explanation)
B2.grid(row=3, column=1)
B2.place(x=300, y=300)
#B2.pack()

#E9=Entry(root, bg="white", bd=9)
#E9.grid(row=0, column=1)
#E9.place(x=150, y=250)

root.mainloop()
