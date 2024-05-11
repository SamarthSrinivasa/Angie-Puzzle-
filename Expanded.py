import matplotlib.pyplot as plt
import numpy as np


#angie.py test
node_depths = [0, 2, 4, 8, 12, 16, 20]
uniform_cost_search = [1, 5, 25, 249, 1887, 11201, 38504]
letter = [1, 3, 8, 51, 472, 2452, 6951]
manhattan_a_star = [1, 3, 5, 39, 382, 2122, 4217]

plt.figure(figsize=(10, 6))
plt.plot(node_depths, uniform_cost_search, marker='o', label='Uniform Cost Search')
plt.plot(node_depths, letter, marker='o', label='Misplaced Tile')
plt.plot(node_depths, manhattan_a_star, marker='o', label='Manhattan (A*)')

plt.title('Nodes Expanded vs Node Depth')
plt.xlabel('Node Depth')
plt.ylabel('Nodes Expanded')
plt.legend()
plt.grid(True)

plt.xticks(np.arange(min(node_depths), max(node_depths) + 1, 2))

plt.show()