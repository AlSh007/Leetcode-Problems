class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        graph = defaultdict(set)
        
        for bus_num, stops in enumerate(routes):
            
            for stop in stops:
                graph[stop].add(bus_num)
        
        bfs = deque([(source, 0)])
        
        seen_stops = set()
        seen_buses = set()
        
        while bfs:
            stop, count = bfs.popleft()
            
            if stop == target:
                return count
            
            for bus_number in graph[stop]:
                if bus_number not in seen_buses:
                    seen_buses.add(bus_number)
                    
                    for stop in routes[bus_number]:
                        if stop not in seen_stops:
                            seen_stops.add(stop)
                            bfs.append((stop, count + 1))
        
        return -1
        
        
        