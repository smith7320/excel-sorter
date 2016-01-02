#!/usr/bin/python
import tkinter
import tkinter.filedialog
import tkinter.messagebox
import xlrd
import xlwt

# vars
# todo

def aboutWin():
    infoWin = tkinter.Toplevel(mainWindow)
    infoWin.minsize(width=480,height=80)
    infoWin.maxsize(width=480,height=80)
    info = tkinter.Label(infoWin, wraplength=0, pady=3, padx=3,
                         text="This program allows the user to create/sort an existing excel file.\n\n"
                              "Created by Douglas Smith.\n"
                              "To see more of my projects check out smith7320 on Github.")

    info.pack()


def openFileWin():
    openWin = tkinter.filedialog.askopenfilename(initialdir="C:/", title="Choose an existing Excel file",
                                              filetypes=(("Excel 1997-2003 files","*.xls"),
                                                         ("Excel 2007 files", "*.xlsx"),
                                                         ("all files","*.*")))


def saveAsFileWin():
    saveAsWin = tkinter.filedialog.asksaveasfilename(initialdir="C:/", title="Save Excel file",
                                              filetypes=(("Excel 1997-2003 files","*.xls"),
                                                         ("Excel 2007 files", "*.xlsx")))


mainWindow = tkinter.Tk()
mainWindow.title("Excel Sorter")
menuBar = tkinter.Menu(mainWindow)

# add menu options
fileMenu = tkinter.Menu(menuBar, tearoff=0)
fileMenu.add_command(label="Open", command=openFileWin)
fileMenu.add_command(label="Save As", command=saveAsFileWin)

aboutMenu = tkinter.Menu(menuBar, tearoff=0)

menuBar.add_cascade(label="File", menu=fileMenu)
menuBar.add_cascade(label="About", command=aboutWin)

# add window options


# organize window
mainWindow.config(menu=menuBar)
mainWindow.mainloop()
