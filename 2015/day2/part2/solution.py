def lint_calc(sorted):
    return sorted[0] * 2 + sorted[1] * 2 + sorted[0] * sorted[1] * sorted[2]

needed_lint = 0

with open("assignment.txt", "r") as f:
    for line in f.readlines():
        needed_lint += lint_calc(sorted([int(i) for i in line.split("x")]))
        
print(needed_lint)