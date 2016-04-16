import cleverbot_io
import threading
from tkinter import *
from tkinter.ttk import *
def startchat():
    def sendtoclev():
        global response
        response = userentry.get()
        userentry.set("")
        enter['state'] = DISABLED
        chat['state'] = NORMAL
        chat.insert(END, response+"\n", "red")
        chat['state'] = DISABLED
        def send1():
            global messagetosend
            global response
            messagetosend = cb2.say(response)
            chat['state'] = NORMAL
            chat.insert(END, messagetosend+"\n", "blue")
            chat.see(END)
            chat['state'] = DISABLED
            send2()
        def send2():
            global messagetosend
            global response
            response = cb1.say(messagetosend)
            chat['state'] = NORMAL
            chat.insert(END, response+"\n", "red")
            chat['state'] = DISABLED
            chat.see(END)
            send1()
        send1()
            
    def sendtoclevthread(event):
        t = threading.Thread(target=sendtoclev)
        t.start()

    def quit():
        root.destroy()

    root = Tk()
    cb1 = cleverbot_io.Cleverbot("Ih7SiAskrVx87xF1","oHqp199HRBOBiN5thoXh1naFh6W2Vb07")
    cb2 = cleverbot_io.Cleverbot("Ih7SiAskrVx87xF1","oHqp199HRBOBiN5thoXh1naFh6W2Vb07")
    userentry = StringVar()
    history = StringVar()
    
    chat = Text(root)
    chat['state'] = DISABLED
    chat.tag_configure("red", foreground = "red")
    chat.tag_configure("blue", foreground = "blue")
    chat.grid(row=0, column = 0, rowspan = 2)
    
    message = Label(root, text="Say something!", anchor=E)
    message.grid(column=0, row=3, sticky=E)
    
    enter = Entry(root, textvariable = userentry)
    enter.grid(column=1, row=3, sticky=SE)
    enter.bind('<Return>', sendtoclevthread)
    
    close = Button(root, text="Quit", command=quit)
    close.grid(row=0, column=1, sticky=N, pady = 20)
    
    root.mainloop()
    cb1.killbot()
    cb2.killbot()

startchat()
