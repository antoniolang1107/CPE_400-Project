# CPE_400-Project

Authors: Antonio Lang, Ian Sturtz
Due: Wednesday, July 26th, 2023
Project description: Simulation of AS network and implementation of Dijkstra's shortest path finding algorithm
to find the shortest paths between devices across the network.

# Package installation and running the program:

Both python and networkx are required to properly run the program. To get all required packages, run the following command via terminal:

* `pip install -r requirements.txt`

and then use the following command via terminal to run the program:

* `python project.py`

# Using the program:

Once the program has been run, the user will encounter a main menu with a list of 4 options. Enter the number corresponding
with the intended command to get the following functionality:

1 - Generate Graph:
 - This will prompt the user to enter the number of nodes intended for the simulated network. Enter a positive natural number to generate an AS network with that many nodes and randomly generated paths and corresponding weights between each node.

2 - Display Network Topology:
 - This will create a pop-up window with the complete AS network, as generated using Function 1. In this window, you may zoom in, scroll around, and other navigation features. Each node will be represented by a blue circle with a number to label it, and each path will be represented by a line with its corresponding weight in the middle. If no network has been generated using Function 1, this Function will generate an error message and return you to the main menu. To resume use of the program, close out of this pop-up window.

3 - Display Network Shortest-Path Summary:
 - This will create a pop-up window with a 2-Dimensional matrix, with each value on the x-axis corresponding with source nodes and each value on the y-axis corresponding with destination nodes. Each node from the network generated using Function 1 will appear here. Additionally, the shortest path distance between nodes, as calculated using Dijkstra's algorithm, will appear in each cell. For reference, the shortest path distance between Node X and Node Y will appear in cell [X,Y]. The distance between a node and itself (i.e. cell [X, X]) is 0. Each cell is color coded, with larger paths colored in darker shades of orange. If no network has been generated using Function 1, this Function will generate an error message and return you to the main menu. To resume use of the program, close out of this pop-up window.

4 - Find Shortest Path To-From Specified Nodes:
- This will prompt the user for a specified source node and destination node. Then, it will run Dijkstra's algorithm in a similar fashion to Function 3, but isolating the path between the two input source and destination nodes. It will then output the distance to the user, as well as the specific path taken in the format of [source node, ordered intermediate nodes ..., destination node].

0 - Exit:
 - This function will exit the program.

 # Results and analysis:

 This program helps to demonstrate a simulated AS network, using python matplotlib to show visual diagrams of the connections within the generated network. Since the scope of our project did not include generating local preference values, this program instead helps to simulate an AS network's implementation of Border Gateway Protocol's second elimination rule to select a route to a network prefix: using Dijkstra's algorithm to find the shortest AS path. This program's third function, as specified above in the "Using the program" section, will generate a table of shortest paths between each node in the generated AS network. In using BGP's elimination rules to select a route, since there are no local preference values between nodes, BGP would determine that the shortest path specified in the table our program generates would be the path selected.