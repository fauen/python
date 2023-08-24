import base64

def base64_encode():
    user_bytes = user_input.encode("ascii")
    base64_bytes = base64.b64encode(user_bytes)
    base64_output = base64_bytes.decode("ascii")
    print(f"\nEncoded string: {base64_output}")

def base64_decode():
    user_bytes = user_input.encode("ascii")
    base64_bytes = base64.b64decode(user_bytes)
    base64_output = base64_bytes.decode("ascii")
    print(f"Decoded string: {base64_output}")

user_input = input("Input the string: ")
user_choice = input("[E]ncode or [D]ecode? ")
if user_choice.upper() == "E":
    encode_done = base64_encode()
elif user_choice.upper() == "D":
    decode_done = base64_decode()
else:
    print("E or D")
    quit
