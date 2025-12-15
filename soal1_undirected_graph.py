"""
Soal 1 — Graf Tak Berarah, Derajat, dan Konektivitas

Diberikan graf tak berarah G = (V, E) dengan:
V = {A, B, C, D, E, F}
E = {(A, B),(A, C),(B, D),(C, E),(D, E),(E, F),(C, F)}

a. Gambarkan graf berdasarkan himpunan sisi di atas.
b. Tentukan derajat setiap simpul.
c. Tentukan apakah graf memiliki cycle. Jika ada, sebutkan.
d. Tentukan apakah graf ini connected. Jelaskan.
"""

from graf import Graf

def solve_problem_1():
    print("="*60)
    print("SOAL 1 - Graf Tak Berarah, Derajat, dan Konektivitas")
    print("="*60)
    
    # Membuat graf tak berarah
    graph = Graf(directed=False)
    
    # Menambahkan nodes
    nodes = ['A', 'B', 'C', 'D', 'E', 'F']
    for node in nodes:
        graph.add_node(node)
    
    # Menambahkan edges
    edges = [
        ('A', 'B'),
        ('A', 'C'),
        ('B', 'D'),
        ('C', 'E'),
        ('D', 'E'),
        ('E', 'F'),
        ('C', 'F')
    ]
    
    for edge in edges:
        graph.add_edge(edge[0], edge[1])
    
    print("\nV = {A, B, C, D, E, F}")
    print("E = {(A, B),(A, C),(B, D),(C, E),(D, E),(E, F),(C, F)}")
    print()
    
    # a. Gambarkan graf
    print("a. Visualisasi Graf")
    print("   (Graf akan ditampilkan dalam window terpisah)")
    graph.visualize_graph()
    
    # b. Tentukan derajat setiap simpul
    print("\nb. Derajat Setiap Simpul:")
    degrees = graph.get_degree()
    for node in sorted(degrees.keys()):
        print(f"   Derajat simpul {node}: {degrees[node]}")
    
    # c. Tentukan apakah graf memiliki cycle
    print("\nc. Deteksi Cycle:")
    has_cycle = graph.has_cycle()
    if has_cycle:
        cycles = graph.find_cycles()
        print(f"   Graf MEMILIKI cycle")
        print(f"   Cycle yang ditemukan:")
        for i, cycle in enumerate(cycles, 1):
            # Tambahkan node pertama di akhir untuk menunjukkan cycle lengkap
            cycle_display = cycle + [cycle[0]]
            print(f"   Cycle {i}: {' -> '.join(map(str, cycle_display))}")
    else:
        print(f"   Graf TIDAK memiliki cycle")
    
    # d. Tentukan apakah graf connected
    print("\nd. Konektivitas Graf:")
    is_connected = graph.is_connected()
    if is_connected:
        print("   Graf adalah CONNECTED")
        print("   Penjelasan: Semua simpul dapat dijangkau dari simpul manapun.")
        print("   Setiap pasangan simpul memiliki jalur yang menghubungkannya.")
    else:
        print("   Graf adalah DISCONNECTED")
        print("   Penjelasan: Terdapat simpul yang tidak dapat dijangkau dari simpul lain.")
    
    print("\n" + "="*60)
    
    # Informasi tambahan
    print("\nINFORMASI TAMBAHAN:")
    print(f"Jumlah simpul (nodes): {graph.number_of_nodes()}")
    print(f"Jumlah sisi (edges): {graph.number_of_edges()}")
    
    print("\nTetangga setiap simpul:")
    for node in sorted(graph.get_nodes()):
        neighbors = graph.get_neighbors(node)
        print(f"   {node}: {sorted(neighbors)}")
    
    print("="*60)

if __name__ == "__main__":
    solve_problem_1()
