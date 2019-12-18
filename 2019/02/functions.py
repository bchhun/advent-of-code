#!/usr/bin/env python3

import math

def divide_chunks(elements, size):
    for x in range(0, len(elements), size):
        yield elements[x:x + size]

opcode_role_index = {
    "opcode": 0,
    "x": 1,
    "y": 2,
    "where": 3
}

opcode_functions = {
    1: lambda x, y: x + y,
    2: lambda x, y: x * y
}

def getOpcodeResult(operation_codes, is_test_run = False):
    operation_codes_list = [
        int(code) for code in operation_codes.split(",")
    ]
    current_index = 0
    operation_codes_limit = math.ceil(len(operation_codes_list) / 4)

    while True:
        if is_test_run:
            print("current_index", current_index)

        opcode = operation_codes_list[
            (current_index * 4) + opcode_role_index.get("opcode")
        ]

        if is_test_run:
            print("opcode", opcode)

        if opcode == 99:
            return ",".join(str(code) for code in operation_codes_list) 

        if not opcode in opcode_functions.keys():
            raise Exception("unexistent opcode")
        
        x = operation_codes_list[
            (current_index * 4) + opcode_role_index.get("x")
        ]

        y = operation_codes_list[
            (current_index * 4) + opcode_role_index.get("y")
        ]

        where = operation_codes_list[
            (current_index * 4) + opcode_role_index.get("where")
        ]

        if is_test_run:
            print("x", x, "y", y, "where", where)

        operation_codes_list[where] = opcode_functions[opcode](
            operation_codes_list[x], 
            operation_codes_list[y]
        )

        if is_test_run:
            print(operation_codes_list)

        if current_index >= operation_codes_limit:
            return ",".join(str(code) for code in operation_codes_list) 

        current_index += 1


if __name__ == "__main__":
    result = getOpcodeResult("1,1,1,4,99,5,6,0,99")
    print(result)
