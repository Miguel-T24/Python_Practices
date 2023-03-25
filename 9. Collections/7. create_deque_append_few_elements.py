# 7. Write a python program to crate deque and append a few elements to the left and right.

from collections import deque

deque_colors = deque(['Red' , 'Green', "White"])
print("Original Deque : {}".format(deque_colors))
print("First Elements of deque:",deque_colors[0])


# Append Left
deque_colors.appendleft("Yellow")
print(deque_colors)

deque_colors.insert(0,"Pink")
print(deque_colors)

# Append Right
deque_colors.append("blue")
print(deque_colors)

#removing from right
deque_colors.pop()
print(deque_colors)

#removing from the left
deque_colors.popleft()
deque_colors.popleft()
print(deque_colors)

# Reverse the deque
deque_colors.reverse()
print(deque_colors)