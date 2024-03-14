import customtkinter
from tkinter import *
from tkinter import messagebox

app = customtkinter.CTk()
app.title('To-Do-List')
app.geometry("350x450")
app.config(bg='#09112e')

font1 = ('Arial',30,'bold')
font2 = ('Arial',18,'bold')
font3 = ('Arial',10,'bold')


# function for add the task 

def add_task():
    task = task_entry.get()
    if task:
        tasks_list.insert(0, task)
        task_entry.delete(0, END)
        save_tasks()
    else:
        messagebox.showerror('Error','Enter a task.')
        
# create a function for remove task

def remove_task():
    selected = tasks_list.curselection()
    if selected:
        tasks_list.delete(selected[0])
        save_tasks()
    else:
        messagebox.showerror('Error','Choose a task to delete.')
        
# created a function for save task

def save_tasks():
    with open("tasks.txt","w") as f:
        tasks = tasks_list.get(0,END)
        for task in tasks:
            f.write(task + "\n")


# created a load tasks function

def load_tasks():
    try:
        with open("tasks.txt","r") as f:
            tasks = f.readlines()
            for task in tasks:
                tasks_list.insert(0, task.strip()) 
    except FileNotFoundError:
        # messagebox.showerror('Error','Cannot load tasks.')
        pass
        
               
#created a title 
   
title_label = customtkinter.CTkLabel(app,font=font1,text='TO DO List',text_color="white",bg_color="#09112e")
title_label.place(x=100,y=20)

# created a add task button 

add_button = customtkinter.CTkButton(app,command=add_task,font=font2,text_color="white",text="Add Task",fg_color="green",hover_color="orange",bg_color="white",cursor='hand2',corner_radius=5,width=120)
add_button.place(x=40,y=80)

# created a remove task button 

remove_button = customtkinter.CTkButton(app,command=remove_task,font=font2,text_color="white",text="Remove Task",fg_color="red",hover_color="red",bg_color="white",cursor='hand2',corner_radius=5)
remove_button.place(x=180,y=80)

#created a task entry stored

task_entry = customtkinter.CTkEntry(app,font=font2,text_color="black",fg_color="white",border_color="black",width=280)
task_entry.place(x=40,y=120)

# created a task list box

tasks_list = Listbox(app,width=39,height=15,font=font3)
tasks_list.place(x=40,y=180)

# load task 

load_tasks()

# run main function

app.mainloop()