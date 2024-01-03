from collections import deque

# Create a deque with a maximum size of 3
my_deque = deque(maxlen=3)

# Append 3 items to the deque
my_deque.append(1)
my_deque.append(2)
my_deque.append(3)

# Display the deque
print("Original deque:", list(my_deque))


try:
    my_deque.append(4)
    print("Updated deque:", list(my_deque))
    print(f'latest second time is {my_deque[-1]}')

except Exception as e:
    print(f'err: {e}')

# Display the updated deque
print("Updated deque:", list(my_deque))
