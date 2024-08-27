from cs50 import get_int

# Initialize pyramid height
height = 0

# Get height from user, where height is greater than equals to 1, 
# or height is equal to less than 8
while height < 1 or height > 8:
    height = get_int("Pyramid Height: ")
    
# Print pyramid of height
for n in range(height):
    print(" " * (height - (n + 1)), end="")
    print("#" * (n + 1), end="")
    print(" ", end="")
    print("#" * (n + 1))