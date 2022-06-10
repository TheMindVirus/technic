with open("sets.txt", "rb") as file:
    lines = file.readlines()

data = b""
total = 0
checked = 0
for i in range(0, len(lines)):
    if i != 0:
        total += 1
        if chr(lines[i][0]) != "0":
            checked += 1
        #else:
        #    print(lines[i])
percent = (checked / total) * 100

print("Progress:", "{}/{}".format(checked, total), "({:.02f}%)".format(percent))
