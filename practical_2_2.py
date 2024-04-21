import time


class Node:
    def __init__(self, x, y, parent):
        self.x = x
        self.y = y
        self.parent = parent

    def applyRule(self, ruleNo, waterJug):
        x = self.x
        y = self.y

        if ruleNo == 1:
            if x < waterJug.maxJug1:
                x = waterJug.maxJug1
            else:
                return None

        elif ruleNo == 2:
            if y < waterJug.maxJug2:
                y = waterJug.maxJug2
            else:
                return None

        elif ruleNo == 3:
            if x > 0:
                x = 0
            else:
                return None

        elif ruleNo == 4:
            if y > 0:
                y = 0
            else:
                return None

        elif ruleNo == 5:
            if (x + y >= waterJug.maxJug1 and x + y > 0) and (y > 0):
                # x = waterJug.maxJug1
                x=self.x
                y = y - (waterJug.maxJug1 - x)
            else:
                return None

        elif ruleNo == 6:
            if (x + y >= waterJug.maxJug2 and x + y > 0) and (x > 0):
                x = x - (waterJug.maxJug2 - y)
                y = waterJug.maxJug2
            else:
                return None

        elif ruleNo == 7:
            if (x + y <= waterJug.maxJug1 and x + y > 0) and (y >= 0):
                x = x + y
                y = 0
            else:
                return None

        elif ruleNo == 8:
            if (x + y <= waterJug.maxJug2 and x + y > 0) and (x >= 0):
                y = y + x
                x = 0
            else:
                return None

        if x == self.x and y == self.y:
            return None

        return Node(x, y, self)

    def generateAllSuccessors(self, waterJug):
        node_list = []
        for rule in range(1, 9):
            next_node = self.applyRule(rule, waterJug)
            if next_node != None:
                node_list.append(next_node)
        return node_list


class waterJug:
    def __init__(self, maxJug1, maxJug2, goal):
        self.maxJug1 = maxJug1
        self.maxJug2 = maxJug2
        self.goal = goal


class bfs_search:
    def __init__(self, initial_state, waterJug):
        self.initial_state = initial_state
        self.waterJug = waterJug

    def execution(self):
        print("BSF searching process is initiated ...")
        queue = [self.initial_state]
        totalExploredNodes = 0
        maxLength = 0

        while len(queue) != 0:
            current_node = queue.pop(0)
            totalExploredNodes += 1
            # print((current_node.x,current_node.y))
            if current_node.x == self.waterJug.goal:
                return current_node, totalExploredNodes, maxLength
            successors = current_node.generateAllSuccessors(self.waterJug)
            # for node in successors:
            #     print(f"({node.x},{node.y})",end=" ")
            queue.extend(successors)
            maxLength = max(maxLength, len(successors))


def print_path(result_node):
    path_list = [result_node]
    node = result_node.parent
    while node != None:
        path_list.append(node)
        node = node.parent
    path_list.reverse()
    print("Congratulation!! BFS algorithm finded the solution, ending the search ...")
    for node in path_list:
        print(f"{node.x,node.y}")
    print("We got the optimal and complete solution using the BFS algo...")
    print("Total path cost is : ", len(path_list))


def checkInputNumber(number):
    if number < 0 or number == 0:
        return False
    return True


def checkGoal(goal, jug1):
    if goal > jug1:
        return False
    return True


def checkBothJug(jug1, jug2, goal):
    if jug1 == jug2 != goal:
        return False
    # if abs(jug1-jug2)<goal:
    #     return False
    # if jug1<jug2 and goal>jug1:
    #     return False
    # if jug1%2==0 and jug2%2==0:
    #     return False

    return True


def test():
    print("-" * 50)
    print("22012012001")
    print("-" * 50)
    jug1 = int(input("Enter maximum capacity of JUG 1 :"))
    if not checkInputNumber(jug1):
        print("You have entered wrong number")
        return

    jug2 = int(input("Enter maximum capacity of JUG 2 :"))
    if not checkInputNumber(jug2):
        print("You have entered wrong number")
        return

    goal = int(input("Enter how many gallons you want to put in JUG 1 :"))
    if not checkBothJug(jug1, jug2, goal):
        print(
            "This will go the infinite loop or goal is greater than jug 1 capcity,Try to re-run"
        )
        return

    if not checkGoal(goal, jug1):
        print("You have entered the goal higher than jug 1 max capacity.")
        return

    initial_node = Node(0, 0, None)
    waterjug = waterJug(jug1, jug2, goal)
    search = bfs_search(initial_node, waterjug)

    start_time = time.time()
    destination_node, total_explored_nodes, maxLen = search.execution()
    end_time = time.time()

    print(f"Goal node : {destination_node.x,destination_node.y}")

    print_path(destination_node)
    print(f"Time to get the solution ( Time Complexty ) is : {end_time-start_time} seconds")
    print(f"Space to get the solution ( Space Complexty ) is : {maxLen}")
    print("Total no of expolred node is : ", total_explored_nodes)
    print("-" * 50)


test()
