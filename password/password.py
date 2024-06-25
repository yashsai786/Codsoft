import random as rd 
import tkinter as tk
from tkinter.constants import SUNKEN
from tkinter import *
from tkinter.ttk import *
# import tkinter as tk
from tkinter import messagebox

#-------Console based Generator-----------
# print("")
#len=int(input("Enter the Length"))

st="abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ@!#$*&"
password=''
#print(password.join(rd.sample(st,len)))
win=tk.Tk()
win.geometry("500x500")
win.resizable(0,0)
win['bg']="#CCEDFF"
win.title("Password Generator")
label4=tk.Label(win,text="",bg="#CCEDFF")
label4.pack()
label5=tk.Label(win,text="",bg="#CCEDFF")
label5.pack()
label1=tk.Label(win,text="Enter the Length",bg="#CCEDFF",font=("Arial", 24, "bold"),fg="#25265E")
label1.pack(padx=2)
label8=tk.Label(win,text="",bg="#CCEDFF")
label8.pack()
label9=tk.Label(win,text="",bg="#CCEDFF")
label9.pack()
entry = tk.Entry(master=win,relief=SUNKEN,bg="green",borderwidth=3,justify=tk.CENTER,fg="white",font=("Arial", 15, "bold"))
entry.pack()
label6=tk.Label(win,text="",bg="#CCEDFF")
label6.pack()
label7=tk.Label(win,text="",bg="#CCEDFF")
label7.pack()
def gen():
    if(entry.get().isdigit()):
        if(int(entry.get())>50):
            messagebox.showinfo("Invalid Length","You should enter the length less than 50")
        elif(int(entry.get())<0):
            messagebox.showinfo("Invalid Length","You should enter the length more than 0")
        else:
            passw=password.join(rd.sample(st,int(entry.get())))
            entry1.delete(0,tk.END)
            entry1.insert(0,passw)
    else:
        messagebox.showinfo("Invalid Input","You should enter the integer")
genima=PhotoImage(file =r"assets/generate_wood.png")
genimag = genima.subsample(4,4)
genimbtn = tk.Button(win,image=genimag,compound = LEFT,command=gen,borderwidth=0).pack()
# genbtn = tk.Button(win,text="GENERATE",justify=tk.CENTER,anchor=tk.CENTER,command=gen, bg="#32a2a8",width=10,height=2,fg="white",font=("Arial", 10, "bold"))#.pack(side = TOP)
# genbtn.pack()
label2=tk.Label(win,text="",bg="#CCEDFF")
label2.pack()
label3=tk.Label(win,text="",bg="#CCEDFF")
label3.pack()
entry1 = tk.Entry(master=win,relief=SUNKEN,bg="BLACK",borderwidth=3,justify=tk.CENTER,fg="#32a2a8",font=("Arial",25, "bold"))
entry1.pack()
#restartbtn.grid(row=2,column=1,padx=1)
win.mainloop()
#print(password)
