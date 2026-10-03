import random


def observe():
    """Observe the environment."""
    temperature = random.randint(15, 35)
    print(f"Observed Temperature: {temperature}°C")
    return temperature


def decide(temperature):
    """Decide what action to take."""
    if temperature > 25:
        return "TURN_ON_FAN"
    else:
        return "TURN_OFF_FAN"


def act(action):
    """Perform the selected action."""
    if random.random() < 0.1:
        raise Exception("Action execution failed!")

    if action == "TURN_ON_FAN":
        print("Action: Fan turned ON")
    elif action == "TURN_OFF_FAN":
        print("Action: Fan turned OFF")


def agent(max_iters=10):
    # State dictionary
    state = {
        "done": False,
        "steps": 0
    }

    for iteration in range(max_iters):

        print(f"\n--- Iteration {iteration + 1} ---")

        try:
            # OBSERVE
            temperature = observe()

            # DECIDE
            action = decide(temperature)
            print(f"Decision: {action}")

            # ACT
            act(action)

            # Update state
            state["steps"] += 1

        except Exception as e:
            print(f"Execution failed: {e}")
            state["done"] = True
            return {
                "status": "FAILURE",
                "state": state
            }

    # Maximum iterations completed
    state["done"] = True

    return {
        "status": "SUCCESS",
        "state": state
    }


# Run the agent
result = agent(max_iters=10)

print("\nFinal Result:")
print(result)