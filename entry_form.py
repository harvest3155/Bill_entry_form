import tkinter
from tkinter import *

window= Tk()
def clear_all():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.deselect()

def enter_all():
    bills_ent= e1.get()
    comp_ent= e2.get()
    amount_ent = e3.get()
    due_ent= e4.get()
    check_ent= Auto_Pay.get()
    
    print(bills_ent)
    print(comp_ent)
    print(amount_ent)
    print(due_ent)
    print(check_ent)

def close_window():
    window.destroy()
    

L1=Label(window, text="Bills")
L1.grid(row=1,column=0)

L1=Label(window, text="Company")
L1.grid(row=2,column=0)

L1=Label(window, text="Amount")
L1.grid(row=3,column=0)

L1=Label(window, text="Due Date")
L1.grid(row=4,column=0)


Bills_text=StringVar()
e1=Entry(window, text="Bills",textvariable=Bills_text)
e1.grid(row=1,column=1)

Company_text=StringVar()
e2=Entry(window,text="Company",textvariable=Company_text)
e2.grid(row=2,column=1)

Amount_text=IntVar()
e3=Entry(window,text="Amount",textvariable=Amount_text)
e3.grid(row=3,column=1)


Due_Date_text=StringVar()
e4=Entry(window,text="Due Date",textvariable=Due_Date_text)
e4.grid(row=4,column=1)


Auto_Pay=IntVar()
e5=Checkbutton(window,text="Auto-Pay",variable=Auto_Pay,\
               onvalue=1,offvalue=0,\
               height = 5, width =20)
e5.grid(row=4,column=2)



b1 =Button(window,text="Clear", width=10,command=clear_all)
b1.grid(row=4,column=3)

b2 =Button(window,text="Enter", width=10, command=enter_all)
b2.grid(row=4,column=4)

b3 =Button(window,text="Exit", width=10,command=close_window)
b3.grid(row=4,column=5)



window.mainloop()

