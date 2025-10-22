#!/usr/bin/env python
# coding: utf-8

# # Frame Widgets

# In[9]:


# Example: tkinter Frame widget
from tkinter import*
root = Tk()
root.title('Frame Example')
root.geometry("400x400")
main_frame = Frame(root, width=200, height=200, bg="Red")
main_frame.grid(row=0, column=0)
framentry2 = Frame(root, width=200, height=200, bg="Green")
framentry2.grid(row=1, column=0)
framentry3 = Frame(root, width=200, height=200, bg="Blue")
framentry3.grid(row=0, column=1)
frame4 = Frame(root, width=200, height=200, bg="Yellow")
frame4.grid(row=1, column=1)
root.mainloop()


# In[19]:


# Arrange Label, Entry, Button in a Frame
from tkinter import*
root=Tk()
root.title('Arrange widgets in Frame')
main_frame=Frame(root)
Label(main_frame, text='Name').grid(row=0, sticky='w', padx=5)
Label(main_frame, text='Age').grid(row=1, sticky='w', padx=5)
Label(main_frame, text = 'PhoneNumber').grid(row=2, sticky='w', padx=5)
entry1 = Entry(main_frame)
entry1.grid(row=0, column=1)
entry2 = Entry(main_frame)
entry2.grid(row=1, column=1)
entry3 = Entry(main_frame)
entry3.grid(row=2, column=1)
view_button = Button(main_frame, text='View', bg='LightGreen')
view_button.grid(row=3, columnspan=2, sticky='e', pady=10)
main_frame.grid(row=0, column=0, padx=10, pady=10)
root.mainloop()


# In[100]:


# Arrange Label, Entry, Button in a Frame
from tkinter import*
root=Tk()
root.title('Arrange widgets in Frame')
main_frame=Frame(root)
Label(main_frame, text='Name').grid(row=0, sticky='w', padx=5)
Label(main_frame, text='Age').grid(row=1, sticky='w', padx=5)
Label(main_frame, text = 'PhoneNumber').grid(row=2, sticky='w', padx=5)
entry1 = Entry(main_frame)
entry1.grid(row=0, column=1)
entry2 = Entry(main_frame)
entry2.grid(row=1, column=1)
entry3 = Entry(main_frame)
entry3.grid(row=2, column=1)
view_button = Button(main_frame, text='View', bg='LightGreen')
view_button.grid(row=3, columnspan=2, sticky='e', pady=10)
main_frame.grid(row=0, column=0, padx=10, pady=10)

# Place other Frame to the right side of the first Frame
side_frame=Frame(root)
Label(side_frame, text='Gender').grid(row=0, sticky='w', padx=5)
Label(side_frame, text='City').grid(row=1, sticky='w', padx=5)
Label(side_frame, text = 'Address').grid(row=2, sticky='w', padx=5)
gender_entry = Entry(side_frame)
gender_entry.grid(row=0, column=1)
city_entry = Entry(side_frame)
city_entry.grid(row=1, column=1)
address_entry = Entry(side_frame)
address_entry.grid(row=2, column=1)
display_button = Button(side_frame, text='Display', bg='LightGreen')
display_button.grid(row=3, columnspan=2, sticky='e', pady=10)
side_frame.grid(row=0, column=1, padx=10, pady=10)

root.mainloop()


# # LabelFrame Widgets

# In[42]:


# LabelFrame Example
from tkinter import *
root = Tk()
root.title('LabelFrame')
labelframentry1 = LabelFrame(root, text="Label and Button Frame ", 
                         font=('Calibri', 12), bg='LightBlue')
labelframentry1.pack(fill="both", expand="yes")
Label(labelframentry1, text="Label1", bg='LightYellow').pack(side=TOP)
Button(labelframentry1, text="Button1", bg='Red', fg='White').pack(side=LEFT)
labelframentry2 = LabelFrame(root, text="CheckButton and Radiobutton Frame", 
                         font=('Calibri', 12), bg = 'LightGreen')
labelframentry2.pack(fill="both", expand="yes")
Checkbutton(labelframentry2, text="CheckButton", bg='Pink').pack(side=RIGHT)
Radiobutton(labelframentry2, text="RadioButton", bg='Yellow').pack(side=BOTTOM)
root.mainloop()


# In[51]:


# Change anchor of label
from tkinter import *
root = Tk()
root.title('Label Anchor Example')
root.geometry('400x200')
labelframentry1 = LabelFrame(root, text="Label Frame", 
                         font = ('Calibri',12), bg = 'LightBlue', 
                         labelanchor = E)
labelframentry1.pack(fill="both", expand="yes")
Label(labelframentry1, text="Label", bg = 'Magenta').pack(side = LEFT)
root.mainloop() 


