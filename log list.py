import random


def observe():
    """Observe the environment."""
    temperature = random.randint(15, 35)
    return temperature


def decide(temperature):
    """Decide what action to take."""
    if temperature > 25:
        return "TURN_ON_FAN"
    else:
        return "TURN_OFF_FAN"


def act(action):
    """Execute the selected action."""

    # Simulate possible failure
    if random.random() < 0.1:
        raise Exception("Action execution failed")

    if action == "TURN_ON_FAN":
        return "Fan turned ON"

    elif action == "TURN_OFF_FAN":
        return "Fan turned OFF"

    else:
        raise Exception("Unknown action")


def agent(max_iters=10):

    # State dictionary
    state = {
        "done": False,
        "steps": 0,
        "status": "RUNNING"
    }

    # List to store every step
    log = []

    for i in range(max_iters):

        step_number = i + 1

        try:
            # 1. OBSERVE
            temperature = observe()

            # 2. DECIDE
            action = decide(temperature)

            # 3. ACT
            result = act(action)

            # Update state
            state["steps"] += 1

            # Log successful step
            log.append({
                "step": step_number,
                "observation": temperature,
                "decision": action,
                "action_result": result,
                "status": "SUCCESS"
            })

        except Exception as e:

            # Update failure state
            state["done"] = True
            state["status"] = "FAILURE"

            # Log failed step
            log.append({
                "step": step_number,
                "status": "FAILURE",
                "error": str(e)
            })

            return {
                "status": "FAILURE",
                "state": state,
                "log": log
            }

    # Agent completed successfully
    state["done"] = True
    state["status"] = "SUCCESS"

    return {
        "status": "SUCCESS",
        "state": state,
        "log": log
    }


# Run the agent
result = agent(max_iters=10)

# Display full log
print("\n===== FULL AGENT LOG =====")

for entry in result["log"]:
    print(entry)

print("\n===== FINAL RESULT =====")
print(result)