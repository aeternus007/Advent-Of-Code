from hashlib import md5

with open("assignment.txt") as data:
    assignment = data.read().strip()

hashed = ""
count = 0

while not hashed.startswith("00000"):
    to_hash = assignment + str(count)
    hashed = md5(to_hash.encode()).hexdigest()
    count += 1

print(count - 1)

"bgvyzdsv"