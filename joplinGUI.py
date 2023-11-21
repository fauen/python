import tkinter as tk
import requests as r
from configparser import ConfigParser
import os.path
import os

config = ConfigParser()

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

def app_quit():
    quit()

def joplin_input():
    title = joplin_title_input.get()
    body = joplin_body_input.get("1.0", tk.END)
    data = {
        "parent_id": notebook,
        "title": title,
        "body": body
    }
    post = r.post(url=url + token, json=data)
    if post.status_code != 200:
        quit()

url = 'http://localhost:41184/notes?token='
token = config.get('joplin', 'token')
notebook = config.get('joplin', 'notebook')

# GUI
window = tk.Tk()

window.geometry("200x300")
window.title("Joplin bookmark window")

frame = tk.Frame(window)
frame.pack()

joplin_frame = tk.LabelFrame(frame, text="Joplin input")
joplin_frame.pack()
joplin_title = tk.Label(joplin_frame, text="Title")
joplin_title.pack()
joplin_title_input = tk.Entry(joplin_frame)
joplin_title_input.pack()
joplin_body = tk.Label(joplin_frame, text="Body")
joplin_body.pack()
joplin_body_input = tk.Text(joplin_frame, height=11)
joplin_body_input.pack()

joplin_send = tk.Button(frame, text="Send it!", command=lambda: [joplin_input(), clear_text()])
joplin_send.pack()

app_quit = tk.Button(frame, text="Quit", command=app_quit)
app_quit.pack()


window.mainloop()
