def observe(step):
    observations = [30, 20]
    return observations[step]


def decide(temperature):
    if temperature > 25:
        return "TURN_ON_FAN"
    else:
        return "TURN_OFF_FAN"


def act(action):
    if action == "TURN_ON_FAN":
        return "Fan turned ON"
    elif action == "TURN_OFF_FAN":
        return "Fan turned OFF"
    else:
        return "Invalid action"


def agent(max_iters=2):

    log = []
    state = {
        "done": False,
        "steps": 0,
        "status": "RUNNING"
    }

    for step in range(max_iters):

        # OBSERVE
        temperature = observe(step)

        # DECIDE
        action = decide(temperature)

        # ACT
        result = act(action)

        # Update state
        state["steps"] += 1

        # Log the step
        log.append({
            "step": step + 1,
            "observation": temperature,
            "decision": action,
            "action_result": result
        })

    state["done"] = True
    state["status"] = "SUCCESS"

    return {
        "status": "SUCCESS",
        "state": state,
        "log": log
    }


# Run two-step agent
result = agent(max_iters=2)

print(result)