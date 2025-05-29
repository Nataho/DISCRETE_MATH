from ST import ST
from Ciphers import Ciphers
from Sorting import Sorting

from basic_math import bMath
from TOOLS import TOOLS
TOOLS.clear_screen()

picked:int = -2

classes = [
    ST,
    Ciphers,
    Sorting,
]

while picked != -1: #-1 is used to exit the loop
    TOOLS.clear_screen()
    print("pick a class to open")
    for i, cls in enumerate(classes):
        print(f"{i + 1}. {cls.__name__}")
    picked = int(input("Enter the number of the class you want to open: ")) - 1

    #picks the class based on user input
    if picked < 0 or picked >= len(classes):
        print("Invalid choice. Please run the program again.")
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
#region test
# print(bMath().modulo(4^543, 3))
#endregion test