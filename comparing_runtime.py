# Comparing runtime of adding to the front vs. adding to the back

# O(n)
def add_to_back(n):
  x = []
  for i in range(0, n):
    x.append(i + 1)
  return x

# O(n^2)
def add_to_front(n):
  x = []
  for i in range(0, n):
    x.insert(0, n - i)
  return x

## testing

import time

start_time = time.time()
add_to_back(500000)  #O(n)
end_time = time.time()
print (f"runtime: {end_time - start_time} seconds")

# runtime: 0.06550788879394531 seconds

start_time = time.time()
add_to_front(500000)  #O(n^2)
end_time = time.time()
print (f"runtime: {end_time - start_time} seconds")

# runtime: 48.826629877090454 seconds

# add_to_back() is over 600x faster than add_to_front