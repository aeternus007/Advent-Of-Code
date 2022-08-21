floor = 0

with open("assignment.txt", "r") as f:
    floor_instructions = f.read()

for instruction in floor_instructions:
    if instruction == ")":
        floor -= 1
    if instruction == "(":
        floor += 1
            
print(floor)