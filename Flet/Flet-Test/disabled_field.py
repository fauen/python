import flet as ft

def main(page):
    first_name = ft.TextField(label="First name", autofocus=True)
    last_name = ft.TextField(label="Last name")
    first_name.disabled = False
    last_name.disabled = True
    page.add(first_name, last_name)

ft.app(target=main)