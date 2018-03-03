### Extended Round Score: 8,339,068

- A breadth first search along with a graph solution was our first attempt but the weighing and updating of the graph proved too time-consuming so we switched to a simpler possible solution.

### Strategy:  
  - For each vehicle determine best ride depending on metric of steps required (driving to location, waiting and bonus)  
  * Push all rides with graded metrics to MinHeap (Lowest steps = best ride)
  - Heappop and assign ride to vehicle
  * Check global steps left
  
    

