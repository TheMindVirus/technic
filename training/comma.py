with open("sets.txt", "rb") as file:
    lines = file.read()

data = b""
i = 0
for line in lines.split(b"\n"):
    data += line
    if i != 0 and line[len(line)-1:] != b",":
        data += b","
    data += b"\n"
    i += 1

with open("sets.txt", "wb") as file:
    file.write(data)

print("Done!")
