import tkinter as tk
from math import *

app=tk.Tk()
app.title('Calculator')

#functions

def clear():
    numbox.delete(0, tk.END)
    
def write(ent):
    FirstNum=str(numbox.get())
    numbox.delete(0,tk.END)
    if ent=='.':
        numbox.insert(0, FirstNum+str(ent))
    elif ent!='.':
        if FirstNum.count('.')==1:
            numbox.insert(0, float(FirstNum+str(ent)))
        elif FirstNum.count('.')!=1:
            numbox.insert(0, int(FirstNum+str(ent)))
            
def add():
    FirstNum=numbox.get()
    if FirstNum.count('.')==1:
        FirstNum=float(FirstNum)
    else:
        FirstNum=int(numbox.get())
    numbox.delete(0,tk.END)
    global F_num
    global math
    F_num=FirstNum
    math='add'

def sub():
    FirstNum=numbox.get()
    if FirstNum.count('.')==1:
        FirstNum=float(FirstNum)
    else:
        FirstNum=int(numbox.get())
    numbox.delete(0,tk.END)
    global F_num
    global math
    F_num=FirstNum
    math='sub'

def mult():
    FirstNum=numbox.get()
    if FirstNum.count('.')==1:
        FirstNum=float(FirstNum)
    else:
        FirstNum=int(numbox.get())
    numbox.delete(0,tk.END)
    global F_num
    global math
    F_num=FirstNum
    math='mult'

def div():
    FirstNum=numbox.get()
    if FirstNum.count('.')==1:
        FirstNum=float(FirstNum)
    else:
        FirstNum=int(numbox.get())
    numbox.delete(0,tk.END)
    global F_num
    global math
    F_num=FirstNum
    math='div'

def root():
    FirstNum=numbox.get()
    if FirstNum.count('.')==1:
        FirstNum=float(FirstNum)
    else:
        FirstNum=int(numbox.get())
    numbox.delete(0,tk.END)
    arith=sqrt(FirstNum)
    numbox.insert(0, arith)

def power():
    FirstNum=numbox.get()
    if FirstNum.count('.')==1:
        FirstNum=float(FirstNum)
    else:
        FirstNum=int(numbox.get())
    numbox.delete(0,tk.END)
    numbox.insert(0, FirstNum*FirstNum)

def equal():
    SecondNum=numbox.get()
    if SecondNum.count('.')==1:
        SecondNum=float(SecondNum)
    else:
        SecondNum=int(SecondNum)
    numbox.delete(0,tk.END)
    if math=='add':
        numbox.insert(0, F_num+SecondNum)
        
    if math=='sub':
        numbox.insert(0, F_num-SecondNum)
        
    if math=='mult':
        numbox.insert(0, F_num*SecondNum)
        
    if math=='div':
        numbox.insert(0, F_num/SecondNum)

def back():
    length=len(str(numbox.get()))
    numbox.delete(length-1)

#buttons

numbox=tk.Entry(app, width=30, font=('Times New Roman',15,'bold'))
button1=tk.Button(app, text='1', padx=20, pady=15, command=lambda: write(1))
button2=tk.Button(app, text='2', padx=20, pady=15, command=lambda: write(2))
button3=tk.Button(app, text='3', padx=20, pady=15, command=lambda: write(3))
button4=tk.Button(app, text='4', padx=20, pady=15, command=lambda: write(4))
button5=tk.Button(app, text='5', padx=20, pady=15, command=lambda: write(5))
button6=tk.Button(app, text='6', padx=20, pady=15, command=lambda: write(6))
button7=tk.Button(app, text='7', padx=20, pady=15, command=lambda: write(7))
button8=tk.Button(app, text='8', padx=20, pady=15, command=lambda: write(8))
button9=tk.Button(app, text='9', padx=20, pady=15, command=lambda: write(9))
button0=tk.Button(app, text='0', padx=20, pady=15, command=lambda: write(0))
dot=tk.Button(app, text='.', padx=20, pady=15, command=lambda: write('.'))
add=tk.Button(app, text='+', padx=20, pady=15, command=add)
div=tk.Button(app, text='÷', padx=20, pady=15, command=div)
mult=tk.Button(app, text='×', padx=20, pady=15, command=mult)
sub=tk.Button(app, text='-', padx=20, pady=15, command=sub)
clear=tk.Button(app, text='C', padx=20, pady=15, command=clear)
back=tk.Button(app, text='<-', padx=20, pady=15, command=back)
root=tk.Button(app, text='√', padx=20, pady=15, command=root)
power=tk.Button(app, text='^2', padx=20, pady=15, command=power)
equal=tk.Button(app, text='=', padx=20, pady=15, command=equal)

#positions

numbox.grid(row=0, column=0, columnspan=4, padx=20, pady=20)
button1.grid(row=4, column=0, padx=5, pady=5)
button2.grid(row=4, column=1, padx=5, pady=5)
button3.grid(row=4, column=2, padx=5, pady=5)
button4.grid(row=3, column=0, padx=5, pady=5)
button5.grid(row=3, column=1, padx=5, pady=5)
button6.grid(row=3, column=2, padx=5, pady=5)
button7.grid(row=2, column=0, padx=5, pady=5)
button8.grid(row=2, column=1, padx=5, pady=5)
button9.grid(row=2, column=2, padx=5, pady=5)
button0.grid(row=5, column=0, padx=5, pady=5)
dot.grid(row=5, column=1, padx=5, pady=5)
add.grid(row=5, column=3, padx=5, pady=5)
div.grid(row=2, column=3, padx=5, pady=5)
mult.grid(row=3, column=3, padx=5, pady=5)
sub.grid(row=4, column=3, padx=5, pady=5)
clear.grid(row=1, column=2, padx=5, pady=5)
back.grid(row=1, column=3, padx=5, pady=5)
root.grid(row=1, column=1, padx=5, pady=5)
power.grid(row=1, column=0, padx=5, pady=5)
equal.grid(row=5, column=2, padx=5, pady=5)

app.mainloop()