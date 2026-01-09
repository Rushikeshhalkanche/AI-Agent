import json
import os
from tools import calculator
from evaluator import evaluate_run

MEMORY_FILE = "memory.json"
LOG_FILE = "run_logs.txt"


class TaskAssistantAgent:
    def __init__(self):
        self.memory = self.load_memory()

    def load_memory(self):
        if not os.path.exists(MEMORY_FILE):
            return {"rules": [], "mistakes": {}}
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)

    def save_memory(self):
        with open(MEMORY_FILE, "w") as f:
            json.dump(self.memory, f, indent=2)

    def log(self, text):
        with open(LOG_FILE, "a") as f:
            f.write(text + "\n")

    def should_use_calculator(self):
        return "ALWAYS_USE_CALCULATOR_FIRST" in self.memory["rules"]

    def update_memory(self, mistake_type):
        self.memory["mistakes"].setdefault(mistake_type, 0)
        self.memory["mistakes"][mistake_type] += 1

        if mistake_type == "SKIPPED_REQUIRED_TOOL" and \
           self.memory["mistakes"][mistake_type] >= 2:
            if "ALWAYS_USE_CALCULATOR_FIRST" not in self.memory["rules"]:
                self.memory["rules"].append("ALWAYS_USE_CALCULATOR_FIRST")

        self.save_memory()

    def run(self, question, expression, correct_value):
        self.log("---- NEW RUN ----")
        self.log(f"Question: {question}")

        used_calculator = False
        answered_early = False

        # Early mistake behavior
        if not self.should_use_calculator():
            answer = correct_value + 5  # intentionally wrong
            answered_early = True
            self.log(f"Agent answered early: {answer}")
        else:
            used_calculator = True
            result = calculator(expression)
            answer = result
            self.log(f"Calculator used: {result}")

        correct_answer = (answer == correct_value)

        success, status = evaluate_run(
            used_calculator,
            answered_early,
            correct_answer
        )

        self.log(f"Evaluation: {status}")

        if not success:
            self.update_memory(status)

        self.log(f"Memory now: {self.memory}")
        self.log("-----------------\n")

        return answer, success


if __name__ == "__main__":
    agent = TaskAssistantAgent()

    question = "What is (12 * 4) + 8?"
    expression = "(12 * 4) + 8"
    correct_value = 56

    for i in range(5):
        print(f"\nRun {i+1}")
        ans, success = agent.run(question, expression, correct_value)
        print("Answer:", ans, "| Success:", success)
