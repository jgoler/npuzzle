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
            if x == "*":
                list_representation.append(0) # We can make this value 0, and then sort it like any other number
            else:
                list_representation.append(int(x))
    return(list_representation)


def DebugPrintState(state):
    n = int(math.sqrt(len(state)))
    i = 0
    while i < len(state):
        print("{}, {}, {}".format(state[i], state[i + 1], state[i + 2]))
         #"Hi {}, you are {}".format(name, age)
        i += n



def ComputeNeighbors(state):
    return True

def isValid(i, n):
    return True


def main():
    result = LoadFromFile("input.txt")
    DebugPrintState(result)

if __name__ == "__main__":
    main()
