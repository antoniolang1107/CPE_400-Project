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

		
def djikstras_algorithm(start_node, end_node = None) -> dict:
	"""Calculates the shortest path from a node to all nodes

	:param start_node:
	:param end_node:
	:return path_dict: Dictionary of format {node : distance} for all nodes
	"""

	# include {start_node : 0} in the dict
	pass

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


def display_graph(network_graph: nx.classes.graph.Graph) -> None:
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
		plt.show()
	else:
		print("A network graph must be created first!\n")


def network_summary(network_graph: nx.classes.graph.Graph) -> None:
	"""Dislpay a summary of shortest paths from all nodes to all others
	
	:param network_graph:
	"""

	distances_dict_list = get_all_shortest_paths(network_graph)
	# below list is for testing
	distances_dict_list = [{0: 0, 1:5, 2:20}, 
						  {0:5, 1:0, 2:15}, 
						  {0:20, 1:15, 2:0}]
	distance_matrix = distance_dict_to_matrix(distances_dict_list)
	display_distance_matrix(distance_matrix)

def get_all_shortest_paths(network: nx.classes.graph.Graph) -> list:
	"""Calculates Djikstra's Algorithm from all nodes

	:param network: Graph of the network
	:return distances: dict of Distances from a node to other nodes
	"""

	shortest_paths = []

	for node in network.nodes():
		shortest_paths.append(djikstras_algorithm(node))
	return shortest_paths

def display_distance_matrix(distance_matrix) -> None:
	plt.matshow(distance_matrix)
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