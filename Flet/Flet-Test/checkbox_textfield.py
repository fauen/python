import flet as ft

def main(page):
    def add_task(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        new_task.focus()
        new_task.update()

    new_task = ft.TextField(hint_text="Task description", width=300)
    page.add(ft.Row([new_task, ft.ElevatedButton("Add task", on_click=add_task)]))

ft.app(target=main)