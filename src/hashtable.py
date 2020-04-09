# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.count = 0


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

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        '''

        # Check if the hast table has enough capacity
        if self.count >= self.capacity:
          # If not, add more capacity
          self.resize()

        # Hash the key and set it to index
        index = self._hash_mod(key)

        # Set the new node to singly linked list
        new_node = LinkedPair(key, value)

        # If there is an existing node here
        if self.storage[index] is not None:

          # Set the node to the Node at [index]
          node = self.storage[index]

          # Traverse node at that location
          while node is not None:

            # If the node key matches the key parameter, set the node value to value parameter
            if node.key == key:
              node.value = value
              break

            # If there's no node at the next index, end the function
            if node.next is None:
              break

            node = node.next

          # Add the new node to the end of the linked list chain
          node.next = new_node

        # If there is no node at this location, set location to LinkedPair with key and value
        else:
          self.storage[index] = new_node


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        '''
        # Hash the key and set it to index
        index = self._hash_mod(key)


        if self.storage[index] is not None:
          current_node = self.storage[index]
          previous_node = None

          while True:
            if current_node.key == key:
              if previous_node is None:
                self.storage[index] = current_node.next
              else:
                previous_node.next = current_node.next
              return

            if current_node.next is None:
              break

            previous_node = current_node
            current_node = current_node.next

        print(f"WARNING: Key {key} not found")


        # Remove the value by reassigning the index to none
        self.storage[index] = None


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        '''
        # Hash the key
        index = self._hash_mod(key)

        # Return storage at index value
        if self.storage[index] is not None:
          current_node = self.storage[index]

          while True:
            if current_node.key == key:
              return current_node.value

            if current_node.next is None:
              break

            current_node = current_node.next

        return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        '''
        # Double the capacity
        self.capacity *= 2

        # Set the old storage to the current storage
        old_storage = self.storage

        # Set the storage buckets to none
        self.storage = [None] * self.capacity

        # Copy all elements from the old storage to new
        for node in old_storage:

          while node is not None:
            self.insert(node.key, node.value)
            node = node.next



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
