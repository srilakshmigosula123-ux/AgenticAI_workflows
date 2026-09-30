def rule_based_agent(temperature):
    if temperature > 100:
        return "cool"
    else:
        return "idle"

temperature = [80, 100, 101, 120]
for temp in temperature:
    action = rule_based_agent(temp)
    print("Temperature: {temp}")
    print("Agent action: {action}")
    print("-" * 30)

