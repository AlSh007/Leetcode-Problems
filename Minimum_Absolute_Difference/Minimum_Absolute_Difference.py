def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = float('inf')
        dic = defaultdict(list)
        for i in range(len(arr) - 1):
            diff = arr[i + 1] - arr[i]
            dic[diff].append([arr[i], arr[i + 1]])
            min_diff = min(min_diff, diff)

        return dic[min_diff]