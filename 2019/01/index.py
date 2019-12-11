#!/usr/bin/env python3

import os
from functions import fuel_calculator, fuel_calculator_part_two

current_dir = os.path.dirname(__file__)

def part_one():
    total_fuel = 0

    with open(os.path.join(current_dir, "input.txt"), "r") as masses:
        total_fuel = sum([fuel_calculator(int(mass)) for mass in masses])
    
    return total_fuel

def part_two():
    total_fuel = 0

    with open(os.path.join(current_dir, "input.txt"), "r") as masses:
        total_fuel = sum([fuel_calculator_part_two([int(mass)]) for mass in masses])
    
    return total_fuel

if __name__ == "__main__":
    print("part one's result is {}".format(part_one()))
    print("part two's result is {}".format(part_two()))
