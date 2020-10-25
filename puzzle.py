import math

def LoadFromFile(filepath):
    f = open(filepath, "r") # opening the file to read
    lines = f.readlines() # f is now equal to all of the lines in the file
    n = int(lines[0].strip()) 
    lines.pop(0) #removing the line containing n
    if len(lines) != n:
        print("Your input value for n does not match the value corresponding data you inputted")
        return None
    list_representation = []
    for j in lines:
        j = j.strip()
        j = j.split('\t')
        if isValid(j, n) == False:
            print("Your input data is invalid")
            return None
        for x in j:
            '''
            if x == "*":
                list_representation.append(0) # We can make this value 0, and then sort it like any other number
            else:
            '''
            if x == "*":
                list_representation.append("*")
            else:
                list_representation.append(int(x))
    return(list_representation)


def DebugPrintState(state):
    n = int(math.sqrt(len(state)))
    i = 0
    while i < len(state):
        print("{}, {}, {}".format(state[i], state[i + 1], state[i + 2]))
        i += n



def ComputeNeighbors(state):
    neighborsList = []
    index = state.index("*")
    n = int(math.sqrt(len(state)))
    if index % n == 0:
        swapping_number = state[index + 1]
        current = state.copy()
        Swap(index + 1, index, current)
        current_moves = (swapping_number, current)
        neighborsList.append(current_moves)
    if index % n == n - 1:
        swapping_number = state[index - 1]
        current = state.copy()
        Swap(index - 1, index, current)
        current_moves = (swapping_number, current)
        neighborsList.append(current_moves)
    if index % n != 0 and index % n != n - 1: #by still checking this case, we don't have to worry about n = 2
        swapping_number = state[index + 1]
        current = state.copy()
        Swap(index + 1, index, current)
        current_moves = (swapping_number, current)
        neighborsList.append(current_moves)
        swapping_number = state[index - 1]
        current = state.copy()
        Swap(index - 1, index, current)
        current_moves = (swapping_number, current)
        neighborsList.append(current_moves)
    if index + 3 < len(state):
        swapping_number = state[index + 3]
        current = state.copy()
        Swap(index + 3, index, current)
        current_moves = (swapping_number, current)
        neighborsList.append(current_moves)
    if index - 3 >= 0:
        swapping_number = state[index - 3]
        current = state.copy()
        Swap(index - 3, index, current)
        current_moves = (swapping_number, current)
        neighborsList.append(current_moves)
    return neighborsList

def IsGoal(state):
    iteration = 1
    while iteration <= len(state):
        if iteration == len(state):
            if state[iteration - 1] == 0:
                return True
        if state[iteration - 1] != iteration:
            return False
        iteration += 1
    return True


def Swap(first_index, second_index, list):
    list[second_index] = list[first_index]
    list[first_index] = 0
    return list
    

def isValid(i, n):
    return True


def main():
    result = LoadFromFile("input.txt")
    DebugPrintState(result)
    print(ComputeNeighbors(result))

if __name__ == "__main__":
    main()
