import requests
import os

API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")

def run():
    # Reset environment
    reset = requests.post(f"{API_BASE_URL}/reset")
    print("RESET:", reset.json())

    # Step call
    step = requests.post(f"{API_BASE_URL}/step", json={"action": "test"})
    print("STEP:", step.json())

if __name__ == "__main__":
    run()