from tkinter import *
#def text_to_lbl(event):
#    t=ent.get()
#    ent.delete(0,END)


aken=Tk()
aken.geometry("500x200")
aken.title("Ruutvõrrandi lahendamine")
namelbl=Label(aken,text="Ruutvõrrandi lahendamine", bg="lightblue",fg="green",font="Roboto 20")
ent1=Entry(aken,fg="blue",bg="lightblue",width=3,font="Roboto 20",justify=CENTER)
ent2=Entry(aken,fg="blue",bg="lightblue",width=3,font="Roboto 20",justify=CENTER)
ent3=Entry(aken,fg="blue",bg="lightblue",width=3,font="Roboto 20",justify=CENTER)
numblbl1=Label(aken,text="x**2+",fg="green",font="Roboto 20")
numblbl2=Label(aken,text="x+",fg="green",font="Roboto 20")
numblbl3=Label(aken,text="=0",fg="green",font="Roboto 20")
btn=Button(aken,text="Lahendama",font="Roboto 20",relief=RAISED,bg="green")
lblfin=Label(aken,width=8,height=3,bg="yellow",text="lahendamine")


namelbl.pack()
ent1.pack(side=LEFT)
numblbl1.pack(side=LEFT)
ent2.pack(side=LEFT)
numblbl2.pack(side=LEFT)
ent3.pack(side=LEFT)
numblbl3.pack(side=LEFT)
btn.pack(side=LEFT)
aken.mainloop()
