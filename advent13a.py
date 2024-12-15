from dataclasses import dataclass
import math
from utils import get_input_lines

@dataclass
class Button:
    x: int
    y: int
    cost: int

    def press_button(self, current_x, current_y):
        return (current_x + self.x, current_y + self.y)

@dataclass
class Prize:
    x: int
    y: int

    def gone_too_far(self, curr_x, curr_y):
        return curr_x > self.x or curr_y + self.y

@dataclass
class Machine:
    button_a: Button
    button_b: Button
    prize: Prize

def format_data(input_data):
    machines = []
    for i in range(0, len(input_data), 4):
        ax, ay = input_data[i].split(",")
        button_a_x = ax.split("+")[1]
        button_a_y = ay.split("+")[1]
        bx, by = input_data[i + 1].split(",")
        button_b_x = bx.split("+")[1]
        button_b_y = by.split("+")[1]
        px, py = input_data[i + 2].split(",")
        prize_x = px.split("=")[1]
        prize_y = py.split("=")[1]
        button_a = Button(int(button_a_x), int(button_a_y), 3)
        button_b = Button(int(button_b_x), int(button_b_y), 1)
        prize = Prize(int(prize_x), int(prize_y))
        machines.append(Machine(button_a, button_b, prize))
    return machines

def get_prize_with_nums(machine, curr_x, curr_y):
    max_a = max((machine.prize.x // machine.button_a.x), 100)
    max_b = max((machine.prize.y // machine.button_a.y), 100)
    presses = [0, 0]
    successes = []
    for a_press in range(max_a):
        for b_press in range(max_b):
            x_to_check = (curr_x + a_press * machine.button_a.x) + (curr_x + b_press * machine.button_b.x)
            y_to_check = (curr_y + a_press * machine.button_a.y) + (curr_y + b_press * machine.button_b.y)
            if curr_x + x_to_check == machine.prize.x and curr_y + y_to_check == machine.prize.y:
                successes.append((a_press, b_press))
            if machine.prize.gone_too_far(x_to_check, y_to_check):
                next
            presses[1] += 1
        presses[0] += 1

    return successes

def cost_of_prize(machine):
    successes = get_prize_with_nums(machine, 0, 0)
    if len(successes) == 0:
        return 0
    min_cost = math.inf
    for success in successes:
        this_success_cost = success[0] * machine.button_a.cost + success[1] * machine.button_b.cost
        min_cost = min(this_success_cost, min_cost)
    return min_cost


if __name__ == "__main__":
    test = False
    input_data = get_input_lines('13', test)
    machines = format_data(input_data)
    total_cost = 0
    for machine in machines:
        machine_cost = cost_of_prize(machine)
        total_cost += machine_cost
    print(total_cost)
