import urllib.request
import json

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
        print("[ERROR] POST:", e, flush=True)
        return None


def get_request(endpoint):
    try:
        url = BASE_URL + endpoint
        with urllib.request.urlopen(url) as response:
            return json.loads(response.read().decode())
    except Exception as e:
        print("[ERROR] GET:", e, flush=True)
        return None


def run_task(task_name):
    print(f"[START] task={task_name}", flush=True)

    res = post_request("/reset")
    total_reward = 0
    steps = 0

    for i in range(3):
        action = {"action": "move"}
        res = post_request("/step", action)

        if res is None:
            break

        reward = res.get("reward", 0)
        total_reward += reward
        steps += 1

        print(f"[STEP] step={steps} reward={reward}", flush=True)

        if res.get("done"):
            break

    print(f"[END] task={task_name} score={total_reward} steps={steps}", flush=True)


if __name__ == "__main__":
    try:
        # ✅ Run 3 tasks (IMPORTANT requirement)
        run_task("easy")
        run_task("medium")
        run_task("hard")
    except Exception as e:
        print("[FATAL ERROR]", e, flush=True)