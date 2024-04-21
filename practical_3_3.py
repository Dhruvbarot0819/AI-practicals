from enum import Enum
import time

class Action(Enum):
    # Enum class for actions
    NO_ACTION = 0
    MOVE_LEFT = 1
    MOVE_DOWN = 2
    MOVE_UP = 3
    MOVE_RIGHT = 4

class Node:
    def __init__(self, puzzle_list, parent, action):
        self.puzzle_list = puzzle_list
        self.parent = parent
        if parent is None:
            self.g = 0
        else:
            self.g = self.parent.g + 1
        self.f = 0
        self.action = action

    def __eq__(self, other):
        return self.puzzle_list == other.puzzle_list

    def __lt__(self, other):
        return self.f < other.f

    def apply_action(self, action):
        zero_index = self.puzzle_list.index(0)
        new_puzzle_list = self.puzzle_list[:]
        if action == Action.MOVE_LEFT and zero_index not in [0, 3, 6]:
            new_puzzle_list[zero_index], new_puzzle_list[zero_index - 1] = new_puzzle_list[zero_index - 1], new_puzzle_list[zero_index]
            return Node(new_puzzle_list, self, action)
        elif action == Action.MOVE_DOWN and zero_index not in [6, 7, 8]:
            new_puzzle_list[zero_index], new_puzzle_list[zero_index + 3] = new_puzzle_list[zero_index + 3], new_puzzle_list[zero_index]
            return Node(new_puzzle_list, self, action)
        elif action == Action.MOVE_UP and zero_index not in [0, 1, 2]:
            new_puzzle_list[zero_index], new_puzzle_list[zero_index - 3] = new_puzzle_list[zero_index - 3], new_puzzle_list[zero_index]
            return Node(new_puzzle_list, self, action)
        elif action == Action.MOVE_RIGHT and zero_index not in [2, 5, 8]:
            new_puzzle_list[zero_index], new_puzzle_list[zero_index + 1] = new_puzzle_list[zero_index + 1], new_puzzle_list[zero_index]
            return Node(new_puzzle_list, self, action)
        return None
 
    def generate_evaluation_function(self, goal_state):
        # h(n) = number of misplaced tiles
        h = sum([1 if self.puzzle_list[i] != goal_state[i] else 0 for i in range(9)])
        self.f = self.g + h

    def generate_all_successors(self):
        successors = []
        for action in Action:
            successor = self.apply_action(action)
            if successor is not None:
                successors.append(successor)
        return successors

class AStarSearch:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.open_list = []
        self.closed_list = []
        self.action_names = {
            Action.NO_ACTION: "No Action",
            Action.MOVE_LEFT: "Move Left",
            Action.MOVE_DOWN: "Move Down",
            Action.MOVE_UP: "Move Up",
            Action.MOVE_RIGHT: "Move Right"
        }

    def perform_algorithm(self):
        start_time = time.time()
        initial_node = Node(self.initial_state, None, Action.NO_ACTION)
        initial_node.generate_evaluation_function(self.goal_state)
        self.open_list.append(initial_node)

        while self.open_list:
            current_node = min(self.open_list)
            self.open_list.remove(current_node)
            self.closed_list.append(current_node)

            if current_node.puzzle_list == self.goal_state:
                end_time = time.time()
                execution_time = end_time - start_time
                self.final_output(current_node, execution_time)
                return

            successors = current_node.generate_all_successors()
            for successor in successors:
                if successor in self.closed_list:
                    continue
                if successor not in self.open_list:
                    successor.generate_evaluation_function(self.goal_state)
                    self.open_list.append(successor)

    def final_output(self, goal_node, execution_time):
        path = self.get_path(goal_node)
        print("Steps to reach goal state:")
        for i, node in enumerate(path):
            print(f"Step {i + 1}:")
            self.print_puzzle_state(node.puzzle_list)
            if node.action != Action.NO_ACTION:
                print(f"Action: {self.action_names[node.action]}")
                print("\n")
        print(f"\nExecution time: {execution_time} seconds")
        print(f"Number of steps: {len(path) - 1}")

    def print_puzzle_state(self, puzzle_list):
        for i in range(3):
            print(' '.join(map(str, puzzle_list[i * 3:i * 3 + 3])))
        print()

    def get_path(self, goal_node):
        path = []
        current_node = goal_node
        while current_node is not None:
            path.insert(0, current_node)
            current_node = current_node.parent
        return path


# Example usage:
initial_state = [1, 2, 3, 4, 5, 0, 6, 7, 8]
goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
solver = AStarSearch(initial_state, goal_state)
solver.perform_algorithm()

#g(n)=  cost of path from root node to current node