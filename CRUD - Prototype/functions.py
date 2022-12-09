file_obj_read = open("Data store.txt","r+")
def read(file_obj_read) -> list :
    """
    Returns the contents of a file as a list
    """
    a = file_obj_read.readlines()
    return a
data = read(file_obj_read)
file_obj_read.close()

def insert(key : str ,value : str ,data = data) -> None :
    """
    Insert is a function that inserts a key value data pair
    to the dataStore
    Inputs:
        key : String data used to identify the value
        value : The value corresponding to the key
    """
    file_obj_write = open("Data store.txt","w+")

    flag = 1
    for i,line in enumerate(data):
        line.strip("\n")
        if line == "":
            continue
        line = line.split(",")
        if line[0] == key:
            line[1] = value
            if len(data) - 1 == i:
                data[i] = f"{line[0]},{line[1]}"
            else:
                data[i] = f"{line[0]},{line[1]}\n"
            flag = 0
            break
    if flag:
        data.append(f"\n{key},{value}")
    file_obj_write.writelines(data)


def find(key : str,data = data):
    """
    This function is used to check if the key is 
    in the DataStore
    inputs:
        key - String data used to identify the value
    returns:
        value -  the value corresponding to the key
    """

    for line in data:
        line = line.strip("\n")
        line = line.split(",")
        if line[0] == key:
            return line[1]
    return "Invalid Key"

def delete(key : str) -> int:
    """
    This function is used to delete the key,value pair
    from the DataStore
    Input:
        key : String data used to identify the value
    """
    global data
    file_obj_write = open("Data store.txt","w+")
    new_data = []
    flag = 1
    for line in data:
        a = line.strip("\n")
        a = a.split(",")
        if a[0] == key:
            flag = 0
            continue
        new_data.append(line)
    data = new_data
    file_obj_write.writelines(new_data)
    return flag
