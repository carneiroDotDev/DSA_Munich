class Trie:
    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self, word):
        current = self.root
        #i will check each letter of word
        for letter in word:
        #if the letter exists goes inside it as a key
        #if not create the letter as a dict
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        #when loops ends add to this letter a { '*' : True }
        current[self.end_symbol]  = True
        pass

    def exists(self, word):
        current = self.root
        #i will check each letter of word
        for letter in word:
            #if the letter exists goes inside it as a key
            if letter not in current:
                return False
            current = current[letter]
        #when loops ends check if this letter has the end symbol
        return self.end_symbol in current
