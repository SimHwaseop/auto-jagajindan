
# importing only those functions which
# are needed
from tkinter import Tk, mainloop, TOP
from tkinter.ttk import Button
 
# time function used to calculate time
from time import time
 
# creating tkinter window
root = Tk()
 
button = Button(root, text = 'Geeks')
button.pack(side = TOP, pady = 5)
 
def a():
    print('Running...')
    root.after(1000, a)
# Calculating starting time
start = time()
 
# in after method 5000 milliseconds
# is passed i.e after 5 seconds
# main window i.e root window will
# get destroyed
a()
 
mainloop()
 
# calculating end time
end = time()
print('Destroyed after % d seconds' % (end-start))