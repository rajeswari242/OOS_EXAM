from queue import Queue

# Create a Queue object
q = Queue()

# Add an element to the queue
q.put("This is the first element")

# Show the current size of the queue
print(f"Queue size: {q.qsize()}")

# Pop an element from the queue
element = q.get()

# Print the popped element
print(f"Popped element: {element}")

# Show the updated size of the queue
print(f"Queue size: {q.qsize()}")
