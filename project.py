# Authors: Antonio Lang, Ian Sturtz
# CPE 400 - Computer Communication Networks
# Script to generate a network and find the shortest path between nodes


import matplotlib.pyplot as plt
import networkx as nx

from enum import Enum

def main():
	"""Driver of the script"""
	
	run = True
	while(run):
		choice = get_input()
		try:
			choice = int(choice)

			if choice == Choice.GENERATE.value:
				print("Generate graph selected")
				graph = generate_graph(5)
			elif choice == Choice.DISPLAY.value:
				print("Display graph selected")
				display_graph(graph)
			elif choice == Choice.SUMMARY.value:
				network_summary(graph)
				
			elif choice == Choice.EXIT.value:
				run = False # or exit("Bye now!")
			else:
				print("Invalid choice selected")

		except ValueError:
			print("Option entered was not a number")

		
def djikstras_algorithm(start_node, end_node = None) -> dict:
	"""Calculates the shortest path from a node to other nodes

	:param start_node:
	:param end_node:
	:return path_dict: Dictionary of format {node : distance} for each other node
	"""
	pass

def get_input() -> str:
	"""Gets the menu selection from the user"""
	print("Select from the following options:\n"
		  "1. Generate Graph"
		  "2. Display Network Topology"
		  "3. Display Network Shortest-Path Summary"
		  "0. Exit")
	return input("Enter your choice: ")

def generate_graph(num_nodes: int) -> nx.classes.graph.Graph: 
	"""Generates and returns an AS network graph
	
	:param num_nodes: Number of nodes to generate
	:return network_graph: AS network graph
	"""
	try:
		num_nodes = int(num_nodes)
		network_graph = nx.random_internet_as_graph(num_nodes)
		return network_graph
	except ValueError:
		print("The number of nodes must be an integer")


def display_graph(network_graph: nx.classes.graph.Graph) -> None:
	"""Displays an existing AS network graph
	:param network_graph:
	"""
	if graph is not None:
		nx.draw(network_graph)
	else:
		print("A network graph must be created first!")


def network_summary(path_matrix): # tentative parameters
	"""Dislpay a summary of shortest paths from all nodes to all others
	"""

	"""
	call get_all_shortest_paths
	display paths
	"""
	pass

def get_all_shortest_paths(network: nx.classes.graph.Graph) -> dict:
	"""Calculates Djikstra's Algorithm from all nodes

	:param network: Graph of the network
	:return distances: dict of Distances from a node to other nodes
	"""


	"""
	for node in graph:
		djikstras(start_end)
	"""

	pass

class Choice(Enum):
	"""Enum class for menu selections"""
	EXIT = 0
	GENERATE = 1
	DISPLAY = 2
	SUMMARY = 3

if __name__ == "__main__":
	main()