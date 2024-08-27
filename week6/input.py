def get_int(propmt):
    while True:
        try:
            return int(input(propmt))
        except:
            print("Not an integer")
        

value = get_int("Value: ")

if value > 2:
    print("Is greater than 2")
else:
    print("Is less than 2")