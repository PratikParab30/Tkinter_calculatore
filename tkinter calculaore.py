from tkinter import *

tk=Tk()

def calcu():
    vms=vm.get()
    if vms=="1":
        val=int(v1.get())+int(v2.get())
        lb2.configure(text=f"The answer is: {val}")
    elif vms=="2":
        val=int(v1.get())-int(v2.get())
        lb2.configure(text=f"The answer is: {val}")
    elif vms=="3":
        val=int(v1.get())*int(v2.get())
        lb2.configure(text=f"The answer is: {val}")
    elif vms=="4":
        val=int(v1.get())/int(v2.get())
        lb2.config(text=f"The answer is: {val}")
    
lbv1=Label(tk,text="plese set values of 1st number")
lbv1.grid(row=0,column=10)    
v1=Spinbox(tk,from_=1,to=10)
v1.grid(row=0,column=20)

lb1=Label(tk,text="1.for addition ,2.for substraction,3.for mutiplication,4.for division")
lb1.grid(row=1,column=10)

vm=Spinbox(tk,from_=1,to=4)
vm.grid(row=1,column=20)

lbv2=Label(tk,text="plese set values of 2nd number")
lbv2.grid(row=2,column=10)
v2=Spinbox(tk,from_=1,to=10)
v2.grid(row=2,column=20)

btn=Button(tk,text="Press" ,command=calcu)
btn.grid(row=3,column=0)

lb2=Label(tk,text="plese set values and press button")
lb2.grid(row=4,column=10)

tk.mainloop()