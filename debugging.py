def total_steps(steps):
    return sum(steps)


def average_steps(steps):
    return sum(steps) // len(steps)


def max_steps(steps):
    return max(steps)


def min_steps(steps):
    return min(steps)


def goal_met(steps):
    result = []
    for day in steps:
        result.append(day >= 10000)
    return result


# Main program
user_input = input()

steps = list(map(int, user_input.split()))

total = total_steps(steps)
average = average_steps(steps)
highest = max_steps(steps)
lowest = min_steps(steps)
goals = goal_met(steps)

print("Total steps:", total)
print("Average daily steps:", average)
print("Highest steps in a day:", highest)
print("Lowest steps in a day:", lowest)
print("Goal met each day:", goals)