with open("sets.csv", "rb") as file:
    lines = file.readlines()

data = b""
for i in range(0, len(lines)):
    if i == 0:
        data += b"checked,is_technic,is_electric,"
    else:
        data += b"0,0,0,"
    data += lines[i]

with open("sets.txt", "wb") as file:
    file.write(data)

print("Done!")
