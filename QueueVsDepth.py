import matplotlib.pyplot as plt
import numpy as np

#from the angie.py tests
node_depths = [0, 2, 4, 8, 12, 16, 20]
uniform_cost_search = [0, 5, 17, 156, 1127, 6035, 17066]
misplaced_tile_heuristic = [0, 3, 9, 43, 294, 1465, 3864]
manhattan_distance_heuristic = [0, 3, 6, 30, 252, 1263, 2476]

plt.figure(figsize=(10, 6))
plt.plot(node_depths, uniform_cost_search, marker='o', label='Uniform Cost Search')
plt.plot(node_depths, misplaced_tile_heuristic, marker='o', label='Misplaced Tile Heuristic')
plt.plot(node_depths, manhattan_distance_heuristic, marker='o', label='Manhattan Distance Heuristic')

plt.title('Maximum Queue Size vs Node Depth')
plt.xlabel('Node Depth')
plt.ylabel('Maximum Queue Size')
plt.legend()
plt.grid(True)

plt.xticks(np.arange(min(node_depths), max(node_depths) + 1, 2))

plt.show()