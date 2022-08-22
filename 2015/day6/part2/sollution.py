class Light:
    def __init__(self):
        self.brightness = 0

    def toggle(self):
        self.brightness += 2

    def turn_on(self):
        self.brightness += 1

    def turn_off(self):
        if self.brightness > 0:
            self.brightness -= 1
        

with open("assignment.txt", "r") as data:
    assignment = [[int(item) for item in line.strip().split(",")] for line in data.readlines()]

total_brightness = 0
light_raster = [[Light() for x in range(1001)] for y in range(1001)]

for step in assignment:
    action = step[0]
    starting_location = (step[1], step[2])
    ending_location = (step[3] + 1, step[4] + 1)

    for light_line in light_raster[starting_location[0] : ending_location[0]]:
        for light in light_line[starting_location[1] : ending_location[1]]:
            if action == 0:
                light.turn_off()
            elif action == 1:
                light.turn_on()
            else:
                light.toggle()

for light_line in light_raster:
    for light in light_line:
        total_brightness += light.brightness

print(total_brightness)