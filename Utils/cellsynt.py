import requests as r

url = "https://se-1.cellsynt.net/sms.php?"
username = input("Input username: ")
password = input("Input password: ")
number = input("Input number (format 0046....): ")
text = input("Input SMS text: ")
data = [('username', username), ('password', password), ('destination', number), ('originatortype', 'alpha'), ('originator', 'BookBeat IT'), ('charset', 'UTF-8'), ('text', text)]

urlpost = r.post(url, data=data)
print(urlpost.text)