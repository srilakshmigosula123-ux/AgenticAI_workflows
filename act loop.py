import random
import time

# Observe → Decide → Act loop
while True:

    # 1. OBSERVE
    temperature = random.randint(15, 35)
    print(f"\nObserved Temperature: {temperature}°C")

    # 2. DECIDE
    if temperature > 25:
        decision = "Turn ON fan"
    else:
        decision = "Turn OFF fan"

    print(f"Decision: {decision}")

    # 3. ACT
    if decision == "Turn ON fan":
        print("Action: Fan is ON")
    else:
        print("Action: Fan is OFF")

    # Wait before next observation
    time.sleep(2)