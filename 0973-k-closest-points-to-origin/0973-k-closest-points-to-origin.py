class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_list = []
        for point in points:
            dist = -(point[0]*point[0] + point[1]*point[1])
            if len(dist_list) <= k - 1:
                heapq.heappush(dist_list,(dist,point))
            else:
                if dist > dist_list[0][0]:
                    heapq.heappop(dist_list)
                    heapq.heappush(dist_list,(dist,point))
        res = []
        for i in range(k):
            res.append(heapq.heappop(dist_list)[1])
        return res
            