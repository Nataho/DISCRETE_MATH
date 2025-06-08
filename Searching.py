from TOOLS import TOOLS
from Sorting import Sorting

class Searching:
    def __init__(self):
        TOOLS.clear_screen()
        self.methods = [
            "Linear Search", #sequential
            "Binary Search", #interval
            "Interpolation Search"
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
                TOOLS.print_type("You chose Linear Search.", "blue")
                self._linear_search()
            case "Binary Search":
                TOOLS.print_type("You chose Binary Search.", "blue")
                self._binary_search()
            case "Interpolation Search":
                TOOLS.print_type("you chose Interpolation Search.", "blue")
                self._interpolation_search()
    
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
                TOOLS.print_type(f"Found {target} at index {i}.", "yellow")
                break
        if not found:
            TOOLS.print_type(f"{target} not found in the array.")
    
    def linear_search(self, arr, target):
        length = len(arr)
        for i in range(length):
            if arr[i] == target:
                return i
    
    def _binary_search(self):
        """Perform binary search on a sorted list."""
        print()
        TOOLS.print_type("Performing Binary Search...")
        # Example implementation
        arr = list(map(int, TOOLS.input_type("Enter the elements of the array(space sepparated): ").split()))
        Sorting.merge_sort(arr)
        TOOLS.print_type(f"Sorted array: {arr}", "green")
        target = int(TOOLS.input_type("Enter the number to search for: "))
        index = self.binary_search(arr, target)
        if index != -1:
            TOOLS.print_type(f"Found {target} at index {index}.", "yellow")
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
    def _interpolation_search(self):
        """Perform interpolation search on a sorted list."""
        print()
        TOOLS.print_type("Performing Interpolation Search...")
        # Example implementation
        arr = list(map(int, TOOLS.input_type("Enter the elements of the array(space sepparated): ").split()))
        Sorting.merge_sort(arr)
        TOOLS.print_type(f"Sorted array: {arr}", "green")
        target = int(TOOLS.input_type("Enter the number to search for: "))
        index = self.interpolation_search(arr, target)
        if index != -1:
            TOOLS.print_type(f"Found {target} at index {index}.", "yellow")
        else:
            TOOLS.print_type(f"{target} not found in the array.", "red")

    def interpolation_search(self, arr, target):
        key = target
        low = 0
        high = len(arr) - 1

        print()
        TOOLS.print_type("low", "blue")
        TOOLS.print_type("high", "green")
        TOOLS.print_type("pos", "yellow")
        print()

        while low <= high and arr[low] <= key <= arr[high]:


            if arr[high] == arr[low]:
                if arr[low] == key:
                    return low
                else:
                    break
            pos = low + int(((key - arr[low]) * (high - low)) / (arr[high] - arr[low]))
            
            #text
            displayed_arr = ""
            for i in range(len(arr)):
                # if i = 0:
                #     displayed_arr += f"{arr[i]}"
                #     continue
                if i == pos:
                    displayed_arr += f", \033[93m{arr[pos]}\033[0m"
                elif i == low:
                    displayed_arr += f", \033[94m{arr[low]}\033[0m"
                elif i == high:
                    displayed_arr += f", \033[92m{arr[high]}\033[0m"
                
                else:
                    displayed_arr += f", {arr[i]}"
            displayed_arr = f"[{displayed_arr[2:]}]"
            
            TOOLS.print_type(displayed_arr)
            if pos < low or pos > high:
                break
            if arr[pos] < key:
                low = pos + 1
            elif arr[pos] > key:
                high = pos - 1
            else:
                return pos
        return -1
    #endregion interpolation search

    #region ternary search
    def _ternary_search(self):
        """Perform ternary search on a sorted list."""
        print()
        TOOLS.print_type("Performing Ternary Search...")
        arr = list(map(int, TOOLS.input_type("Enter the elements of the array(space sepparated): ").split()))
        Sorting.merge_sort(arr)
        TOOLS.print_type(f"Sorted array: {arr}", "blue")
        target = int(TOOLS.input_type("Enter the number to search for: "))
        index = self.ternary_search(arr, target)
        if index != -1:
            TOOLS.print_type(f"Found {target} at index {index}.", "yellow")
        else:
            TOOLS.print_type(f"{target} not found in the array.", "red")

    def ternary_search(self, arr, target):
        """Perform ternary search on a sorted list."""
        left, right = 0, len(arr) - 1
        while left <= right:
            third = (right - left) // 3
            mid1 = left + third
            mid2 = right - third
            if arr[mid1] == target:
                return mid1
            if arr[mid2] == target:
                return mid2
            if target < arr[mid1]:
                right = mid1 - 1
            elif target > arr[mid2]:
                left = mid2 + 1
            else:
                left = mid1 + 1
                right = mid2 - 1
        return -1
    #endregion ternary search