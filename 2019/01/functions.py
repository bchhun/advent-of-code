#!/usr/bin/env python3

import math

def fuel_calculator(mass):
    fuel = math.floor(mass / 3) - 2

    return fuel

def fuel_calculator_part_two(fuel_array):
    current_needed_fuel = fuel_calculator(fuel_array[-1])

    if current_needed_fuel <= 0:
        if len(fuel_array) > 1:
            fuel_array.pop(0)
        return sum(fuel_array)

    fuel_array.append(current_needed_fuel)
    return fuel_calculator_part_two(fuel_array)
    