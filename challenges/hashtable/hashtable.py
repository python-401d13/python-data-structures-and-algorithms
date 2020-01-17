from collections import deque


class Hashtable():
    """
    Hashtable data structure.
    """

    HASH_PRIME = 599
    HASH_SIZE = 32

    def __init__(self):
        """
        Hashtable constructor.
        """

        self.buckets = [None for _ in range(self.HASH_SIZE)]


    def add(self, key, value):
        """
        Add a pair key and value to a hashtable.

        Input:
        key (): Key of key-value pair.
        value (): Value of key-value pair.
        """

        index = self.hash(key)
        bucket_pair = [key, value]

        if self.buckets[index]:
            self.buckets[index].append(bucket_pair)
        else:
            self.buckets[index] = deque()
            self.buckets[index].append(bucket_pair)


    def get(self, key):
        """
        Given a key paired with a value get the value from a hashtable.
        """

        # Exception, key isn't in hashtable
        if not self.contains(key):
            return None

        index = self.hash(key)

        for bucket_list in self.buckets[index]:
            if key == bucket_list[0]:
                return bucket_list[1]


    def contains(self, key):
        """
        Given a key tell if the key is paired with a value.

        Input:
        key (): The key of the key-value pair.
        """

        index = self.hash(key)

        if not self.buckets[index]:
            return False
        else:
            for bucket_list in self.buckets[index]:
                if key == bucket_list[0]:
                    return True

            return False


    def hash(self, key):
        """
        Hash a key for a hashtable.

        Hash function:
        1. Add all key character ascii numbers.
        2. Multiply by a prime number.
        3. Modulo by hashtable length to get hashtable index.

        Input:
        key (): Key to hash.

        Output:
        (int): Index of Hashtable for key-value pair.
        """

        hsum = sum([ord(c) for c in str(key)])
        hproduct = hsum * self.HASH_PRIME
        index = hproduct % self.HASH_SIZE

        return index
