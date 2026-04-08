from fastapi import FastAPI

app = FastAPI()

@app.post("/reset")
def reset():
    return {
        "observation": {"state": "reset"},
        "reward": 0.0,
        "done": False,
        "info": {}
    }

@app.post("/step")
def step(action: dict):
    return {
        "observation": {"state": "next"},
        "reward": 0.5,
        "done": False,
        "info": {}
    }

@app.get("/state")
def state():
    return {
        "state": "current_state"
    }

@app.get("/")
def root():
    return {"status": "running"}