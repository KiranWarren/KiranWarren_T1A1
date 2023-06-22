# Q15 - Weather Description

# Initialise the two variables to be used for describing the weather.
raining = False
temperature = 15

# Conditional statement based on whether it is raining or not.
# if it is raining, run this block.
if raining:

    # Conditional statement checking whether the temp is below 15C.
    # Provide the console output for below 15C.
    if temperature < 15:
        print("It's wet and cold")

    # Provide the console output for above or equal to 15C.
    else:
        print("It's warm and raining")

# If it is NOT raining, run this block.
else:

    # Conditional statement checking whether the temp is below 15C.
    # Provide the console output for <15C.
    if temperature < 15:
        print("It's not raining but cold")
        
    # Provide the console output for above or equal to 15C.
    else:
        print("It's warm but not raining")
