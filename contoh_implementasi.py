"""
Contoh Implementasi Graf - Sesuai dengan Spesifikasi Proyek

Proyek ini mendemonstrasikan penggunaan kelas Graf untuk analisis teori graf.
"""

from graf import Graf

def main():
    print("="*60)
    print("CONTOH IMPLEMENTASI TEORI GRAF")
    print("="*60)
    
    # Membuat Object
    print("\n1. Membuat Object Graf")
    graph = Graf()
    print("   graph = Graf()")
    
    # Menambah Node (titik)
    print("\n2. Menambah Node (titik)")
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_node(4)
    graph.add_node(5)
    print("   Nodes ditambahkan: 1, 2, 3, 4, 5")
    
    # Menambah sisi (Edge)
    print("\n3. Menambah Sisi (Edge) dengan Bobot")
    graph.add_edge(1, 2, weight=4.5)
    graph.add_edge(1, 3, weight=3.2)
    graph.add_edge(2, 4, weight=2.7)
    graph.add_edge(3, 4, weight=1.8)
    graph.add_edge(1, 4, weight=6.7)
    graph.add_edge(3, 5, weight=2.7)
    print("   Edges ditambahkan dengan bobot:")
    print("   (1-2: 4.5), (1-3: 3.2), (2-4: 2.7)")
    print("   (3-4: 1.8), (1-4: 6.7), (3-5: 2.7)")
    
    # Visualisasi Graf
    print("\n4. Visualisasi Graf")
    print("   graph.visualize_graph()")
    print("   (Graf akan ditampilkan dalam window terpisah)")
    graph.visualize_graph()
    
    # Jalur terpendek
    print("\n5. Mencari Jalur Terpendek")
    path = graph.shortest_path(1, 5)
    print(f"   graph.shortest_path(1, 5)")
    print(f"   Hasil: {path}")
    
    # Visualisasi Jalur terpendek
    print("\n6. Visualisasi Jalur Terpendek")
    print("   graph.visual_shortest_path(1, 5)")
    print("   (Graf dengan jalur terpendek akan ditampilkan)")
    graph.visual_shortest_path(1, 5)
    
    # Mendemonstrasikan metode tambahan
    print("\n" + "="*60)
    print("METODE TAMBAHAN")
    print("="*60)
    
    # Derajat simpul
    print("\n7. Derajat Simpul")
    degrees = graph.get_degree()
    print("   graph.get_degree()")
    for node in sorted(degrees.keys()):
        print(f"   Node {node}: degree {degrees[node]}")
    
    # Cek konektivitas
    print("\n8. Konektivitas Graf")
    is_connected = graph.is_connected()
    print(f"   graph.is_connected()")
    print(f"   Hasil: {is_connected}")
    
    # Cek cycle
    print("\n9. Deteksi Cycle")
    has_cycle = graph.has_cycle()
    print(f"   graph.has_cycle()")
    print(f"   Hasil: {has_cycle}")
    if has_cycle:
        cycles = graph.find_cycles()
        print(f"   Cycles yang ditemukan: {cycles}")
    
    # BFS
    print("\n10. Breadth-First Search (BFS)")
    bfs_result = graph.bfs(1)
    print(f"   graph.bfs(1)")
    print(f"   Urutan kunjungan: {bfs_result}")
    
    # DFS
    print("\n11. Depth-First Search (DFS)")
    dfs_result = graph.dfs(1)
    print(f"   graph.dfs(1)")
    print(f"   Urutan kunjungan: {dfs_result}")
    
    # Dijkstra ke semua node
    print("\n12. Algoritma Dijkstra (jarak ke semua node)")
    distances = graph.dijkstra(1)
    print(f"   graph.dijkstra(1)")
    for node in sorted(distances.keys()):
        print(f"   Jarak dari 1 ke {node}: {distances[node]:.1f}")
    
    # Dijkstra ke node tertentu
    print("\n13. Algoritma Dijkstra (ke node tertentu)")
    distance, path = graph.dijkstra(1, 5)
    print(f"   graph.dijkstra(1, 5)")
    print(f"   Jarak: {distance:.1f}")
    print(f"   Jalur: {path}")
    
    # Informasi graf
    print("\n14. Informasi Graf")
    print(f"   Jumlah nodes: {graph.number_of_nodes()}")
    print(f"   Jumlah edges: {graph.number_of_edges()}")
    print(f"   Semua nodes: {graph.get_nodes()}")
    
    # Tetangga node
    print("\n15. Tetangga Setiap Node")
    for node in sorted(graph.get_nodes()):
        neighbors = graph.get_neighbors(node)
        print(f"   Tetangga node {node}: {neighbors}")
    
    print("\n" + "="*60)
    print("SELESAI")
    print("="*60)

if __name__ == "__main__":
    main()
