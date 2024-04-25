import flet as ft
import time

def main(page: ft.Page):
    t = ft.Text(color="green", size=50)
    page.add(t)

    for i in range(11):
        t.value = f"Time: {i}"
        page.update()
        time.sleep(1)
        
    t.value = "Time's up!"
    page.update()
    
ft.app(target=main)