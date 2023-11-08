from a_star import AStar

class Node:
    def __init__(self, value, position, weight=0, volume=0):
        self.value = value
        self.position = position
        self.weight = weight
        self.volume = volume
        self.neighbours = []
        self.distance_from_start = float('inf')  # Initialize distance_from_start as infinity
        self.parent = None

    def get_value(self):
        return self.value

    def get_position(self):
        return self.position

    def get_weight(self):
        return self.weight

    def set_weight(self, weight):
        self.weight = weight

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = volume

    def add_neighbour(self, node, cost):
        self.neighbours.append((node, cost))

    def get_neighbours(self):
        return [neighbour[0] for neighbour in self.neighbours]
    
    def get_distance_to(self, node):
        for neighbour in self.neighbours:
            if neighbour[0] == node:
                return neighbour[1]
        return None

    def get_edge_cost(self, node):
        for neighbour in self.neighbours:
            if neighbour[0] == node:
                return neighbour[1]
        return None

    def __str__(self):
        return str(self.value)


class Graph:
    def __init__(self):
        self.nodes = []
        self.start_node = None  # Reference to the start node
        self.target_node = None  # Reference to the current target node
        self.weight_limit = None  # Weight limit for the robot cleaner
        self.volume_limit = None  # Volume limit for the robot cleaner

    def add_node(self, value, position, weight=0, volume=0):
        node = Node(value, position, weight, volume)
        self.nodes.append(node)

    def find_node(self, value):
        for node in self.nodes:
            if node.value == value:
                return node
        return None

    def add_edge(self, value1, value2, cost):
        node1 = self.find_node(value1)
        node2 = self.find_node(value2)

        if node1 is not None and node2 is not None:
            node1.add_neighbour(node2, cost)
            node2.add_neighbour(node1, cost)
        else:
            print("Error: One or more nodes were not found")

    def get_rubbish_nodes(self):
        return [node for node in self.nodes if node.get_weight() > 0 or node.get_volume() > 0]

    def get_rubbish_max_weight(self, node):
        max_weight = 0
        if node.get_weight() > max_weight:
            max_weight = node.get_weight()
        return max_weight

    def find_nearest_node(self, start_node, nodes):
        nearest_distance = None
        nearest_node = None
        
        for node in nodes:
            distance = AStar.manhattan_distance(self, start_node, node)
            if nearest_distance is None or distance < nearest_distance:
                nearest_distance = distance
                nearest_node = node
            # Choose the nearest node with higher weight 
            elif distance == nearest_distance:
                weight = self.get_rubbish_max_weight(node)
                current_weight = self.get_rubbish_max_weight(nearest_node)
                if weight > current_weight:
                    nearest_node = node
        return nearest_node

    def find_next_rubbish(self, start_node):
        rubbish_nodes = [node for node in self.nodes if node.get_weight() > 0 or node.get_volume() > 0]
        if start_node in rubbish_nodes:
            rubbish_nodes.remove(start_node)        
        return self.find_nearest_node(start_node, rubbish_nodes)
    
    def find_disposal_node(self, current_node):
        disposal_nodes = [node for node in self.nodes if node.get_value() in ('30', '31', '54')]
        if not disposal_nodes:
            return None
        return self.find_nearest_node(current_node, disposal_nodes)