# # Tabbed/Notebook Widget

# In[96]:


from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry("400x200")
root.title("Tab Widget")
tabcontrol = ttk.Notebook(root, padding=10)
tab1 = ttk.Frame(tabcontrol)
tab2 = ttk.Frame(tabcontrol)
tabcontrol.add(tab1, text = 'Tab1')
tabcontrol.add(tab2, text = 'Tab2')
tabcontrol.pack(expand = 1, fill = "both")
ttk.Label(tab1, text = "A label in tab1", 
          font = ('Helvetica',12)).grid(column = 0,row = 0, 
                                        padx = 50, pady = 50)
ttk.Label(tab2, text = "A label in tab2", 
          font = ('Times New Roman',12)).grid(column = 0, row = 0, 
                                              padx = 50, pady = 50)
tabcontrol.select(1)
root.mainloop()


# # Paned Window Widget

# In[98]:


root = Tk()
root.title('Panned Window')
root.geometry('400x300')
# The 1st paned window
panedwindow1 = PanedWindow(root)
panedwindow1.pack(fill = BOTH, expand = 1)
entry1 = Entry(panedwindow1, bd = 5, relief = 'groove', justify='center',
               font = ('Calibri', 30), width = 10, bg = 'LightBlue')
panedwindow1.add(entry1)

#adding 2nd paned window to the 1st paned window
panedwindow2 = PanedWindow(panedwindow1, orient = VERTICAL)
panedwindow1.add(panedwindow2)
entry2 = Spinbox(panedwindow2, from_ = 10, to = 20, 
                 font = ('Calibri', 12), bg = 'LightPink')
entry3 = Entry(panedwindow2, bg = 'LightGreen', font = ('Calibri',12) )
entry3.insert(0,3)
# show sash
panedwindow1.configure(sashrelief = RAISED)
def subtract():
    num1 = int(entry2.get()) # getting value of spinbox
    num2 = int(entry3.get()) # getting value of entry
    data = str(num1-num2)
    entry1.delete(0, END)
    entry1.insert(1,data)
# adding spinbox to the 2nd paned window
panedwindow2.add(entry2)
# adding entry to the 2nd paned window
panedwindow2.add(entry3)
# creation of button widget
subtract_button = Button(panedwindow2, text = "Subtract", 
                         font=('Calibri', 14), bg = 'LightYellow',
                         command = subtract)
# adding button to the 2nd paned window
panedwindow2.add(subtract_button)
# infinte loop
root.mainloop()


# In[99]:


# Set sash width
from tkinter import *
# main window creation
root = Tk()
#window size
root.geometry('300x300')
# paned window object
panedwindow1 = PanedWindow(root, orient ='vertical')
# expand option for widgets to expand and fill for letting widgets adjust itself
panedwindow1.pack(fill = BOTH, expand = 1)
# Checkbutton object
checkbutton = Checkbutton(panedwindow1, text ="I am checkbutton")
checkbutton.pack(side = TOP)
# Adding Checkbutton to panedwindow
panedwindow1.add(checkbutton)
# Radiobutton object
radiobutton = Radiobutton(panedwindow1, text ="I am radiobutton")
radiobutton.pack(side = TOP)
# Adding Radiobutton to panedwindow
panedwindow1.add(radiobutton)
# button object
button1 = Button(panedwindow1, text ="I am button")
button1.pack(side = TOP)
# Adding button to panedwindow
panedwindow1.add(button1)
# Tkinter string variable
str = StringVar()
# entry widget
entry1 = Entry(panedwindow1, textvariable = str, 
               font =('arial', 15, 'bold'))
entry1.pack()
# will focus on entry widget particularly
entry1.focus_force()
str.set(' PanedWindow')
# configure sash border and width
panedwindow1.configure(sashrelief = RAISED, sashwidth = 5)
# adding entry widget to the paned window
panedwindow1.add(entry1)
#infinite loop
root.mainloop()


# # Toplevel Widget

# In[90]:


from tkinter import *
root = Tk()
root.title('Main window')
root.geometry("350x250")
def navigate():
    # top level object for creation of a new window
    topobj = Toplevel(root)
    topobj.geometry('300x150')
    topobj.title('New window')
    topobj.mainloop()
btn1 = Button(root, text = "Navigate", command = navigate)
btn1.pack(pady=100)
root.mainloop()


# In[94]:


from tkinter import *
root = Tk()
root.geometry("300x300")
root.title('Main window')
topobj = Toplevel(root)
topobj.title('New window')
topobj.geometry("300x300")
root.lift(topobj)
topobj.deiconify()
root.mainloop()


# In[ ]:




