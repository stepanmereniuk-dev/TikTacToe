matrix_board = [["x","-","x"],
                ["-","x","-"],
                ["x","-","x"]]

def check_if_array_equal(list):
    for element in list:
        if element =="-":
            return False
    s = len(set(list))
    if s == 1:
        return True
    return False

def check_diagonals(matrix):
    win = False
    list_of_items = []
    
    for i in range(len(matrix)):
        list_of_items.append(matrix[i][i])
        #print(list_of_items)
    if check_if_array_equal(list_of_items) == True:
        print("True: left -> right")
        return True
    
    index = 0
    list_of_items = []
    for i in range(len(matrix)):
        index -=1
        list_of_items.append(matrix[i][index])
        #print(list_of_items)
    print(check_if_array_equal(list_of_items))
    if check_if_array_equal(list_of_items) == True:
        print("True: right -> left")
        return True
    return win


def check_rows_and_columns(matrix):
    win = False

    for i in range(len(matrix)):
        list_of_items = []
        for b in range(len(matrix)):
            list_of_items.append(matrix[i][b])
        if check_if_array_equal(list_of_items):
            print(f"True: Row = {i+1}")       
            return True
        #print(list_of_items)

    for i in range(len(matrix)):
        list_of_items = []
        for b in range(len(matrix)):
            list_of_items.append(matrix[b][i])
        if check_if_array_equal(list_of_items):
            print(f"True: Column = {i+1}")       
            return True
    #print(list_of_items)
