from TOOLS import TOOLS

def arrColor(arr, blue = [None], green = [None], yellow = [None], magenta = [None]):
    #blue = [index]
    length = len(arr)
    display_arr = ""
    for k in range(length):
        if k in magenta:
            display_arr += f", \033[95m{arr[k]}\033[0m"
            continue
        if k in yellow:
            display_arr += f", \033[93m{arr[k]}\033[0m"
            continue
        if k in blue:
            display_arr += f", \033[94m{arr[k]}\033[0m"
            continue
        if k in green:
            display_arr += f", \033[92m{arr[k]}\033[0m"
            continue
        display_arr += f", {arr[k]}"
    
    display_arr = f"[{display_arr[2:]}]"
    TOOLS.print_type(display_arr,None,0.001)

    #use case
    #myarr = [1,3,5,7,9,2,4,6,8,0]
    #coloredArr = arrColor(myarr, [0], [8], [5,6])

    return display_arr

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
            "Shell Sort",
            "Comb Sort",
            "Radix Sort",
            "Tree Sort",
        ]
        self.start()
        # self.selection_sort()  # For testing purposes, directly calling bubble_sort

    def start(self):
        TOOLS.print_type("pick your desired sorting method.")
        for i, method in enumerate(self.methods):
            TOOLS.print_type(f"{i + 1}. {method}")
        TOOLS.print_type("")
        choice = int(TOOLS.input_type("Enter the number of the method you want to use: ")) - 1
        TOOLS.print_type("")
        if choice < 0 or choice >= len(self.methods):
            TOOLS.print_type("Invalid choice. Please run the program again.")
            exit()
        picked_method = self.methods[choice]
        TOOLS.print_type(f"You have selected: {picked_method}")
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
            case "Shell Sort":
                self._shell_sort()
            case "Comb Sort":
                self._comb_sort()
            case "Radix Sort":
                self._radix_sort()
            case "Tree Sort":
                self._tree_sort()
            case _:
                TOOLS.print_type("This method is not implemented yet.")

#region bubble sort
    def _bubble_sort(self):
        arr = list(map(int, TOOLS.input_type("Enter the items to sort (space-separated): ").split()))
        unsorted = arr.copy()
        self.bubble_sort(arr)
        TOOLS.sleep(0.5)
        TOOLS.print_type(f"Unsorted array:\t {unsorted}", "blue")
        TOOLS.print_type(f"Sorted array:\t {arr}", "yellow")

    def bubble_sort(self,arr):
        length = len(arr)
        for i in range(length):
            for j in range(0, length-i-1):
                arrColor(arr,[j],[j+1])
                # for k in range(length):
                #     if k == j:
                #         display_arr += f", \033[94m{arr[k]}\033[0m"
                #         continue
                #     if k == j+1:
                #         display_arr += f", \033[92m{arr[k]}\033[0m"
                #         continue

                #     display_arr += f", {arr[k]}"

                # display_arr = f"[{display_arr[2:]}]"
                
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j] #swap

                    # display_arr = f"[{display_arr[2:]}]"
                    # TOOLS.print_type(display_arr,None,0.01)

                    arrColor(arr,[],[],[j,j+1])
                    # for k in range(length):
                    #     if k == j or k == j+1:
                    #         display_arr += f", \033[93m{arr[k]}\033[0m"
                    #         continue
                    #     display_arr += f", {arr[k]}"

                    # display_arr = f"[{display_arr[2:]}]"
                    continue
        return arr
#endregion bubble sort

#region selection sort
    def _selection_sort(self):
        arr = list(map(int, TOOLS.input_type("Enter the items to sort (space-separated): ").split()))
        self.selection_sort(arr)
        TOOLS.sleep(0.5)
        TOOLS.print_type(f"Sorted array: {arr}")

    def selection_sort(self,arr):
        length = len(arr)
        for i in range(length):
            min_idx = i
            for j in range(i+1, length):

                if arr[j] < arr[min_idx]:
                    min_idx = j
                    # arrColor(arr, [],[], [], [min_idx])

            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr
#endregion selection sort

#region insertion sort
    def _insertion_sort(self):
        arr = list(map(int, TOOLS.input_type("Enter the items to sort (space-separated): ").split()))
        self.insertion_sort(arr)
        TOOLS.sleep(0.5)
        TOOLS.print_type(f"Sorted array: {arr}")

    def insertion_sort(self,arr):
        length = len(arr)
        for i in range(1, length):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                arrColor(arr,[j], [key])
                j -= 1
            arr[j + 1] = key
        return arr
#endregion insertion sort

#region merge sort
    def _merge_sort(self):
        arr = list(map(int, TOOLS.input_type("Enter the items to sort (space-separated): ").split()))
        self.merge_sort(arr)
        TOOLS.sleep(0.5)
        TOOLS.print_type(f"Sorted array: {arr}")

    @staticmethod
    def merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]

            Sorting.merge_sort(L)
            Sorting.merge_sort(R)

            Sorting.merge(arr, L, R)
        return arr

    @staticmethod
    def merge(arr, L, R):
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
#endregion merge sort

#region quick sort
    def _quick_sort(self):
        arr = list(map(int, TOOLS.input_type("Enter the items to sort (space-separated): ").split()))
        self.quick_sort(arr, 0, len(arr) - 1)
        TOOLS.sleep(0.5)
        TOOLS.print_type(f"Sorted array: {arr}")

    def quick_sort(self, arr, low, high):
        if low < high:
            pi = self.partition(arr, low, high)
            self.quick_sort(arr, low, pi - 1)
            self.quick_sort(arr, pi + 1, high)

    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
