import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while (len(stones) > 1):
            stone1 = -heapq.heappop(stones)
            stone2 = -heapq.heappop(stones)

            if stone1 == stone2:
                continue
            elif stone1 > stone2:
                stone1 = stone1 - stone2
                heapq.heappush(stones, -stone1)
            elif stone2 > stone1:
                stone2 = stone2 - stone1
                heapq.heappush(stones, -stone2)
        
        return len(stones) == 1 and -heapq.heappop(stones) or 0