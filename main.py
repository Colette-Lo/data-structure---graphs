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


