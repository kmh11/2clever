import clever
from tkinter import *
import threading
from tkinter.ttk import *
def startchat():
    def sendtoclev():
        messagetosend = userentry.get()
        chat['state'] = NORMAL
        chat.insert(END, messagetosend+"\n", "blue")
        chat['state'] = DISABLED
        userentry.set("")
        response = cb1.say(messagetosend)
        chat['state'] = NORMAL
        chat.insert(END, response+"\n", "red")
        chat['state'] = DISABLED
        chat.see(END)

    def sendtoclevthread(event):
        t = threading.Thread(target=sendtoclev)
        t.start()
        

    root = Tk()
    cb1 = clever.mkbot()
    userentry = StringVar()
    history = StringVar()
    chat = Text(root)
    chat['state'] = DISABLED
    chat.tag_configure("red", foreground = "red")
    chat.tag_configure("blue", foreground = "blue")
    chat.grid(row=0)
    message = Label(root, text="Say something!")
    message.grid(column=0,row=1)
    enter = Entry(root, textvariable = userentry)
    enter.grid(column=1,row=1)
    enter.bind('<Return>', sendtoclevthread)
    root.mainloop()
    cb1.killbot()

startchat()
