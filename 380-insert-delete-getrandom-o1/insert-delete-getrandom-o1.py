import random
class RandomizedSet:

    def __init__(self):
        self.data = []
        self.val_to_idx_map = {}

    def insert(self, val: int) -> bool:
        if val in self.val_to_idx_map:
            return False

        self.val_to_idx_map[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_idx_map:
            return False

        last_val = self.data[-1]
        idx = self.val_to_idx_map[val]
        self.data[idx] = last_val
        self.val_to_idx_map[last_val] = idx
        self.data.pop()
        del self.val_to_idx_map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.data)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()