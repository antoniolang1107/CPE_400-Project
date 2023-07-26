# Authors: Antonio Lang, Ian Sturtz
# CPE 400 - Computer Communication Networks
# Script to generate a network and find the shortest path between nodes


import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

from enum import Enum

def main():
	"""Driver of the script"""

	run = True
	graph = None
	while(run):
		choice = get_input()
		try:
			choice = int(choice)

			#Function 1: generate network graph
			if choice == Choice.GENERATE.value:
				num_nodes = input("Enter the number of nodes in the network: ")
				graph = generate_graph(num_nodes)
			#Function 2: display network graph
			elif choice == Choice.DISPLAY.value:
				display_graph(graph)
			#Function 3: display Dijkstra's shortest paths
			elif choice == Choice.SUMMARY.value:
				network_summary(graph)
			elif choice == Choice.ROUTE.value:
				find_path(graph)
			#Function 0: exit function
			elif choice == Choice.EXIT.value:
				run = False
				print("Bye now!\n")
			#Default: invalid choice
			else:
				print("Invalid choice selected\n")

		except ValueError:
			print("Option entered was not a number\n")

		
def djikstras_algorithm(graph, start_node) -> dict:
	"""Calculates the shortest path from a node to all nodes

	:param graph: AS network graph
	:param start_node: source node in the AS
	:return path_dict: Dictionary of format {node : distance from start_node} for all nodes
	"""
	
	unchecked_nodes = list(graph.nodes())
	path_dict = {}
 
    
	max_value = 10000

	for node in unchecked_nodes:
		path_dict[node] = max_value
   
	path_dict[int(start_node)] = 0
    
   
	while unchecked_nodes:
        
		current_min_node = None
        
		for node in unchecked_nodes: 
			if current_min_node == None:
				current_min_node = node
			elif path_dict[node] < path_dict[current_min_node]:
				current_min_node = node
        
		neighbors = list(graph.neighbors(current_min_node))
        
		for neighbor in neighbors:
           
			tentative_value = path_dict[current_min_node] + graph[current_min_node][neighbor]["weight"]
            
			if tentative_value < path_dict[neighbor]:
               
				path_dict[neighbor] = tentative_value
                
		unchecked_nodes.remove(current_min_node)
	return path_dict

def get_input() -> str:
	"""Gets the menu selection from the user

	:return: input string
	"""
	
	print("Select from the following options:\n"
		  "1. Generate Graph\n"
		  "2. Display Network Topology\n"
		  "3. Display Network Shortest-Path Summary\n"
		  "4. Find Shortest Path To-From Specified Nodes\n"
		  "0. Exit\n")
	return input("Enter your choice: ")

def generate_graph(num_nodes: int) -> nx.classes.graph.Graph: 
	"""Generates and returns an AS network graph
	
	:param num_nodes: Number of nodes to generate
	:return network_graph: AS network graph
	"""
	
	try:
		num_nodes = int(num_nodes)
		network_graph = nx.random_internet_as_graph(num_nodes)
		for i, edge in enumerate(network_graph.edges()):
			network_graph[edge[0]][edge[1]]['weight'] = np.random.randint(99, size=1)[0] + 1
		return network_graph
	except ValueError:
		print("The number of nodes must be an integer\n")


def display_graph(network_graph: nx.classes.graph.Graph):
	"""Displays an existing AS network graph
	
	:param network_graph: AS network graph
	"""
	
	if network_graph is not None:
		position = nx.kamada_kawai_layout(network_graph)
		labels = nx.get_edge_attributes(network_graph, "weight")
		nx.draw_networkx(network_graph,
						 pos=position,
						 node_size=250,
						 width=1.25)
		nx.draw_networkx_edge_labels(network_graph, position, labels)
		plt.title("AS Network Graph")
		plt.axis("off")
		plt.show()
	else:
		print("A network graph must be created first!\n")


def network_summary(network_graph: nx.classes.graph.Graph) -> None:
	"""Dislpay a summary of shortest paths from all nodes to all others
	
	:param network_graph: AS network graph
	"""

	if network_graph is not None:
		distances_dict_list = get_all_shortest_paths(network_graph)
		distance_matrix = distance_dict_to_matrix(distances_dict_list)
		display_distance_matrix(distance_matrix)
	else:
		print("A network graph must be created first!\n")

def get_all_shortest_paths(network: nx.classes.graph.Graph) -> list:
	"""Calculates Djikstra's Algorithm from all nodes

	:param network: AS network graph
	:return distances: dict of Distances from a node to other nodes
	"""

	shortest_paths = []

	for node in network.nodes():
		shortest_paths.append(djikstras_algorithm(network, node))
	return shortest_paths

def display_distance_matrix(distance_matrix: np.array) -> None:
	"""Displays the shortest distance matrix for all nodes to all others

	:param distance_matrix: 2-D numpy array with distance from source to destination node
	"""
	fig, ax = plt.subplots()
	ax.matshow(distance_matrix, cmap = 'Oranges')

	for (i,j), z in np.ndenumerate(distance_matrix):
		ax.text(j, i, z, ha = 'center', va = 'center')
	plt.title("Shortest Node-Node Paths")
	plt.xlabel("Destination Node")
	plt.ylabel("Source Node")
	plt.show()

def distance_dict_to_matrix(distances: list) -> np.array:
	"""Converts a list of distance dictionaries to a 2-D numpy array

	:param distances: list of dictionaries with distances to destination nodes
	:return distance_matrix: 2-D numpy array of distances from source to destination node
	"""
	num_nodes = len(distances)
	distance_matrix = np.empty([num_nodes,num_nodes])
	
	for i in range(num_nodes):
		for j in range(num_nodes):
			distance_matrix[i,j] = distances[i][j]
	return distance_matrix

def find_path(network_graph: nx.classes.graph.Graph) -> None:
	"""Finds the shortest path from a source to destination node

	:param network_graph: AS network graph
	"""

	if network_graph is not None:
		source, destination = get_source_dest_nodes(network_graph)
		path = None
		# path = djikstras_algorithm(source, destination)
		print(f"The shortest path from {source} to {destination} is: {path}")

	else:
		print("A network graph must be created first!\n")

def get_source_dest_nodes(network_graph: nx.classes.graph.Graph) -> tuple:
	"""Prompts the user for the source and destination nodes and returns repsective values

	:param network_graph: AS network graph
	:return: source node, destination node
	"""
	index = 0
	graph_nodes = network_graph.nodes()
	nodes_name = ['starting', 'ending']
	nodes = [None, None]
	while index < 2:
		node = input(f"Please enter the {nodes_name[index]} node: ")
		try:
			node = int(node)
			if node in graph_nodes:
				nodes[index] = node
				index += 1
			else:
				print("Node entered is not in the network")
		except ValueError:
			print("Node entered was not a number\n")

	return nodes[0], nodes[1]

class Choice(Enum):
	"""Enum class for menu selections"""
	EXIT = 0
	GENERATE = 1
	DISPLAY = 2
	SUMMARY = 3
	ROUTE = 4

if __name__ == "__main__":
	main()