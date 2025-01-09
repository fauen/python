import requests as r
from nicegui import ui

def get_data(e: events.GenericEventArguments):
    print(url)

def main():
    ui.input(label="Text", placeholder="Input URL").on('keydown.enter', get_data)
    result = ui.label()
    ui.run()

if __name__ in {"__main__", "__mp_main__"}:
    main()