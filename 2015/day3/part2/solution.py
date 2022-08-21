houses = {(0, 0): 2}
santa = {"x": 0, "y": 0}
robo = {"x": 0, "y": 0}
count = -1

with open("assignment.txt", "r") as f:
    data = f.read()

for command in data:
    count += 1
    if count % 2 == 0:
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
        
    else:
        if command == "v":
            robo["y"] -= 1
        if command == "^":
            robo["y"] += 1
        if command == "<":
            robo["x"] -= 1
        if command == ">":
            robo["x"] += 1
            
        try:
            houses[(robo["x"], robo["y"])] += 1
        except:
            houses[(robo["x"], robo["y"])] = 1

print(len(houses))