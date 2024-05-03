import asyncio
import requests

async def get_weather(location: str):
    print("Getting weather")
    response = requests.get(f"https://wttr.in/{location}")
    return response

async def main():
    location = input("Input location: ")
    weather = get_weather(location)
    result = await weather
    print(result.text)
    
if __name__ == "__main__":
    asyncio.run(main())