from fastapi import FastAPI
import redis

app = FastAPI()
red = redis.Redis(host="redis", port=6379)

@app.get("/")
def read_root():
    return {"Hello": "World!", "Hello2": "There!"}

@app.get("/hits")
def read_root():
    red.incr("hits")
    return {"Number of hits": red.get("hits")}