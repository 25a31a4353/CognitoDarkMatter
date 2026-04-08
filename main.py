from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="CognitoDarkMatter API",
    version="1.0.0"
)

# ✅ CORS (important for HF + browser access)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Root endpoint (must exist)
@app.get("/")
def root():
    return {"status": "ok"}

# ✅ Health check (VERY IMPORTANT for Hugging Face)
@app.get("/health")
def health():
    return {"status": "ok"}

# ✅ Example API (optional but good for demo)
@app.get("/hello")
def say_hello():
    return {"message": "Hello from CognitoDarkMatter 🚀"}