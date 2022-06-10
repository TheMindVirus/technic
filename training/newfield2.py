with open("sets.txt", "rb") as file:
    lines = file.readlines()

def find_instance(data, query, n):
    index = -1
    start = 0
    try:
        if n > 1:
            start = find_instance(data, query, n - 1)
        index = data.find(query, start + 1) + 1
    except:
        index = -1
    return index

data = b""
for i in range(0, len(lines)):
    if i == 0:
        data += b"checked,is_technic,is_electric,is_train,set_num,name,year,theme_id,num_parts,comment\n"
    else:
        pos = find_instance(lines[i], b",", 3)
        data += lines[i][:pos]
        data += b"0,"
        data += lines[i][pos:]

with open("sets.txt", "wb") as file:
    file.write(data)

print("Done!")
