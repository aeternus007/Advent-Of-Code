houses = {(0, 0): 1}

santa = {"x": 0, "y": 0}

with open("assignment.txt", "r") as f:
    data = f.read()

for command in data:
    if command == "v":
        santa["y"] -= 1
    if command == "^":
        santa["y"] += 1
    if command == "<":
        santa["x"] -= 1
    if command == ">":
        santa["x"] += 1

    try:
        houses[(santa["x"], santa["y"])] += 1
    except:
        houses[(santa["x"], santa["y"])] = 1

print(len(houses.keys()))