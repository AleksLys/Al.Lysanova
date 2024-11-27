from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.ttk import Radiobutton 
from tkinter import messagebox 
import tkinter as tk
from tkinter import Menu, filedialog
 
window = Tk()
window.title("Лысанова Александра Ивановна")
window.geometry('400x250') 

tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Калькулятор')
tab_control.add(tab2, text='Чекбоксы')
tab_control.add(tab3, text='Текст')

# первая вкладка
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                result = "Деление на ноль!"
            else:
                result = num1 / num2
        else:
            result = "Неверная операция"

        result_label.config(text=f"Результат: {result}")

    except ValueError:
        result_label.config(text="Неверная операция")


label1 = tk.Label(tab1, text="Число 1:")
label1.grid(row=0, column=0)
entry1 = tk.Entry(tab1)
entry1.grid(row=0, column=1)

label2 = tk.Label(tab1, text="Число 2:")
label2.grid(row=1, column=0)
entry2 = tk.Entry(tab1)
entry2.grid(row=1, column=1)

operation_var = tk.StringVar(tab1)
operation_var.set("+")  # default value
operation_options = ["+", "-", "*", "/"]
operation_dropdown = ttk.Combobox(tab1, textvariable=operation_var, values=operation_options)
operation_dropdown.grid(row=2, column=0, columnspan=2)

button = tk.Button(tab1, text="Калькулятор", command=calculate)
button.grid(row=3, column=0, columnspan=2)

result_label = tk.Label(tab1, text="")
result_label.grid(row=4, column=0, columnspan=2)


# вторая вкладка
selected1 = IntVar()   
selected2 = IntVar() 
selected3 = IntVar() 

rad1 = Radiobutton(tab2,text='Первый', value=1, variable=selected1)   
rad2 = Radiobutton(tab2,text='Второй', value=2, variable=selected2)   
rad3 = Radiobutton(tab2,text='Третий', value=3, variable=selected3) 

rad1.grid(column=0, row=0)   
rad2.grid(column=1, row=0)   
rad3.grid(column=2, row=0)  

def clicked():
    total = 0
    if selected1.get():
        total += 1
    if selected2.get():
        total += 2
    if selected3.get():
        total += 3
    messagebox.showinfo("Выбор", f"Вы выбрали: {total}")

btn = Button(tab2, text="Клик", command=clicked) 
btn.grid(column=3, row=0) 

tab_control.pack(expand=1, fill='both')

# третья вкладка
txt = scrolledtext.ScrolledText(tab3, width=40, height=10)   
txt.grid(column=0, row=0)

def open_file():
    filepath = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if filepath:
        try:
            with open(filepath, "r") as f:
                text = f.read()
                txt.delete("1.0", tk.END)  # Clear existing text
                txt.insert(tk.END, text)
        except FileNotFoundError:
            txt.delete("1.0", tk.END)
            txt.insert(tk.END, "Error: File not found.")
        except Exception as e:
            txt.delete("1.0", tk.END)
            txt.insert(tk.END, f"Error: {e}")

menu = Menu(window)   
new_item = Menu(menu, tearoff=0)   
new_item.add_command(label='Открыть', command=open_file)   
menu.add_cascade(label='Файл', menu=new_item)   

window.config(menu=menu) 

window.mainloop()