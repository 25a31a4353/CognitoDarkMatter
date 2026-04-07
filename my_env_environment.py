class MyEnvironment:
    def __init__(self):
        self.step_count = 0

    def reset(self):
        self.step_count = 0
        return {
            "observation": "reset done",
            "reward": 0,
            "done": False
        }

    def step(self, action):
        self.step_count += 1

        return {
            "observation": f"step {self.step_count}",
            "reward": 1,
            "done": self.step_count >= 5
        }