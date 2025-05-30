from TOOLS import TOOLS
class Sorting:
    def __init__(self):
        TOOLS.clear_screen()
        self.methods = [
            "Bubble Sort",
            "Selection Sort",
            "Insertion Sort",
            "Merge Sort",
            "Quick Sort",
            "Bucket Sort",
        ]
        self.start()
        # self.selection_sort()  # For testing purposes, directly calling bubble_sort
    
    def start(self):
        print("pick your desired sorting method.")
        for i, method in enumerate(self.methods):
            print(f"{i + 1}. {method}")
        print()
        choice = int(input("Enter the number of the method you want to use: ")) - 1
        print()
        if choice < 0 or choice >= len(self.methods):
            print("Invalid choice. Please run the program again.")
            exit()
        picked_method = self.methods[choice]
        print(f"You have selected: {picked_method}")
        match picked_method:
            case "Bubble Sort":
                self._bubble_sort()
            case "Selection Sort":
                self._selection_sort()
            case "Insertion Sort":
                self._insertion_sort()
            case "Merge Sort":
                self._merge_sort()
            case "Quick Sort":
                self._quick_sort()
            case "Bucket Sort":
                self._bucket_sort()
            case _:
                print("This method is not implemented yet.")

#region bubble sort
    def _bubble_sort(self):
        # print()
        arr = input("Enter the items to sort (space-separated): ").split()
        self.bubble_sort(arr)
        TOOLS.sleep(0.5)
        print(f"Sorted array: {arr}")

    def bubble_sort(self,arr):
        # print()
        length = len(arr)
        for i in range(length):
            for j in range(0, length-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j] #swap
                # TOOLS.sleep(1)
                # print(i, j, arr)
        return arr
        print(f"Sorted array: {arr}")
#endregion bubble sort

#region selection sort
    def _selection_sort(self):
        # print()
        arr = input("Enter the items to sort (space-separated): ").split()
        self.selection_sort(arr)
        TOOLS.sleep(0.5)
        print(f"Sorted array: {arr}")

    def selection_sort(self,arr):
        # print()
        length = len(arr)
        for i in range(length):
            min_idx = i
            for j in range(i+1, length):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            # TOOLS.sleep(1)
            # print(i, min_idx, arr)
        return arr
        print(f"Sorted array: {arr}")
#endregion selection sort

#region insertion sort
    def _insertion_sort(self):
        # print()
        arr = input("Enter the items to sort (space-separated): ").split()
        self.insertion_sort(arr)
        TOOLS.sleep(0.5)
        print(f"Sorted array: {arr}")

    def insertion_sort(self,arr):
        # print()
        length = len(arr)
        for i in range(1, length):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
            # TOOLS.sleep(1)
            # print(i, j, arr)
        return arr
        print(f"Sorted array: {arr}")
#endregion insertion sort

#region merge sort
    def _merge_sort(self):
        # print()
        arr = input("Enter the items to sort (space-separated): ").split()
        self.merge_sort(arr)
        TOOLS.sleep(0.5)
        print(f"Sorted array: {arr}")

    def merge_sort(self, arr):
        # If the array has more than one element, split and sort recursively
        if len(arr) > 1:
            mid = len(arr) // 2  # Find the middle point
            L = arr[:mid]        # Divide the array elements into 2 halves
            R = arr[mid:]

            self.merge_sort(L)   # Sort the first half
            self.merge_sort(R)   # Sort the second half

            self.merge(arr, L, R)  # Merge the sorted halves
        return arr

    def merge(self, arr, L, R):
        # Initialize pointers for L, R, and arr
        i = j = k = 0

        # Copy data to arr[] from L[] and R[] in sorted order
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Check if any element was left in L[]
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # Check if any element was left in R[]
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
#endregion merge sort

#region quick sort
    def _quick_sort(self):
        # print()
        arr = input("Enter the items to sort (space-separated): ").split()
        self.quick_sort(arr, 0, len(arr) - 1)
        TOOLS.sleep(0.5)
        print(f"Sorted array: {arr}")

    def quick_sort(self, arr, low, high):
        # Recursive Quick Sort implementation
        if low < high:
            # pi is partitioning index, arr[pi] is now at right place
            pi = self.partition(arr, low, high)
            # Separately sort elements before and after partition
            self.quick_sort(arr, low, pi - 1)
            self.quick_sort(arr, pi + 1, high)

    def partition(self, arr, low, high):
        # Partition the array using the last element as pivot
        pivot = arr[high]
        i = low - 1  # Index of smaller element
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]  # Swap if element is smaller than pivot
        arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Place pivot in correct position
        return i + 1  # Return the partitioning index
#endregion quick sort

#region bucket sort
    def _bucket_sort(self):
        # print()
        arr = list(map(float, input("Enter the items to sort (space-separated): ").split()))
        sorted_arr = self.bucket_sort(arr)
        TOOLS.sleep(0.5)
        print(f"Sorted array: {sorted_arr}")

    def bucket_sort(self, arr):
        # Create empty buckets
        bucket = []
        for i in range(len(arr)):
            bucket.append([])

        # Put array elements in different buckets
        for j in arr:
            index_b = min(int(10 * j), len(arr) - 1)
            bucket[index_b].append(j)
        # Sort individual buckets
        for i in range(len(arr)):
            bucket[i] = self.insertion_sort(bucket[i])
        # Concatenate all sorted buckets
        sorted_arr = []
        for i in range(len(arr)):
            sorted_arr = sorted_arr + bucket[i]
        arr = sorted_arr.copy()  # Copy sorted array back to original array
        return sorted_arr
        
#endregion bucket sort
