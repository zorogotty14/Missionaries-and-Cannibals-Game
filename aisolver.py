class State:
    def __init__(self, cannibalLeft, missionaryLeft, boat, cannibalRight, missionaryRight):
        self.cannibalLeft = cannibalLeft
        self.missionaryLeft = missionaryLeft
        self.boat = boat
        self.cannibalRight = cannibalRight
        self.missionaryRight = missionaryRight
        self.parent = None

    def is_goal(self):
        return self.cannibalLeft == 0 and self.missionaryLeft == 0

    def is_valid(self):
        return (self.missionaryLeft >= 0 and self.missionaryRight >= 0 and
                self.cannibalLeft >= 0 and self.cannibalRight >= 0 and
                (self.missionaryLeft == 0 or self.missionaryLeft >= self.cannibalLeft) and
                (self.missionaryRight == 0 or self.missionaryRight >= self.cannibalRight))

    def __eq__(self, other):
        return (self.cannibalLeft == other.cannibalLeft and
                self.missionaryLeft == other.missionaryLeft and
                self.boat == other.boat and
                self.cannibalRight == other.cannibalRight and
                self.missionaryRight == other.missionaryRight)

    def __hash__(self):
        return hash((self.cannibalLeft, self.missionaryLeft, self.boat, self.cannibalRight, self.missionaryRight))

def successors(cur_state):
    children = []
    if cur_state.boat == 'left':
        new_states = [
            State(cur_state.cannibalLeft, cur_state.missionaryLeft - 2, 'right',
                  cur_state.cannibalRight, cur_state.missionaryRight + 2),
            State(cur_state.cannibalLeft - 2, cur_state.missionaryLeft, 'right',
                  cur_state.cannibalRight + 2, cur_state.missionaryRight),
            State(cur_state.cannibalLeft - 1, cur_state.missionaryLeft - 1, 'right',
                  cur_state.cannibalRight + 1, cur_state.missionaryRight + 1),
            State(cur_state.cannibalLeft, cur_state.missionaryLeft - 1, 'right',
                  cur_state.cannibalRight, cur_state.missionaryRight + 1),
            State(cur_state.cannibalLeft - 1, cur_state.missionaryLeft, 'right',
                  cur_state.cannibalRight + 1, cur_state.missionaryRight)
        ]
    else:
        new_states = [
            State(cur_state.cannibalLeft, cur_state.missionaryLeft + 2, 'left',
                  cur_state.cannibalRight, cur_state.missionaryRight - 2),
            State(cur_state.cannibalLeft + 2, cur_state.missionaryLeft, 'left',
                  cur_state.cannibalRight - 2, cur_state.missionaryRight),
            State(cur_state.cannibalLeft + 1, cur_state.missionaryLeft + 1, 'left',
                  cur_state.cannibalRight - 1, cur_state.missionaryRight - 1),
            State(cur_state.cannibalLeft, cur_state.missionaryLeft + 1, 'left',
                  cur_state.cannibalRight, cur_state.missionaryRight - 1),
            State(cur_state.cannibalLeft + 1, cur_state.missionaryLeft, 'left',
                  cur_state.cannibalRight - 1, cur_state.missionaryRight)
        ]
    for state in new_states:
        if state.is_valid():
            state.parent = cur_state
            children.append(state)
    return children

def breadth_first_search(missionaries, cannibals):
    initial_state = State(cannibals, missionaries, 'left', 0, 0)
    if initial_state.is_goal():
        return initial_state
    frontier = list()
    explored = set()
    frontier.append(initial_state)
    while frontier:
        state = frontier.pop(0)
        if state.is_goal():
            return state
        explored.add(state)
        children = successors(state)
        for child in children:
            if child not in explored and child not in frontier:
                frontier.append(child)
    return None

def print_solution(solution):
    path = []
    path.append(solution)
    parent = solution.parent
    while parent:
        path.append(parent)
        parent = parent.parent

    for t in range(len(path)):
        state = path[len(path) - t - 1]
        print(f"({state.cannibalLeft},{state.missionaryLeft},{state.boat},{state.cannibalRight},{state.missionaryRight})")

# Example usage
if __name__ == "__main__":
    missionaries = 3
    cannibals = 3
    solution = breadth_first_search(missionaries, cannibals)
    if solution:
        print("Solution found:")
        print_solution(solution)
    else:
        print("No solution found.")
