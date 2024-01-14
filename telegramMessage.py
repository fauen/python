def telegram_message(token, chatid, message):
    import requests as r
    message = r.post(url=f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chatid}&text={message}")
    return message

if __name__ == "__main__":
    import requests as r
    telegram_token = input("Input token: ")
    telegram_chatid = input("Input chat id: ")
    telegram_text = input("Input message: ")
    telegram_message(telegram_token, telegram_chatid, telegram_text)