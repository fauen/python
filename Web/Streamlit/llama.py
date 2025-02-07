import streamlit as st

def botter(question: str) -> str:
    client = ollama.Client()
    model = "llama3.2"
    prompt = question
    response = client.generate(model, prompt)
    return response.response

def main():
    st.chat_input(label="Question for our overlords", key="text")
    question = st.session_state.get('something', '')
    if question:
        st.write(f"Prompt: {question}")
        st.write(botter(question))

main()

if __name__ == "__main__":
    main()
