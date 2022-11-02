from email import message
from tkinter import *
from tkinter import messagebox
import os
import webbrowser
import time


def click():
    #while True:
        #messagebox.showinfo(title='This is a damn messagebox', message='je moeder')
        #messagebox.showwarning(title='System 32 got deleted', message='Your pc is infected by a virus')
        #messagebox.showerror(title='Traceback most recent call last', message='"Tkinter" module not found ModuelNotFoundError')
    if messagebox.askokcancel(title='E', message='Do you want to shutdown your computer: '):
        os.system('cmd /c "shutdown -s"')
    else:
        messagebox.showinfo(title='E', message='Ok then not I guess')
    #if messagebox.askyesno(title='E', message='Do you like Rick Astley?'):
        #webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    #else:
        #messagebox.showinfo(title='You are a idiot', message='You are a idiot')
        
window = Tk()

button = Button(window, command=click, text="Click me!")
button.pack()


window.mainloop()
