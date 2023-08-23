from Node import Node

def move_up(state):
    new_state = state[:]
    index = new_state.index(0)
    if index not in [0, 3, 6]:
        temp = new_state[index - 1]
        new_state[index - 1] = new_state[index]
        new_state[index] = temp
        return new_state
    else:
        return None


def move_down(state):
    new_state = state[:]
    index = new_state.index(0)
    if index not in [2, 5, 8]:
        # Swap the values.
        temp = new_state[index + 1]
        new_state[index + 1] = new_state[index]
        new_state[index] = temp
        return new_state
    else:
        return None


def move_left(state):
    new_state = state[:]
    index = new_state.index(0)
    if index not in [0, 1, 2]:
        # Swap the values.
        temp = new_state[index - 3]
        new_state[index - 3] = new_state[index]
        new_state[index] = temp
        return new_state
    else:
        return None


def move_right(state):
    new_state = state[:]
    index = new_state.index(0)
    # Sanity check
    if index not in [6, 7, 8]:
        # Swap the values.
        temp = new_state[index + 3]
        new_state[index + 3] = new_state[index]
        new_state[index] = temp
        return new_state
    else:
        return None

def expand_node(node):
    expanded_nodes = []
    expanded_nodes.append(create_node(move_up(node.state), node, "Up", node.depth + 1, 0))
    expanded_nodes.append(create_node(move_down(node.state), node, "Down", node.depth + 1, 0))
    expanded_nodes.append(create_node(move_left(node.state), node, "Left", node.depth + 1, 0))
    expanded_nodes.append(create_node(move_right(node.state), node, "Right", node.depth + 1, 0))
    expanded_nodes = [node for node in expanded_nodes if node.state != None]  # list comprehension!
    return expanded_nodes
    


def create_node(state, parent, operator, depth, cost):
    return Node(state, parent, operator, depth, cost)

def uniform_cost(start,goal):
    start_node=create_node(start,None,None,0,0)
    fringe=[]
    path=[]
    fringe.append(start_node)
    current=fringe.pop(0)
    while(current.state!=goal):
        temp=expand_node(current)
        for item in temp:
            item.depth+=current.depth
            fringe.append(item)
        fringe.sort(key =lambda x: x.depth)
        current=fringe.pop(0)
    while(current.parent!=None):
        path.insert(0,current.operator)
        current=current.parent
    return path