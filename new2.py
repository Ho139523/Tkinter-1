import tkinter as tk

app=tk.Tk()
app.title('Calculator')

#functions



#Buttons

numbox=tk.Entry(app, width=35, font=('Times New Roman',12,'bold'))
num1=tk.Button(app, text='1', padx=20, pady=15)
num2=tk.Button(app, text='2', padx=20, pady=15)
num3=tk.Button(app, text='3', padx=20, pady=15)
num4=tk.Button(app, text='4', padx=20, pady=15)
num5=tk.Button(app, text='5', padx=20, pady=15)
num6=tk.Button(app, text='6', padx=20, pady=15)
num7=tk.Button(app, text='7', padx=20, pady=15)
num8=tk.Button(app, text='8', padx=20, pady=15)
num9=tk.Button(app, text='9', padx=20, pady=15)
num0=tk.Button(app, text='0', padx=20, pady=15)
add=tk.Button(app, text='+', padx=20, pady=15)
sub=tk.Button(app, text='-', padx=20, pady=15)
mult=tk.Button(app, text='×', padx=20, pady=15)
div=tk.Button(app, text='÷', padx=20, pady=15)
power=tk.Button(app, text='^2', padx=20, pady=15)
root=tk.Button(app, text='√', padx=20, pady=15)
back=tk.Button(app, text='<-', padx=20, pady=15)
clear=tk.Button(app, text='C', padx=20, pady=15)
equal=tk.Button(app, text='=', padx=20, pady=15)
dot=tk.Button(app, text='.', padx=20, pady=15)


#Positions

numbox.grid(row=0, column=0, padx=20, pady=20, columnspan=4)
num1.grid(row=4, column=0, padx=5, pady=5)
num2.grid(row=4, column=1, padx=5, pady=5)
num3.grid(row=4, column=2, padx=5, pady=5)
num4.grid(row=3, column=0, padx=5, pady=5)
num5.grid(row=3, column=1, padx=5, pady=5)
num6.grid(row=3, column=2, padx=5, pady=5)
num7.grid(row=2, column=0, padx=5, pady=5)
num8.grid(row=2, column=1, padx=5, pady=5)
num9.grid(row=2, column=2, padx=5, pady=5)
num0.grid(row=5, column=0, padx=5, pady=5)
add.grid(row=5, column=3, padx=5, pady=5)
sub.grid(row=4, column=3, padx=5, pady=5)
mult.grid(row=3, column=3, padx=5, pady=5)
div.grid(row=2, column=3, padx=5, pady=5)
power.grid(row=1, column=0, padx=5, pady=5)
root.grid(row=1, column=1, padx=5, pady=5)
equal.grid(row=5, column=2, padx=5, pady=5)
dot.grid(row=5, column=1, padx=5, pady=5)
back.grid(row=1, column=3, padx=5, pady=5)
clear.grid(row=1, column=2, padx=5, pady=5)

app.mainloop()