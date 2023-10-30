import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def edit_task():
    selected_task = task_list.curselection()
    if selected_task:
        new_task = task_entry.get()
        if new_task:
            index = selected_task[0]
            task_list.delete(index)
            task_list.insert(index, new_task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a new task.")
    else:
        messagebox.showwarning("Warning", "Please select a task to edit.")

def delete_task():
    selected_task = task_list.curselection()
    if selected_task:
        task_list.delete(selected_task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def exit_app():
    root.destroy()

root = tk.Tk()
root.title("To-Do List")

task_list = tk.Listbox(root)
task_list.pack(pady=20)

task_entry = tk.Entry(root)
task_entry.pack()

add_button = tk.Button(root, text="Add Task", command=add_task)
edit_button = tk.Button(root, text="Edit Task", command=edit_task)
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
exit_button = tk.Button(root, text="Exit", command=exit_app)

add_button.pack()
edit_button.pack()
delete_button.pack()
exit_button.pack()

root.mainloop()
