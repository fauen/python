import streamlit as st

def main():
    st.title("Home")
    st.button(label="Up", on_click=st.balloons)
    st.button(label="Frozen", on_click=st.snow)

    st.sidebar.title("Sidebar")

main()

if __name__ == "__main__":
    main()
