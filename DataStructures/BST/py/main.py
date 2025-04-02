class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return
        if self.val == val:
            return
        if val > self.val:
            if not self.right:
               self.right = BSTNode(val)
            else:
                self.right.insert(val)
            return
        if not self.left:
            self.left = BSTNode(val)
            return
        self.left.insert(val)
        return
