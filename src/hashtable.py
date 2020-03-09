# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
      return '{' + f'"{self.key}":{self.value}, next: {self.next}' + '}'

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.count = 0
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        self.count += 1
        if self.count >= self.capacity:
          self.resize()
        index = self._hash_mod(key)
        newPair = LinkedPair(key, value)
        bucket = self.storage[index]
        if bucket is None:
          self.storage[index] = newPair
          return newPair.value

        # colision handling
        prev = bucket
        keyExists = False
        while bucket is not None:
          prev = bucket
          if bucket.key == key:
            keyExists = True
            break
          bucket = bucket.next
        if keyExists:
          bucket.value = value
        else:
          prev.next = newPair
        return newPair.value

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        bucket = self.storage[index]
        prev = None
        while bucket is not None and bucket.key != key:
          prev = bucket
          bucket = bucket.next
        if bucket is None:
          return None
        else:
          self.count -= 1
          value = bucket.value
          if prev is None:
            self.storage[index] = None
          else:
            prev.next = prev.next.next
          return value

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        bucket = self.storage[index]
        while bucket is not None and bucket.key != key:
          bucket = bucket.next
        if bucket is not None:
          return bucket.value
        else:
          return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        oldStorage = self.storage
        oldCount = self.count
        self.count = 0
        self.capacity *= 2
        self.storage = [None] * self.capacity
        #print('resize -> new storage', self.capacity, self.storage)
        for i in range(0, oldCount):
          bucket = oldStorage[i]
          if bucket is not None:
            while bucket is not None:
              #print('resize -> insert', bucket.key, bucket.value)
              self.insert(bucket.key, bucket.value)
              bucket = bucket.next
