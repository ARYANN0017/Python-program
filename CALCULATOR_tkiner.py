# import tkinter as tk
#
# root = tk.Tk()         # Main window create
# root.title("My First Tkinter App")
# root.geometry("1024x675")   # Width x Height window size
#
# root.mainloop()        # Always last line – window ko display rakhta hai


# import tkinter as tk
#
# window = tk.Tk()
# window.title("ABC")
# window.geometry("300x300")
# label = tk.Label(window, text="ABCdef")
# label.pack()
#
# def clicked():
#     print("clicked")
#
# btn = tk.Button(window, text="Click Me", command=clicked)
# btn.pack()
# window.mainloop()

# import tkinter as tk
#
# root = tk.Tk()
# root.title("Label Example")
#
# label = tk.Label(root, text="Hello Tkinter!", font=("Arial", 20))
# label.pack()
#
# root.mainloop()



#add button
# import tkinter as tk
#
# def click_btn():
#     print("Button clicked!")
#
# root = tk.Tk()
#
# btn = tk.Button(root, text="Click Me", command=click_btn)
# btn.pack()
#
# root.mainloop()


#entRy button
# import tkinter as tk
#
# root = tk.Tk()
#
# entry = tk.Entry(root, font=("Arial", 14))
# entry.pack()
#
# root.mainloop()


#
# import tkinter as tk
#
# def show():
#     name = entry.get()
#     label.config(text=f"haL haL nikL, {name}")
#
# root = tk.Tk()
#
# entry = tk.Entry(root, font=("Arial", 14))
# entry.pack()
#
# btn = tk.Button(root, text="Submit", command=show)
# btn.pack()
#
# label = tk.Label(root, text="", font=("Arial", 16))
# label.pack()
#
# root.mainloop()



import tkinter as tk
import math   #just because python does not support squar function soo!


root = tk.Tk()
root.title("Calculator")
root.geometry("350x700")

expression = ""  # this store whaT ever User Type!!


display = tk.Entry(root, font=("Arial", 20), bd=10, relief=tk.FLAT, justify="right")
#varible    single-line entry  font family size  border 10px  border look & flat

display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
                                           #paddinf x=left-right 10px   y=top-bottom

def press(num):
    global expression  #global variable allow to use a variable  outside the function
    expression += str(num)
    display.delete(0, tk.END)
    display.insert(tk.END, expression)
                    #all clear END
def clear():
    global expression
    expression = ""
    display.delete(0, tk.END)
    #clear all screen

def delete():
    global expression
    expression = expression[:-1]
    display.delete(0, tk.END)
                #strating index 0
    display.insert(tk.END, expression)

def equal():
    global expression
    try:
        result = str(eval(expression.replace("×", "*").replace("÷", "/")))
        # convert text into number
        display.delete(0, tk.END)
        display.insert(tk.END, result)
        expression = result
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")
        expression = ""

def square():
    global expression
    try:
        result = str(eval(expression+ "**2"))
        display.delete(0, tk.END)
        display.insert(tk.END, result)
        expression = result
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")
        expression = ""

def s_root():
    global expression
    try:
        value = eval(expression)
        result = math.sqrt(value)

        if result.is_integer():
            #result check whole num : true  ||  decimal num: false
            result = int(result)

        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")
        expression = ""

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("÷", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("×", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    #button row col
]

for (text, r, c) in buttons:
    if text == "=":
        tk.Button(root, text=text, font=("Arial", 18), bg="#ffa", command=equal)\
            .grid(row=r, column=c, ipadx=20, ipady=20)
    else:
        tk.Button(root, text=text, font=("Arial", 18),
                  command=lambda t=text: press(t))\
            .grid(row=r, column=c, ipadx=20, ipady=20)


tk.Button(root, text="C", font=("Arial", 20), bg="#f77", command=clear)\
    .grid(row=5, column=0, columnspan=2, sticky="nsew", ipadx=20, ipady=20)

tk.Button(root, text="Del", font=("Arial", 20), bg="#faa", command=delete)\
    .grid(row=5, column=2, columnspan=2, sticky="nsew", ipadx=20, ipady=20)

tk.Button(root, text="X2", font=("Arial", 20), bg="#aaf", command=square)\
    .grid(row=6, column=0, columnspan=2, sticky="nsew", ipadx=20, ipady=20)

tk.Button(root, text="√", font=("Arial", 20), bg="#8f8", command=s_root)\
    .grid(row=6, column=2, columnspan=2, sticky="nsew", ipadx=20, ipady=20)

root.mainloop()

