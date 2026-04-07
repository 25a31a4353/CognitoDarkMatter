from fastapi import FastAPI
from my_env_environment import MyEnvironment

app = FastAPI()

env = MyEnvironment()

@app.get("/")
def root():
    return {"message": "Hello"}   # 🔥 CHANGE THIS LINE

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(action: dict):
    return env.step(action)