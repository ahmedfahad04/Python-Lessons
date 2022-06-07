from tkinter import *


def show_data():
    txt.delete(0.0,'end')
    txtName = ent.get()
    gen = var_char.get()
    
    if gen == 1:
        gen = 'sir'
    else:
        gen = 'madam'
    
    sentense = "Hello " + str(txtName)  + "\nHow are you "+gen+"?"
    txt.insert(0.0,sentense)


root = Tk()
root.geometry("200x300")


l1 = Label(root, text="Name: ")
l2 = Label(root, text="Gender: ")

ent = Entry(root)

var_char = IntVar()
r1 = Radiobutton(root, text="Male", variable=var_char, value=1)
r2 = Radiobutton(root, text="Female", variable=var_char, value=2)

l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
ent.grid(row=0, column=1)
r1.grid(row=1,column=1, sticky=W)
r2.grid(row=1,column=1, sticky=E)

txt = Text(root, width=25, wrap=WORD)
txt.grid(row=3, columnspan=2,sticky=W)

btn = Button(root, text="Register", bg="purple", fg='white', command=show_data)
btn.grid(row=2, columnspan=2)

root.mainloop()