import streamlit as st
import requests as r
import ollama

def weather(city: str) -> str:
    url = f"https://wttr.in/{city}?format=3"
    response = r.get(url)
    return response.text

def botter(question: str) -> str:
    client = ollama.Client()
    model = "llama3.2"
    prompt = question
    response = client.generate(model, prompt)
    return response.response

def main():
    st.write(weather("Stockholm"))

    st.title("Title")
    st.header("Header")
    st.subheader("Subheader")
    st.write({"key": "value"})
    st.write({"numbers": [0, 1, 2, 3, 4]})
    st.write([0, 1, 2, 3, 4])

    st.sidebar.title("Sidebar!")
    st.sidebar.link_button(label="SL", url="https://sl.se")
    question = st.sidebar.text_input(label="Question for our overlords")
    st.sidebar.write(botter(question))
    
    
    with st.form(key="weather", clear_on_submit=True, enter_to_submit=False, border=True):
        city_name = st.text_input("City name: ")
        st.form_submit_button(label="Submit")
        if city_name:
            st.write(weather(city_name))

def este():
    tools = st.Page(page="tools.py", title="Tools", icon=":material/construction:")
    links = st.Page(page="links.py", title="Links", icon=":material/link:")

    pg = st.navigation(pages=[tools, links])
    st.set_page_config(page_title="Daniel's abode", page_icon=":material/house:")
    pg.run()

if __name__ == "__main__":
    este()
