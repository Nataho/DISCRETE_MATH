from TOOLS import TOOLS
from Sorting import Sorting

class Searching:
    def __init__(self):
        TOOLS.clear_screen()
        self.methods = [
            "Linear Search", #sequential
            "Binary Search", #interval
            # "Jump Search",
            # "Exponential Search",
            # "Interpolation Search"
        ]
        self.start()

    def start(self):
        TOOLS.print_type("Pick a method to perform searching:")
        for i, method in enumerate(self.methods):
            TOOLS.print_type(f"{i + 1}. {method}")
        choice = int(TOOLS.input_type("Enter the number of your choice: ")) - 1
        if choice < 0 or choice >= len(self.methods):
            TOOLS.print_type("Invalid choice. Please try again.")
            return
        method_name = self.methods[choice]

        match method_name:
            case "Linear Search":
                TOOLS.print_type("You chose Linear Search.")
                self._linear_search()
            case "Binary Search":
                TOOLS.print_type("You chose Binary Search.")
                self._binary_search()
            #     # Implement Binary Search logic here
            # case "Jump Search":
            #     TOOLS.print_type("You chose Jump Search.")
            #     # Implement Jump Search logic here
            # case "Exponential Search":
            #     TOOLS.print_type("You chose Exponential Search.")
            #     # Implement Exponential Search logic here
            # case "Interpolation Search":
            #     TOOLS.print_type("You chose Interpolation Search.")
            #     # Implement Interpolation Search logic here

        # TOOLS.print_type("")
        # TOOLS.print_type(f"You chose: {method_name}")
        
        # # Placeholder for actual search implementations
        # TOOLS.print_type("This feature is under development.")
        # Implement the search methods here
        # match method_name:
        #     case "Linear Search":
    
    def _linear_search(self): 
        """Perform linear search on a list."""
        TOOLS.print_type("Performing Linear Search...")
        # Example implementation
        arr = list(map(int, TOOLS.input_type("Enter the elements of the array(space sepparated): ").split()))
        target = int(TOOLS.input_type("Enter the number to search for: "))
        found = False
        for i, num in enumerate(arr):
            if num == target:
                found = True
                TOOLS.print_type(f"Found {target} at index {i}.")
                break
        if not found:
            TOOLS.print_type(f"{target} not found in the array.")
    
    def linear_search(self, arr, target):
        length = len(arr)
        for i in range(length):
            if arr[i] == target:
                return i
    
    def _binary_search(self):
        print()
        """Perform binary search on a sorted list."""
        TOOLS.print_type("Performing Binary Search...")
        # Example implementation
        arr = list(map(int, TOOLS.input_type("Enter the elements of the array(space sepparated): ").split()))
        Sorting.merge_sort(arr)
        TOOLS.print_type(f"Sorted array: {arr}")
        target = int(TOOLS.input_type("Enter the number to search for: "))
        index = self.binary_search(arr, target)
        if index != -1:
            TOOLS.print_type(f"Found {target} at index {index}.")
        else:
            TOOLS.print_type(f"{target} not found in the array.")

    def binary_search(self, arr, target):
        """Perform binary search on a sorted list."""
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    #region interpolation search
    #endregion interpolation search

    #region ternary search
    #endregion ternary search