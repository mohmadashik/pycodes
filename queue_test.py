from queue import Queue

# Create a Queue with a maximum size of 3
queue_obj = Queue(maxsize=3)

# Add 3 items to the queue
queue_obj.put(1)
queue_obj.put(2)
queue_obj.put(3)

# Display the queue
print("Original Queue:", list(queue_obj.queue))

# Add one more item, automatically removing the least recently added (1)
try:
    queue_obj.put(4)
except Exception as e:
    print(f'err: {e}')
# Display the updated queue
print("Updated Queue:", list(queue_obj.queue))
