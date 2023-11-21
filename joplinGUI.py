import tkinter as tk
# If you want a popup to show.
#from tkinter import messagebox
import requests as r
from configparser import ConfigParser
import os.path
import os

config = ConfigParser()

# Checking to see if the config files exist, if not, write correct information to it.
if not os.path.isfile('./config.ini'):
    token_input = input("Input your token: ")
    notebook_input = input("Input notebook id: ")
    config['joplin'] = {
        "token": token_input,
        "notebook": notebook_input
    }
    with open('./config.ini', 'w') as conf:
        config.write(conf)
    config.read('./config.ini')
else:
    config.read('./config.ini')

def clear_text():
    joplin_title_input.delete(0, tk.END)
    joplin_body_input.delete("1.0", tk.END)

# No need to have this currently.
# def app_quit():
    # quit()

def joplin_input():
    title = joplin_title_input.get()
    body = joplin_body_input.get("1.0", tk.END)
    data = {
        "parent_id": notebook,
        "title": title,
        "body": body
    }
    post = r.post(url=url + token, json=data)
    # If you want a popup to show up.
    #tk.messagebox.showinfo(title="Note added!", message="Note has been added to Joplin!")
    if post.status_code != 200:
        quit()

# Main parts for communicating with the Joplin application.
url = 'http://localhost:41184/notes?token='
token = config.get('joplin', 'token')
notebook = config.get('joplin', 'notebook')

# GUI
window = tk.Tk()

# We can set the geometry if we want, but how it is right now is not needed.
#window.geometry("200x300")

# Main window title, what you see in the application bar.
window.title("Joplin bookmark window")

# We add a frame to contain all the Joplin related thing to it.
frame = tk.Frame(window, padx=5)
frame.pack()

# Here we start adding our Joplin specific frame and what should be in it.
joplin_frame = tk.LabelFrame(frame, text="Joplin input", padx=10, pady=10)
joplin_frame.pack()
joplin_title = tk.Label(joplin_frame, text="Title")
joplin_title.pack()
joplin_title_input = tk.Entry(joplin_frame)
joplin_title_input.pack(fill='x') # We want the Entry bar to fill all available x space.
joplin_body = tk.Label(joplin_frame, text="Body")
joplin_body.pack()
joplin_body_input = tk.Text(joplin_frame, height=11, width=30) # Setting a width here so entry has an end.
joplin_body_input.pack()

# This part sets all the padding we want in the main Joplin frame.
for widget in joplin_frame.winfo_children():
    widget.pack_configure(padx=10, pady=5)

# Creating a specific frame for our button at the end.
button_frame = tk.Frame(window, pady=5)
button_frame.pack()
# Because we want two function to run we have to use lambda here. Make sure in this case with lambda to have (), with the normal command you should not.
joplin_send = tk.Button(button_frame, text="Done", command=lambda: [joplin_input(), clear_text()], font=('', 15), pady=5, padx=10)
joplin_send.pack()

# We don't have to have a quit button, I had this for testing.
#app_quit = tk.Button(frame, text="Quit", command=app_quit)
#app_quit.pack()

window.mainloop()
