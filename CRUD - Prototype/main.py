from tkinter import *
from tkinter import messagebox
import functions
def insert():
    key = key_Entry.get().strip()
    value = value_Entry.get().strip()
    if key == "" or value == "":
        messagebox.showerror("Key Value DataStore","Invalid input!")
    else:
        functions.insert(key= key, value= value)
        messagebox.showinfo("Key Value DataStore","Inserted the data!")
        key_Entry.delete(0,END)
        value_Entry.delete(0,END)

def find():
    key = key_Entry.get().strip()
    if key == "":
        messagebox.showerror("Key Value DataStore","Invalid input!")
    else:
        value = functions.find(key= key)
        if value == "Invalid Key":
            messagebox.showerror("Key Value DataStore","Invalid Key!")
        else:
            messagebox.showinfo("Key Value DataStore",f"The value for the key : {key} -> {value}")
            key_Entry.delete(0,END)


def delete():
    key = key_Entry.get().strip()
    if key == "":
        messagebox.showerror("Key Value DataStore","Invalid input!")
    else:
        msg = functions.delete(key= key)
        if msg:
            messagebox.showerror("Key Value DataStore","Invalid Key!")
        else:
            messagebox.showinfo("Key Value DataStore","Deleted the data")
            key_Entry.delete(0,END)

root = Tk()
root.title("😁")
root.geometry("400x550")
title = Label(root, text= "Key Value DataStore")
title.config(font=("Comic Sans MS",20))
key_label = Label(root, text= "Key")
key_label.config(font=("default",15))
key_label.place(x=40,y=100)
key_Entry = Entry(root,width=40)
key_Entry.place(x= 100 ,y= 106)
value_label = Label(root, text= "Value")
value_label.config(font= ("default",15))
value_label.place(x = 40, y = 200)
value_Entry = Entry(root, width= 40)
value_Entry.place(x = 100, y = 205)
title.pack()

insert_button = Button(root, text= "Insert",command= insert)
insert_button.config(font= ("default",15))
insert_button.place(x= 40, y = 350)

find_button = Button(root, text= "Find", command= find)
find_button.config(font= ("default",15))
find_button.place(x= 150, y = 350)

Delete_button = Button(root, text= "Delete", command= delete)
Delete_button.config(font= ("default",15))
Delete_button.place(x= 260, y = 350)


root.mainloop()