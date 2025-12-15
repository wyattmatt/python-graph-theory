"""
Soal 3 — BFS, DFS, dan Dijkstra

Diberikan graf berbobot:
V = {A, B, C, D, E, F, G}
E = {(A, B, 2),(A, C, 5),(B, D, 4),(B, E, 6),(C, F, 3),(D, G, 2),(E, F, 4),(F, G, 1)}

a. Gambarkan Grafnya!
b. Tentukan urutan kunjungan menggunakan Breadth-First Search (BFS) dimulai dari simpul A.
c. Tentukan urutan kunjungan menggunakan Depth-First Search (DFS) (rekursif)
   dengan simpul awal A dan urutan tetangga berdasarkan alfabet.
d. Gunakan Algoritma Dijkstra dari simpul A untuk menentukan:
   1. Jarak minimum dari A ke seluruh simpul.
   2. Jalur terpendek dari A ke G.
"""

from graf import Graf

def solve_problem_3():
    print("="*60)
    print("SOAL 3 - BFS, DFS, dan Dijkstra")
    print("="*60)
    
    # Membuat graf berbobot
    graph = Graf(directed=False)
    
    # Menambahkan nodes
    nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    for node in nodes:
        graph.add_node(node)
    
    # Menambahkan edges dengan bobot
    edges = [
        ('A', 'B', 2),
        ('A', 'C', 5),
        ('B', 'D', 4),
        ('B', 'E', 6),
        ('C', 'F', 3),
        ('D', 'G', 2),
        ('E', 'F', 4),
        ('F', 'G', 1)
    ]
    
    for edge in edges:
        graph.add_edge(edge[0], edge[1], weight=edge[2])
    
    print("\nV = {A, B, C, D, E, F, G}")
    print("E = {(A, B, 2),(A, C, 5),(B, D, 4),(B, E, 6),(C, F, 3),")
    print("     (D, G, 2),(E, F, 4),(F, G, 1)}")
    print()
    
    # a. Gambarkan graf
    print("a. Visualisasi Graf Berbobot")
    print("   (Graf akan ditampilkan dalam window terpisah)")
    graph.visualize_graph()
    
    # b. BFS dari simpul A
    print("\nb. Breadth-First Search (BFS) dari simpul A:")
    bfs_order = graph.bfs('A')
    print(f"   Urutan kunjungan: {' -> '.join(bfs_order)}")
    print(f"   Penjelasan: BFS mengunjungi simpul level per level,")
    print(f"   dimulai dari A, kemudian tetangga langsung A (B, C),")
    print(f"   lalu tetangga dari B dan C, dan seterusnya.")
    
    # c. DFS dari simpul A
    print("\nc. Depth-First Search (DFS) dari simpul A:")
    dfs_order = graph.dfs('A')
    print(f"   Urutan kunjungan: {' -> '.join(dfs_order)}")
    print(f"   Penjelasan: DFS mengeksplorasi sejauh mungkin sebelum backtrack.")
    print(f"   Dengan urutan tetangga alfabetis, DFS akan mengikuti")
    print(f"   cabang pertama hingga habis sebelum pindah ke cabang lain.")
    
    # d. Dijkstra dari simpul A
    print("\nd. Algoritma Dijkstra dari simpul A:")
    
    # d.1 Jarak minimum ke semua simpul
    print("\n   1. Jarak minimum dari A ke seluruh simpul:")
    distances = graph.dijkstra('A')
    for node in sorted(distances.keys()):
        print(f"      A ke {node}: {distances[node]}")
    
    # d.2 Jalur terpendek dari A ke G
    print("\n   2. Jalur terpendek dari A ke G:")
    distance_to_g, path_to_g = graph.dijkstra('A', 'G')
    print(f"      Jalur: {' -> '.join(path_to_g)}")
    print(f"      Total jarak: {distance_to_g}")
    print(f"\n      Penjelasan langkah jalur:")
    
    # Menampilkan detail setiap langkah
    for i in range(len(path_to_g) - 1):
        current = path_to_g[i]
        next_node = path_to_g[i + 1]
        # Cari bobot edge
        edge_data = graph.graph.get_edge_data(current, next_node)
        weight = edge_data['weight']
        print(f"      {current} -> {next_node}: bobot {weight}")
    
    print("\n   Visualisasi jalur terpendek A ke G:")
    print("   (Graf akan ditampilkan dalam window terpisah)")
    graph.visual_shortest_path('A', 'G')
    
    print("\n" + "="*60)
    
    # Informasi tambahan
    print("\nINFORMASI TAMBAHAN:")
    print(f"Jumlah simpul (nodes): {graph.number_of_nodes()}")
    print(f"Jumlah sisi (edges): {graph.number_of_edges()}")
    
    print("\nTetangga setiap simpul dengan bobot:")
    for node in sorted(graph.get_nodes()):
        neighbors = []
        for neighbor in sorted(graph.get_neighbors(node)):
            edge_data = graph.graph.get_edge_data(node, neighbor)
            weight = edge_data['weight']
            neighbors.append(f"{neighbor}(w={weight})")
        print(f"   {node}: {', '.join(neighbors)}")
    
    print("="*60)

if __name__ == "__main__":
    solve_problem_3()
