floor = 0
position = 1

with open("assignment.txt", "r") as f:
    floor_instructions = f.read()
    
for instruction in floor_instructions:
    if instruction == ")":
        floor -= 1
    if instruction == "(":
        floor += 1
    if floor == -1:
        print(position)
        break
    position += 1