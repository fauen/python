import ollama
import keyboard

def main(prompt: str) -> None:
    client = ollama.Client()

    model = "llama3.2"
    prompt = prompt

    respone = client.generate(model=model, prompt=prompt)

    print("Response from Ollama:")
    print(respone.response)

if __name__ == "__main__":
    try:
        while True:
            prompt = input("\nWhat is thy bidding my mastah?\n")
            main(prompt)
    except KeyboardInterrupt:
        pass
