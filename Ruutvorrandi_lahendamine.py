
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt


def prov():
    a=ent1.get()
    if a.isdigit():
        ent1.configure(bg="green")
        e1=True
    else:
        ent1.configure(bg="red")
        e1=False
    b=ent2.get()
    if b.isdigit():
        ent2.configure(bg="green")
        e2=True
    else:
        ent2.configure(bg="red")
        e2=False
    c=ent3.get()
    if c.isdigit():
        ent3.configure(bg="green")
        e3=True
    else:
        ent3.configure(bg="red")
        e3=False
    if e1==True and e2==True and e3==True:
        u=True
        return u,a,b,c


def lahenda(event):
    u,a,b,c=prov()
    if u==True:
        b=float(b);c=float(c);a=float(a)
        K=(b**2)-(4*a*c)
    if K<0:
        lblfin.configure(text="Vale resultaat. Väiksem kei 0")
    else:
        x1=round((-b-(K**(1/2)))/(2*a),2)
        x2=round((-b+(K**(1/2)))/(2*a),2)
        lblfin.configure(text=f"D={K}\nX1={x1}\nX2={x2}")

def graafika():
        a=float(ent1.get())
        b=float(ent2.get())
        c=float(ent3.get())
        x0=(-b)/2*a
        y0=a*x0*x0+b*x0+c
        x=np.arange(x0-15,x0+15,1)#min,max,step
        y=a*x*x+b*x+c
        fig=plt.figure()
        plt.plot(x,y,"r-d")
        plt.title("Ruudvõrrand graafika")
        plt.ylabel("Y")
        plt.xlabel("X")
        plt.grid(True)
        plt.show()


aken=Tk()
aken.geometry("700x250")
aken.title("Ruutvõrrandi lahendamine")
namelbl=Label(aken,text="Ruutvõrrandi lahendamine", bg="lightblue",fg="green",font="Roboto 20")
ent1=Entry(aken,fg="blue",bg="lightblue",width=3,font="Roboto 20",justify=CENTER)
ent2=Entry(aken,fg="blue",bg="lightblue",width=3,font="Roboto 20",justify=CENTER)
ent3=Entry(aken,fg="blue",bg="lightblue",width=3,font="Roboto 20",justify=CENTER)
numblbl1=Label(aken,text="x**2+",fg="green",font="Roboto 20")
numblbl2=Label(aken,text="x+",fg="green",font="Roboto 20")
numblbl3=Label(aken,text="=0",fg="green",font="Roboto 20")
btn=Button(aken,text="Lahendama",font="Roboto 20",relief=RAISED,bg="green")
btngr=Button(aken,text="Graafika",font="Roboto 20",relief=RAISED,bg="green",command=graafika)
lblfin=Label(aken,bg="yellow",text="lahendamine",height=5,width=50)

btn.bind("<Button-1>", lahenda)
#btngr.bind("<Button-1>", graafika)

lblfin.pack(side=BOTTOM)
namelbl.pack()
ent1.pack(side=LEFT)
numblbl1.pack(side=LEFT)
ent2.pack(side=LEFT)
numblbl2.pack(side=LEFT)
ent3.pack(side=LEFT)
numblbl3.pack(side=LEFT)
btn.pack(side=LEFT)
btngr.pack(side=LEFT)
aken.mainloop()
