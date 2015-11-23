import Tkinter
import tkFileDialog

root = Tkinter.Tk()
root.withdraw()
foldername = tkFileDialog.askdirectory(parent = root)
print foldername

csvOutput = tkFileDialog.asksaveasfilename()
print csvOutput