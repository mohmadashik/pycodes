from queue import LifoQueue

# Create a LifoQueue with a maximum size of 3
my_lifo_queue = LifoQueue(maxsize=3)

# Add 3 items to the queue
my_lifo_queue.put(1)
my_lifo_queue.put(2)
my_lifo_queue.put(3)

# Display the queue
print("Original LifoQueue:", list(my_lifo_queue.queue))

# Add one more item, automatically removing the least recently added (1)
try:
    my_lifo_queue.put(4)
except Exception as e:
    print(f'err: {e}')
# Display the updated queue
print("Updated LifoQueue:", list(my_lifo_queue.queue))
