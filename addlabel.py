# -*- coding: utf-8 -*-
"""
Created on Thu Nov 02 22:19:49 2017

@author: Pavilion
"""

from Tkinter import *
import random
import scipy.io as sio

class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)            
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom

root = Tk()
app=FullScreenApp(root)
label = Label(root, text="Directions", font=("Courier",20))
label.pack(pady=10, padx=10)

ii = 0
tim = 1
a  = sio.loadmat('../times.mat')['a'][0]
#a = a[285:]

tt1 = "stop everything and"
tt2 = "Start normal breathing"
tt3 = "Next up: Breathhold in 9 sec"
tt4 = '\n'+'\n'+'\n'+'\n'+str(len(a)-ii-1)+' events remain'
label2 = Label(root, text=tt1, font=("Courier", 30))
label2.pack()
label3 = Label(root, text=tt2, fg="black", bg="yellow", font=("Courier 34 bold"))
label3.pack()
label4 = Label(root, text=tt3, font=("Courier", 30))
label4.pack()
label5 = Label(root, text=tt4, font=("Courier", 34))
label5.pack()

def f(x):
    return {
        0 : 'stop normal breathing',
        1 : 'stop breath hold',
        2 : 'stop hyperventilation'
    }[x]
    
def g(x):
    return {
        0 : 'start breath hold',
        1 : 'start hyperventilation',
        2 : 'start normal breathing',
    }[x]
    
def h(x):
    return {
        0 : 'Hyperventilation',
        1 : 'Normal Breathing',
        2 : 'Breathhold',
    }[x]    

def add_label():
    global ii
    global label2
    global label3
    global label4
    global label5
    global tt1
    global tt2
    global tt3
    global tt4
    global tim
    
    label2.pack_forget()
    label3.pack_forget()
    label4.pack_forget()
    label5.pack_forget()
    label2 = Label(root, text=tt1, font=("Courier", 30))
    label2.pack()
    label3 = Label(root, text=tt2, fg="black", bg="yellow", font=("Courier 34 bold"))
    label3.pack()
    label4 = Label(root, text=tt3, font=("Courier", 30))
    label4.pack()
    label5 = Label(root, text=tt4, font=("Courier", 34))
    label5.pack()
     
    if ii == len(a):
        ii = len(a)
        tt1 = 'done\n'
        tt2 = 'done\n'
        tt3 = 'done\n'
    elif tim != 1:
        tim -= 1
        tt1 = f(mod(ii-1,3))
        tt2 = g(mod(ii-1,3))
        tt3 = "Next Up: "+h(mod(ii-1,3))
        tt4 = '\n'+str(tim)+' sec remaining'+'\n'+'\n'+'\n'+str(len(a)-ii-1)+' events remain'        
        root.after(1000, add_label)
    else:
        ii+=1
        tim = a[ii]
        tt1 = f(mod(ii-1,3))
        tt2 = g(mod(ii-1,3))
        tt3 = "Next Up: "+h(mod(ii-1,3))
        tt4 = '\n'+str(tim)+' sec remaining'+'\n'+'\n'+'\n'+str(len(a)-ii-1)+' events remain'
        root.after(1000, add_label)
        
    #root.after(a[ii]*1000, add_label)

root.after((a[ii]-2)*1000, add_label)
root.mainloop()