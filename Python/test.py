import matplotlib.pyplot as plt
import networkx as nx

# 집과 길 정보
edges = [
    (1, 2, 3), (1, 3, 2), (3, 2, 1), (2, 5, 2),
    (3, 4, 4), (7, 3, 6), (5, 1, 5), (1, 6, 2),
    (6, 4, 1), (6, 5, 3), (4, 5, 3), (6, 7, 4)
]

# 그래프 생성
G = nx.Graph()

# 집 연결 및 비용 추가
for u, v, cost in edges:
    G.add_edge(u, v, weight=cost)

# 좌표 설정
pos = nx.spring_layout(G)

# 그래프 그리기
plt.figure(figsize=(8, 8))
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=12, font_weight='bold')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("House and Road Connections with Costs")
plt.show()
