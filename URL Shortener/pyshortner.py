# TO short Any url python "pyshorteners" module is used 
# pyshortener short any ural that give to progarm 
# url need to be valid

"""import pyshorteners 
# install pyshorteners "pip install pyshorteners"

url = url_var.get()
#taking url input from user

short = pyshorteners.Shortener().tinyurl.short(url)
#shortener fuction store in variable short

print("url shorted -->",short)"""


#define function 1 clear 2 copy 3 paste 4 shortener
#insatll clipboard ,validators 

from pyshorteners import Shortener
import clipboard
import validators

def clear():
    url_entry.delete(0,"end")
    shorten_url.config(text="")
    
    
def copy():
    clipboard.copy(shorten_url.cget("text"))
    c =Label(root,text="Copied",font=(20))
    c.pack()
    root.after(2000,c.destroy)
    
    
"""def shorten():
    link =url_entry.get()
    valid =validators.url("https://" + link)
    if(valid == True):
        short=Shortener().tinyurl.short(link)
        shorten_url.config(text=short)
    else:
        shorten_url.config(text="Invalid Address")"""
         

def Shorten():
    link = url_entry.get()
    valid = validators.url("https://" + link)
    if(valid == True):
        short = Shortener().tinyurl.short(link)
        shorten_url.config(text=short)
    else:
       shorten_url.config(text="Invalid Address")














#creating GUI using tkinter module

from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from tkinter import font



#create the main window of application
# main window object named root
root = Tk()

#giving the title to main window
root.title("URL Shortener")

#defie size of window 
root.geometry("500x500")


#lable  is used to display text or image on the screen

label = Label(root,text="Short Any URL" ).pack()

url_label = Label(root,text='Enter URL', font=('calibri',20,'bold'))
url_label.place(x=50,y=60)

url_entry = Entry(root, font=('arial',10,'bold'))
url_entry.place(x=170,y=67)

url_clear_b = Button(root,text="clear",command=clear )
url_clear_b.place(x=250,y=120)


url_shorten_b =Button(root,text='Shortene',command=Shorten)
url_shorten_b.place(x=150,y=120)


 
 
shorten_url  = Label(root,font=(20) ,relief="solid")
shorten_url.place(x=150,y=230)


copy_b = Button(root,text="COPY",command=copy)
copy_b.place(x=200,y=270)


label= Label(root,text="Shortener URL Here ! " ,font=('calibri',20,'bold'))
label.place(x=130,y=170)







root.mainloop()

