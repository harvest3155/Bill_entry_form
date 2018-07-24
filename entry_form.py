import tkinter
from tkinter import *

window= Tk()

    
def clear_all():
    e1.delete(0,END)
    e2.delete(0,END)
    Amount_text.set(0)
    e4.delete(0,END)
    e5.delete(0,END)
    Auto_Pay.deselect()
    Ongoing_pay.deselect()
    Name_text.set("Name")

def enter_all():
    bills_ent= e1.get()
    comp_ent= e2.get()
    amount_ent = e3.get()
    due_ent= e4.get()
    end_ent=e5.get()
    auto_chk= Auto_Pay.get()
    ongoing_chk =Ongoing_pay.get()
    name_sel=Name_text.get()
    
    print(bills_ent)
    print(comp_ent)
    print(amount_ent)
    print(due_ent)
    print(auto_chk)
    print(end_ent)
    print(ongoing_chk)
    print(name_sel)

def close_window():
    window.destroy()
    
#labels
L1=Label(window, text="Name")
L1.grid(row=1,column=2)

L1=Label(window, text="Bills")
L1.grid(row=1,column=0)

L1=Label(window, text="Company")
L1.grid(row=2,column=0)

L1=Label(window, text="Amount")
L1.grid(row=3,column=0)

L1=Label(window, text="Due Date")
L1.grid(row=4,column=0)

L1=Label(window, text="End Date")
L1.grid(row=5,column=0)

#Entry Boxes3

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

End_Date_text=StringVar()
e5=Entry(window,text="End Date",textvariable=End_Date_text)
e5.grid(row=5,column=1)

#checkboxes
Auto_Pay=IntVar()
e6=Checkbutton(window,text="Auto-Pay",variable=Auto_Pay,\
               onvalue=1,offvalue=0,\
               height = 1, width =10)
e6.grid(row=4,column=2,sticky = 'w')

Ongoing_pay=IntVar()
e7=Checkbutton(window,text="On-going Payment",variable=Ongoing_pay,\
               onvalue=1,offvalue=0,\
               height = 1, width =18)
e7.grid(row=5,column=2,sticky = 'w')

#dropdown
Name={"Andy","Jackie"}

Name_text=StringVar()
e8=OptionMenu(window, Name_text,*Name)
e8.grid(row=1,column=3)
Name_text.set("Name")
#buttons
b1 =Button(window,text="Clear", width=10,command=clear_all)
b1.grid(row=6,column=3)

b2 =Button(window,text="Enter", width=10, command=enter_all)
b2.grid(row=6,column=4)

b3 =Button(window,text="Exit", width=10,command=close_window)
b3.grid(row=6,column=5)



window.mainloop()
