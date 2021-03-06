from tkinter import *

root = Tk()
root.title("test")

e = Entry(root, width=40, fg="black", borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_add():
    first_num = e.get()
    global g_num
    global math
    math = "add"
    g_num = int(first_num)
    e.delete(0, END)


def button_min():
    first_num = e.get()
    global g_num
    global math
    math = "subtraction"
    g_num = int(first_num)
    e.delete(0, END)


def button_mul():
    first_num = e.get()
    global g_num
    global math
    math = "multiplication"
    g_num = int(first_num)
    e.delete(0, END)


def button_div():
    first_num = e.get()
    global g_num
    global math
    math = "division"
    g_num = int(first_num)
    e.delete(0, END)


def button_eq():
    second = e.get()
    e.delete(0, END)
    if math == "add":
        e.insert(0, g_num + int(second))
    if math == "division":
        e.insert(0, str(int(g_num / int(second))))
    if math == "subtraction":
        e.insert(0, g_num - int(second))
    if math == "multiplication":
        e.insert(0, g_num * int(second))


def button_click(num: int):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))


def clear():
    e.delete(0, END)


button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(10))
add_button = Button(root, text="+", padx=40, pady=20, command=button_add)
min_button = Button(root, text="-", padx=40, pady=20, command=button_add)
mul_button = Button(root, text="X", padx=40, pady=20, command=button_mul)
div_button = Button(root, text="/", padx=40, pady=20, command=button_div)
clear_button = Button(root, text="clear", padx=79, pady=20, command=lambda: clear())
equal_button = Button(root, text="=", padx=40, pady=20, command=button_eq)

button_1.grid(row=3, column=0, )
button_2.grid(row=3, column=1, )
button_3.grid(row=3, column=2, )

button_4.grid(row=2, column=0, )
button_5.grid(row=2, column=1, )
button_6.grid(row=2, column=2, )

button_7.grid(row=1, column=0, )
button_8.grid(row=1, column=1, )
button_9.grid(row=1, column=2, )

button_0.grid(row=4, column=0, )
clear_button.grid(row=4, column=1, columnspan=2)
add_button.grid(row=5, column=0)
min_button.grid(row=5, column=1)
equal_button.grid(row=5, column=2)
mul_button.grid(row=6, column=0)
div_button.grid(row=6, column=1)
root.mainloop()
