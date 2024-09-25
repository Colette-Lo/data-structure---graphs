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

stack_obg = Stack()

current_node = "J"

stack_obg.push(current_node)

visited = []

def dft(stack_obj):
    while stack_obj.get_size() != 0:
        visited.append(current_node)
        for i in range(len(adj_list[current_node]) -1):
            if adj_list[current_node][i] < adj_list[current_node][i+1]: