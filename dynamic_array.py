class DynamicArray:
  def __init__(self, capacity=1):
    self.count = 0   # Number of elements in the array
    self.capacity = capacity   # Total amount of storage in the array
    self.storage = [None] * capacity

  def insert(self, index, value):
    # Check if we have enough capacity
    if self.count >= self.capacity:
      # If not, add more capacity
      self.resize()
    # Shift over every item after index to the right by 1
    for i in range(self.count, index, -1):
      self.storage[i] = self.storage[i-1]
    # Add the new value to the index
    self.storage[index] = value
    # Increment count
    self.count += 1

 def append(self, value):
    # Check if we have enough capacity
    if self.count >= self.capacity:
      # If not, double the size
      self.resize()
    # Add value to the index of count
    self.storage[self.count] = value
    # Increment count
    self.count += 1
