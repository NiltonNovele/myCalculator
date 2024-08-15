import tkinter as tk
from tkinter import messagebox

def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid input")

def button_click(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + value)

def clear_entry():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("NIlton's Calculator")

root.configure(bg='black')


entry = tk.Entry(root, width=16, font=('Arial', 24), bd=5, insertwidth=4, borderwidth=4,
                 bg='black', fg='white', insertbackground='white')  
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0, 4)
]

for button in buttons:
    text = button[0]
    row = button[1]
    column = button[2]
    if len(button) == 4:
        colspan = button[3]
        tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18), 
                  bg='black', fg='white', activebackground='gray', command=clear_entry).grid(row=row, column=column, columnspan=colspan, sticky='nsew')
    else:
        tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18), 
                  bg='black', fg='white', activebackground='gray', 
                  command=lambda t=text: button_click(t) if t != '=' else evaluate_expression()).grid(row=row, column=column, sticky='nsew')

for i in range(6):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
