import requests as r
import json

def main(question: str) -> None:
    url = "http://localhost:11434/api/chat"
    payload = {
            "model": "llama3.2",
            "messages": [{"role": "user", "content": question}]
            }

    response  = r.post(url, json=payload, stream=True)

    if response.status_code == 200:
        print("Streaming response from Ollama:")
        for line in response.iter_lines(decode_unicode=True):
            if line:
                try:
                    json_data = json.loads(line)
                    if "message" in json_data and "content" in json_data["message"]:
                        print(json_data["message"]["content"], end="")
                except json.JSONDecodeError:
                    print(f"\nFailed to parse line: {line}")
        print()
    else:
        print(f"Error: {response.status_code}")
        print(response.text)


if __name__ == "__main__":
    question = input("What do you want to ask?\n")
    main(question)
