from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
def page():
    return {"message": "Main page..."}

@app.get('/api/greet')
def greet():
    return {"message": "Hello there!"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
