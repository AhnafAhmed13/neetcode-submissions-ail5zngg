class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.time = 0
        self.history = {}
        self.cache = {}

    def get(self, key: int) -> int:
        print("get", key, self.cache, self.history)
        if key in self.cache:
            self.history[key] = self.time
            self.time += 1
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # if key already in cache / no pop needed
        if key in self.cache:
            self.cache[key] = value
            self.history[key] = self.time
            self.time += 1
        else: # if a new key
            # if capacity full
            if self.length == self.capacity:
                # find LRU
                LRU = None
                oldest_time = float("inf")
                for k, t in self.history.items():
                    if not LRU or t < oldest_time:
                        LRU = k
                        oldest_time = t
                # pop LRU
                del self.cache[LRU]
                del self.history[LRU]
                self.cache[key] = value
                self.history[key] = self.time
                self.time += 1
            else: # if space available
                self.cache[key] = value
                self.history[key] = self.time
                self.time += 1
                self.length += 1
        print("put", key, value, self.cache, self.history)
                

                
