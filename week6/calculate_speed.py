def calculate_final_speed(initial_speed, inclinations):
    for x in inclinations:
        initial_speed += (x * -1)
        if initial_speed <= 0:
            return 0
        
    return initial_speed

print(calculate_final_speed(60, [0, 30, 0, -45, 0]))