from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.post("/reset")
def reset():
    return {
        "observation": {},
        "reward": 0.0,
        "done": False,
        "info": {}
    }

@app.post("/step")
def step(action: dict):
    return {
        "observation": {},
        "reward": 0.5,
        "done": False,
        "info": {}
    }

@app.get("/state")
def state():
    return {"state": "ok"}

@app.get("/")
def root():
    return {"status": "running"}

def main():
    uvicorn.run(app, host="0.0.0.0", port=7860)

# ✅ THIS LINE WAS MISSING
if __name__ == "__main__":
    main()
    