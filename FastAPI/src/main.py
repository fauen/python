from fastapi import FastAPI
import requests as r

api = FastAPI()

@api.get('/')
def page():
    return {"message": "Hello, World!"}

@api.get('/api/greet/')
def greet():
    return {"message": "Hello!"}

@api.get('/api/greet/{name}')
def greet_person(name: str):
    return {"message": f"Hello there {name}!"}

@api.get('/api/weather/{location}')
def weather(location: str):
    url = f"https://wttr.in/{location}"
    response = r.get(url = url)
    return response.text


#if __name__ == "__main__":
#    uvicorn.run(app, host="127.0.0.1", port=8000)
