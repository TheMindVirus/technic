### WARNING: Please use with caution at a steady pace.
###          "Don't lose your heads, don't get over-excited..."

def main():
    #read_long_file_test()
    print("[Electric Lego Set Checker]")
    dataset = "sets.txt"
    while True:
        try:
            lego_set = input("Lego Set: ")
            #is_technic(dataset, lego_set)
            is_electric(dataset, lego_set)
            #is_train(dataset, lego_set)
        except Exception as error:
            print(error) #error.with_traceback()

def read_long_file_test():
    data = b""
    line = b""
    number = 0
    file = open("sets.txt", "rb")
    try:
        line = file.readline()
        while line:
            line = file.readline()
            data += line
            number += 1
    except Exception as error:
        print(error)
        print(number) #1000 lines, 65535 bytes
    print("Done!")
    print(len(data))
    file.close()

def get_field_index(headings, field):
    for i in range(0, len(headings)):
        if headings[i] == field.encode():
            return i
    return -1

def scan(dataset, field, query):
    file = open(dataset, "rb")

    headings = file.readline().split(b",")
    set_id_column = get_field_index(headings, "set_num")
    search_column = get_field_index(headings, field)

    if set_id_column < 0 or search_column < 0:
        print("Unknown Search Heading")
        return False

    line = headings
    while line:
        line = file.readline()
        tokens = line.split(b",")
        if tokens and len(tokens) > max(set_id_column, search_column):
            set_id = tokens[set_id_column].decode()
            entry = tokens[search_column].decode()
            if set_id == query:
                print(line)
                if entry == "1":
                    file.close()
                    return True
                else:
                    file.close()
                    return False
    file.close()
    return False
        
def is_technic(dataset, lego_set):
    print("Is Set " + str(lego_set) + " Technic?")
    if scan(dataset, "is_technic", lego_set):
        print("I think so")
    else:
        print("I don't know")

def is_electric(dataset, lego_set):
    print("Is Set " + str(lego_set) + " Electric?")
    if scan(dataset, "is_electric", lego_set):
        print("I think so")
    else:
        print("I don't know")

def is_train(dataset, lego_set):
    print("Is Set " + str(lego_set) + " Train related?")
    if scan(dataset, "is_train", lego_set):
        print("I think so")
    else:
        print("I don't know")

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
