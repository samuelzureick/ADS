import config

class bstree:
    def __init__(self):
        self.verbose = config.verbose
        self.finds = 0
        self.comparisons = 0
        
        
    def size(self):
        if (self.tree()):
            return 1 + self.left.size() + self.right.size()
        return 0
        
    def tree(self):
        return hasattr(self, 'value')
        
    def insert(self, value):
        if (self.tree()):
            # first check node so no duplicates are entered (this is a set)
            # then insert in left or right given string value
            if (self.value == value):
                return None
            elif self.value > value:
                self.left.insert(value)
            elif self.value < value:
                self.right.insert(value)
        else:
            # if this isnt a valid node, make it a valid node, and create left and right (uninitialized) subtrees
            self.value = value
            self.left = bstree()
            self.right = bstree()
        
    def find(self, value):
        self.finds += 1
        if self.tree():
            # if incorrect node with no kids
            if(self.value != value and not hasattr(self, 'right') and not hasattr(self, 'left')):
                return False
            # found
            elif self.value == value:
                return True
            # check left
            elif self.value > value and hasattr(self, 'left'):
                self.comparisons += 1
                return self.left.find(value)
            # check right
            elif self.value < value and hasattr(self, 'right'):
                self.comparisons += 1
                return self.right.find(value)
        else:
            return False
            


        
        
    # You can update this if you want
    def print_set_recursive(self, depth):
        if (self.tree()):
            for i in range(depth):
                print(" ", end='')
            print("%s" % self.value)
            self.left.print_set_recursive(depth + 1)
            self.right.print_set_recursive(depth + 1)
            
    # You can update this if you want
    def print_set(self):
        print("Tree:\n")
        self.print_set_recursive(0)
        
    def height(self):
        if not self.tree():
            return 0
        elif (hasattr(self, 'right') and not hasattr(self, 'left')):
            return 1 + self.right.height()
        elif (hasattr(self, 'left') and not hasattr(self, 'right')):
            return 1 + self.left.height()
        elif (hasattr(self, 'left') and hasattr(self, 'right')):
            return 1 + self.left.height() + self.right.height()



    def print_stats(self):
        # TODO update code to record and print statistic
        print("average comparisons per find: " + str(self.comparisons/self.finds))
        print("height: " + str(self.height()))
        # self.print_set()

