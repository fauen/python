import streamlit as st
import requests as r
from dotenv import load_dotenv
from os import getenv
from sys import argv
from getpass import getpass as gp

load_dotenv('.env')

colors: tuple = ("red", "green", "yellow", "blue", "white", "cyan", "magenta")
patterns: tuple = ("police", "traffic lights", "random 1", "random 2", "random 3", "random 4", "random 5", "rainbow", "sea", "white wave", "synthetic")

def luxafor_color(color: str = "red") -> None:
    hook = getenv('hook')
    url = "https://api.luxafor.com/webhook/v1/actions/solid_color"
    body = {
            'userId': hook,
            'actionFields': {
                'color': color
                }
            }
    r.post(url=url, json=body)

def luxafor_pattern(pattern: str = 'police') -> None:
    hook = getenv('hook')
    url = "https://api.luxafor.com/webhook/v1/actions/pattern"
    body = {
            'userId': hook,
            'actionFields': {
                'pattern': pattern
                }
            }
    r.post(url=url, json=body)

def main():
    st.title("Tools")
    col1, col2 = st.columns(2)
    with col1:
        st.header("Colors")
        luxafor_input = st.button("Red", on_click=luxafor_color, args=["red"])
        luxafor_input = st.button("Green", on_click=luxafor_color, args=["green"])
        luxafor_input = st.button("Yellow", on_click=luxafor_color, args=["yellow"])
        luxafor_input = st.button("Blue", on_click=luxafor_color, args=["blue"])
        luxafor_input = st.button("White", on_click=luxafor_color, args=["white"])
        luxafor_input = st.button("Cyan", on_click=luxafor_color, args=["cyan"])
        luxafor_input = st.button("Magenta", on_click=luxafor_color, args=["magenta"])

    with col2:
        st.header("Patterns")
        luxafor_input = st.button("Police", on_click=luxafor_pattern, args=["police"])
        luxafor_input = st.button("Traffic lights", on_click=luxafor_pattern, args=["traffic lights"])
        luxafor_input = st.button("Rainbow", on_click=luxafor_pattern, args=["rainbow"])
        luxafor_input = st.button("Sea", on_click=luxafor_pattern, args=["sea"])
        luxafor_input = st.button("White wave", on_click=luxafor_pattern, args=["white wave"])
        luxafor_input = st.button("Synthetic", on_click=luxafor_pattern, args=["synthetic"])

main()
