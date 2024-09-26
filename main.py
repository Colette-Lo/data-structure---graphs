from stack import Stack

adj_list = {
    "A":["B", "C"],
    "B":["A", "K"],
    "C":["D", "F"],
    "D":["C", "E", "G", "H"],
    "E":["D"],
    "F":["C", "G", "J"],
    "G":["D", "F"],
    "H":["D", "J"],
    "J":["F", "H"],
    "K":["B"]
}

def print_neighbour(new_list, node):
    print(new_list[node])

def is_connected(new_list, node1, node2):
    if node1 in adj_list[node2]:
        print(True)



def dft(graph, start):
    stack_obj = Stack()
    # Start from J.
    current_node = start
    # Push current node to the stack.
    stack_obj.push(current_node)
    # A list of visited node.
    visited = []
    while stack_obj.get_size() != 0:
        # Save the current node for later if new node is found.
        temp_current = current_node

        # Look through all the current node neighbours in alphabetical order.
        for neighbour in sorted(graph[current_node]):
            # If neighbour hasn't been visited, set current node to the neighbour.
            if neighbour not in visited:
                current_node = neighbour
                stack_obj.push(current_node)
                visited.append(current_node)
                break

        # If no change to the current node (no unvisited neighbours),
        # pop the stack and set current node to be the returned node.
        if current_node == temp_current:
            current_node = stack_obj.pop()

    print(visited)

dft(adj_list, "J")

