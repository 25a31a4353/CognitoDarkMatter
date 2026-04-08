from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Any, Dict

app = FastAPI(
    title="CognitoDarkMatter API",
    version="1.0.0"
)

# Enable CORS (important for HF)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------
# ENVIRONMENT STATE (GLOBAL)
# -------------------------------
env_state = {
    "step_count": 0,
    "last_action": None,
    "history": []
}

# -------------------------------
# REQUEST MODEL
# -------------------------------
class ActionInput(BaseModel):
    action: Any


# -------------------------------
# ROOT
# -------------------------------
@app.get("/")
def root():
    return {"status": "ok"}


# -------------------------------
# HEALTH
# -------------------------------
@app.get("/health")
def health():
    return {"status": "ok"}


# -------------------------------
# RESET (REQUIRED)
# -------------------------------
@app.post("/reset")
def reset():
    global env_state

    env_state = {
        "step_count": 0,
        "last_action": None,
        "history": []
    }

    return {
        "observation": "Environment reset successfully",
        "reward": 0.0,
        "done": False,
        "info": {}
    }


# -------------------------------
# STEP (REQUIRED)
# -------------------------------
@app.post("/step")
def step(input_data: ActionInput):
    global env_state

    action = input_data.action

    env_state["step_count"] += 1
    env_state["last_action"] = action
    env_state["history"].append(action)

    # Simple intelligent reward logic
    if isinstance(action, str) and "assumption" in action.lower():
        reward = 1.0
    else:
        reward = 0.2

    done = env_state["step_count"] >= 5

    return {
        "observation": f"Processed action: {action}",
        "reward": reward,
        "done": done,
        "info": {
            "step_count": env_state["step_count"]
        }
    }


# -------------------------------
# STATE (VERY IMPORTANT)
# -------------------------------
@app.get("/state")
def state():
    global env_state

    return {
        "state": env_state
    }