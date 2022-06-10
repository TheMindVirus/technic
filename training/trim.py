with open("sets.txt", "rb") as file:
    lines = file.readlines()

data = b""
data += lines[0]
errored = False
for i in range(1, len(lines)):
    try:
        tokens = lines[i].split(b",")
        checked = tokens[0]
        technic = tokens[1]
        electric = tokens[2]
        if checked == b"1" and technic == b"1" and electric == b"1":
            data += lines[i]
    except Exception as error:
        print(error)
        errored = True
        break

if not errored:
    with open("sets.min.txt", "wb") as file:
        file.write(data)

print("Done!")
