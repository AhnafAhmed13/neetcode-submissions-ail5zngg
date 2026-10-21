class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # key: value
        self.cnt = {} # key: freq
        self.use = [] # get/put

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cnt[key] += 1
            self.use.remove(key)
            self.use.append(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        # Update
        if key in self.cache:
            self.cache[key] = value
            self.cnt[key] += 1
            self.use.remove(key)
            self.use.append(key)
        else: # Add
            if len(self.cache) == self.cap: # Full
                min_val = float("inf")
                candidates = set()
                for k, freq in self.cnt.items():
                    if freq < min_val:
                        min_val = freq
                        candidates = set([k])
                    elif freq == min_val:
                        candidates.add(k)
                if len(candidates) == 1: # No-tie
                    LFU = candidates.pop()
                    self.use.remove(LFU)
                    del self.cache[LFU]
                    del self.cnt[LFU]
                else: # Tie
                    cnt = 0; i = len(self.use) - 1
                    while i >= 0:
                        if self.use[i] in candidates:
                            cnt += 1
                            if cnt == len(candidates):
                                LFU = self.use[i]
                                self.use.remove(LFU)
                                del self.cache[LFU]
                                del self.cnt[LFU]
                                break
                        i -= 1
            self.cache[key] = value
            self.cnt[key] = 1
            self.use.append(key)



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)