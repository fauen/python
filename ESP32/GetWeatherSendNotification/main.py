from machine import Pin
from time import sleep
import urequests as r
import asyncio
import network
import json


def led_light(led_value: int):
    led = Pin(2, Pin.OUT)
    led.value(led_value)

async def wifi_setup():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    with open("ssid.json") as f:
        config = json.load(f)
    if not wlan.isconnected():
        print("Connecting to network...")
        for key, value in config.items():
            try:
                wlan.connect(key, value)
            except:
                pass
        while not wlan.isconnected():
            pass
    print("Network config:", wlan.ifconfig())
    

async def get_weather():
    print("Getting weather...")
    response = r.get(url="https://wttr.in/?format=3")
    return response

async def telegram_message():
    print("Sending message...")
    token = ""
    chatid = ""
    msg = "ESP32 online"
    response = r.post(url=f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chatid}&text={msg}")
    return response
    
async def main():
    led_light(1)
    netnet = wifi_setup()
    net_connect = await netnet
    weather_resp = get_weather()
    weather = await weather_resp
    print(weather.text)
    telegram_resp = telegram_message()
    telegram = await telegram_resp
    led_light(0)

asyncio.run(main())
