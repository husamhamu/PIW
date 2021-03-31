#python
x = 10
y = 5

# x now becomes the sum of x and y
x = x + y

# now subtracting y from the sum, we can get the previous value of x and
# and set to be equal y
y = x - y

# and subtracting the new value of y from the sum gives us the previous #value of y
x = x - y
print(f"After Swapping: x ={x} , y={y} ")

