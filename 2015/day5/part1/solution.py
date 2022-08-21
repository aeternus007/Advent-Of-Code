import re

with open("assignment.txt", "r") as f:
    words = f.readlines()

print(len([word for word in words if (re.search(r'([aeiou].*){3,}', word) and re.search(r'(.)\1', word) and not re.search(r'ab|cd|pq|xy', word))]))