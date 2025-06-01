from ST import ST
from Ciphers import Ciphers
from Sorting import Sorting

#region main
from basic_math import bMath
from TOOLS import TOOLS
# import TOOLS as Tools

# TOOLS = tools()

TOOLS.clear_screen()

picked:int = -2

classes = [
    ST,
    Ciphers,
    Sorting,
]

# delay = 0

# decision = TOOLS.input_type("Activate Typewriter Mode? (y/n): ", 0.05)
# if decision.lower() == 'y':
#     delay_input = TOOLS.input_type("Delay time(float): ", 0.05)
#     try:
#         delay = float(delay_input)
#     except (TypeError, ValueError):
#         delay = 0.03
#     TOOLS.set_delay(delay)
# else:
#     delay = 0
#     TOOLS.set_delay(delay)

while picked != -1: #-1 is used to exit the loop
    TOOLS.clear_screen()
    TOOLS.print_type("pick a class to open")
    for i, cls in enumerate(classes):
        TOOLS.print_type(f"{i + 1}. {cls.__name__}")
    picked = int(TOOLS.input_type("Enter the number of the class you want to open: ")) - 1

    #picks the class based on user input
    if picked < 0 or picked >= len(classes):
        TOOLS.print_type("Invalid choice. Please run the program again.")
        exit()

    picked_class = classes[picked]
    picked_class()
    while True:
        print()
        decision = input("would you like to restart the class? (y/n): ")
        if decision.lower() == 'y':
            picked_class()
        else:
            break
#endregion main

#region test
# print(TOOLS.is_prime(29))  # True
# print(TOOLS.is_prime(15))  # False
# print(TOOLS.is_prime(2))   # True
#endregion test