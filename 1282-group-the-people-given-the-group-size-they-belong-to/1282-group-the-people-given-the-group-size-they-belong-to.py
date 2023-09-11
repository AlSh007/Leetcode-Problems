class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        size_to_group, res = defaultdict(list), []
        for i, size in enumerate(groupSizes):
            size_to_group[size].append(i)
            if len(size_to_group[size]) == size:
                res.append(size_to_group.pop(size))
        return res