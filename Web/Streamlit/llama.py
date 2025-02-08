import streamlit as st
import ollama
import time

def llama_client(prompt: str) -> str:
    client = ollama.Client()
    model = "llama3.2"
    prompt = prompt
    response = client.generate(model, prompt)
    return response.response

def llama_stream(prompt: str) -> str:
    user_input = ollama.chat(
            model="llama3.2",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ]
        )
    response = user_input["message"]["content"]
    return response

def response_stream(response):
    for word in response.split():
        yield word + " "
        time.sleep(0.02)

def main():
    st.title("Llama 3.2")
    #with st.form(key="llama", clear_on_submit=True, enter_to_submit=True, border=True):
        #prompt = st.text_input("Chat with the llama: ")
        #st.form_submit_button(label="Send")
        #if prompt:
            #st.write(botter(prompt))

    prompt = st.chat_input("Message the llama")
    # if prompt:
        # st.write(prompt)
        # with st.spinner("Thinking about it...", show_time=True):
            # st.write(llama_client(prompt))

    if prompt:
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("ai"):
            #response = llama_stream(prompt)
            #st.write_stream(response_stream(response))
            st.write(llama_client(prompt))

main()

if __name__ == "__main__":
    main()
