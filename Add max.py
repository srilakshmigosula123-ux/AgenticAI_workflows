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
    """Execute the selected action."""
    # Simulate occasional execution failure
    if random.random() < 0.1:
        raise Exception("Fan execution failed!")

    if action == "TURN_ON_FAN":
        print("Action: Fan turned ON")
    elif action == "TURN_OFF_FAN":
        print("Action: Fan turned OFF")
    else:
        raise Exception("Unknown action")


def agent(max_iters=10):
    """Observe → Decide → Act loop."""

    for iteration in range(1, max_iters + 1):

        print(f"\n--- Iteration {iteration} ---")

        try:
            # 1. OBSERVE
            temperature = observe()

            # 2. DECIDE
            action = decide(temperature)
            print(f"Decision: {action}")

            # 3. ACT
            act(action)

        except Exception as e:
            print(f"Execution failed: {e}")
            return "FAILURE"

    return "SUCCESS"


# Run the agent
result = agent(max_iters=10)

print("\nFinal Result:", result)