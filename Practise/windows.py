from tkinter import *

root = Tk()
font = ('Tahoma', 12)
padx, pady = 10, 10
bg = 'LightGreen'

# Label 1 — solid border
label1 = Label(root, text='Hello', bg=bg, bd=2, relief='solid', font=font)
label1.pack(padx=padx, pady=pady)

# Label 2 — sunken border
label2 = Label(root, text='Python', bd=5, relief='sunken', bg=bg,
               font=font, padx=padx, pady=pady)
label2.pack(padx=padx, pady=pady)

# Label 3 — raised border
label3 = Label(root, text='Tkinter', bd=5, relief='raised', bg=bg,
               font=font, padx=padx, pady=pady)
label3.pack(padx=padx, pady=pady)

root.mainloop()
