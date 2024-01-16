class RandomizedSet:

    def __init__(self):
        self.indices = {}
        self.data = []

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        self.data.append(val)
        self.indices[val] = len(self.data) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        
        i = self.indices[val]
        self.indices[self.data[-1]] = i
        
        self.data[i] = self.data[-1]
        
        self.indices.pop(val)
        self.data.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.data)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()