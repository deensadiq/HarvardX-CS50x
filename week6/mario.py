from cs50 import get_int 
height = 0

while height < 1 or height > 8:
    height = get_int("Pyramid Height: ")

for n in range(height):
    print(" " * (height - (n + 1)), end="")
    print("#" * (n + 1))
    