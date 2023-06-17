from data import MapData
from entities import Worker
from lazy_picker import read_map_data
from service import Map
"""--------------------------------------------------------
    This contains all the scripts for testing
    --------------------------------------------------------"""""
"""--------------------------------------------------------
    Test for configuration should be written below
    --------------------------------------------------------"""""
items, shelves = read_map_data('qvBox-warehouse-data-s23-v01.txt')

worker = Worker(0, 0)

item_id = 1500
target = None
"""-------------------------------------------------------- 
   Data initialization should be written below
--------------------------------------------------------"""

for item in items:
    if item.item_id == item_id:
        target = item
        break
    else:
        continue

map_data = MapData(worker, shelves, items, target)

"""--------------------------------------------------------
    All the test for algorithm should be written below
    --------------------------------------------------------"""
grid = Map(map_data)
# grid.dijkstra()
grid.a_star()
# grid.bfs()

# while True:
#     print("NEXT ITERATION")
#     input()
#     grid.iterate(algorithm='Dijkstra')

# for testing
