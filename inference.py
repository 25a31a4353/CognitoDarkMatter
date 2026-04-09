import urllib.request
import json
import os
from openai import OpenAI

BASE_URL = "http://localhost:7860"

# ✅ LLM CLIENT (REQUIRED)
client = OpenAI(
    base_url=os.environ["API_BASE_URL"],
    api_key=os.environ["API_KEY"]
)


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


def call_llm(prompt):
    try:
        response = client.chat.completions.create(
            model=os.environ.get("MODEL_NAME", "gpt-4o-mini"),
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print("[LLM ERROR]", e, flush=True)
        return "default_action"


def run_task(task_name):
    print(f"[START] task={task_name}", flush=True)

    res = post_request("/reset")
    total_reward = 0
    steps = 0

    for i in range(3):
        # ✅ USE LLM TO DECIDE ACTION
        prompt = f"You are solving {task_name}. Give next action."
        action_text = call_llm(prompt)

        action = {"action": action_text}

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
        run_task("easy")
        run_task("medium")
        run_task("hard")
    except Exception as e:
        print("[FATAL ERROR]", e, flush=True)