import streamlit as st

def main():
    home = st.Page(page="home.py", title="Home", icon=":material/house:")
    luxafor = st.Page(page="luxafor.py", title="Luxafor", icon=":material/light:")
    links = st.Page(page="links.py", title="Links", icon=":material/link:")
    #llama = st.Page(page="llama.py", title="llama", icon=":material/robot:")
    demo = st.Page(page="demo.py", title="Demo", icon=":material/school:")

    #pg = st.navigation(pages=[home, luxafor, links, llama, demo], expanded=False)
    pg = st.navigation(pages=[home, luxafor, links, demo], expanded=False)
    st.set_page_config(page_title="Daniel's abode", page_icon=":material/house:")
    pg.run()

if __name__ == "__main__":
    main()
