import networkx as nx
import matplotlib.pyplot as plt
def plot_graph():
    G = nx.Graph()

    num_node = 16
    self_link = [(i, i) for i in range(num_node)]
    neighbor_link = [(0, 1), (0, 10), (0, 13),
                     (1, 2),
                     (2, 3), (2, 4), (2, 7),
                     (4, 5),
                     (5, 6),
                     (7, 8),
                     (8, 9),
                     (10, 11),
                     (11, 12),
                     (13, 14),
                     (14, 15)]

    edges = self_link + neighbor_link
    G.add_edges_from(edges)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='gray', node_size=3000, font_size=20, font_color='black')

    plt.title('Graph Visualization')
    plt.show()




    num_node = 16
    self_link = [(i, i) for i in range(num_node)]
    neighbor_link = [(0, 1), (0, 10), (0, 13),
                     (1, 2),
                     (2, 3), (2, 4), (2, 7),
                     (4, 5),
                     (5, 6),
                     (7, 8),
                     (8, 9),
                     (10, 11),
                     (11, 12),
                     (13, 14),
                     (14, 15)]

    edges = self_link + neighbor_link
    G.add_edges_from(edges)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='gray', node_size=3000, font_size=20, font_color='black')

    plt.title('Graph Visualization')
    plt.show()

plot_graph()

"""
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def plot_adjacency(adjacency_matrix, title="Graph"):
    G = nx.from_numpy_array(adjacency_matrix)
    pos = nx.spring_layout(G)
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='gray', node_size=3000, font_size=20, font_color='black')
    plt.title(title)
    plt.show()

# 인접 행렬 예제
num_node = 16
hop_dis = np.random.randint(0, 4, size=(num_node, num_node))  # 임의의 홉 거리 행렬 생성

class Graph:
    def __init__(self):
        self.num_node = num_node
        self.max_hop = 3
        self.dilation = 1
        self.hop_dis = hop_dis
        self.center = 0

    def normalize_digraph(self, A):
        Dl = np.sum(A, 0)
        num_node = A.shape[0]
        Dn = np.zeros((num_node, num_node))
        for i in range(num_node):
            if Dl[i] > 0:
                Dn[i, i] = Dl[i]**(-1)
        AD = np.dot(A, Dn)
        return AD

    def get_adjacency(self, strategy):
        valid_hop = range(0, self.max_hop + 1, self.dilation)
        adjacency = np.zeros((self.num_node, self.num_node))
        for hop in valid_hop:
            adjacency[self.hop_dis == hop] = 1
        normalize_adjacency = self.normalize_digraph(adjacency)

        if strategy == 'uniform':
            A = np.zeros((1, self.num_node, self.num_node))
            A[0] = normalize_adjacency
            self.A = A
        elif strategy == 'distance':
            A = np.zeros((len(valid_hop), self.num_node, self.num_node))
            for i, hop in enumerate(valid_hop):
                A[i][self.hop_dis == hop] = normalize_adjacency[self.hop_dis == hop]
            self.A = A
        elif strategy == 'spatial':
            A = []
            for hop in valid_hop:
                a_root = np.zeros((self.num_node, self.num_node))
                a_close = np.zeros((self.num_node, self.num_node))
                a_further = np.zeros((self.num_node, self.num_node))
                for i in range(self.num_node):
                    for j in range(self.num_node):
                        if self.hop_dis[j, i] == hop:
                            if self.hop_dis[j, self.center] == self.hop_dis[i, self.center]:
                                a_root[j, i] = normalize_adjacency[j, i]
                            elif self.hop_dis[j, self.center] > self.hop_dis[i, self.center]:
                                a_close[j, i] = normalize_adjacency[j, i]
                            else:
                                a_further[j, i] = normalize_adjacency[j, i]
                if hop == 0:
                    A.append(a_root)
                else:
                    A.append(a_root + a_close)
                    A.append(a_further)
            A = np.stack(A)
            self.A = A
        else:
            raise ValueError("Do Not Exist This Strategy")

graph = Graph()
graph.get_adjacency('uniform')
plot_adjacency(graph.A[0], title="Uniform Strategy")

graph.get_adjacency('distance')
plot_adjacency(np.sum(graph.A, axis=0), title="Distance Strategy")

graph.get_adjacency('spatial')
plot_adjacency(np.sum(graph.A, axis=0), title="Spatial Strategy")


import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def get_hop_distance(num_node, edge, max_hop=1):
    A = np.zeros((num_node, num_node))
    for i, j in edge:
        A[j, i] = 1
        A[i, j] = 1

    # compute hop steps
    hop_dis = np.zeros((num_node, num_node)) + np.inf
    transfer_mat = [np.linalg.matrix_power(A, d) for d in range(max_hop + 1)]
    arrive_mat = (np.stack(transfer_mat) > 0)
    for d in range(max_hop, -1, -1):
        hop_dis[arrive_mat[d]] = d
    return hop_dis

def plot_hop_distance(hop_distance_matrix, title="Hop Distance Graph"):
    G = nx.from_numpy_array(hop_distance_matrix)
    pos = nx.spring_layout(G)
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='gray', node_size=3000, font_size=20, font_color='black')
    plt.title(title)
    plt.show()

# 인접 행렬 예제
num_node = 16
edge = [(0, 1), (0, 10), (0, 13),
        (1, 2),
        (2, 3), (2, 4), (2, 7),
        (4, 5),
        (5, 6),
        (7, 8),
        (8, 9),
        (10, 11),
        (11, 12),
        (13, 14),
        (14, 15)]

hop_distance_matrix = get_hop_distance(num_node, edge, max_hop=3)
plot_hop_distance(hop_distance_matrix, title="Hop Distance Graph")
"""