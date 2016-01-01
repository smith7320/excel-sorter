#!/usr/bin/python
import tkinter


def test():
    test = tkinter.Toplevel(mainWindow)
    button = tkinter.Button(test, text="test")
    button.pack()

def aboutWin():
    infoWin = tkinter.Toplevel(mainWindow)
    infoWin.minsize(width=350,height=180)
    infoWin.maxsize(width=350,height=180)
    info = tkinter.Text(infoWin)

    info.insert(tkinter.INSERT, "this is a test message")
    info.pack()


mainWindow = tkinter.Tk()
menuBar = tkinter.Menu(mainWindow)

fileMenu = tkinter.Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New", command=test)
fileMenu.add_command(label="Open", command=test)
fileMenu.add_command(label="Save", command=test)
fileMenu.add_command(label="Save As", command=test)

aboutMenu = tkinter.Menu(menuBar, tearoff=0)

menuBar.add_cascade(label="File", menu=fileMenu)
menuBar.add_cascade(label="About", command=aboutWin)

mainWindow.config(menu=menuBar)
mainWindow.mainloop()
