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
        def collisionHandlerLinear(self, hashSum, value):
            for i in range(self.hash_table_size):
                loc = (hashSum+i) % self.hash_table_size
                self.collisionCount += 1
                if (self.hashTable[loc].state == state.empty or self.hashTable[loc].state == state.deleted):
                    if (self.hashTable[loc].getValue() == value):
                        return None
                    self.hashTable[loc].setValue(value)
                    self.num_entries += 1
                    return None

        self.accessCount += 1


        if (self.num_entries > self.hash_table_size*.8):
            self.oldTable = self.hashTable
            newSize = self.nextPrime(2*self.hash_table_size)
            oldSize = self.hash_table_size
            self.hashTable = [cell() for x in range(newSize)]
            self.hash_table_size = newSize

            for i in range (int(oldSize)):
                if self.oldTable[i].state.value == state.in_use.value:
                    self.insert(self.oldTable[i].getValue())



        if (self.mode == HashingModes.HASH_1_LINEAR_PROBING.value):
            sum = 0
            sum2 = 0
            leng = len(value)
            for i in range(leng):
                sum += ord(value[i]) ** (leng-i)
            revValue = value[::-1]
            for i in range(leng):
                sum2 += ord(revValue[i]) ** (leng-i)
            sum ^= sum2

            location = sum % self.hash_table_size
            if ((self.hashTable[location].state == state.empty.value or self.hashTable[location].state == state.deleted.value)):
                self.hashTable[location].setValue(value)
                self.num_entries += 1
            elif (self.hashTable[location].getValue() == value):
                return None
            else:
                collisionHandlerLinear(self, sum+1, value)
        elif (self.mode == HashingModes.HASH_2_LINEAR_PROBING.value):
            sum = 0
            for i in range(len(value)):
                sum += ord(value[i]) ** (len(value)-i)

            location = sum % self.hash_table_size
            if ((self.hashTable[location].state == state.empty.value or self.hashTable[location].state == state.deleted.value)):
                self.hashTable[location].setValue(value)
                self.num_entries += 1
            elif (self.hashTable[location].getValue() == value):
                return None
            else:
                collisionHandlerLinear(self, sum+1, value)
        else:
            print("**** MODE NOT IMPLEMENTED ****")

    def find(self, value):
        def linearCollisionFinder(self, hashSum, value):
            for i in range(self.hash_table_size):
                loc = (hashSum+i) % self.hash_table_size
                self.collisionCount += 1
                if (self.hashTable[loc].state == state.empty):
                    return False
                elif (self.hashTable[loc].state == state.deleted):
                    pass
                elif (self.hashTable[loc].getValue() == value):
                    return True

        if (self.mode == HashingModes.HASH_1_LINEAR_PROBING.value):
            #self.print_set()
            sum = 0
            sum2 = 0
            leng = len(value)
            for i in range(leng):
                sum += ord(value[i]) ** (leng-i)
            revValue = value[::-1]
            for i in range(leng):
                sum2 += ord(revValue[i]) ** (leng-i)
            sum ^= sum2
            #print("searching for: " +value)
            
            loc = sum%self.hash_table_size
            #print("found: " +str(self.hashTable[loc].getValue()))
            if (self.hashTable[loc].getValue() == value):
                return True
            else:
                return linearCollisionFinder(self, sum+1, value)
        elif (self.mode == HashingModes.HASH_2_LINEAR_PROBING.value):
            sum = 0
            for i in range(len(value)):
                sum += ord(value[i]) ** (len(value)-i)
            loc = sum %self.hash_table_size
            if (self.hashTable[loc].getValue() == value):
                return True
            else:
                return linearCollisionFinder(self, sum+1, value)
        return False
        
    def print_set(self):
        for i in range(self.hash_table_size):
            if self.hashTable[i].key != None:
                print("Hash: " +str(i) +" value: " +str(self.hashTable[i].key) +"\n")
      
    

    def print_stats(self):
        # some debug statements 
        # print("number of entries: " +str(self.num_entries))
        # print("Size of hashtable: " +str(self.hash_table_size))
        print("Average collisions per access: " +str(self.collisionCount/self.accessCount) +"\n")
        
# This is a cell structure assuming Open Addressing
# It should contain and element that is the key and a state which is empty, in_use or deleted
# You will need alternative data-structures for separate chaining
class cell:
    def __init__(self):
        self.state = state.empty
        self.key = None

    def setValue(self, val):
        self.key = val
        self.state = state.in_use

    def deleteValue(self, val):
        self.val = Null
        self.state = state.deleted
    def getValue(self):
        return self.key


        
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
