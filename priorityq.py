import heapq

# Create a priority queue object
priorityq = []

# Add an element with priority 1
heapq.heappush(priorityq, (1, "This is the first element"))

# Add another element with priority 2
heapq.heappush(priorityq, (2, "This is the second element"))

# Add another element with priority 2
heapq.heappush(priorityq, (3, "This is the third element"))

# Show the current size of the queue
print(f"Queue size: {len(priorityq)}")

# Pop an element from the queue
element = heapq.heappop(priorityq)

# Print the popped element
print(f"Popped element: {element}")

# Show the updated size of the queue
print(f"Queue size: {len(priorityq)}")
