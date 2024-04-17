import flet as ft
import requests as r
from dotenv import load_dotenv
from os import getenv

load_dotenv('../.env')

def main(page: ft.Page) -> None:
    ...

if __name__ == "__main__":
    ft.app(target=main)