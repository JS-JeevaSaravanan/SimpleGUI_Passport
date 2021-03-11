from tkinter import *
from tkinter import messagebox
import time
import sqlite3


class a:

    def __init__(self):

        hu=Tk()
        self.b1=Button(hu,text="user",command=lambda:self.ul(hu))
        self.b1.pack()

        self.b2=Button(hu,text="admin",command=lambda:self.al(hu))
        self.b2.pack()

        hu.mainloop()

    def ul(self,k):
        k.destroy()
        ts=Tk()
        self.l1=Label(ts,text="username")
        self.l1.pack()
        self.e1=Entry(ts)
        self.e1.pack()
        self.l2=Label(ts,text="password")
        self.l2.pack()
        self.e2=Entry(ts)
        self.e2.pack()
        self.b1=Button(ts,text="enter",command=lambda:self.ula(ts))
        self.b1.pack()
        self.b2=Button(ts,text="create account",command=lambda:self.ulb(ts))
        self.b2.pack()
        ts.mainloop()

    def ulb(self,k):
        k.destroy()
        ts=Tk()
        self.l1=Label(ts,text="username")
        self.l1.pack()
        self.e1=Entry(ts)
        self.e1.pack()
        self.l2=Label(ts,text="password")
        self.l2.pack()
        self.e2=Entry(ts)
        self.e2.pack()
        self.l3=Label(ts,text="re-enter password")
        self.l3.pack()
        self.e3=Entry(ts)
        self.e3.pack()
        self.b2=Button(ts,text="create account",command=lambda:self.ulba(ts,o))
        self.b2.pack()
        ts.mainloop()


        
    def ulba(self,k,p):
        print(p)
        k.destroy()

        ts=Tk()
        self.l1=Label(ts,text="thanks for registeration")
        self.l1.pack()
        self.b2=Button(ts,text="back to login",command=lambda:self.ul(ts))
        self.b2.pack()       
        self.b1=Button(ts,text="exit",command=ts.destroy)
        self.b1.pack()
        ts.mainloop()

    

    def al(self,k):
        k.destroy()
        ts=Tk()
        self.l1=Label(ts,text="adminname")
        self.l1.pack()
        self.e1=Entry(ts)
        self.e1.pack()
        self.l2=Label(ts,text="password")
        self.l2.pack()
        self.e2=Entry(ts)
        self.e2.pack()
        self.b1=Button(ts,text="enter",command=lambda:self.ala(ts))
        self.b1.pack()
        
        ts.mainloop()


    def ula(self,k):
        k.destroy()

        if True:
            ts=Tk()
            self.l1=Label(ts,text="detail 1")
            self.l1.pack()
            self.e1=Entry(ts)
            self.e1.pack()
            self.l2=Label(ts,text="detail 2")
            self.l2.pack()
            self.e2=Entry(ts)
            self.e2.pack()
            self.b1=Button(ts,text="history",command=lambda:self.ulah(ts))
            self.b1.pack()
            self.b2=Button(ts,text="enter",command=lambda:self.ula1(ts))
            self.b2.pack()
            ts.mainloop()

        else:
            pirnt("huu")


    
    def ula1(self,k):
        k.destroy()

        ts=Tk()
        self.l1=Label(ts,text="thanks for applying")
        self.l1.pack()
        
        self.b1=Button(ts,text="exit",command=ts.destroy)
        self.b1.pack()
        ts.mainloop()


    def ulah(self,k):
        k.destroy()
        ts=Tk()
        self.b1=Button(ts,text="back",command=lambda:self.ula(ts))
        self.b1.pack()
        self.b2=Button(ts,text="exit",command=ts.destroy)
        self.b2.pack()
        ts.mainloop()



    def ala(self,k):
        k.destroy()

        hu=Tk()
        self.b1=Button(hu,text="reg off update",command=lambda:self.alar(hu))
        self.b1.pack()

        self.b2=Button(hu,text="police update",command=lambda:self.alap(hu))
        self.b2.pack()

        self.b2=Button(hu,text="history",command=lambda:self.alah(hu))
        self.b2.pack()
        
        hu.mainloop()



    def alar(self,k):
        k.destroy()
        ts=Tk()
        # for loop

        self.b3=Button(ts,text="update")#,command=lambda:self.ala(ts))
        self.b3.pack()
        self.b4=Button(ts,text="view")#,command=ts.destroy)
        self.b4.pack()

        
        self.b1=Button(ts,text="back",command=lambda:self.ala(ts))
        self.b1.pack()
        self.b2=Button(ts,text="exit",command=ts.destroy)
        self.b2.pack()
        
        ts.mainloop()


    def alap(self,k):
        k.destroy()
        ts=Tk()
        # for loop

        self.b3=Button(ts,text="update")#,command=lambda:self.ala(ts))
        self.b3.pack()
        self.b4=Button(ts,text="view")#,command=ts.destroy)
        self.b4.pack()

        
        self.b1=Button(ts,text="back",command=lambda:self.ala(ts))
        self.b1.pack()
        self.b2=Button(ts,text="exit",command=ts.destroy)
        self.b2.pack()
        
        ts.mainloop()



    def alah(self,k):
        k.destroy()
        ts=Tk()
        # for loop

        self.b3=Button(ts,text="reason")#,command=lambda:self.ala(ts))
        self.b3.pack()
        self.b4=Button(ts,text="view")#,command=ts.destroy)
        self.b4.pack()

        
        self.b1=Button(ts,text="back",command=lambda:self.ala(ts))
        self.b1.pack()
        self.b2=Button(ts,text="exit",command=ts.destroy)
        self.b2.pack()
        
        ts.mainloop()

'''
messagebox.showinfo("jii")

if True:
    time.sleep(5)

'''
    
p=a()




