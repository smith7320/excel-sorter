#!/usr/bin/python
import tkinter
import tkinter.filedialog
import tkinter.messagebox
import xlrd
import xlwt

# main window class
class Overview():
    def __init__(self, master):
        self.master = master
        master.title("Excel Sorter")

        self.menuBar = tkinter.Menu(master)

        self.fileMenu = tkinter.Menu(self.menuBar, tearoff=0)
        self.fileMenu.add_command(label="Open", command=self.openFileWin)
        self.fileMenu.add_command(label="Save As", command=self.saveAsFileWin)

        self.menuBar.add_cascade(label="File", menu=self.fileMenu)
        self.menuBar.add_cascade(label="About", command=self.aboutWin)

        master.config(menu=self.menuBar)

    def aboutWin(self):
        infoWin = tkinter.Toplevel(self.master)
        infoWin.minsize(width=480,height=80)
        infoWin.maxsize(width=480,height=80)
        info = tkinter.Label(infoWin, wraplength=0, pady=3, padx=3,
                             text="This program allows the user to create/sort an existing excel file.\n\n"
                                  "Created by Douglas Smith.\n"
                                  "To see more of my projects check out smith7320 on Github.")

        info.pack()


    def openFileWin(self):
        validBook = False
        while validBook == False:
            try:
                openWin = tkinter.filedialog.askopenfilename(initialdir="C:/", title="Choose an existing Excel file",
                                                    filetypes=(("Excel 1997-2003 files","*.xls"),
                                                                ("All files","*.*")))
                book = xlrd.open_workbook(openWin)
            except xlrd.XLRDError:
                tkinter.messagebox.showerror(title="Wrong filetype", message="Error: Wrong filetype unsupported by this program. Please choose correct filetype.")
            else:
                validBook != validBook




    def saveAsFileWin(self):
        saveAsWin = tkinter.filedialog.asksaveasfilename(initialdir="C:/", title="Save Excel file",
                                                  filetypes=(("Excel 1997-2003 files","*.xls"),
                                                             ("All files", "*.*")))


def main():
   mainWindow = tkinter.Tk()
   app = Overview(mainWindow)
   mainWindow.mainloop()


if __name__ == "__main__":
    main()
