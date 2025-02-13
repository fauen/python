import streamlit as st
import requests as r
import ollama
import time

def weather(city: str) -> str:
    while True:
        url = f"https://wttr.in/{city}?format=3"
        response = r.get(url)
        return response.text


def clear_text():
    st.session_state.something = st.session_state.text
    st.session_state.text = ''

def main():
    st.write(f"The page was loaded: ", time.asctime())
    st.title("Title")
    st.header("Header")
    st.subheader("Subheader")
    st.write({"key": "value"})
    st.write({"numbers": [0, 1, 2, 3, 4], "letters": ['A', 'B', 'C', 'D', 'E']})
    st.write([0, 1, 2, 3, 4])
    picture = st.camera_input("Smile")
    if picture:
        st.image(picture)
    audio = st.audio_input("Tjenis")
    if audio:
        st.audio(audio)

    st.sidebar.balloons()
    st.sidebar.title(f"Sidebar!\n {weather("Stockholm")}")
    st.sidebar.link_button(label="SL", url="https://sl.se")

    
    
    with st.form(key="weather", clear_on_submit=True, enter_to_submit=False, border=True):
        city_name = st.text_input("City name: ")
        st.form_submit_button(label="Submit")
        if city_name:
            st.write(weather(city_name))

main()

if __name__ == "__main__":
    main()
