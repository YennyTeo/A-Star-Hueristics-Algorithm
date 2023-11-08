import math

class AStar:
    def __init__(self, graph, start, target):
        self.graph = graph
        self.start = start
        self.target = target
        self.opened = []
        self.closed = []
        self.number_of_steps = 0
    
    def manhattan_distance(self, node1, node2):
      return abs(node1.position[0] - node2.position[0]) + abs(node1.position[1] - node2.position[1])
    
    def euclidean_distance(self, node1, node2):
        return math.sqrt((node1.position[0] - node2.position[0]) ** 2 + (node1.position[1] - node2.position[1]) ** 2)

    def calculate_distance(self, parent, child):
        for neighbour in parent.neighbours:
            if neighbour[0] == child:
                distance = parent.distance_from_start + neighbour[1]
                if distance < child.distance_from_start:
                    child.parent = parent
                    child.distance_from_start = distance
                return distance
        return child.distance_from_start

    def calculate_heuristic_value(self, parent, child, target):
        return self.calculate_distance(parent, child) + self.euclidean_distance(child, target)

    def insert_to_list(self, list_category, node):
        if list_category == "open":
            self.opened.append(node)
        else:
            self.closed.append(node)

    def remove_from_opened(self):
        self.opened.sort(key=lambda node:node.heuristic_value)
        node = self.opened.pop(0)
        self.closed.append(node)
        return node

    def opened_is_empty(self):
        return len(self.opened) == 0

    def search(self):
        target = self.target
        if self.start is None:
            print("Start node is None")
            return [], 0, 0, 0 # path, total cost, accumulated weight, and accumulated volume

        self.start.distance_from_start = 0
        accumulated_weight = 0
        accumulated_volume = 0
        self.start.heuristic_value = self.calculate_heuristic_value(self.start, self.target, target)
        self.opened.append(self.start)

        while True:
            if self.opened_is_empty():
                print(f"No Solution Found after {self.number_of_steps} steps!!!")
                break

            selected_node = self.remove_from_opened()

            if selected_node == self.target:
                path = self.calculate_path(self.start, selected_node)
                total_cost = self.calculate_cost(path)
                total_weight = self.calculate_weight(path)
                total_volume = self.calculate_volume(path)
                
                accumulated_weight += total_weight
                accumulated_volume += total_volume
                
                # clear the rubbish node weight and volume
                selected_node.weight = 0
                selected_node.volume = 0

                return path, total_cost, accumulated_weight, accumulated_volume

            new_nodes = selected_node.get_neighbours()

            if new_nodes is not None and len(new_nodes) > 0:
                for new_node in new_nodes:
                    new_node.heuristic_value = self.calculate_heuristic_value(selected_node, new_node, self.target)
                    
                    if new_node not in self.closed and new_node not in self.opened:
                        new_node.parent = selected_node
                        self.insert_to_list("open", new_node)
                        
                    elif new_node in self.opened and new_node.parent != selected_node:
                        old_node = self.graph.find_node(new_node.value)
                        
                        if new_node.heuristic_value < old_node.heuristic_value:
                            new_node.parent = selected_node
                            self.insert_to_list("open", new_node)
            else:
                break  # Exit the loop if there are no new nodes to process
            self.number_of_steps += 1

        print("No solution found!")
        return [], 0, 0, 0

    def calculate_edge_weight(self, node1, node2):
        edge_weight = None
        for neighbor, cost in node1.neighbours:
            if neighbor == node2:
                edge_weight = cost
                break
        return edge_weight

    def calculate_path(self, start_node, target_node):
        path = [target_node]
        node = target_node
        while node is not None and node != start_node:
            node = node.parent
            path.append(node)
        path.reverse()
        return path

    def calculate_cost(self, path):
        total_cost = 0
        for i in range(len(path) - 1):
            child = path[i]
            parent = path[i+1]
            edge_cost = self.calculate_edge_weight(child, parent)
            if edge_cost is not None:
                total_cost += edge_cost
        return total_cost

    def calculate_weight(self, path):
        total_weight = 0
        for node in path:
            total_weight += node.weight
        return total_weight

    def calculate_volume(self, path):
        total_volume = 0
        for node in path:
            total_volume += node.volume
        return total_volume



