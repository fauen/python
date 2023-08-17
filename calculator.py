import tkinter as tk
from tkinter import messagebox, Entry, Button, END, Frame

styleButtonNumbers = ['Helvetica', 20]
styleButtonMath  = ['Arial', 15]


root = tk.Tk()
#root.geometry("400x500")
root.title("Daniel's Calculator")

def buttonClick(number):
    current = ent.get()
    ent.delete(0, END)
    ent.insert(0, str(current) + str(number))

ent = Entry(root, borderwidth=5)
ent.pack()

buttonFrame = tk.Frame(root)
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)
buttonFrame.columnconfigure(3, weight=1)
buttonFrame.columnconfigure(4, weight=1)

numberButton1 = Button(buttonFrame, text="1", padx=15, pady=5, command=lambda: buttonClick(1))
numberButton2 = Button(buttonFrame, text="2", padx=15, pady=5, command=lambda: buttonClick(2))
numberButton3 = Button(buttonFrame, text="3", padx=15, pady=5, command=lambda: buttonClick(3))
numberButton4 = Button(buttonFrame, text="4", padx=15, pady=5, command=lambda: buttonClick(4))
numberButton5 = Button(buttonFrame, text="5", padx=15, pady=5, command=lambda: buttonClick(5))
numberButton6 = Button(buttonFrame, text="6", padx=15, pady=5, command=lambda: buttonClick(6))
numberButton7 = Button(buttonFrame, text="7", padx=15, pady=5, command=lambda: buttonClick(7))
numberButton8 = Button(buttonFrame, text="8", padx=15, pady=5, command=lambda: buttonClick(8))
numberButton9 = Button(buttonFrame, text="9", padx=15, pady=5, command=lambda: buttonClick(9))
numberButton0 = Button(buttonFrame, text="0", padx=15, pady=5, command=lambda: buttonClick(0))

mathButtonAddition = Button(buttonFrame, text="+", padx=15, pady=5, command=lambda: buttonClick())
mathButtonSubstraction = Button(buttonFrame, text="-", padx=15, pady=5, command=lambda: buttonClick())
mathButtonMultiply = Button(buttonFrame, text="*", padx=15, pady=5, command=lambda: buttonClick())
mathButtonDivision = Button(buttonFrame, text="/", padx=15, pady=5, command=lambda: buttonClick())
mathButtonEquals = Button(buttonFrame, text="=", padx=15, pady=5, command=lambda: buttonClick())
mathButtonComma = Button(buttonFrame, text=".", padx=15, pady=5, command=lambda: buttonClick())

# Put buttons on screen

numberButton1.grid(row=4, column=1, sticky="we")
numberButton2.grid(row=4, column=2, sticky="we")
numberButton3.grid(row=4, column=3, sticky="we")
numberButton4.grid(row=3, column=1, sticky="we")
numberButton5.grid(row=3, column=2, sticky="we")
numberButton6.grid(row=3, column=3, sticky="we")
numberButton7.grid(row=2, column=1, sticky="we")
numberButton8.grid(row=2, column=2, sticky="we")
numberButton9.grid(row=2, column=3, sticky="we")
numberButton0.grid(row=5, column=1, columnspan=2, sticky="we")

mathButtonAddition.grid(row=2, rowspan=2, column=4, sticky="ns")
mathButtonSubstraction.grid(row=1, column=4, sticky="we")
mathButtonMultiply.grid(row=1, column=3, sticky="we")
mathButtonDivision.grid(row=1, column=2, sticky="we")
mathButtonEquals.grid(row=4, rowspan=2, column=4, sticky="ns")
mathButtonComma.grid(row=5, column=3, sticky="we")

buttonFrame.pack(fill="x")

root.mainloop()