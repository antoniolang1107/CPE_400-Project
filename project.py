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

			if choice == Choice.GENERATE.value:
				num_nodes = input("Enter the number of nodes in the network: ")
				graph = generate_graph(num_nodes)
			elif choice == Choice.DISPLAY.value:
				display_graph(graph)
			elif choice == Choice.SUMMARY.value:
				network_summary(graph)
			elif choice == Choice.EXIT.value:
				run = False
				print("Bye now!\n")
			else:
				print("Invalid choice selected\n")

		except ValueError:
			print("Option entered was not a number\n")

		
def djikstras_algorithm(graph, start_node) -> dict:
	"""Calculates the shortest path from a node to all nodes

	:param graph:
	:param start_node:
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
	"""Gets the menu selection from the user"""
	
	print("Select from the following options:\n"
		  "1. Generate Graph\n"
		  "2. Display Network Topology\n"
		  "3. Display Network Shortest-Path Summary\n"
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
	
	:param network_graph:
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
	
	:param network_graph:
	"""
	if network_graph is not None:
		distances_dict_list = get_all_shortest_paths(network_graph)
		distance_matrix = distance_dict_to_matrix(distances_dict_list)
		display_distance_matrix(distance_matrix)
	else:
		print("A network graph must be created first!\n")

def get_all_shortest_paths(network: nx.classes.graph.Graph) -> list:
	"""Calculates Djikstra's Algorithm from all nodes

	:param network: Graph of the network
	:return distances: dict of Distances from a node to other nodes
	"""

	shortest_paths = []

	for node in network.nodes():
		shortest_paths.append(djikstras_algorithm(network, node))
	return shortest_paths

def display_distance_matrix(distance_matrix) -> None:
	fig, ax = plt.subplots()
	ax.matshow(distance_matrix, cmap = 'Oranges')

	for (i,j), z in np.ndenumerate(distance_matrix):
		ax.text(j, i, z, ha = 'center', va = 'center')
	plt.title("Shortest Node-Node Paths")
	plt.xlabel("Destination Node")
	plt.ylabel("Source Node")
	plt.show()

def distance_dict_to_matrix(distances: list) -> np.array:
	num_nodes = len(distances)
	distance_matrix = np.empty([num_nodes,num_nodes])
	
	for i in range(num_nodes):
		for j in range(num_nodes):
			distance_matrix[i,j] = distances[i][j]
	return distance_matrix


class Choice(Enum):
	"""Enum class for menu selections"""
	EXIT = 0
	GENERATE = 1
	DISPLAY = 2
	SUMMARY = 3

if __name__ == "__main__":
	main()