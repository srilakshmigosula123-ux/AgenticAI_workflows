import random


def observe():
    """Observe the environment."""
    temperature = random.randint(15, 35)
    print(f"Observed: Temperature = {temperature}°C")
    return temperature


def decide(temperature):
    """Decide what action to take."""
    if temperature > 25:
        return "TURN_ON_FAN"
    else:
        return "TURN_OFF_FAN"


def act(action):
    """Execute the action."""
    
    # Simulate possible execution failure
    if random.random() < 0.1:
        raise Exception("Action execution failed")

    if action == "TURN_ON_FAN":
        print("Action: Fan turned ON")

    elif action == "TURN_OFF_FAN":
        print("Action: Fan turned OFF")

    else:
        raise Exception("Unknown action")


def agent(max_iters=10):

    # Agent state
    state = {
        "done": False,
        "steps": 0,
        "status": "RUNNING"
    }

    for i in range(max_iters):

        print(f"\n--- Step {i + 1} ---")

        try:
            # 1. OBSERVE
            temperature = observe()

            # 2. DECIDE
            action = decide(temperature)
            print(f"Decision: {action}")

            # 3. ACT
            act(action)

            # Update step count
            state["steps"] += 1

        except Exception as e:

            # Failure state
            state["done"] = True
            state["status"] = "FAILURE"

            return {
                "status": "FAILURE",
                "message": str(e),
                "state": state
            }

    # Success state
    state["done"] = True
    state["status"] = "SUCCESS"

    return {
        "status": "SUCCESS",
        "message": "Agent completed successfully",
        "state": state
    }


# Run the agent
result = agent(max_iters=10)

print("\nFinal Result:")
print(result)