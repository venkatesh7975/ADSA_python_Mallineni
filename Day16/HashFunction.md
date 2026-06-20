# Day 16: HashFunction

# Hash Function - Pseudocode

## Problem Statement
Implement hash functions for converting keys to hash table indices.

## Algorithm

### Division Hash Function
```
FUNCTION hashDivision(key, tableSize):
    RETURN key % tableSize
END FUNCTION
```

### Multiplication Hash Function
```
FUNCTION hashMultiplication(key, tableSize):
    A = 0.6180339887  // Golden ratio - 1
    fractionalPart = (key * A) - floor(key * A)
    RETURN floor(tableSize * fractionalPart)
END FUNCTION
```

### Folding Hash Function
```
FUNCTION hashFolding(key, tableSize):
    keyString = convert(key, string)
    partSize = 2
    sum = 0
    
    FOR i = 0 TO length(keyString) - 1 STEP partSize:
        part = extract(keyString, i, i + partSize - 1)
        sum = sum + convert(part, integer)
    END FOR
    
    RETURN sum % tableSize
END FUNCTION
```

### Mid-Square Hash Function
```
FUNCTION hashMidSquare(key, tableSize):
    squared = key * key
    mid = extract middle digits of squared
    RETURN mid % tableSize
END FUNCTION
```

### String Hash Function
```
FUNCTION hashString(string, tableSize):
    hash = 0
    prime = 31
    
    FOR i = 0 TO length(string) - 1:
        hash = (hash * prime + asciiValue(string[i])) % tableSize
    END FOR
    
    RETURN hash
END FUNCTION
```

### Universal Hash Function
```
FUNCTION universalHash(key, a, b, p, tableSize):
    // p should be prime and greater than key range
    hash = ((a * key + b) % p) % tableSize
    RETURN hash
END FUNCTION
```

## Handling Collisions

### Linear Probing
```
FUNCTION linearProbing(key, hashValue, tableSize):
    i = 0
    WHILE table[(hashValue + i) % tableSize] is occupied:
        i = i + 1
    END WHILE
    
    RETURN (hashValue + i) % tableSize
END FUNCTION
```

### Quadratic Probing
```
FUNCTION quadraticProbing(key, hashValue, tableSize):
    i = 0
    WHILE table[(hashValue + i*i) % tableSize] is occupied:
        i = i + 1
    END WHILE
    
    RETURN (hashValue + i*i) % tableSize
END FUNCTION
```

### Chaining
```
FUNCTION insertWithChaining(key, value, table):
    hashValue = hash(key, tableSize)
    
    IF table[hashValue] is null:
        table[hashValue] = new LinkedList
    END IF
    
    table[hashValue].insert(key, value)
END FUNCTION
```

## Time Complexity
- Good hash function: O(1) average case
- With collisions: O(n) worst case

## Properties of Good Hash Function
1. Should distribute keys uniformly
2. Should minimize collisions
3. Should be fast to compute
4. Should use all bits of the key
5. Should be deterministic


## Python Implementation
```python

class Node:
    def __init__(self,key,value):
        self.key=key 
        self.value =value 
        self.next=None 

class HashTable:
    def __init__(self):
        self.size=10
        self.Table=[None]*self.size 
    def hashFunc(self,key):
        return key%self.size
    
    def insert(self,key,value):
        index=self.hashFunc(key)
        newNode=Node(key,value)
        if self.Table[index] is None:
            self.Table[index]=newNode
        else:
            curr=self.Table[index]
            while curr.next:
                curr=curr.next 
            curr.next=newNode 
        print(f"Inserted: ({key},{value})")
    
    def get(self,key):
        index=self.hashFunc(key)
        curr=self.Table[index]
        while curr:
            if curr.key==key:
                print(f"{key} -> {curr.value}")
                return 
            curr=curr.next 
        print(f" {key} not found")

    def display(self):
        for i in range(self.size):
            print(f"{i}:",end=" ")
            curr=self.Table[i]
            if not curr:
                print("Null")
            else:
                while curr:
                    print(f"({curr.key},{curr.value})->",end=" ")
                    curr=curr.next 
                print("NULL")

ht=HashTable() 
while True:
    op=int(input())
    if op==1:
        key,value=list(map(int,input().split()))
        ht.insert(key,value)
    elif op==2:
        key=int(input())
        ht.get(key)
    elif op==3:
        ht.display()
    elif op==4:
        print("Exit")
        break 
        

```

## Interactive Visualization
> **[Visualization Link](This is practical17 notes file.)**

