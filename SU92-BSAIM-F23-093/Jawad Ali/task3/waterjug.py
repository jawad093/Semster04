def waterJugDFS(capacity1, capacity2, goal):
    stack = []  
    visited = set()  

    stack.append((0, 0))  
    visited.add((0, 0)) 

    actions = []  

    while stack:
        jug1, jug2 = stack.pop() 
        actions.append((jug1, jug2))  

        if jug1 == goal or jug2 == goal:
            print("Solution Found")
            for action in actions:
                print(action)
            return True

        rules = [
            (capacity1, jug2),  # 1: Fill jug1
            (jug1, capacity2),  # 2: Fill jug2
            (0, jug2),  # 3: Empty jug1
            (jug1, 0),  # 4: Empty jug2
            (jug1 - min(jug1, capacity2 - jug2), jug2 + min(jug1, capacity2 - jug2)),  # 5: Pour jug1 → jug2
            (jug1 + min(jug2, capacity1 - jug1), jug2 - min(jug2, capacity1 - jug1)),  # 6: Pour jug2 → jug1
            (jug1 + jug2, 0),  # 7: Pour all jug1 → jug2
            (0, jug1 + jug2),  # 8: Pour all jug2 → jug1
        ] 

        for state in rules:
            if state not in visited:
                visited.add(state)
                stack.append(state)

    print("No Solution Found")
    return False


jug1Capacity = 4
jug2Capacity = 3
target = 2          

waterJugDFS(jug1Capacity, jug2Capacity, target)
