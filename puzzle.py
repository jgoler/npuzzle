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



def isValid(j, n):
    flag = True
    if len(j) != n:
        return False
    for letter in j:
        if letter.isdigit() or letter == '*':
            flag = True
        else:
            return False
    return flag


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
    '''
    iteration = 1
    while iteration <= len(state):
        if iteration == len(state):
            if state[iteration - 1] == 0:
                return True
        if state[iteration - 1] != iteration:
            return False
        iteration += 1
    return True
    '''
    new_list = [i for i in range(1, len(state) + 1)]
    new_list[-1] = "*"
    return state == new_list


def Swap(first_index, second_index, list):
    list[second_index] = list[first_index]
    list[first_index] = '*'
    return list

'''
def BFS(state):
    frontier = [state]
    discovered = set(tuple(state))
    parents = {tuple(state): None}
    while len(frontier) > 0:
        #print("while loop iteration")
        current_state = frontier.pop(0)
        discovered.add(tuple(current_state))
        print("current_state is ", current_state)
        #print(IsGoal(current_state))
        if IsGoal(current_state):
            #print("in if statement")
            test = current_state
            backtrack = []
            backtrack.append(current_state)
            value = parents[state]
            while value != None:
                backtrack.append(value)
                value = parents[value]
            backtrack.reverse()
            return backtrack
'''









def Transform(state):
    return [state]

def Flatten(state):
    new_list = []
    for i in state:
        for j in i:
            new_list.append(j)
    return new_list


def ConvertStates(neighbors):
    n = int(math.sqrt(len(neighbors[0][1])))
    states = []
    for i in neighbors:
        list = i[1]
        state = [[0 for i in range(n)] for j in range(n)]
        line = 0
        for x in range(len(list)):
            if x%n == 0 and x != 0:
                line += 1 
            state[line][x%n] = list[x]
        states.append(state)    
    return states



def BFS(state):
    frontier = [state]
    discovered = {tuple(state)}
    parents = {tuple(state): ()}
    while len(frontier) != 0:
        current_state = frontier.pop(0)
        if IsGoal(current_state):
            return parents[tuple(current_state)]
        neighboring_states = ConvertStates(ComputeNeighbors(current_state))
        for neighbor in range(len(neighboring_states)):
            neighbor_state = neighboring_states[neighbor]
            if tuple(Flatten(neighbor_state)) not in discovered:
                frontier.append(Flatten(neighbor_state))
                discovered.add(tuple(Flatten(neighbor_state)))
                path = list((parents[tuple(current_state)]))
                path.append(ComputeNeighbors(current_state)[neighbor][0])
                parents[tuple(Flatten(neighbor_state))] = tuple(path)


def DFS(state):
    frontier = [state]
    discovered = {tuple(state)}
    parents = {tuple(state): ()}
    while len(frontier) != 0:
        current_state = frontier.pop(0)
        if IsGoal(current_state):
            print("current_state is equal to ", tuple(current_state))
            return parents[tuple(current_state)][::-1]
        neighboring_states = ConvertStates(ComputeNeighbors(current_state))
        for neighbor in range(len(neighboring_states)):
            neighbor_state = neighboring_states[neighbor]
            if tuple(Flatten(neighbor_state)) not in discovered:
                frontier.insert(0, Flatten(neighbor_state))
                discovered.add(tuple(Flatten(neighbor_state)))
                path = list((parents[tuple(current_state)]))
                path.insert(0, ComputeNeighbors(current_state)[neighbor][0])
                parents[tuple(Flatten(neighbor_state))] = tuple(path)



def MakeGoal(state):
    goal_list = [i for i in range(1, len(state) + 1)]
    goal_list[-1] = "*"
    return goal_list


def BidirectionalSearch(state):
    frontier = [state]
    second_frontier = [MakeGoal(state)]
    discovered = {tuple(state)}
    second_discovered = {tuple(second_frontier[0])}
    parents = {tuple(state): ()}
    second_parents = {tuple(second_frontier[0]): ()}
    while len(frontier) != 0 and len(second_frontier) != 0:
        current_state = frontier.pop(0)
        second_current_state = second_frontier.pop(0)
        if discovered & second_discovered:
            '''
            final_value = []
            final_value.append(parents[tuple(current_state)])
            final_value.append(second_parents[tuple(second_current_state)][::-1])
            return final_value
            '''
            shared_tuple = discovered & second_discovered
            tuple_one = tuple(parents[tuple(Flatten(tuple(shared_tuple)))])
            tuple_two = tuple(second_parents[tuple(Flatten(tuple(shared_tuple)))][::-1])

            return tuple_one + tuple_two
        '''
            final_value = []

            new_value = []
            new_value.append(parents[tuple(current_state)])
            new_value.append(second_parents[tuple(second_current_state)][::-1])
            final_value.append(new_value)
            return final_value
            '''
        neighboring_states = ConvertStates(ComputeNeighbors(current_state))
        for neighbor in range(len(neighboring_states)):
            neighbor_state = neighboring_states[neighbor]
            if tuple(Flatten(neighbor_state)) not in discovered:
                frontier.append(Flatten(neighbor_state))
                discovered.add(tuple(Flatten(neighbor_state)))
                path = list((parents[tuple(current_state)]))
                path.append(ComputeNeighbors(current_state)[neighbor][0])
                parents[tuple(Flatten(neighbor_state))] = tuple(path)
        second_neighboring_states = ConvertStates(ComputeNeighbors(second_current_state))
        for neighbor in range(len(second_neighboring_states)):
            second_neighbor_state = second_neighboring_states[neighbor]
            if tuple(Flatten(second_neighbor_state)) not in second_discovered:
                second_frontier.append(Flatten(second_neighbor_state))
                second_discovered.add(tuple(Flatten(second_neighbor_state)))
                path = list((second_parents[tuple(second_current_state)]))
                path.append(ComputeNeighbors(second_current_state)[neighbor][0])
                second_parents[tuple(Flatten(second_neighbor_state))] = tuple(path)
    


def main():
    #print(Transform([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    result = LoadFromFile("input.txt")
    #print(LoadFromFile("input.txt"))
    #DebugPrintState(result)
    #print(ComputeNeighbors(result))
    print(BFS(result))
    #print(IsGoal([1, 2, 3, 4, 5, 6, 7, 8, "*"]))

if __name__ == "__main__":
    main()
