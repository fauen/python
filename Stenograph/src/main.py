def encode_message() -> None:
    message = input("Input message: ")
    image = input("Input file: ")
    with open(image, "ab") as f:
        f.write(message.encode('utf8'))

def decode_message() -> None:
    image = input("Input file: ")
    with open(image, "rb") as f:
        for chunk in iter(lambda: f.read(8), b''):
            print(chunk.decode('utf-8', errors='ignore'), end="")

def main() -> None:
    question = input("[E]ncode or [D]ecode? ")
    if question.lower() == 'e': 
        encode_message()
    elif question.lower() == 'd':
        decode_message()
    else:
        print("You need to specify E or D...")

if __name__ == "__main__":
    main()
