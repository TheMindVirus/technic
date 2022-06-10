with open("sets.txt", "rb") as file:
    data = file.readlines()

### WARNING: Please use with caution at a steady pace.
###          "Don't lose your heads, don't get over-excited..."

def get_field_index(headings, field):
    for i in range(0, len(headings)):
        if headings[i] == field.encode():
            return i
    return -1

def scan(lines, field, query):
    headings = data[0].split(b",")
    set_id_column = get_field_index(headings, "set_num")
    search_column = get_field_index(headings, field)

    if set_id_column < 0 or search_column < 0:
        print("Unknown Search Heading")
        return False
    for i in range(1, len(lines)):
        tokens = lines[i].split(b",")
        set_id = tokens[set_id_column].decode()
        entry = tokens[search_column].decode()
        if set_id == query:
            print(lines[i])
            if entry == "1":
                return True
    return False
        
def is_technic(lego_set):
    print("Is Set " + str(lego_set) + " Technic?")
    if scan(data, "is_technic", lego_set):
        print("I think so")
    else:
        print("I don't know")

def is_electric(lego_set):
    print("Is Set " + str(lego_set) + " Electric?")
    if scan(data, "is_electric", lego_set):
        print("I think so")
    else:
        print("I don't know")

def is_train(lego_set):
    print("Is Set " + str(lego_set) + " Train related?")
    if scan(data, "is_train", lego_set):
        print("I think so")
    else:
        print("I don't know")

def main():
    print("[Electric Lego Set Checker]")
    while True:
        try:
            lego_set = input("Lego Set: ")
            #is_technic(lego_set)
            is_electric(lego_set)
            #is_train(lego_set)
        except Exception as error:
            print(error.with_traceback())

if __name__ == "__main__":
    main()

"""
[Electric Lego Set Checker]
Lego Set: 001-1
Is Set 001-1 Electric?
b'1,1,0,0,001-1,Gears,1965,1,43,\n'
I don't know
Lego Set: 002-1
Is Set 002-1 Electric?
b'1,1,1,0,002-1,4.5V Samsonite Gears Motor Set,1965,1,3,\n'
I think so
Lego Set:
"""
