import random as rd
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter import messagebox
from tkinter.constants import SUNKEN

#usint=0
#a=0
compscore = 0
userscore = 0
result="PENDING"
def restart():
    global userscore
    global compscore
    replay()
    messagebox.showinfo("Restart","Initializing Scores to Zero(0) Good Luck!!")
    userscore=0
    compscore=0
    y=str(userscore)
    entry.delete(0,tk.END)
    entry.insert(0,y)
    x=str(compscore)
    entry1.delete(0,tk.END)
    entry1.insert(0,x)

def getval(usint):
    global result
    global userscore
    global compscore
    a=rd.randint(1,3)
    if(a==1):
        combtn = tk.Button(compframe,image=stnimag,compound = LEFT,bg="#32a2a8",borderwidth=0)#.pack(side = TOP)
        combtn.grid(row=1,column=2)
    elif(a==2):
        combtn = tk.Button(compframe,image=papimag,compound = LEFT,bg="#32a2a8",borderwidth=0)#.pack(side = TOP)
        combtn.grid(row=1,column=2)
    else:
        combtn = tk.Button(compframe,image=sciimag,compound = LEFT,bg="#32a2a8",borderwidth=0)#.pack(side = TOP)
        combtn.grid(row=1,column=2)

    if(usint==1 and a==3):
        #messagebox.showinfo("Result","You Won So, +1")
        result="You Won"
        userscore +=1
    elif(usint==2 and a==1):
        #messagebox.showinfo("Result","You Won So, +1")
        result="You Won"
        userscore +=1    
    elif(usint==3 and a==2):
        #messagebox.showinfo("Result","You Won So, +1")
        result="You Won"
        userscore +=1
    elif(a==1 and usint==3):
        #messagebox.showinfo("Result","Oops! Computer Won")
        result="Computer Won"
        compscore +=1
    elif(a==2 and usint==1):
        #messagebox.showinfo("Result","Oops! Computer Won")
        result="Computer Won"
        compscore +=1
    elif(a==3 and usint==2):
        #messagebox.showinfo("Result","Oops! Computer Won")
        result="Computer Won"
        compscore +=1
    else:
        messagebox.showinfo("Result","Draw")
        result="Draw"
    #lblResult.config(textvariable=result)
    y=str(userscore)
    entry.delete(0,tk.END)
    entry.insert(0,y)
    x=str(compscore)
    entry1.delete(0,tk.END)
    entry1.insert(0,x)

def stn():
    papbtn["state"] = tk.DISABLED
    scibtn["state"] = tk.DISABLED
    getval(1)
def pap():
    stnbtn["state"] = tk.DISABLED
    scibtn["state"] = tk.DISABLED
    getval(2)
def sci():
    papbtn["state"] = tk.DISABLED
    stnbtn["state"] = tk.DISABLED
    getval(3)
def replay():
    papbtn["state"] = tk.NORMAL
    scibtn["state"] = tk.NORMAL
    stnbtn["state"] = tk.NORMAL
win=Tk()
#win.geometry("500x500")
win.title("Stone,Paper,Scissor Game")
win['bg'] = "#32a2a8"
frame = Frame(win)
#frame.config(background="#32a2a8")
#frame.pack()
#frame['background'] = "#32a2a8"
win.resizable(0,0)
label = tk.Label(frame, 
                 text="Welcome to the Stone,Paper & Scissor Game", 
                 anchor=tk.CENTER,       
                 bg="lightblue",
                 width=70,
                 bd=3,                  
                 font=("Arial", 16, "bold"), 
                 cursor="hand2",   
                 fg="red",                             
                 justify=tk.CENTER,    
                 relief=tk.RAISED,          
                )
label.pack()
frame.pack()
win1=tk.Frame(win, bg="#32a2a8")
compframe=tk.Frame(win1,bg="#32a2a8")
compframe.grid(row=2,column=3)

#label.grid(row=0,column=4)
label1 = tk.Label(win1, 
                 text="Choose any one", 
                 anchor=tk.CENTER,       
                 bg="lightblue",                                  
                 bd=3,
                 height=3,
                width=19,
                 font=("Arial", 16, "bold"), 
                 cursor="hand2",   
                 fg="red",                    
                 justify=tk.CENTER,    
                 relief=tk.RAISED,              
                )
