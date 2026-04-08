from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    title="CognitoDarkMatter API",
    version="1.0.0"
)

# ✅ CORS (keep this)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------
# Request Model
# -------------------------------
class StepInput(BaseModel):
    action: str


# -------------------------------
# Root Endpoint
# -------------------------------
@app.get("/")
def root():
    return {"message": "CognitoDarkMatter is running"}


# -------------------------------
# Health Check
# -------------------------------
@app.get("/health")
def health():
    return {"status": "ok"}


# -------------------------------
# Reset Endpoint (CRITICAL 🔥)
# -------------------------------
@app.post("/reset")
def reset():
    return {
        "observation": "environment reset",
        "reward": 0,
        "done": False
    }


# -------------------------------
# Step Endpoint (CRITICAL 🔥)
# -------------------------------
@app.post("/step")
def step(input_data: StepInput):
    return {
        "observation": f"action received: {input_data.action}",
        "reward": 1,
        "done": False
    }