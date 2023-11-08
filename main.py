from graph import Graph
from a_star import AStar
from visualize import Visualization
import signal
import sys
import time

def run():
    start_time = time.time()
    
    # Create a graph
    graph = Graph()

    # Add nodes
    graph.add_node('1', (0,0), weight=0, volume=0)
    graph.add_node('2', (0,1), weight=0, volume=0)
    graph.add_node('3', (1,1), weight=0, volume=0)
    graph.add_node('4', (1,0), weight=0, volume=0)
    graph.add_node('5', (0,2), weight=0, volume=0)
    graph.add_node('6', (1,2), weight=0, volume=0)
    graph.add_node('7', (2,1), weight=0, volume=0)
    graph.add_node('8', (2,0), weight=0, volume=0)
    graph.add_node('9', (0,3), weight=0, volume=0)
    graph.add_node('10', (1,3), weight=30, volume=3)
    graph.add_node('11', (2,2), weight=5, volume=1)
    graph.add_node('12', (3,2), weight=0, volume=0)
    graph.add_node('13', (3,1), weight=5, volume=1)
    graph.add_node('14', (3,0), weight=0, volume=0)
    graph.add_node('15', (0,4), weight=0, volume=0)
    graph.add_node('16', (1,4), weight=0, volume=0)
    graph.add_node('17', (2,3), weight=0, volume=0)
    graph.add_node('18', (3,3), weight=0, volume=0)
    graph.add_node('19', (4,2), weight=10, volume=2)
    graph.add_node('20', (4,1), weight=0, volume=0)
    graph.add_node('21', (4,0), weight=0, volume=0)
    graph.add_node('22', (0,5), weight=10, volume=1)
    graph.add_node('23', (1,5), weight=0, volume=0)
    graph.add_node('24', (2,4), weight=0, volume=0)
    graph.add_node('25', (3,4), weight=5, volume=3)
    graph.add_node('26', (4,3), weight=0, volume=0)
    graph.add_node('27', (5,3), weight=0, volume=0)
    graph.add_node('28', (5,2), weight=0, volume=0)
    graph.add_node('29', (5,1), weight=0, volume=0)
    graph.add_node('30', (5,0), weight=0, volume=0)
    graph.add_node('31', (2,5), weight=0, volume=0)
    graph.add_node('32', (3,5), weight=0, volume=0)
    graph.add_node('33', (4,4), weight=20, volume=1)
    graph.add_node('34', (5,4), weight=0, volume=0)
    graph.add_node('35', (6,3), weight=0, volume=0)
    graph.add_node('36', (6,2), weight=0, volume=0)
    graph.add_node('37', (6,1), weight=10, volume=2)
    graph.add_node('38', (6,0), weight=0, volume=0)
    graph.add_node('39', (4,5), weight=0, volume=0)
    graph.add_node('40', (5,5), weight=0, volume=0)
    graph.add_node('41', (6,4), weight=5, volume=2)
    graph.add_node('42', (7,4), weight=0, volume=0)
    graph.add_node('43', (7,3), weight=20, volume=2)
    graph.add_node('44', (7,2), weight=0, volume=0)
    graph.add_node('45', (7,1), weight=0, volume=0)
    graph.add_node('46', (7,0), weight=30, volume=1)
    graph.add_node('47', (6,5), weight=0, volume=0)
    graph.add_node('48', (7,5), weight=0, volume=0)
    graph.add_node('49', (8,4), weight=0, volume=0)
    graph.add_node('50', (8,3), weight=0, volume=0)
    graph.add_node('51', (8,2), weight=0, volume=0)
    graph.add_node('52', (8,1), weight=10, volume=3)
    graph.add_node('53', (8,0), weight=0, volume=0)
    graph.add_node('54', (8,5), weight=0, volume=0)
    
    # Add edges
    graph.add_edge('1', '2', 1)
    graph.add_edge('1', '3', 1)
    graph.add_edge('1', '4', 1)
    graph.add_edge('2', '3', 1)
    graph.add_edge('2', '5', 1)
    graph.add_edge('2', '6', 1)
    graph.add_edge('3', '4', 1)
    graph.add_edge('3', '6', 1)
    graph.add_edge('3', '7', 1)
    graph.add_edge('3', '8', 1)
    graph.add_edge('4', '8', 1)
    graph.add_edge('5', '6', 1)
    graph.add_edge('5', '9', 1)
    graph.add_edge('5', '10', 1)
    graph.add_edge('6', '7', 1)
    graph.add_edge('6', '10', 1)
    graph.add_edge('6', '11', 1)
    graph.add_edge('7', '8', 1)
    graph.add_edge('7', '11', 1)
    graph.add_edge('7', '12', 1)
    graph.add_edge('7', '13', 1)
    graph.add_edge('8', '13', 1)
    graph.add_edge('8', '14', 1)
    graph.add_edge('9', '10', 1)
    graph.add_edge('9', '15', 1)
    graph.add_edge('9', '16', 1)
    graph.add_edge('10', '11', 1)       
    graph.add_edge('10', '16', 1)
    graph.add_edge('10', '17', 1)
    graph.add_edge('11', '12', 1)
    graph.add_edge('11', '17', 1)
    graph.add_edge('11', '18', 1)
    graph.add_edge('12', '13', 1)
    graph.add_edge('12', '18', 1)
    graph.add_edge('12', '19', 1)
    graph.add_edge('12', '20', 1)
    graph.add_edge('13', '14', 1)
    graph.add_edge('13', '20', 1)
    graph.add_edge('13', '21', 1)
    graph.add_edge('14', '21', 1)
    graph.add_edge('15', '16', 1)
    graph.add_edge('15', '22', 1)
    graph.add_edge('15', '23', 1)
    graph.add_edge('16', '17', 1)
    graph.add_edge('16', '23', 1)
    graph.add_edge('16', '24', 1)
    graph.add_edge('17', '18', 1)
    graph.add_edge('17', '24', 1)
    graph.add_edge('17', '25', 1)
    graph.add_edge('18', '19', 1)
    graph.add_edge('18', '25', 1)
    graph.add_edge('18', '26', 1)
    graph.add_edge('19', '20', 1)
    graph.add_edge('19', '26', 1)
    graph.add_edge('19', '27', 1)
    graph.add_edge('19', '28', 1)
    graph.add_edge('20', '21', 1)
    graph.add_edge('20', '28', 1)
    graph.add_edge('20', '29', 1)
    graph.add_edge('21', '29', 1)
    graph.add_edge('21', '30', 1)
    graph.add_edge('22', '23', 1)
    graph.add_edge('23', '24', 1)
    graph.add_edge('23', '31', 1)
    graph.add_edge('24', '25', 1)
    graph.add_edge('24', '31', 1)
    graph.add_edge('24', '32', 1)
    graph.add_edge('25', '26', 1)
    graph.add_edge('25', '32', 1)
    graph.add_edge('25', '33', 1)
    graph.add_edge('26', '27', 1)
    graph.add_edge('26', '33', 1)
    graph.add_edge('26', '34', 1)
    graph.add_edge('27', '28', 1)
    graph.add_edge('27', '34', 1)
    graph.add_edge('27', '35', 1)
    graph.add_edge('27', '36', 1)
    graph.add_edge('28', '29', 1)
    graph.add_edge('28', '36', 1)
    graph.add_edge('28', '37', 1)
    graph.add_edge('29', '30', 1)
    graph.add_edge('29', '37', 1)
    graph.add_edge('29', '38', 1)
    graph.add_edge('30', '38', 1)
    graph.add_edge('31', '32', 1)
    graph.add_edge('32', '33', 1)
    graph.add_edge('32', '39', 1)
    graph.add_edge('33', '34', 1)
    graph.add_edge('33', '39', 1)
    graph.add_edge('33', '40', 1)
    graph.add_edge('34', '35', 1)
    graph.add_edge('34', '40', 1)
    graph.add_edge('34', '41', 1)
    graph.add_edge('35', '36', 1)
    graph.add_edge('35', '41', 1)
    graph.add_edge('35', '42', 1)
    graph.add_edge('35', '43', 1)
    graph.add_edge('36', '37', 1)
    graph.add_edge('36', '43', 1)
    graph.add_edge('36', '44', 1)
    graph.add_edge('37', '38', 1)
    graph.add_edge('37', '44', 1)
    graph.add_edge('37', '45', 1)
    graph.add_edge('38', '45', 1)
    graph.add_edge('38', '46', 1)
    graph.add_edge('39', '40', 1)
    graph.add_edge('40', '41', 1)
    graph.add_edge('40', '47', 1)
    graph.add_edge('41', '42', 1)
    graph.add_edge('41', '47', 1)
    graph.add_edge('41', '48', 1)
    graph.add_edge('42', '43', 1)
    graph.add_edge('42', '48', 1)
    graph.add_edge('42', '49', 1)
    graph.add_edge('42', '50', 1)
    graph.add_edge('43', '44', 1)
    graph.add_edge('43', '50', 1)
    graph.add_edge('43', '51', 1)
    graph.add_edge('44', '45', 1)
    graph.add_edge('44', '51', 1)
    graph.add_edge('44', '52', 1)
    graph.add_edge('45', '46', 1)
    graph.add_edge('45', '52', 1)
    graph.add_edge('45', '53', 1)
    graph.add_edge('46', '53', 1)
    graph.add_edge('47', '48', 1)
    graph.add_edge('48', '49', 1)
    graph.add_edge('48', '54', 1)
    graph.add_edge('49', '50', 1)
    graph.add_edge('49', '54', 1)
    graph.add_edge('50', '51', 1)
    graph.add_edge('51', '52', 1)
    graph.add_edge('52', '53', 1)

    print("======================================================================================\n")
    print("  Output below shows the path to collect all the rubbish in maze using A* algorithm  ")
    print("\n======================================================================================\n")
    
    # Set up the start node and initial target
    start = graph.find_node('1')  # Start from node (0, 0)
    target = graph.find_next_rubbish(start)  # Initial target is the next rubbish node
    weight_limit = 40  # Weight limit for the robot cleaner
    volume_limit = 5  # Volume limit for the robot cleaner
    accumulated_cost = 0
    accumulated_weight = 0
    accumulated_volume = 0
    
    # Register signal handler for keyboard interrupt
    def signal_handler(sig, frame):
        print("Keyboard interrupt detected. Stopping...")
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)
    
    if target is None:
        print("No rubbish in the maze!\n")
    
    all_paths = []  # Initialize a list to store all the paths
    is_all_rubbish_cleared = False
    move = 0
    counter = 1
    # Loop the A* algorithm until all rubbish is cleared
    while len(graph.get_rubbish_nodes()) > 0 or (accumulated_weight != 0 or accumulated_volume != 0):
        move += 1
        print("\n===============================================================")
        print("Movement\tFrom\t\tTo\t\t\tCoordinate")
        print("===============================================================")
        print(f"{move}:\t\t\t{start} {start.position}\t{target} {target.position}\t{start.position} to {target.position}")
        print("===============================================================")

        # Create a new instance of AStar for each search
        alg = AStar(graph, start, target)
        path, total_cost, total_weight, total_volume = alg.search()
        
        # Print the result for each search
        paths = " -> ".join([node.value for node in path]) 
        all_paths.append(" -> ".join([node.value for node in path[1:]]))
        print(f"Path {counter}:", paths)
        print(f"Weight/Volume of rubbish in current room: {total_weight}kg / {total_volume}m³")
        
        # Accumulate the cost, weight and volume
        accumulated_cost += total_cost
        accumulated_weight += total_weight
        accumulated_volume += total_volume
        print(f"Total Weight/Volume in bin: {accumulated_weight}kg / {accumulated_volume}m³\n")
        
        # Check if target node is a disposal node
        if target.value in ('30', '31', '54'):
            print("Reach disposal room, rubbish has been cleared..\n")
            # Reset accumulated weight and volume to 0
            accumulated_weight = 0
            accumulated_volume = 0
            counter += 1

        # Update the start and target nodes simultaneously
        if target == path[-1]:
            # The search reached the target node, update both start and target to current target node
            start = path[-1]
            
            if start is not None:
                    # Check if the accumulated weight and volume will exceed the limits with the next rubbish node
                    temp_accumulated_weight = accumulated_weight
                    temp_accumulated_volume = accumulated_volume
                    next_rubbish_node = graph.find_next_rubbish(start)
                    
                    if next_rubbish_node is not None:
                        temp_accumulated_weight += next_rubbish_node.weight
                        temp_accumulated_volume += next_rubbish_node.volume
                        print(f"Next nearest rubbish room is {next_rubbish_node} ({next_rubbish_node.weight}kg / {next_rubbish_node.volume}m³)")
                        print(f"Accumulated Weight/Volume if visit: {temp_accumulated_weight}kg / {temp_accumulated_volume}m³")
                        if temp_accumulated_weight <= weight_limit or temp_accumulated_volume <= volume_limit:
                            print("Rubbish can be collected! Go to the rubbish room...")
                
                    if temp_accumulated_weight > weight_limit or temp_accumulated_volume > volume_limit:
                        # Next rubbish node will exceed the limit, select disposal node as the target
                        print("Exceed limit (40kg/5m³)! Go to nearest disposal room...")
                        target = graph.find_disposal_node(start)
                    else:
                        target = next_rubbish_node 
                    
            if target is None:
                target = graph.find_disposal_node(start)
                if target == graph.find_disposal_node(start):
                    if not is_all_rubbish_cleared:
                        print("No more rubbish in all rooms! Go to nearest disposal room...")
                        is_all_rubbish_cleared = True
                    
        else:
            # The search did not reach the target node, update start to current selected node and keep the target unchanged
            start = graph.find_node(path[-1])
            
    print("Algorithm terminated. All rubbish has been cleared successfully!")
    
    all_paths = " -> ".join(all_paths)
    print("\n\nFinal Path Summary:\n1 ->", all_paths) 
    print("\nTotal path cost:", accumulated_cost)
    print("Number of disposal room used:", counter-1)
    
    execution_time = time.time() - start_time
    print(f"Execution time: {execution_time:.4f} seconds")
    
    visualization = Visualization()
    visualization.visualize_graph(graph, all_paths)

if __name__ == '__main__':
  run()
  
  
