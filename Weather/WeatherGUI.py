import requests as r
import tkinter as tk

def weather_info():
    city = input_field.get()
    url = f'https://wttr.in/{city}?m?T?0'
    get_weather = r.get(url)
    #print(get_weather.text)
    output_string.set(get_weather.text)

window = tk.Tk()

frame = tk.Frame(window)
frame.pack()
frame_label = tk.LabelFrame(frame, text="Weather info")
frame_label.pack()
input_label = tk.Label(frame_label, text="Input the city")
input_label.pack()
input_field = tk.Entry(frame_label)
input_field.pack()
button = tk.Button(frame_label, text="Send it", command=weather_info)
button.pack()

output_string = tk.StringVar()
output_data = tk.Label(frame_label, textvariable=output_string, justify='left')
output_data.pack()

window.mainloop()