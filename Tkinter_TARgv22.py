from inspect import indentsize
from textwrap import indent
from tkinter import *
from tkinter import ttk
k=0
w=30
def klikker(event):
    global k
    k+=1
    lbl.configure(text=k)
def klikker1(event):
    global k
    if k>0:
        k-=1
    lbl.configure(text=k)  
def entry_to_label(event):
    text=ent.get()
    lbl.configure(text=text)
    ent.delete(0,END) #0,END or 5,10
def valik():
    text=var.get()
    ent.insert(END,text)

i=0
def uus_aken(ind:int): 
    def tab_valik(*ind):
        ind=tabs.index(tabs.select())
        uusaken.title(texts[ind])
    uusaken=Toplevel()
    tabs=ttk.Notebook(uusaken)
    texts=["Esimene","Teine","Kolmas","Neljas"]
    tab=[]
    for i in range(len(texts)):
        tab.append("tab"+str(i)) #tab0,tab1,tab2,tab3
        tab[i]=Frame(tabs)
        tabs.add(tab[i],text=texts[i])
    tabs.grid(row=0,column=0)
    tabs.select(ind)
    ind=tabs.index(tabs.select())
    tabs.bind("<<NotebookTabChanged>>",tab_valik)#
    uusaken.title(texts[ind])
    uusaken.mainloop()

aken=Tk()
aken.title("Minu esimene aken")
aken.geometry("600x300")
m=Menu(aken)
aken.config(menu=m)
m1=Menu(m)
m.add_cascade(label="Kaardid",menu=m1)
m1.add_command(label="1.Kaart",accelerator="Command+A",command=lambda:uus_aken(0))
m1.add_command(label="2.Kaart",accelerator="Command+B",command=lambda:uus_aken(1))
m1.add_command(label="3.Kaart",accelerator="Command+C",command=lambda:uus_aken(2))
m1.add_command(label="4.Kaart",accelerator="Command+D",command=lambda:uus_aken(3))

lbl=Label(aken,
          text="...",
          font="Arial 20")
btn=Button(aken, 
           text="Vajuta siia", 
           font="Arial 20", 
           fg="blue", 
           bg="#148038", 
           width=w, 
           height=5,
           relief=GROOVE)# SUNKEN, RAISED
ent=Entry(aken,
          fg="blue", 
          bg="#148038",
          width=30,
          font="Arial 20",
          justify=CENTER)
var=IntVar() #StringVar()
r1=Radiobutton(aken,
               text="Esimene",
               width=20,
               font="Arial 20",
               variable=var,
               value=1,
               command=valik)
r2=Radiobutton(aken,
               text="Teine",
               width=20,
               font="Arial 20",
               variable=var,
               value=2,
               command=valik)
btn.bind("<Button-1>",klikker) #LKM
btn.bind("<Button-3>",klikker1) #PKM
ent.bind("<Return>",entry_to_label) #Enter
btn.pack()
lbl.pack()
ent.pack()
r1.pack(side=LEFT)
r2.pack(side=LEFT)
aken.mainloop()