import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        selected_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")

root = tk.Tk()
root.title("My To-Do List")
root.geometry("400x350")

frame_tasks = tk.Frame(root)
frame_tasks.pack(pady=10, fill=tk.BOTH, expand=True)

listbox_tasks = tk.Listbox(frame_tasks, height=10, width=50, selectbackground="#a6a6a6")
listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=50)
entry_task.pack(pady=10)

frame_buttons = tk.Frame(root)
frame_buttons.pack()

button_add_task = tk.Button(frame_buttons, text="Add Task", width=20, command=add_task)
button_add_task.pack(side=tk.LEFT, padx=5)

button_delete_task = tk.Button(frame_buttons, text="Delete Selected Task", width=20, command=delete_task)
button_delete_task.pack(side=tk.LEFT, padx=5)

root.mainloop()