def password_generator(len, letters=True, digits=True):
    import string
    import random
    
    letters = string.ascii_letters
    digits = string.digits
    #special = string.punctuation
    #pass_list = letters + digits
    #pass_list = letters + digits + special
    
    password = ''
    for i in range(len):
        password += random.choice(letters)
        password += random.choice(digits)
    return password

if __name__ == "__main__":
    pass_len = int(input("Input password length: "))
    generator = password_generator(pass_len)
    print(generator)