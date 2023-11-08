# Maze Cleaning Robot

## Overview
This project aims to solve the maze clearing problem by implementing a maze clearing robot that utilizes the A* algorithm to find the optimal path for collecting rubbish in a maze. The robot navigates through the maze, collects rubbish, and disposes of it in disposal nodes until all the rubbish is cleared and no more rubbish is found in any node.

## Files
There are four files in this project:

* main.py : Run the main program. It creates instance of Graph class, add nodes and edges to represent the maze. It uses A* algorithm to find the optimal path for collecting rubbish. 

* a_star.py:Contains the implementation of A* search algorithm to find shortest pathe between two nodes in the graph.

* graph.py: Defines Node and Graph classes. The Node class represents a node in the graph and stores information such as its value, position, weight, volume, neighbors, distance from the start node, and parent node. The Graph class represents the maze and provides methods for adding nodes, adding edges between nodes, finding rubbish nodes, finding the nearest node, finding the next rubbish node, and finding the disposal node.

* visualize.py: Visualize the representation of the maze and the robot's movement. It uses the Pygame library to draw the maze, nodes, edges, and animate the robot's movement.

## Istallation
To run the maze cleaning robot:
1. Ensure that Python 3 was installed on your system.
2. Install the Pygame library by using 'pip instal pygame'.
3. Run the main.py script. The output shows the path to collect all the rubbish in the maze using A* algorithm along with the weight and volume of rubbish in current node and total weight and volume in the bin. It also shows the total path cost, number of disposal rooms used, and the execution time.
4. After finish running the script, a visualization window will open, displaying the maze and the robot's movement'. A replay button can be clicked to replay the animation.

## Usage
Steps to use the maze cleaning robot in your own project:
1. Copy the files main.py, a_star.py, graph.py, and visualize.py into your project directory.
2. Import the necessary classes and functions from these files into your own script.
3. Create an instance of the Graph class and add nodes and edges to represent your maze.
4. Set up the start node, target node, weight limit, and volume limit for the robot cleaner.
5. Use the A* algorithm to find the optimal path for collecting rubbish.
6. Process the output to collect the rubbish, update the robot's position, and dispose of the rubbish in the disposal nodes.

# Dependencies
The project has the following dependencies:
* Python 3
* Pygame

## License
This project is licensed under the [MIT License](LICENSE).