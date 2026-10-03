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

    valid_actions = ["TURN_ON_FAN", "TURN_OFF_FAN"]

    # Validate action
    if action not in valid_actions:
        return {
            "status": "ERROR",
            "error": f"Invalid action: {action}"
        }

    if action == "TURN_ON_FAN":
        return {
            "status": "SUCCESS",
            "message": "Fan turned ON"
        }

    if action == "TURN_OFF_FAN":
        return {
            "status": "SUCCESS",
            "message": "Fan turned OFF"
        }


def agent(max_iters=10):

    state = {
        "done": False,
        "steps": 0,
        "status": "RUNNING"
    }

    log = []

    # Loop counter
    iteration = 0

    while iteration < max_iters:

        # FIX: increment iteration every loop
        iteration += 1

        try:
            # 1. OBSERVE
            temperature = observe()

            # 2. DECIDE
            action = decide(temperature)

            # 3. ACT
            result = act(action)

            # Handle invalid action
            if result["status"] == "ERROR":

                state["done"] = True
                state["status"] = "ERROR"

                log.append({
                    "step": iteration,
                    "observation": temperature,
                    "decision": action,
                    "status": "ERROR",
                    "error": result["error"]
                })

                return {
                    "status": "ERROR",
                    "error": result["error"],
                    "state": state,
                    "log": log
                }

            # Successful step
            state["steps"] += 1

            log.append({
                "step": iteration,
                "observation": temperature,
                "decision": action,
                "action_result": result["message"],
                "status": "SUCCESS"
            })

        except Exception as e:

            state["done"] = True
            state["status"] = "ERROR"

            log.append({
                "step": iteration,
                "status": "ERROR",
                "error": str(e)
            })

            return {
                "status": "ERROR",
                "error": str(e),
                "state": state,
                "log": log
            }

    # Maximum iterations completed
    state["done"] = True
    state["status"] = "SUCCESS"

    return {
        "status": "SUCCESS",
        "state": state,
        "log": log
    }


# Run the agent
result = agent(max_iters=10)

print("===== FINAL RESULT =====")
print(result)

print("\n===== FULL LOG =====")

for entry in result["log"]:
    print(entry)