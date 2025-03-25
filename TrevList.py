import os
from tkinter import * 
from tkinter import messagebox
import sys

# Get the folder where the script or .exe is located
if getattr(sys, 'frozen', False):
    # If running as a bundled exe
    app_path = os.path.dirname(sys.executable)
else:
    # If running as a .py script
    app_path = os.path.dirname(os.path.abspath(__file__))

# Final path to your todo file
todo_file = os.path.join(app_path, "TrevList_SavedList.txt")






to_do_list = []

def load_list():
    global to_do_list
    if os.path.exists(todo_file):
        with open(todo_file, "r") as File:
            to_do_list = [line.strip() for line in File]


def load_list_gui():
    load_list()
    listbox.delete(0, END)
    for item in to_do_list:
        listbox.insert(END, item)

def clear_list_gui():
    global to_do_list
    confirm = messagebox.askyesno(message="Are you sure you want to delete list?")
    if confirm:
        listbox.delete(0, END)
        to_do_list.clear()
        save_list()
   
    else:
        pass


def save_list():
    global to_do_list
    with open(todo_file, "w") as file:
        for i in to_do_list:
            file.write(i + "\n")


    #function to add item



def add_item_GUI():
    item = item_entry.get().strip().title()  
    if item:
        to_do_list.append(item)             # update your internal list
        listbox.insert(END, item)           # update visual list
        item_entry.delete(0, END)                   # clear the input box

    

    

    # Remove function

def remove_item_GUI():
    global to_do_list
    try: 
        item = listbox.curselection()[0]
        to_do_list.pop(item)
        listbox.delete(item)
    
    except:
        pass





if os.path.exists("TrevList/Saved_List.txt"):
    load_list()
    
else:
    pass



def handle_enter_key(event):
    add_item_GUI()

def handle_delete_key(event):
    remove_item_GUI()



window = Tk()


window.geometry("600x600")  # width x height in pixels
window.eval('tk::PlaceWindow . center')
window.configure(bg='lightblue')

    
    # Header Section

header_frame = Frame(window, bg='lightblue', bd=2, relief=SUNKEN)
header_frame.pack(pady=(10,5))
window.title("TrevList")
window_title = Label(window, text='TrevList', font=("Ariel", 24), bg='lightblue')
window_title.pack(pady=5)

    
    # Input Section

input_frame = Frame(window, bg='lightblue')
input_frame.pack(pady=(0, 10))
item_entry = Entry(input_frame, width=40, font=('Helvetica', 24))
item_entry.bind("<Return>", handle_enter_key)
item_entry.pack(pady=5)


    # Add/Remove/Clear Section

button_frame_1 = Frame(window, bg='lightblue')
button_frame_1.pack(pady=(0,5))

add_button = Button(button_frame_1, text='Add', command=add_item_GUI, width=20, font=('Ariel', 14))
remove_button = Button(button_frame_1, text='Remove', command=remove_item_GUI, width=20, font=('Ariel', 14))
clear_button = Button(button_frame_1, text='Clear', command=clear_list_gui, width=20, font=('Ariel', 14))

add_button.pack(side='left',pady=5)
remove_button.pack(side='left', pady=5)
clear_button.pack(side='left', pady=5)


    # Save / Load Section


button_frame_2 = Frame(window, bg='lightblue')
button_frame_2.pack(pady=(0,10))

save_button = Button(button_frame_2, text='Save', command=save_list, width=20, font=('Ariel', 14))
load_button = Button(button_frame_2, text='Load', command=load_list_gui, width=20, font=('Ariel', 14))

save_button.pack(side='left', pady=5)
load_button.pack(side='left', pady=5)


    # List Section


list_frame = Frame(window, bg='lightblue')
list_frame.pack()

listbox = Listbox(list_frame, width=40, height=10, font=('Ariel', 18))
listbox.bind("<Delete>", handle_delete_key)
listbox.pack(pady=10)








window.mainloop()