import streamlit as st

def main():
    home = st.Page(page="home.py", title="Home", icon=":material/house:")
    tools = st.Page(page="tools.py", title="Tools", icon=":material/construction:")
    links = st.Page(page="links.py", title="Links", icon=":material/link:")
    llama = st.Page(page="llama.py", title="llama", icon=":material/robot:")
    demo = st.Page(page="demo.py", title="Demo", icon=":material/school:")

    pg = st.navigation(pages=[home, tools, links, llama, demo], expanded=False)
    st.set_page_config(page_title="Daniel's abode", page_icon=":material/house:")
    pg.run()

if __name__ == "__main__":
    main()
