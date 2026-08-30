class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        psgs = defaultdict(int)

        for i in range(len(trips)):
            for km in range(trips[i][1], trips[i][2]):
                psgs[km] += trips[i][0]
                if psgs[km] > capacity:
                    return False

        return True