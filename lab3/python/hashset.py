from enum import Enum
import config

class hashset:
    def __init__(self):
        # TODO: create initial hash table
        self.verbose = config.verbose
        self.mode = config.mode
        self.hash_table_size = config.init_size

        self.hashTable = [cell() for x in range(self.hash_table_size)]
        self.collisionCount = 0
        self.accessCount = 0
        self.num_entries = 0
        


                
    # Helper functions for finding prime numbers
    def isPrime(self, n):
        i = 2
        while (i * i < n):
            if (n % i == 0):
                return False
            i = i + 1
        return True
        
    def nextPrime(self, n):
        while (not self.isPrime(n)):
            n = n + 1
        return n
        
    def insert(self, value):
        self.accessCount += 1


        if (self.num_entries == self.hash_table_size):
            quit()

        if (self.mode == HashingModes.HASH_1_LINEAR_PROBING):
            sum = 0
            for i in range(len(value)):
                sum += ord(value[i]) ** (len(value)-i)

            location = sum % self.hash_table_size
            if (self.hashTable[location].state == state.empty or self.hashTable[location].state == state.deleted):
                self.hashTable[location].setValue(value)
                self.num_entries += 1
            else:
                collisionHandlerLinear(location, value)

        
    def collisionHandlerLinear(self, location, value):
        loc = location + 1
        val = value
        while (loc < self.hash_table_size):
            self.collisionCount += 1
            if (hashTable[loc].state == state.empty or hashTable[loc].state == state.deleted):
                hashTable[location].setValue(value)
                self.num_entries += 1
                return None
            loc+=1

        loc = 0
        while (loc < location):
            self.collisionCount += 1
            if (hashTable[loc].state == state.empty or hashTable[loc].state == state.deleted):
                hashTable[location].setValue(value)
                self.num_entries += 1
                return None
            loc+=1

    def find(self, value):
        if (self.mode == HashingModes.HASH_1_LINEAR_PROBING):
            sum = 0
            for i in range(len(value)):
                sum += ord(value[i]) ** (len(value)-i)
            if (self.hashTable[sum].key == value):
                return True
        return False
        
    def print_set(self):
        for i in range(self.hash_table_size):
            print("Hash: " +str(i) +" value: " +self.hashTable[i].key +"\n")
        
    def print_stats(self):
        print("Average collisions per access: " +str(self.collisionCount/self.accessCount) +"\n")
        
# This is a cell structure assuming Open Addressing
# It should contain and element that is the key and a state which is empty, in_use or deleted
# You will need alternative data-structures for separate chaining
class cell:
    def __init__(self):
        self.state = state.empty

    def setValue(self, val):
        self.key = val
        self.state = state.in_use

    def deleteValue(self, val):
        self.val = Null
        self.state = state.deleted

        
class state(Enum):
    empty = 0
    in_use = 1
    deleted = 2
        
# Hashing Modes
class HashingModes(Enum):
    HASH_1_LINEAR_PROBING=0
    HASH_1_QUADRATIC_PROBING=1
    HASH_1_DOUBLE_HASHING=2
    HASH_1_SEPARATE_CHAINING=3
    HASH_2_LINEAR_PROBING=4
    HASH_2_QUADRATIC_PROBING=5
    HASH_2_DOUBLE_HASHING=6
    HASH_2_SEPARATE_CHAINING=7
