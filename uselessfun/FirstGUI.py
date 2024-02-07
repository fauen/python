import tkinter as tk

fontTitle = ['Arial', 35]
fontText = ['Helvetica', 17]

root = tk.Tk()

root.geometry("1000x1000")
root.title("The first application (I think...)")
# root.config(background="#282828")

label = tk.Label(root, text="Hello there boss!", font=fontTitle)
label.pack(padx=25, pady=15)

textbox = tk.Text(root, height=2, font=fontText)
textbox.pack(padx=25, pady=15)

entry = tk.Entry(root, width="50")
entry.pack(padx=25, pady=15)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text="1", font=fontText)
btn1.grid(row=0, column=0, sticky="we")

btn2 = tk.Button(buttonframe, text="2", font=fontText)
btn2.grid(row=0, column=1, sticky="we")

btn3 = tk.Button(buttonframe, text="3", font=fontText)
btn3.grid(row=0, column=2, sticky="we")

btn4 = tk.Button(buttonframe, text="4", font=fontText)
btn4.grid(row=1, column=0, sticky="we")

btn5 = tk.Button(buttonframe, text="5", font=fontText)
btn5.grid(row=1, column=1, sticky="we")

btn6 = tk.Button(buttonframe, text="6", font=fontText)
btn6.grid(row=1, column=2, sticky="we")

btn7 = tk.Button(buttonframe, text="7", font=fontText)
btn7.grid(row=2, column=0, sticky="we")

btn8 = tk.Button(buttonframe, text="8", font=fontText)
btn8.grid(row=2, column=1, sticky="we")

btn9 = tk.Button(buttonframe, text="9", font=fontText)
btn9.grid(row=2, column=2, sticky="we")

btn10 = tk.Button(buttonframe, text="10", font=fontText)
btn10.grid(row=3, column=0, columnspan=3, sticky="we")

buttonframe.pack(fill="x")

button = tk.Button(root, text="Touch me", font=fontText)
button.place(x=800, y=800, height=150, width=150, )

root.mainloop()