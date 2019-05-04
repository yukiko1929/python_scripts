import tkinter
from functools import partial

window = tkinter.Tk()
label = tkinter.Label(window, text = 'hello yukiko', font = 'Arial 30')
MyButton = partial(tkinter.Button, window, fg = 'blue', bg = 'pink')
b1 = MyButton(text = 'button1')
b2 = MyButton(text = 'button2')
qb = MyButton(text = 'quit', command = window.quit)

label.pack()
b1.pack()
b2.pack()
qb.pack()

window.mainloop()