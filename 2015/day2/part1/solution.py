def paper_calc(l, w, h, sorted):
    return 2 * l * w + 2 * w * h + 2 * h * l + (sorted[0] * sorted[1])

needed_paper = 0

with open("assignment.txt", "r") as f:
    for line in f.readlines():
        needed_paper += paper_calc(*[int(i) for i in line.split("x")], sorted([int(i) for i in line.split("x")]))
        
print(needed_paper)