import networkx as nx
import matplotlib.pyplot as plt

class Graf:
    def __init__(self, directed=False):
        """
        Initialize a graph object
        
        Parameters:
        directed (bool): If True, creates a directed graph. Default is False (undirected).
        """
        if directed:
            self.graph = nx.DiGraph()
        else:
            self.graph = nx.Graph()
    
    def add_node(self, node):
        """
        Add a node to the graph
        
        Parameters:
        node: Node identifier (can be int, string, etc.)
        """
        self.graph.add_node(node)
    
    def add_edge(self, node1, node2, weight=1):
        """
        Add an edge between two nodes
        
        Parameters:
        node1: First node
        node2: Second node
        weight: Edge weight (default is 1)
        """
        self.graph.add_edge(node1, node2, weight=weight)
    
    def visualize_graph(self):
        """
        Visualize the graph using matplotlib
        """
        plt.figure(figsize=(10, 8))
        pos = nx.spring_layout(self.graph, seed=42)
        
        # Draw nodes
        nx.draw_networkx_nodes(self.graph, pos, node_color='lightblue', 
                              node_size=1000, alpha=0.9)
        
        # Draw edges
        nx.draw_networkx_edges(self.graph, pos, width=2, alpha=0.6)
        
        # Draw labels
        nx.draw_networkx_labels(self.graph, pos, font_size=14, font_weight='bold')
        
        # Draw edge labels (weights)
        edge_labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels, font_size=10)
        
        plt.title("Graph Visualization")
        plt.axis('off')
        plt.tight_layout()
        plt.show()
    
    def shortest_path(self, source, target):
        """
        Find the shortest path between two nodes
        
        Parameters:
        source: Starting node
        target: Ending node
        
        Returns:
        list: Shortest path from source to target
        """
        try:
            path = nx.shortest_path(self.graph, source, target, weight='weight')
            return path
        except nx.NetworkXNoPath:
            print(f"No path exists between {source} and {target}")
            return None
        except nx.NodeNotFound as e:
            print(f"Node not found: {e}")
            return None
    
    def visual_shortest_path(self, source, target):
        """
        Visualize the shortest path between two nodes
        
        Parameters:
        source: Starting node
        target: Ending node
        """
        try:
            path = nx.shortest_path(self.graph, source, target, weight='weight')
            
            plt.figure(figsize=(10, 8))
            pos = nx.spring_layout(self.graph, seed=42)
            
            # Draw all nodes
            nx.draw_networkx_nodes(self.graph, pos, node_color='lightblue', 
                                  node_size=1000, alpha=0.9)
            
            # Highlight path nodes
            nx.draw_networkx_nodes(self.graph, pos, nodelist=path, 
                                  node_color='lightgreen', node_size=1000, alpha=0.9)
            
            # Draw all edges
            nx.draw_networkx_edges(self.graph, pos, width=2, alpha=0.3)
            
            # Highlight path edges
            path_edges = list(zip(path, path[1:]))
            nx.draw_networkx_edges(self.graph, pos, edgelist=path_edges, 
                                  width=4, edge_color='red', alpha=0.8)
            
            # Draw labels
            nx.draw_networkx_labels(self.graph, pos, font_size=14, font_weight='bold')
            
            # Draw edge labels
            edge_labels = nx.get_edge_attributes(self.graph, 'weight')
            nx.draw_networkx_edge_labels(self.graph, pos, edge_labels, font_size=10)
            
            plt.title(f"Shortest Path from {source} to {target}")
            plt.axis('off')
            plt.tight_layout()
            plt.show()
            
        except nx.NetworkXNoPath:
            print(f"No path exists between {source} and {target}")
        except nx.NodeNotFound as e:
            print(f"Node not found: {e}")
    
    # Additional methods for graph analysis
    
    def get_degree(self, node=None):
        """
        Get the degree of a node or all nodes
        
        Parameters:
        node: Specific node (optional). If None, returns degrees of all nodes.
        
        Returns:
        dict or int: Degree(s) of node(s)
        """
        if node is not None:
            return self.graph.degree(node)
        else:
            return dict(self.graph.degree())
    
    def is_connected(self):
        """
        Check if the graph is connected
        
        Returns:
        bool: True if connected, False otherwise
        """
        if isinstance(self.graph, nx.DiGraph):
            return nx.is_weakly_connected(self.graph)
        else:
            return nx.is_connected(self.graph)
    
    def find_cycles(self):
        """
        Find all cycles in the graph
        
        Returns:
        list: List of cycles
        """
        try:
            cycles = list(nx.simple_cycles(self.graph))
            return cycles if cycles else None
        except:
            # For undirected graphs, find cycle basis
            cycles = nx.cycle_basis(self.graph)
            return cycles if cycles else None
    
    def has_cycle(self):
        """
        Check if the graph has any cycle
        
        Returns:
        bool: True if graph has cycle, False otherwise
        """
        cycles = self.find_cycles()
        return cycles is not None and len(cycles) > 0
    
    def bfs(self, start_node):
        """
        Perform Breadth-First Search starting from a node
        
        Parameters:
        start_node: Starting node for BFS
        
        Returns:
        list: Nodes in BFS order
        """
        return list(nx.bfs_tree(self.graph, start_node).nodes())
    
    def dfs(self, start_node):
        """
        Perform Depth-First Search starting from a node
        
        Parameters:
        start_node: Starting node for DFS
        
        Returns:
        list: Nodes in DFS order
        """
        return list(nx.dfs_tree(self.graph, start_node).nodes())
    
    def dijkstra(self, source, target=None):
        """
        Apply Dijkstra's algorithm to find shortest paths
        
        Parameters:
        source: Starting node
        target: Target node (optional). If None, finds paths to all nodes.
        
        Returns:
        dict or tuple: If target is None, returns dict of distances to all nodes.
                       If target is specified, returns (distance, path).
        """
        if target is None:
            # Return distances to all nodes
            distances = nx.single_source_dijkstra_path_length(self.graph, source, weight='weight')
            return dict(distances)
        else:
            # Return distance and path to specific target
            distance = nx.shortest_path_length(self.graph, source, target, weight='weight')
            path = nx.shortest_path(self.graph, source, target, weight='weight')
            return distance, path
    
    def get_nodes(self):
        """
        Get all nodes in the graph
        
        Returns:
        list: List of all nodes
        """
        return list(self.graph.nodes())
    
    def get_edges(self):
        """
        Get all edges in the graph
        
        Returns:
        list: List of all edges
        """
        return list(self.graph.edges(data=True))
    
    def number_of_nodes(self):
        """
        Get the number of nodes in the graph
        
        Returns:
        int: Number of nodes
        """
        return self.graph.number_of_nodes()
    
    def number_of_edges(self):
        """
        Get the number of edges in the graph
        
        Returns:
        int: Number of edges
        """
        return self.graph.number_of_edges()
    
    def get_neighbors(self, node):
        """
        Get neighbors of a specific node
        
        Parameters:
        node: Node to get neighbors for
        
        Returns:
        list: List of neighboring nodes
        """
        return list(self.graph.neighbors(node))
