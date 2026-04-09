import urllib.request
import json
import time

BASE_URL = "http://localhost:7860"

def post_request(endpoint, data=None):
    try:
        url = BASE_URL + endpoint
        headers = {"Content-Type": "application/json"}

        if data is not None:
            data = json.dumps(data).encode("utf-8")

        req = urllib.request.Request(url, data=data, headers=headers, method="POST")
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode())
    except Exception as e:
        print("POST ERROR:", e)
        return None


def get_request(endpoint):
    try:
        url = BASE_URL + endpoint
        with urllib.request.urlopen(url) as response:
            return json.loads(response.read().decode())
    except Exception as e:
        print("GET ERROR:", e)
        return None


def run_task():
    print("Running inference...")

    # reset environment
    res = post_request("/reset")
    print("Reset:", res)

    total_reward = 0

    for step in range(3):
        action = {"action": "move"}
        res = post_request("/step", action)

        if res is None:
            break

        reward = res.get("reward", 0)
        total_reward += reward

        print(f"Step {step}: reward={reward}")

        if res.get("done"):
            break

    state = get_request("/state")
    print("Final State:", state)

    return total_reward


if __name__ == "__main__":
    try:
        score = run_task()
        print("FINAL SCORE:", score)
    except Exception as e:
        print("Inference failed safely:", e)