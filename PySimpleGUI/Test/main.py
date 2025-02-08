import PySimpleGUI as sg
import ollama

def llama(prompt: str) -> str:
    client = ollama.Client()
    model = "llama3.2"
    prompt = prompt
    response = client.chat(model, prompt)
    return response.response

def main():
    layout = [
            [sg.Text("Chat with llama")],
            [sg.InputText()],
            [sg.Button("Send"), sg.Button("Cancel")],
            [sg.Output(size=(50,50))]
            ]

    window = sg.Window('llama client', layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Cancel":
            break

        #print('Hello', values[0], '!')
        prompt = values[0]
        response = llama(prompt)
        print(response)
        print(event)

    window.close

if __name__ == "__main__":
    main()