label1.grid(row=1,column=0)
complabel = tk.Label(compframe, 
                 text="Computer has Chosen :", 
                 anchor=tk.CENTER,       
                 bg="lightblue",                                
                 bd=3,
                 height=3,
                 font=("Arial", 16, "bold"), 
                 cursor="hand2",   
                 fg="red",                    
                 justify=tk.CENTER,    
                 relief=tk.RAISED,         
                )
complabel.grid(row=1,column=1)
stnima=PhotoImage(file =r"assets/stone.png")
stnimag = stnima.subsample(3,3)
papima = PhotoImage(file = r"assets/paper.png")
papimag = papima.subsample(3,3)
sciima = PhotoImage(file = r"assets/scissor.png")
sciimag = sciima.subsample(3,3)
stnbtn = tk.Button(win1,image=stnimag,compound = LEFT,command=stn,bg="#32a2a8",borderwidth=0)#.pack(side = TOP)
stnbtn.grid(row=1,column=1,padx=1)
papbtn = tk.Button(win1,image=papimag,compound = LEFT,command=pap,bg="#32a2a8",borderwidth=0)#.pack(side = TOP)
papbtn.grid(row=2,column=1)
scibtn = tk.Button(win1,image=sciimag,compound = LEFT,borderwidth=0,command=sci,bg="#32a2a8")#.pack(side = TOP)
scibtn.grid(row=3,column=1)
#borima=PhotoImage(file =r"border.png")
#borimag = borima.subsample(3,3)
#borbtn = tk.Button(win1,image=borimag,compound = LEFT,command=stn,bg="#32a2a8",borderwidth=0,width=20)#.pack(side = TOP)
#borbtn.grid(row=3,column=0,padx=1)
win1.pack()
resultframe=tk.Frame(win1,bg="#32a2a8")
label1 = tk.Label(resultframe, 
                 text="Your Score :",        
                 bg="lightblue",width=15,
                 height=2,                            
                 bd=3,                  
                 font=("Arial", 10, "bold"), 
                 cursor="hand2",   
                 fg="red",                        
                 relief=tk.RAISED             
                )
label1.grid(row=0,column=0)
label2 = tk.Label(resultframe, 
                 text="Computer Score :",       
                 bg="lightblue",
                  width=15,
                 height=2,                            
                 bd=3,                  
                 font=("Arial", 10, "bold"), 
                 cursor="hand2",   
                 fg="red",                        
                 relief=tk.RAISED       
                )
label2.grid(row=3,column=0)
label3=tk.Label(resultframe,bg="#32a2a8")
label3.grid(row=1)
label3=tk.Label(resultframe,bg="#32a2a8")
label3.grid(row=2)
label3=tk.Label(resultframe,bg="#32a2a8")
label3.grid(row=0,column=1)
label3=tk.Label(resultframe,bg="#32a2a8")
label3.grid(row=3,column=1)

entry=tk.Entry(master=resultframe,relief=SUNKEN,bg="BLACK",borderwidth=3,width=2,justify=tk.RIGHT,fg="#32a2a8",font=("Arial", 15, "bold"))
entry.grid(row=0,column=2,columnspan=4,ipady=4,pady=4)
#entry.config(state='readonly')
entry1=tk.Entry(master=resultframe,relief=SUNKEN,bg="BLACK",borderwidth=3,width=2,justify=tk.RIGHT,fg="#32a2a8",font=("Arial", 15, "bold"))
entry1.grid(row=3,column=2,columnspan=4,ipady=4,pady=4)
#entry1.config(state='readonly')
resultframe.grid(row=1,column=3,columnspan=2)
endframe=tk.Frame(win1, bg="#32a2a8")
replaybtn = tk.Button(endframe,text="Replay",compound = CENTER,justify=tk.CENTER,anchor=tk.CENTER,command=replay, bg="#CCEDFF",width=20,height=2,fg="#32a2a8",font=("Arial", 20, "bold"))#.pack(side = TOP)
replaybtn.grid(row=1,column=1,padx=1)
restartbtn = tk.Button(endframe,text="Restart",compound = CENTER,justify=tk.CENTER,anchor=tk.CENTER,command=restart, bg="#32a2a8",width=20,height=2,fg="white",font=("Arial", 20, "bold"))#.pack(side = TOP)
restartbtn.grid(row=2,column=1,padx=1)

#lblResult = tk.Label(master=endframe,textvariable="result")  
#lblResult.grid(row=2, column=2)
    

endframe.grid(row=3,column=3,columnspan=2)
win.mainloop()
