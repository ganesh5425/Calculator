from tkinter import *
import math

def btnClick(number):
    global val
    val=val+str(number)
    data.set(val)

def btnClear():
    global val
    val=""
    data.set("")

def btnEquals():
    global val
    result = str(eval(val))
    data.set(result)
    
def btnSqroot(data):
    result = math.sqrt(val)
    result1 = str(result)
    data.set(result1)


root=Tk()
root.title("My Simple Calculator")
root.geometry("351x381+480+190")
val=""
data=StringVar()
display=Entry(root,textvariable=data,bd=10,justify="right",bg="sky blue",font=("ariel",22))
display.grid(row=0,columnspan=5)

btn7=Button(root,text="7",font=("Ariel",12,"bold"),bd=9.5,height=2,width=6,command=lambda:btnClick(7))
btn7.grid(row=1,column=0)
btn8=Button(root,text="8",font=("Ariel",12,"bold"),bd=9.5,height=2,width=6,command=lambda:btnClick(8))
btn8.grid(row=1,column=1)
btn9=Button(root,text="9",font=("Ariel",12,"bold"),bd=9.5,height=2,width=6,command=lambda:btnClick(9))
btn9.grid(row=1,column=2)
btnc=Button(root,text="C",bg="grey",font=("Ariel",12,"bold"),bd=9.5,height=2,width=6,command=btnClear)
btnc.grid(row=1,column=3)

btn4=Button(root,text="4",font=("Ariel",12,"bold"),bd=9.5,height=2,width=6,command=lambda:btnClick(4))
btn4.grid(row=2,column=0)
btn5=Button(root,text="5",font=("Ariel",12,"bold"),bd=9.5,height=2,width=6,command=lambda:btnClick(5))
btn5.grid(row=2,column=1)
btn6=Button(root,text="6",font=("Ariel",12,"bold"),bd=9.5,height=2,width=6,command=lambda:btnClick(6))
btn6.grid(row=2,column=2)
btn_mul=Button(root,text="*",bg="grey",font=("Ariel",12,"bold"),bd=9.5,height=2,width=6,command=lambda:btnClick('*'))
btn_mul.grid(row=2,column=3)

btn1=Button(root,text="1",font=("Ariel",12,"bold"),bd=9.5,height=2,width=6,command=lambda:btnClick(1))
btn1.grid(row=3,column=0)
btn2=Button(root,text="2",font=("Ariel",12,"bold"),bd=9.5,height=2,width=6,command=lambda:btnClick(2))
btn2.grid(row=3,column=1)
btn3=Button(root,text="3",font=("Ariel",12,"bold"),bd=9.5,height=2,width=6,command=lambda:btnClick(3))
btn3.grid(row=3,column=2)
btn_sub=Button(root,text="-",bg="grey",font=("Ariel",12,"bold"),bd=9.5,height=2,width=6,command=lambda:btnClick('-'))
btn_sub.grid(row=3,column=3)

btnd=Button(root,text=".",bg="grey",font=("Ariel",12,"bold"),bd=9.5,height=2,width=6,command=lambda:btnClick('.'))
btnd.grid(row=4,column=0)
btn0=Button(root,text="0",font=("Ariel",12,"bold"),bd=9.5,height=2,width=6,command=lambda:btnClick(0))
btn0.grid(row=4,column=1)
btn_div=Button(root,text="/",bg="grey",font=("Ariel",12,"bold"),bd=9.5,height=2,width=6,command=lambda:btnClick('/'))
btn_div.grid(row=4,column=2)
btn_add=Button(root,text="+",bg="grey",font=("Ariel",12,"bold"),bd=9.5,height=2,width=6,command=lambda:btnClick('+'))
btn_add.grid(row=4,column=3)

btn_equals=Button(root,text="=",bg="light green",font=("Ariel",12,"bold"),bd=9.5,height=1,width=6,command=btnEquals)
btn_equals.grid(row=5,column=3)
btn_sqr=Button(root,text="x^2",bg="grey",font=("Ariel",12,"bold"),bd=9.5,height=1,width=6,command=lambda:btnClick("**2"))
btn_sqr.grid(row=5,column=0)
btn_sqroot=Button(root,text="Sqrt",bg="grey",font=("Ariel",12,"bold"),bd=9.5,height=1,width=6,command=lambda:btnClick("**0.5"))
btn_sqroot.grid(row=5,column=1)
btn_pow=Button(root,text="x^n",bg="grey",font=("Ariel",12,"bold"),bd=9.5,height=1,width=6,command=lambda:btnClick("**"))
btn_pow.grid(row=5,column=2)
root.mainloop()