#endregion quick sort

#region bucket sort
    def _bucket_sort(self):
        arr = list(map(int, TOOLS.input_type("Enter the items to sort (space-separated): ").split()))
        sorted_arr = self.bucket_sort(arr)
        TOOLS.sleep(0.5)
        TOOLS.print_type(f"Sorted array: {sorted_arr}")

    def bucket_sort(self, arr):
        bucket = []
        for i in range(len(arr)):
            bucket.append([])

        for j in arr:
            index_b = min(int(10 * j), len(arr) - 1)
            bucket[index_b].append(j)
        for i in range(len(arr)):
            self.insertion_sort(bucket[i])
        sorted_arr = []
        for i in range(len(arr)):
            sorted_arr = sorted_arr + bucket[i]
        arr = sorted_arr.copy()
        return sorted_arr
#endregion bucket sort

#region shell sort
    def _shell_sort(self):
        arr = list(map(int, TOOLS.input_type("Enter the items to sort (space-separated): ").split()))
        self.shell_sort(arr)
        TOOLS.sleep(0.5)
        TOOLS.print_type(f"Sorted array: {arr}")

    def shell_sort(self, arr):
        n = len(arr)
        gap = n // 2
        while gap > 0:
            for start in range(gap):
                subarray_indices = list(range(start, n, gap))
                subarray = [arr[i] for i in subarray_indices]
                self.insertion_sort(subarray)
                TOOLS.print_type(subarray)
                TOOLS.sleep(0.5)
            for idx, val in zip(subarray_indices, subarray):
                arr[idx] = val
            gap //= 2
        return arr
#endregion shell sort

#region comb sort
    def _comb_sort(self):
        arr = list(map(int, TOOLS.input_type("Enter the items to sort (space-separated): ").split()))
        self.comb_sort(arr)
        TOOLS.sleep(0.5)
        TOOLS.print_type(f"Sorted array: {arr}")

    def comb_sort(self, arr):
        n = len(arr)
        gap = n
        shrink = 1.3
        sorted_flag = False

        while gap > 1 or not sorted_flag:
            gap = int(gap / shrink)
            if gap < 1:
                gap = 1
            sorted_flag = True

            for i in range(n - gap):
                if arr[i] > arr[i + gap]:
                    arr[i], arr[i + gap] = arr[i + gap], arr[i]
                    sorted_flag = False
        return arr
#endregion comb sort

#region radix sort
    def _radix_sort(self):
        arr = list(map(int, TOOLS.input_type("Enter the items to sort (space-separated):").split()))
        self.radix_sort(arr)
        TOOLS.sleep(0.5)
        TOOLS.print_type(f"Sorted array: {arr}")
        for i in arr:
            TOOLS.print_type(f"{arr.index(i) + 1}. {i}")

    def radix_sort(self, arr):
        max_num = max(arr)
        exp = 1
        while max_num // exp > 0:
            self.counting_sort(arr, exp)
            exp *= 10
        return arr
    
    def counting_sort(self, arr, exp):
        n = len(arr)
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            index = arr[i] // exp
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        for i in range(n - 1, -1, -1):
            index = arr[i] // exp
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1

        for i in range(n):
            arr[i] = output[i]
        return arr
#endregion radix sort

#region tree sort
    def _tree_sort(self):
        arr = list(map(int, TOOLS.input_type("Enter the items to sort (space-separated): ").split()))
        sorted_arr = self.tree_sort(arr)
        TOOLS.sleep(0.5)
        TOOLS.print_type(f"Sorted array: {sorted_arr}")

    def tree_sort(self, arr):
        class Node:
            def __init__(self, key):
                self.left = None
                self.right = None
                self.val = key

        def insert(root, key):
            if root is None:
                return Node(key)
            else:
                if root.val < key:
                    root.right = insert(root.right, key)
                else:
                    root.left = insert(root.left, key)
            return root

        def inorder_traversal(root, sorted_arr):
            if root:
                inorder_traversal(root.left, sorted_arr)
                sorted_arr.append(root.val)
                inorder_traversal(root.right, sorted_arr)

        root = None
        for key in arr:
            root = insert(root, key)

        sorted_arr = []
        inorder_traversal(root, sorted_arr)
        return sorted_arr
#endregion tree sort

#region tournament sort
    def _tournament_sort(self):
        arr = list(map(int, TOOLS.input_type("Enter the items to sort (space-separated): ").split()))
        sorted_arr = self.tournament_sort(arr)
        TOOLS.sleep(0.5)
        TOOLS.print_type(f"Sorted array: {sorted_arr}")

    def tournament_sort(self, arr):
        n = len(arr)
        if n == 0:
            return arr
        if n == 1:
            return arr

        # Create a tournament tree
        tree = [None] * (2 * n - 1)

        # Build the tree
        for i in range(n):
            tree[n - 1 + i] = arr[i]

        for i in range(n - 2, -1, -1):
            tree[i] = min(tree[2 * i + 1], tree[2 * i + 2])

        sorted_arr = []
        while len(sorted_arr) < n:
            # Find the minimum element
            min_index = 0
            for i in range(1, n):
                if tree[n - 1 + i] < tree[n - 1 + min_index]:
                    min_index = i

            sorted_arr.append(tree[n - 1 + min_index])
            # Remove the minimum element from the tree
            tree[n - 1 + min_index] = float('inf')

            # Update the tree
            for i in range((n - 2) // 2, -1, -1):
                tree[i] = min(tree[2 * i + 1], tree[2 * i + 2])

        return sorted_arr
#endregion tournament sort