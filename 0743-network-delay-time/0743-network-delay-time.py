class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        import heapq
        heap = [(0, k)] 
        visited = set()
        links = {}
        table = {}

        for i in range(1, n+1, 1):
            table[i] = float("inf")
        table[k] = 0

        for node, destination, time in times:
            links.setdefault(node, []).append((destination, time))

        while heap:
            distance, current_node = heapq.heappop(heap)
            if distance != table[current_node]:
                continue
            if current_node in visited:
                continue
    
            for neighbour, time in links.get(current_node, []):
                new_distance = time + distance
                if new_distance < table[neighbour]:
                    table[neighbour] = new_distance
                    heapq.heappush(heap, (new_distance, neighbour))
            
            visited.add(current_node)
        total = max(table.values())
        
        return total if total < float("inf") else -1


        
        
            


        