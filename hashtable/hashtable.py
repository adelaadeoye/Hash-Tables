class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    def __init__(self,capacity):
        self.capacity=capacity
        self.storage=[None]*capacity
        self.count=0

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """
        hash = 5381
        ht = 0

        ord_func = ord
        try:
            ord_func(key[0])
        except TypeError:
        # bytearray
            ord_func = lambda x: x
        except IndexError:
            return hash

        for c in key:
       
            ht = (hash * 33) % (2**32)
            hash = (ht + ord_func(c)) % (2**32)

        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        index=self.hash_index(key)
        node=self.storage[index]

        if not node:
            self.storage[index]=HashTableEntry(key,value)
            return
        while node:
            if node.key== key:
                node.value= value
                break
            elif node.next:
                node = node.next
            else:
                node.next= HashTableEntry(key,value)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this
        """
     
        index=self.hash_index(key)
        node=self.storage[index]

        if node is not None:
            if node.key==key:
                node.value=None
            else:
                cur_node=node.next
                while cur_node:
                    if cur_node.key==key:
                        cur_node.value= None
                    cur_node=cur_node.next
        else:
            print("Key not found")

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index=self.hash_index(key)
        node=self.storage[index]

        if node is not None:
            if node.key==key:
                return node.value
            else:
                cur_node=node.next
                while cur_node:
                    if cur_node.key==key:
                        return cur_node.value
                    cur_node=cur_node.next
        else:
            return None
    def resize(self, new_capacity):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """

if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
