from tkinter import *
root = Tk()
root.title("sample calculator")
e = Entry(root, width=30, borderwidth=5 )
e.grid(row=0,column=0,padx=10,pady=10,columnspan=3)

def click(num):
    if num=="clear":
        e.delete(0,END)
    else:
        curr=e.get()
        e.delete(0,END)
        e.insert (0,str(curr)+str(num))
def calculaion(op):
    global opr
    opr=op
    curr=e.get()
    e.delete(0,END)
    global first
    first=eval(curr)
def equal():
    sec=eval(e.get())
    e.delete(0,END)
    if opr=="+":
        e.insert(0,first+sec)
    elif opr=="-":
        e.insert(0,first-sec)
    elif opr=="*":
        e.insert(0,first*sec)
    elif opr=="/":
        e.insert(0,first/sec)
mybutton1 = Button(root ,text="1", padx=40, pady=20, command=lambda: click(1))
mybutton2 = Button(root ,text="2", padx=41, pady=20, command=lambda: click(2))
mybutton3 = Button(root ,text="3", padx=41, pady=20, command=lambda: click(3))
mybutton4= Button(root ,text="4", padx=40, pady=20, command=lambda: click(4))
mybutton5= Button(root ,text="5", padx=41, pady=20, command=lambda: click(5))
mybutton6 = Button(root ,text="6", padx=41, pady=20, command=lambda: click(6))
mybutton7 = Button(root ,text="7", padx=40, pady=20, command=lambda: click(7))
mybutton8 = Button(root ,text="8", padx=41, pady=20, command=lambda: click(8))
mybutton9 = Button(root ,text="9", padx=41, pady=20, command=lambda: click(9))
mybutton10 = Button(root ,text="0", padx=40.49999, pady=20, command=lambda: click(0))
mybutton11 = Button(root ,text="clear", padx=80, pady=20, command=lambda: click("clear"))
mybutton12 = Button(root ,text="+", padx=41, pady=20, command= lambda: calculaion("+"))
mybutton13 = Button(root ,text="-", padx=42, pady=20, command= lambda:calculaion("-"))
mybutton14 = Button(root ,text="*", padx=40.7, pady=20, command= lambda:calculaion("*"))
mybutton15 = Button(root ,text="/", padx=41, pady=20, command= lambda:calculaion("/"))
mybutton17 = Button(root ,text="=", padx=40, pady=20, command=equal)
mybutton18=Button(root ,text="." ,padx=41.5,pady=20,command=lambda:click("."))

mybutton1.grid(row=3,column=0)
mybutton2.grid(row=3,column=1)
mybutton3.grid(row=3,column=2)
mybutton4.grid(row=2,column=0)
mybutton5.grid(row=2,column=1)
mybutton6.grid(row=2,column=2)
mybutton7.grid(row=1,column=0)
mybutton8.grid(row=1,column=1)
mybutton9.grid(row=1,column=2)
mybutton10.grid(row=4,column=0)
mybutton13.grid(row=4,column=2)
mybutton18.grid(row=4,column=1)
mybutton14.grid(row=5,column=1)
mybutton11.grid(row=6,column=1,columnspan=2)
mybutton15.grid(row=5,column=0)
mybutton12.grid(row=5,column=2)
mybutton17.grid(row=6,column=0)

root.mainloop()