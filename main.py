from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="CognitoDarkMatter API",
    version="1.0.0"
)

# ✅ CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Root
@app.get("/")
def root():
    return {"status": "ok"}

# ✅ Health
@app.get("/health")
def health():
    return {"status": "ok"}

# ✅ REQUIRED: RESET ENDPOINT
@app.post("/reset")
def reset():
    return {
        "observation": "environment reset",
        "reward": 0,
        "done": False
    }

# ✅ REQUIRED: STEP ENDPOINT
@app.post("/step")
def step(action: dict):
    return {
        "observation": f"action received: {action}",
        "reward": 1,
        "done": False
    }