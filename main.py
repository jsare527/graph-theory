import networkx as nx
import matplotlib.pyplot as plt
import random
import time


graph_types = ["Sparse", "Dense", "Complete"]
node_counts = [100, 200, 300, 400, 500]
results = {graph_type: [] for graph_type in graph_types}

def generate_graph(graph_type, num_nodes):
    if graph_type == "Sparse":
        return nx.gnm_random_graph(num_nodes, num_nodes * 2)
    elif graph_type == "Dense":
        return nx.gnm_random_graph(num_nodes, num_nodes * (num_nodes - 1) // 2 // 3)
    elif graph_type == "Complete":
        return nx.complete_graph(num_nodes)
    
def run_dijkstra():
    for graph_type in graph_types:
        for num_nodes in node_counts:
            G = generate_graph(graph_type, num_nodes)

            for (u, v) in G.edges():
                G.edges[u, v]['weight'] = random.randint(1, 10)

            start_time = time.time()
            nx.single_source_dijkstra_path_length(G, source=0)
            execution_time = time.time() - start_time

            results[graph_type].append(execution_time)

    plt.figure(figsize=(10, 6))
    for graph_type in graph_types:
        plt.plot(node_counts, results[graph_type], marker='o', label=graph_type)

    plt.title("Dijkstra's Algorithm Execution Time on Different Graph Types")
    plt.xlabel("Number of Nodes")
    plt.ylabel("Execution Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.show()
    print(results)

def run_bellman():
    for graph_type in graph_types:
        for num_nodes in node_counts:
            G = generate_graph(graph_type, num_nodes)

            for (u, v) in G.edges():
                G.edges[u, v]['weight'] = random.randint(1, 10)

            start_time = time.time()
            nx.single_source_bellman_ford_path_length(G, source=0)
            execution_time = time.time() - start_time

            results[graph_type].append(execution_time)

    plt.figure(figsize=(10, 6))
    for graph_type in graph_types:
        plt.plot(node_counts, results[graph_type], marker='o', label=graph_type)

    plt.title("Bellman-Ford Algorithm Execution Time on Different Graph Types")
    plt.xlabel("Number of Nodes")
    plt.ylabel("Execution Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.show()
    print(results)

def run_astar():
    for graph_type in graph_types:
        for num_nodes in node_counts:
            G = generate_graph(graph_type, num_nodes)

            for (u,v) in G.edges():
                G.edges[u, v]['weight'] = random.randint(1, 10)

            source, target = random.sample(list(G.nodes), 2)

            def heuristic(u, v):
                return 0 # No specific heuristic (acts like Dijkstra)
            
            start_time = time.time()
            try:
                nx.astar_path_length(G, source, target, heuristic=heuristic)
            except nx.NetworkXNoPath:
                pass

            execution_time = time.time() - start_time
            results[graph_type].append(execution_time)

    plt.figure(figsize=(10, 6))
    for graph_type in graph_types:
        plt.plot(node_counts, results[graph_type], marker='o', label=graph_type)

    plt.title("A* Algorithm Execution Time for Sparse, Dense, and Complete Graphs")
    plt.xlabel("Number of Nodes")
    plt.ylabel("Execution Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.show()
    print(results)

def visualize_sparse_graph():
    G = generate_graph("Sparse", 20)
    for (u, v) in G.edges():
        G.edges[u, v]['weight'] = random.randint(1, 10)

    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=800, edge_color='gray')
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)})
    plt.title("Visualization of a Sparse graph with 20 nodes")
    plt.show()

def visualize_dense_graph():
    G = generate_graph("Dense", 20)
    for (u, v) in G.edges():
        G.edges[u, v]['weight'] = random.randint(1, 10)

    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=800, edge_color='gray')
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)})
    plt.title("Visualization of a Sparse graph with 20 nodes")
    plt.show()

def visualize_complete_graph():
    G = generate_graph("Complete", 20)
    for (u, v) in G.edges():
        G.edges[u, v]['weight'] = random.randint(1, 10)

    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=800, edge_color='gray')
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)})
    plt.title("Visualization of a Sparse graph with 20 nodes")
    plt.show()

if __name__ == '__main__':
    run_astar()