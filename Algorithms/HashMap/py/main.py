class HashMap:
    def insert(self, key, value):
        self.resize()
        index = self.key_to_index(key)
        self.hashmap[index] = (key, value)

    def resize(self):
        if len(self.hashmap) == 0:
            self.hashmap = [None]
            return
        load = self.current_load()
        if load < 0.05:
            return
        old_hashmap = self.hashmap
        self.hashmap = [None] * (len(old_hashmap) * 10)
        for kvp in old_hashmap:
            if kvp is not None:
                self.insert(kvp[0], kvp[1])

    def current_load(self):
        if len(self.hashmap) == 0:
            return 1
        filled_slots = 0
        for slot in self.hashmap:
            if slot is not None:
                filled_slots += 1
        return filled_slots / len(self.hashmap)

    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {str(v)}\n"
        return final

testMap = HashMap(0)
testMap.insert("hello", "world")
#testMap.insert("hell1", "world")
#testMap.insert("hell2", "world")
#testMap.insert("hell3", "world")
#testMap.insert("hell4", "world")
testMap.current_load()

print(testMap.hashmap)
print(round(0.2,3))