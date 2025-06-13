import os
import time
import random

# region Helper Functions
# Helper function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Helper function to simulate a delay (in seconds)
def sleep(seconds):
    time.sleep(seconds)
# endregion

# region GCD & LCM
class GCD_LCM:
    """Performs GCD and LCM calculations using classic number theory."""

    def __init__(self):
        clear_screen()
        print(">> Welcome to the GCD & LCM Utility!")
        sleep(1)
        self.start()

    def start(self):
        print("\nWhich operation do you need?")
        print(" 1. Find the GCD (Greatest Common Divisor)")
        print(" 2. Find the LCM (Least Common Multiple)")
        print(" 3. Exit to Main Menu")

        choice = input("Choose (1, 2 or 3): ").strip()

        if choice == '1':
            self.gcd()
        elif choice == '2':
            self.lcm()
        elif choice == '3':
            print("👋 Returning to main menu...")
            sleep(1)
        else:
            print("⚠️ Invalid option. Returning to menu.")

    def gcd(self):
        try:
            a = int(input("\nEnter the first number: "))
            b = int(input("Enter the second number: "))
        except ValueError:
            print("⚠️ Invalid input. Use integers only.")
            return

        print(f"\n🔍 Finding GCD of {a} and {b} using Euclidean Algorithm:")
        while b != 0:
            print(f"{a} % {b} = {a % b}")
            a, b = b, a % b

        print(f"✅ Result: GCD = {a}")

    def lcm(self):
        try:
            a = int(input("\nEnter the first number: "))
            b = int(input("Enter the second number: "))
        except ValueError:
            print("⚠️ Please enter valid integers.")
            return

        original_a, original_b = a, b
        print(f"\n🧮 Calculating LCM of {a} and {b}...")

        while b != 0:
            a, b = b, a % b
        gcd = a

        lcm = abs(original_a * original_b) // gcd
        print(f"Step 1: GCD = {gcd}")
        print(f"Step 2: LCM = |{original_a} × {original_b}| ÷ {gcd} = {lcm}")
        print(f"✅ Result: LCM = {lcm}")
# endregion

# region conversion
class Conversion:
    """A flexible number base converter with detailed, step-by-step tracing."""

    def __init__(self):
        clear_screen()
        print("🚀 Welcome to the Number Base Conversion Hub!")
        sleep(1)
        self.start()

    def start(self):
        print("\nWhat kind of number magic do you want to perform today?\n")

        options = [
            ("Decimal → Binary", self.decimal_to_binary),
            ("Binary → Decimal", self.binary_to_decimal),
            ("Decimal → Octal", self.decimal_to_octal),
            ("Decimal → Hexadecimal", self.decimal_to_hex),
            ("Octal → Decimal", self.octal_to_decimal),
            ("Hexadecimal → Decimal", self.hex_to_decimal),
            ("Binary → Octal", self.binary_to_octal),
            ("Binary → Hexadecimal", self.binary_to_hex),
            ("Octal → Binary", self.octal_to_binary),
            ("Octal → Hexadecimal", self.octal_to_hex),
            ("Hexadecimal → Binary", self.hex_to_binary),
            ("Hexadecimal → Octal", self.hex_to_octal),
        ]

        random.shuffle(options)

        for i, (label, _) in enumerate(options, 1):
            print(f" {i}. {label}")

        try:
            choice = int(input("\nPick a number from above to get started: "))
            if 1 <= choice <= len(options):
                print()
                options[choice - 1][1]()
            else:
                print("❗ That number isn’t available in the list.")
        except ValueError:
            print("⚠️ Numbers only, please.")

    def decimal_to_binary(self):
        try:
            num = int(input("Type in a decimal number and watch it become binary: "))
            self._decimal_to_base(num, 2, "Binary")
        except ValueError:
            print("⚠️ Please enter a valid integer.")

    def binary_to_decimal(self):
        binary = input("Drop a binary number here (only 0s and 1s): ").strip()
        if not all(c in '01' for c in binary):
            print("⚠️ Invalid binary format.")
            return
        steps = [f"{digit} × 2^{i} = {int(digit)*(2**i)}"
                 for i, digit in enumerate(binary[::-1])]
        print("Let's break it down step-by-step:\n" + "\n".join(steps))
        print(f"→ That’s {int(binary, 2)} in decimal!")

    def decimal_to_octal(self):
        try:
            num = int(input("Enter a decimal number, and I'll convert it to octal: "))
            self._decimal_to_base(num, 8, "Octal")
        except ValueError:
            print("⚠️ Please enter a valid integer.")

    def decimal_to_hex(self):
        try:
            num = int(input("Pop in a decimal number, and let's make it hexadecimal: "))
            self._decimal_to_base(num, 16, "Hexadecimal")
        except ValueError:
            print("⚠️ Please enter a valid integer.")

    def octal_to_decimal(self):
        octal = input("Give me an octal number (digits 0–7): ").strip()
        if not all(c in '01234567' for c in octal):
            print("⚠️ That’s not a valid octal number.")
            return
        steps = [f"{digit} × 8^{i} = {int(digit)*(8**i)}"
                 for i, digit in enumerate(octal[::-1])]
        print("Here's how that octal number adds up:\n" + "\n".join(steps))
        print(f"→ In decimal, that’s {int(octal, 8)}!")

    def hex_to_decimal(self):
        hex_str = input("Enter a hexadecimal number (0–9, A–F): ").upper()
        valid = all(c in "0123456789ABCDEF" for c in hex_str)
        if not valid:
            print("⚠️ Invalid hexadecimal input.")
            return
        steps = [f"{char} × 16^{i} = {int(char, 16)*(16**i)}"
                 for i, char in enumerate(hex_str[::-1])]
        print("Let’s decode it together:\n" + "\n".join(steps))
        print(f"→ Converted to decimal: {int(hex_str, 16)}!")

    def binary_to_octal(self):
        binary = input("Type a binary number, and I'll turn it into octal: ").strip()
        if not all(c in '01' for c in binary):
            print("⚠️ Invalid binary input.")
            return
        dec = int(binary, 2)
        print(f"First, let's see what that is in decimal: {dec}")
        self._decimal_to_base(dec, 8, "Octal")

    def binary_to_hex(self):
        binary = input("Pop a binary number here, and I’ll convert it to hex: ").strip()
        if not all(c in '01' for c in binary):
            print("⚠️ Invalid binary input.")
            return
        dec = int(binary, 2)
        print(f"Step one, decimal version is: {dec}")
        self._decimal_to_base(dec, 16, "Hexadecimal")

    def octal_to_binary(self):
        octal = input("Give me an octal number, I’ll flip it to binary: ").strip()
        if not all(c in '01234567' for c in octal):
            print("⚠️ Invalid octal input.")
            return
        dec = int(octal, 8)
        print(f"Let's convert that to decimal first: {dec}")
        self._decimal_to_base(dec, 2, "Binary")

    def octal_to_hex(self):
        octal = input("Enter an octal number, and I'll give you the hex: ").strip()
        if not all(c in '01234567' for c in octal):
            print("⚠️ Invalid octal input.")
            return
        dec = int(octal, 8)
        print(f"Decimal form first: {dec}")
        self._decimal_to_base(dec, 16, "Hexadecimal")

    def hex_to_binary(self):
        hex_str = input("Drop a hex number here, and I'll show you binary: ").strip().upper()
        if not all(c in "0123456789ABCDEF" for c in hex_str):
            print("⚠️ Invalid hexadecimal input.")
            return
        dec = int(hex_str, 16)
        print(f"Decimal equivalent is: {dec}")
        self._decimal_to_base(dec, 2, "Binary")

    def hex_to_octal(self):
        hex_str = input("Type a hex number, and I’ll convert it to octal: ").strip().upper()
        if not all(c in "0123456789ABCDEF" for c in hex_str):
            print("⚠️ Invalid hexadecimal input.")
            return
        dec = int(hex_str, 16)
        print(f"Step one, decimal is: {dec}")
        self._decimal_to_base(dec, 8, "Octal")

    def _decimal_to_base(self, decimal, base, label):
        digits = "0123456789ABCDEF"
        original = decimal
        steps = []
        if decimal == 0:
            print(f"Conversion Steps:\n{decimal} is zero, so {label} is 0.")
            print(f"→ {label}: 0")
            return
        while decimal > 0:
            r = decimal % base
            q = decimal // base
            step = f"{decimal} ÷ {base} = {q} remainder {r}"
            if base == 16:
                step += f" (which is '{digits[r]}')"
            steps.append(step)
            decimal = q
        print("Step-by-step breakdown:\n" + "\n".join(reversed(steps)))
        if base == 2:
            converted = bin(original)[2:]
        elif base == 8:
            converted = oct(original)[2:]
        else:
            converted = hex(original)[2:].upper()
        print(f"🎉 And here’s the final {label} value: {converted}")
# endregion conversion

# region set theory
class SetTheory:
    """Handles user interaction and operations related to basic set theory."""

    def __init__(self):
        self.set_a = set()
        self.set_b = set()
        clear_screen()
        print("🧠 Set Theory Function Activated!")
        sleep(1)
        self.run()

    def run(self):
        self.display_welcome()
        self.get_sets()
        self.display_sets()
        self.compute_results()

    def display_welcome(self):
        print("👋 Welcome to the Set Theory Console!")
        print("Let's explore how sets interact...")

    def get_sets(self):
        self.set_a = self.input_set("A")
        self.set_b = self.input_set("B")

    def input_set(self, label):
        raw = input(f"\nEnter elements of set {label} (separated by spaces): ")
        cleaned = set(raw.strip().split())
        print(f"✅ Set {label} captured: {cleaned}")
        return cleaned

    def display_sets(self):
        print("\n📦 You entered:")
        print(f"Set A: {self.set_a}")
        print(f"Set B: {self.set_b}")

    def compute_results(self):
        print("\n🔄 Processing set operations...\n")
        sleep(1)

        operations = [
            ("🔗 Union", self._union),
            ("🎯 Intersection", self._intersection),
            ("➖ Difference (A - B)", self._difference),
            ("📋 Subset Check", self._subset_check),
            ("🆚 Equality Check", self._equality_check),
        ]
        random.shuffle(operations)

        for label, func in operations:
            print(f"{label}")
            func()
            print("-" * 40)

    def _union(self):
        result = self.set_a.copy()
        for item in self.set_b:
            if item not in result:
                print(f"➕ Adding '{item}' to the union set")
                result.add(item)
            else:
                print(f"🔁 '{item}' already in the union")
        print(f"✅ Union: {result}")

    def _intersection(self):
        result = set()
        for item in self.set_a:
            if item in self.set_b:
                print(f"✅ '{item}' found in both A and B")
                result.add(item)
            else:
                print(f"❌ '{item}' only in A")
        print(f"🎯 Intersection: {result}")

    def _difference(self):
        result = set()
        for item in self.set_a:
            if item not in self.set_b:
                print(f"✅ Keeping '{item}' (not in B)")
                result.add(item)
            else:
                print(f"✂️ Removing '{item}' (exists in B)")
        print(f"➖ A - B: {result}")

    def _subset_check(self):
        print("🔎 Checking if A is a subset of B...")
        for item in self.set_a:
            if item not in self.set_b:
                print(f"❌ '{item}' missing in B → Not a subset")
                print("📌 Result: No (A ⊄ B)")
                return
            print(f"✅ '{item}' found in B")
        print("📌 Result: Yes (A ⊆ B)")

    def _equality_check(self):
        print("🔍 Checking if A equals B...")
        all_items = self.set_a.union(self.set_b)
        equal = True
        for item in sorted(all_items):
            in_a = item in self.set_a
            in_b = item in self.set_b
            symbol = "✓" if in_a and in_b else "✗"
            print(f"{symbol} '{item}': in A={in_a}, in B={in_b}")
            if in_a != in_b:
                equal = False
        print(f"📌 Result: {'Yes (A == B)' if equal else 'No (A ≠ B)'}")
# endregion set theory

# region Searching
class Searching:
    """A tool to demonstrate various search algorithms interactively."""

    def __init__(self):
        clear_screen()
        print("🔍 Welcome to the Interactive Search Tool!")
        sleep(1)
        self.menu()

    def menu(self):
        options = [
            ("Interpolation Search", self.interpolation_search),
            ("Linear Search", self.linear_search),
            ("Binary Search", self.binary_search)
        ]
        random.shuffle(options)

        print("\nWhich search adventure shall we take on today?")
        for i, (label, _) in enumerate(options, 1):
            print(f" {i}. {label}")

        try:
            choice = int(input("Pick a number (1–3) to dive in: "))
            if 1 <= choice <= 3:
                print(f"\n➡️ Launching: {options[choice - 1][0]}")
                sleep(1)
                options[choice - 1][1]()  # Call the corresponding function
            else:
                print("⚠️ That number isn’t in range. Try again!")
                self.menu()
        except ValueError:
            print("⚠️ That wasn't a valid number. Let’s go again.")
            self.menu()

    def get_array_and_target(self, sort_array=False):
        try:
            raw = input("\nEnter numbers (space-separated): ")
            arr = list(map(int, raw.strip().split()))
            if sort_array:
                theArray = arr[:]
                theArray.sort()
                print(f"🔢 Sorted Array: {theArray}")
            else:
                theArray = arr[:]
                print(f"📦 Your Array: {theArray}")
            target = int(input("🎯 What number are we searching for? "))
            return theArray, target
        except ValueError:
            print("⚠️ Invalid input. Use only integers please!")
            return self.get_array_and_target(sort_array)

    def linear_search(self):
        arr, target = self.get_array_and_target()
        print("\n🔎 Starting linear search...\n")
        sleep(0.5)

        for idx, val in enumerate(arr):
            print(f"Checking index {idx}: {val}")
            if val == target:
                print(f"🎉 Match found! {target} is at index {idx}")
                return
            print("→ Nope, trying next...")
        print(f"😞 Sadly, {target} is not in the list.")

    def binary_search(self):
        arr, target = self.get_array_and_target(sort_array=True)
        print("\n🔎 Beginning binary search...\n")
        sleep(0.5)

        left, right = 0, len(arr) - 1
        step = 1

        while left <= right:
            mid = (left + right) // 2
            print(f"Step {step}: left={left}, right={right}, mid={mid} → {arr[mid]}")
            step += 1

            if arr[mid] == target:
                print(f"🎯 Found {target} at index {mid}!")
                return
            elif arr[mid] < target:
                print(f"{arr[mid]} < {target}, moving right ➡️")
                left = mid + 1
            else:
                print(f"{arr[mid]} > {target}, moving left ⬅️")
                right = mid - 1

        print(f"😔 {target} was not found.")

    def interpolation_search(self):
        arr, target = self.get_array_and_target(sort_array=True)
        print("\n🔎 Beginning interpolation search...\n")
        sleep(0.5)

        low, high = 0, len(arr) - 1
        step = 1

        while low <= high and arr[low] <= target <= arr[high]:
            if arr[high] == arr[low]:
                if arr[low] == target:
                    print(f"🎯 Target {target} found at index {low}!")
                    return
                break

            pos = low + int(((target - arr[low]) * (high - low)) / (arr[high] - arr[low]))

            if pos < low or pos > high:
                break

            print(f"Step {step}: low={low}, high={high}, pos={pos} → {arr[pos]}")
            step += 1

            if arr[pos] == target:
                print(f"🎉 Jackpot! {target} found at index {pos}")
                return
            elif arr[pos] < target:
                print(f"{arr[pos]} < {target}, shifting right ➡️")
                low = pos + 1
            else:
                print(f"{arr[pos]} > {target}, shifting left ⬅️")
                high = pos - 1

        print(f"💔 No match found for {target}.")
# endregion

#region sorting
class Sorting:
    """A simple class for sorting algorithms."""

    def __init__(self):
        clear_screen()
        print("⏳ Initializing Sorting Module...")
        sleep(1)
        self.start()

    def start(self):
        methods = [
            ("Quick Sort", self.quick_sort),
            ("Tree Sort", self.tree_sort),
            ("Insertion Sort", self.insertion_sort),
            ("Merge Sort", self.merge_sort),
            ("Bubble Sort", self.bubble_sort),
            ("Bucket Sort", self.bucket_sort),
            ("Comb Sort", self.comb_sort),
            ("Shell Sort", self.shell_sort),
            ("Radix Sort", self.radix_sort),
            ("Selection Sort", self.selection_sort),
        ]

        clear_screen()
        print("\n📊 Available Sorting Algorithms:")
        for idx, (name, _) in enumerate(methods, 1):
            print(f" {idx}. {name}")
        print(" 0. Back to Main Menu")

        try:
            choice = int(input("\n🔢 Select an option: "))
            if choice == 0:
                return
            _, func = methods[choice - 1]
            func()
        except (ValueError, IndexError):
            print("⚠️ Invalid input. Please select a valid number.")
            sleep(1.5)

    def bubble_sort(self):
        arr = list(map(int, input("Enter numbers (space-separated): ").split()))
        print("\n🔁 Performing Bubble Sort...")
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    print(f"Swapping {arr[j]} and {arr[j+1]} →", end=" ")
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    print(arr)
                    sleep(0.01)
        print(f"✅ Sorted Result: {arr}")

    def selection_sort(self):
        arr = list(map(int, input("Enter numbers (space-separated): ").split()))
        print("\n🔍 Performing Selection Sort...")
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            print(f"Step {i+1}: {arr}")
            sleep(0.01)
        print(f"✅ Sorted Result: {arr}")

    def insertion_sort(self):
        arr = list(map(int, input("Enter numbers (space-separated): ").split()))
        print("\n📥 Performing Insertion Sort...")
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
            print(f"Step {i}: {arr}")
            sleep(0.01)
        print(f"✅ Sorted Result: {arr}")

    def merge_sort(self):
        arr = list(map(int, input("Enter numbers (space-separated): ").split()))
        print("\n🔗 Performing Merge Sort...")
        self._merge_sort(arr)
        print(f"✅ Sorted Result: {arr}")

    def _merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]
            print(f"Split: {L} | {R}")
            self._merge_sort(L)
            self._merge_sort(R)
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
            print(f"Merged: {arr}")
            sleep(0.05)

    def quick_sort(self):
        arr = list(map(int, input("Enter numbers (space-separated): ").split()))
        print("\n⚡ Performing Quick Sort...")
        self._quick_sort(arr, 0, len(arr) - 1)
        print(f"✅ Sorted Result: {arr}")

    def _quick_sort(self, arr, low, high):
        if low < high:
            pi = self._partition(arr, low, high)
            self._quick_sort(arr, low, pi - 1)
            self._quick_sort(arr, pi + 1, high)

    def _partition(self, arr, low, high):
        pivot = arr[high]
        print(f"Pivot: {pivot}")
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                print(f"Swapped: {arr}")
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def bucket_sort(self):
        arr = list(map(int, input("Enter numbers (space-separated): ").split()))
        if not arr:
            print("⚠️ Empty list")
            return
        print("\n🪣 Performing Bucket Sort...")
        bucket_count = 10
        max_val, min_val = max(arr), min(arr)
        buckets = [[] for _ in range(bucket_count)]
        for num in arr:
            idx = int((num - min_val) / (max_val - min_val + 1) * (bucket_count - 1))
            buckets[idx].append(num)
        for i, b in enumerate(buckets):
            b.sort()
            print(f"Bucket {i}: {b}")
        sorted_arr = [num for b in buckets for num in b]
        print(f"✅ Sorted Result: {sorted_arr}")

    def shell_sort(self):
        arr = list(map(int, input("Enter numbers (space-separated): ").split()))
        print("\n🔩 Performing Shell Sort...")
        gap = len(arr) // 2
        while gap > 0:
            for i in range(gap, len(arr)):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            print(f"Gap {gap}: {arr}")
            gap //= 2
        print(f"✅ Sorted Result: {arr}")

    def comb_sort(self):
        arr = list(map(int, input("Enter numbers (space-separated): ").split()))
        print("\n🧹 Performing Comb Sort...")
        gap = len(arr)
        shrink = 1.3
        sorted_flag = False
        while gap > 1 or not sorted_flag:
            gap = int(gap / shrink)
            if gap < 1:
                gap = 1
            sorted_flag = True
            for i in range(len(arr) - gap):
                if arr[i] > arr[i + gap]:
                    arr[i], arr[i + gap] = arr[i + gap], arr[i]
                    sorted_flag = False
                    print(f"Swapped: {arr}")
        print(f"✅ Sorted Result: {arr}")

    def radix_sort(self):
        arr = list(map(int, input("Enter numbers (space-separated): ").split()))
        print("\n🔢 Performing Radix Sort...")
        max_val = max(arr)
        exp = 1
        while max_val // exp > 0:
            self._counting_sort(arr, exp)
            print(f"Exp {exp}: {arr}")
            exp *= 10
        print(f"✅ Sorted Result: {arr}")

    def _counting_sort(self, arr, exp):
        n = len(arr)
        output = [0] * n
        count = [0] * 10
        for i in arr:
            index = (i // exp) % 10
            count[index] += 1
        for i in range(1, 10):
            count[i] += count[i - 1]
        for i in reversed(arr):
            index = (i // exp) % 10
            output[count[index] - 1] = i
            count[index] -= 1
        for i in range(n):
            arr[i] = output[i]

    def tree_sort(self):
        print("\n🌳 Tree Sort not yet implemented. (Placeholder)")
#endregion sorting

# region Prime
class Prime:
    """A simple class for prime number operations."""

    def __init__(self):
        clear_screen()
        print("🔢 Prime Numbers Playground")
        sleep(1)
        self.start()

    def start(self):
        print("\nChoose an option:")
        print(" 1. Check if a number is prime")
        print(" 2. List primes in a range (Sieve)")
        print(" 3. Prime factorization")
        print(" 4. Fermat's Little Theorem calculator")
        print(" 5. Primitive roots explorer")
        try:
            choice = int(input("Select (1–5): "))
        except ValueError:
            print("⚠️ Please enter a number from the menu.")
            return

        match choice:
            case 1: self.check_prime()
            case 2: self.sieve()
            case 3: self.prime_factors()
            case 4: self.fermats()
            case 5: self.primitive_roots()
            case _: print("⚠️ Invalid selection.")

    def check_prime(self):
        try:
            n = int(input("\nNumber to test for primality: "))
        except ValueError:
            print("⚠️ Enter a valid integer.")
            return

        if n < 2:
            print(f"{n} is not prime.")
            return

        for i in range(2, int(n ** 0.5) + 1):
            print(f"Testing {n} ÷ {i} (remainder: {n % i})")
            if n % i == 0:
                print(f"{n} is divisible by {i}, so it is not prime.")
                return

        print(f"{n} is prime.")

    @staticmethod
    def _check_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def prime_factors(self):
        try:
            n = int(input("\nEnter a number to factor: "))
        except ValueError:
            print("⚠️ Please enter a valid integer.")
            return

        original = n
        factors = []

        print(f"\nFactoring {original}:")

        while n % 2 == 0:
            print(f"{n} is even, add 2.")
            factors.append(2)
            n //= 2

        i = 3
        while i * i <= n:
            while n % i == 0:
                print(f"{n} is divisible by {i}, add {i}.")
                factors.append(i)
                n //= i
            i += 2

        if n > 2:
            print(f"Remaining prime: {n}")
            factors.append(n)

        print(f"\nPrime factors of {original}: {factors}")

    def sieve(self):
        print("\nSieve of Eratosthenes: Find all primes in a range.")
        try:
            start = int(input("Range start (inclusive): "))
            end = int(input("Range end (exclusive): "))
        except ValueError:
            print("⚠️ Please enter valid numbers.")
            return

        if end <= start:
            print("End must be greater than start.")
            return

        print(f"\nFinding primes from {start} to {end}...")
        primes = [i for i in range(start, end) if self._check_prime(i)]

        print(f"\nPrimes in range {start} to {end}:")
        print(primes)

    def fermats(self):
        print("\nFermat’s Little Theorem: a^(k) mod p")
        try:
            a = int(input("Enter a: "))
            k = int(input("Enter exponent k: "))
            p = int(input("Enter a prime p: "))
        except ValueError:
            print("⚠️ Enter integers only.")
            return

        if not self._check_prime(p):
            print("p must be prime.")
            return

        result = pow(a, k, p)
        print(f"\n{a}^{k} mod {p} = {result}")

    def primitive_roots(self):
        print("\nPrimitive Roots Explorer")
        try:
            p = int(input("Prime p: "))
            a = int(input("Test number a: "))
        except ValueError:
            print("Enter positive integers.")
            return

        if p <= 0 or a <= 0:
            print("Only positive integers allowed.")
            return

        if not self._check_prime(p):
            print("p must be prime.")
            return

        required = set(range(1, p))
        actual = set(pow(a, k, p) for k in range(1, p))

        if actual == required:
            print(f"{a} is a primitive root modulo {p}.")
        else:
            print(f"{a} is not a primitive root modulo {p}.")

        print(f"\nAll primitive roots of {p}:")
        roots = []
        for g in range(2, p):
            if set(pow(g, k, p) for k in range(1, p)) == required:
                roots.append(g)

        print(roots)
# endregion

#region ciphers
class Ciphers:
    """Encrypts and decrypts text using various classical ciphers."""

    def __init__(self):
        clear_screen()
        print("🔐 Welcome to the Cipher Workshop!")
        sleep(1)
        self.mode_menu()

    def mode_menu(self):
        print("\nWould you like to encrypt or decrypt today?")
        modes = [("Encrypt", self.run_menu_encrypt), ("Decrypt", self.run_menu_decrypt)]
        random.shuffle(modes)
        for i, (label, _) in enumerate(modes, start=1):
            print(f" {i}. {label}")
        try:
            choice = int(input("Select your mode (number): "))
            modes[choice - 1][1]()
        except (ValueError, IndexError):
            print("Oops! That's not a valid choice. Let's try again.")
            self.mode_menu()

    def run_menu_encrypt(self):
        print("\nPick a cipher to use for encryption:")
        options = [
            ("Rail Fence Cipher", self.rail_fence_encrypt),
            ("Playfair Cipher", self.playfair_encrypt),
            ("Hill Cipher", self.hill_encrypt),
            ("Columnar Cipher", self.columnar_encrypt),
            ("Caesar Cipher", self.caesar_encrypt),
            ("Vernam Cipher", self.vernam_encrypt),
            ("Vigenère Cipher", self.vigenere_encrypt),
            ("One-Time Pad Cipher", self.one_time_pad_encrypt)
        ]
        random.shuffle(options)
        for i, (label, _) in enumerate(options, start=1):
            print(f" {i}. {label}")
        try:
            choice = int(input("Choose your cipher (number): "))
            options[choice - 1][1]()
        except (ValueError, IndexError):
            print("That wasn't a valid option. Please try again.")

    def run_menu_decrypt(self):
        print("\nPick a cipher to use for decryption:")
        options = [
            ("Rail Fence Cipher", self.rail_fence_decrypt),
            ("Playfair Cipher", self.playfair_decrypt),
            ("Hill Cipher", self.hill_decrypt),
            ("Columnar Cipher", self.columnar_decrypt),
            ("Caesar Cipher", self.caesar_decrypt),
            ("Vernam Cipher", self.vernam_decrypt),
            ("Vigenère Cipher", self.vigenere_decrypt),
            ("One-Time Pad Cipher", self.one_time_pad_decrypt)
        ]
        random.shuffle(options)
        for i, (label, _) in enumerate(options, start=1):
            print(f" {i}. {label}")
        try:
            choice = int(input("Choose your cipher (number): "))
            options[choice - 1][1]()
        except (ValueError, IndexError):
            print("That wasn't a valid option. Please try again.")

    # Caesar Encrypt and Decrypt
    def caesar_encrypt(self):
        text = input("Enter your message to encrypt: ")
        shift = int(input("How many positions should we shift? (1–25): "))
        encrypted = ""
        print("\n[Encrypting]")
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                shifted = chr((ord(char) - base + shift) % 26 + base)
                print(f"{char} -> {shifted}")
                encrypted += shifted
            else:
                encrypted += char
        print(f"\nYour encrypted message: {encrypted}")

    def caesar_decrypt(self):
        text = input("Paste the encrypted message: ")
        shift = int(input("What shift was used? (1–25): "))
        decrypted = ""
        print("\n[Decrypting]")
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                shifted = chr((ord(char) - base - shift) % 26 + base)
                print(f"{char} -> {shifted}")
                decrypted += shifted
            else:
                decrypted += char
        print(f"\nYour decrypted message: {decrypted}")

    # Vigenere Encrypt and Decrypt
    def vigenere_encrypt(self):
        text = input("Enter the text to encrypt: ")
        key = input("Enter the keyword: ")
        key_extended = (key * ((len(text) // len(key)) + 1))[:len(text)]
        result = ""
        print("\n[Encrypting]")
        for i, char in enumerate(text):
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                key_char = key_extended[i].upper() if char.isupper() else key_extended[i].lower()
                shift = ord(key_char) - base
                encrypted = chr((ord(char) - base + shift) % 26 + base)
                print(f"{char} + {key_char} -> {encrypted}")
                result += encrypted
            else:
                result += char
        print(f"\nYour encrypted message: {result}")

    def vigenere_decrypt(self):
        text = input("Enter the encrypted text: ")
        key = input("Enter the keyword used: ")
        key_extended = (key * ((len(text) // len(key)) + 1))[:len(text)]
        result = ""
        print("\n[Decrypting]")
        for i, char in enumerate(text):
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                key_char = key_extended[i].upper() if char.isupper() else key_extended[i].lower()
                shift = ord(key_char) - base
                decrypted = chr((ord(char) - base - shift) % 26 + base)
                print(f"{char} - {key_char} -> {decrypted}")
                result += decrypted
            else:
                result += char
        print(f"\nYour decrypted message: {result}")

    # Playfair Encrypt and Decrypt (decrypt method added)
    def playfair_encrypt(self):
        text = input("Message to encrypt: ")
        keyword = input("Keyword to construct matrix: ")
        matrix = self._generate_playfair_matrix(keyword)
        prepared = self._prepare_playfair_text(text)
        encrypted = ""
        print("\n[Playfair Matrix]")
        for row in matrix:
            print(" ".join(row))
        print("\n[Letter Pairs]")
        for i in range(0, len(prepared), 2):
            pair = prepared[i], prepared[i + 1]
            cipher_pair = self._playfair_encrypt_pair(matrix, *pair)
            print(f"{pair[0]}{pair[1]} -> {cipher_pair}")
            encrypted += cipher_pair
        print(f"\nEncrypted output: {encrypted}")

    def playfair_decrypt(self):
        text = input("Ciphertext to decrypt: ")
        keyword = input("Keyword to reconstruct matrix: ")
        matrix = self._generate_playfair_matrix(keyword)
        decrypted = ""
        print("\n[Playfair Matrix]")
        for row in matrix:
            print(" ".join(row))
        print("\n[Letter Pairs]")
        for i in range(0, len(text), 2):
            pair = text[i], text[i + 1]
            plain_pair = self._playfair_decrypt_pair(matrix, *pair)
            print(f"{pair[0]}{pair[1]} -> {plain_pair}")
            decrypted += plain_pair
        print(f"\nDecrypted message: {decrypted}")

    def _playfair_decrypt_pair(self, matrix, a, b):
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == a:
                    row1, col1 = i, j
                if matrix[i][j] == b:
                    row2, col2 = i, j
        if row1 == row2:
            return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            return matrix[row1][col2] + matrix[row2][col1]

    # Vernam encrypt/decrypt (same operation)
    def vernam_encrypt(self):
        text = input("Enter the text to encrypt: ")
        key = input("Enter the key (same length as text): ")
        key = (key * ((len(text) // len(key)) + 1))[:len(text)]
        print("\n[Encrypting]")
        for c, k in zip(text, key):
            print(f"{c} ^ {k} = {chr(ord(c) ^ ord(k))}")
        result = "".join(chr(ord(c) ^ ord(k)) for c, k in zip(text, key))
        print(f"\nEncrypted result: {result}")
        print(f"Hexadecimal representation: {result.encode().hex()}")

    def vernam_decrypt(self):
        text = input("Enter the encrypted text: ")
        key = input("Enter the key used (same length): ")
        key = (key * ((len(text) // len(key)) + 1))[:len(text)]
        print("\n[Decrypting]")
        for c, k in zip(text, key):
            print(f"{c} ^ {k} = {chr(ord(c) ^ ord(k))}")
        result = "".join(chr(ord(c) ^ ord(k)) for c, k in zip(text, key))
        print(f"\nDecrypted result: {result}")
        print(f"Hexadecimal representation: {result.encode().hex()}")

    # One-Time Pad encrypt/decrypt (same operation)
    def one_time_pad_encrypt(self):
        text = input("Enter your message: ")
        key = os.urandom(len(text))
        encrypted = bytes([ord(c) ^ k for c, k in zip(text, key)])
        print("\n[Encrypting]")
        for c, k in zip(text, key):
            print(f"{c} ^ {k} = {ord(c) ^ k}")
        print(f"Generated key (hex): {key.hex()}")
        print(f"Encrypted output (hex): {encrypted.hex()}")

    def one_time_pad_decrypt(self):
        encrypted_hex = input("Paste the encrypted message (hex): ")
        key_hex = input("Paste the key used (hex): ")
        try:
            encrypted = bytes.fromhex(encrypted_hex)
            key = bytes.fromhex(key_hex)
        except Exception:
            print("Couldn't parse hex input. Please check and try again.")
            return
        decrypted = "".join(chr(e ^ k) for e, k in zip(encrypted, key))
        print("\n[Decrypting]")
        for e, k in zip(encrypted, key):
            print(f"{e} ^ {k} = {e ^ k}")
        print(f"\nDecrypted message: {decrypted}")

    # Hill cipher encrypt/decrypt
    def hill_encrypt(self):
        text = input("Text to encrypt: ")
        key_input = input("Enter a 3x3 key matrix (space-separated 9 numbers): ")
        try:
            values = list(map(int, key_input.split()))
            if len(values) != 9:
                print("You must provide exactly 9 numbers.")
                return
            matrix = [values[i:i+3] for i in range(0, 9, 3)]
        except:
            print("Invalid matrix input.")
            return

        small = [chr(i) for i in range(97, 123)]
        big = [chr(i) for i in range(65, 91)]
        chars = [c for c in text if c.isalpha()]
        while len(chars) % 3 != 0:
            chars.append('x')
        nums = [(small + big).index(c.lower()) % 26 for c in chars]
        print("\n[Encrypting]")
        result = ""
        for i in range(0, len(nums), 3):
            block = nums[i:i+3]
            res = [(sum(matrix[r][c] * block[r] for r in range(3)) % 26) for c in range(3)]
            for j, val in enumerate(res):
                orig = chars[i + j]
                print(f"Block: {block} * Col {j} → {val}")
                result += big[val] if orig.isupper() else small[val]
        print("\nKey matrix used:")
        for row in matrix:
            print(row)
        print(f"Encrypted message: {result}")

    def hill_decrypt(self):
        text = input("Text to decrypt: ")
        key_input = input("Enter the 3x3 key matrix (space-separated 9 numbers): ")
        try:
            values = list(map(int, key_input.split()))
            if len(values) != 9:
                print("You must provide exactly 9 numbers.")
                return
            matrix = [values[i:i+3] for i in range(0, 9, 3)]
        except:
            print("Invalid matrix input.")
            return

        # Calculate modular inverse matrix mod 26
        inv_matrix = self._hill_matrix_inverse(matrix)
        if inv_matrix is None:
            print("Matrix is not invertible mod 26. Decryption not possible.")
            return

        small = [chr(i) for i in range(97, 123)]
        big = [chr(i) for i in range(65, 91)]
        chars = [c for c in text if c.isalpha()]
        while len(chars) % 3 != 0:
            chars.append('x')
        nums = [(small + big).index(c.lower()) % 26 for c in chars]
        print("\n[Decrypting]")
        result = ""
        for i in range(0, len(nums), 3):
            block = nums[i:i+3]
            res = [(sum(inv_matrix[r][c] * block[r] for r in range(3)) % 26) for c in range(3)]
            for j, val in enumerate(res):
                orig = chars[i + j]
                print(f"Block: {block} * InvCol {j} → {val}")
                result += big[val] if orig.isupper() else small[val]
        print("\nInverse matrix used:")
        for row in inv_matrix:
            print(row)
        print(f"Decrypted message: {result}")

    def _hill_matrix_inverse(self, matrix):
        # Calculate determinant mod 26
        def det3(m):
            return (m[0][0]*m[1][1]*m[2][2] + m[0][1]*m[1][2]*m[2][0] + m[0][2]*m[1][0]*m[2][1]
                    - m[0][2]*m[1][1]*m[2][0] - m[0][1]*m[1][0]*m[2][2] - m[0][0]*m[1][2]*m[2][1]) % 26
        det = det3(matrix)
        # Find modular inverse of determinant mod 26
        det_inv = self._modular_inverse(det, 26)
        if det_inv is None:
            return None
        # Calculate matrix of cofactors
        cof = [[0]*3 for _ in range(3)]
        cof[0][0] = (matrix[1][1]*matrix[2][2] - matrix[1][2]*matrix[2][1]) % 26
        cof[0][1] = -(matrix[1][0]*matrix[2][2] - matrix[1][2]*matrix[2][0]) % 26
        cof[0][2] = (matrix[1][0]*matrix[2][1] - matrix[1][1]*matrix[2][0]) % 26
        cof[1][0] = -(matrix[0][1]*matrix[2][2] - matrix[0][2]*matrix[2][1]) % 26
        cof[1][1] = (matrix[0][0]*matrix[2][2] - matrix[0][2]*matrix[2][0]) % 26
        cof[1][2] = -(matrix[0][0]*matrix[2][1] - matrix[0][1]*matrix[2][0]) % 26
        cof[2][0] = (matrix[0][1]*matrix[1][2] - matrix[0][2]*matrix[1][1]) % 26
        cof[2][1] = -(matrix[0][0]*matrix[1][2] - matrix[0][2]*matrix[1][0]) % 26
        cof[2][2] = (matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]) % 26
        # Transpose cofactor matrix to get adjugate
        adj = [[cof[j][i] % 26 for j in range(3)] for i in range(3)]
        # Multiply by determinant inverse mod 26
        inv = [[(adj[i][j] * det_inv) % 26 for j in range(3)] for i in range(3)]
        return inv

    def _modular_inverse(self, a, m):
        # Extended Euclidean Algorithm for modular inverse
        a = a % m
        if a == 0:
            return None
        m0, x0, x1 = m, 0, 1
        while a > 1:
            q = a // m
            a, m = m, a % m
            x0, x1 = x1 - q * x0, x0
        return x1 + m0 if x1 < 0 else x1

    # Rail Fence encrypt/decrypt
    def rail_fence_encrypt(self):
        text = input("Enter the message to encrypt: ")
        if any(c.isdigit() for c in text):
            print("Numbers are not allowed in this cipher.")
            return
        try:
            rails = int(input("How many rails? (2–10): "))
            if rails < 2 or rails > 10:
                raise ValueError
        except:
            print("Please enter a valid number of rails.")
            return

        fence = [''] * rails
        rail, direction = 0, 1
        print("\n[Building Zigzag Pattern]")
        for char in text:
            print(f"{char} -> Rail {rail}")
            fence[rail] += char
            rail += direction
            if rail == 0 or rail == rails - 1:
                direction *= -1
        encrypted = ''.join(fence)
        print(f"\nEncrypted message: {encrypted}")

    def rail_fence_decrypt(self):
        ciphertext = input("Enter the ciphertext: ")
        try:
            rails = int(input("How many rails were used? (2–10): "))
            if rails < 2 or rails > 10:
                raise ValueError
        except:
            print("Please enter a valid number of rails.")
            return

        n = len(ciphertext)
        fence = [['' for _ in range(n)] for _ in range(rails)]
        rail, direction = 0, 1
        for i in range(n):
            fence[rail][i] = '*'
            rail += direction
            if rail == 0 or rail == rails - 1:
                direction *= -1

        index = 0
        print("\n[Placing ciphertext in zigzag]")
        for r in range(rails):
            for c in range(n):
                if fence[r][c] == '*' and index < n:
                    fence[r][c] = ciphertext[index]
                    print(f"Placed {ciphertext[index]} at rail {r}, position {c}")
                    index += 1

        result = []
        rail, direction = 0, 1
        print("\n[Reading message in zigzag order]")
        for i in range(n):
            result.append(fence[rail][i])
            print(f"Rail {rail}, position {i} → {fence[rail][i]}")
            rail += direction
            if rail == 0 or rail == rails - 1:
                direction *= -1
        decrypted = ''.join(result)
        print(f"\nDecrypted message: {decrypted}")

    # Columnar encrypt/decrypt
    def columnar_encrypt(self):
        text = input("Enter the plaintext: ").replace(" ", "")
        key = input("Enter the keyword: ").lower()
        n = len(key)
        matrix = [list(text[i:i+n]) for i in range(0, len(text), n)]
        while len(matrix[-1]) < n:
            matrix[-1].append('x')
        print("\n[Columnar Matrix]")
        for row in matrix:
            print("".join(row))

        sorted_key = sorted(list(set(key)))
        order = [sorted_key.index(k) for k in key]
        print(f"Column order based on keyword: {order}")

        result = ""
        for col_num in sorted(order):
            col_idx = order.index(col_num)
            col_text = "".join(matrix[row][col_idx] for row in range(len(matrix)))
            print(f"Column {col_idx} ({key[col_idx]}) -> {col_text}")
            result += col_text
        print(f"\nEncrypted message: {result}")

    def columnar_decrypt(self):
        ciphertext = input("Enter the ciphertext: ")
        key = input("Enter the keyword: ").lower()
        n = len(key)
        num_rows = len(ciphertext) // n
        sorted_key = sorted(list(set(key)))
        order = [sorted_key.index(k) for k in key]

        # Number of chars per column
        cols = {}
        start = 0
        for col_num in sorted(order):
            length = num_rows
            cols[col_num] = ciphertext[start:start+length]
            start += length
        print("\n[Extracted Columns]")
        for k, v in cols.items():
            print(f"Column {k}: {v}")

        # Rebuild matrix by key order
        matrix = [[""]*n for _ in range(num_rows)]
        for col_idx, col_num in enumerate(order):
            col_text = cols[col_num]
            for row in range(num_rows):
                matrix[row][col_idx] = col_text[row]

        print("\n[Reconstructed Matrix]")
        for row in matrix:
            print("".join(row))

        result = "".join(matrix[row][col] for row in range(num_rows) for col in range(n))
        print(f"\nDecrypted message: {result}")
#endregion ciphers

# region Main Program Loop
def main():
    modules = [
        GCD_LCM,
        Conversion,
        SetTheory,
        Searching,
        Sorting,
        Prime,
        Ciphers,
    ]

    while True:
        clear_screen()
        random.shuffle(modules)

        greetings = [
            " Which module piques your curiosity today?",
            " Select a challenge to dive into:",
            " Explore an algorithmic world below:",
            " What topic shall we tackle next?",
        ]
        print(" === Welcome to Nel Jun Endrina's Algorithm Field === \n")
        print(random.choice(greetings))

        for idx, module in enumerate(modules, start=1):
            print(f" {idx}. 🔹 {module.__name__}")
        print(" 0. 🔚 Exit Arena")

        try:
            choice = int(input("\n📥 Enter your choice (0 to quit): "))
        except ValueError:
            print(random.choice([
                "\n⚠️ That wasn’t a number. Try again.",
                "\n⚠️ Numbers only! Let’s go again.",
                "\n⚠️ Input error — please choose by number.",
            ]))
            sleep(1.5)
            continue

        if choice == 0:
            print(random.choice([
                "\n👋 Thanks for exploring with me! See you next time!",
                "\n🚪 Exiting the arena. Until our next algorithm adventure!",
                "\n🌟 You’ve been great! Come back soon.",
            ]))
            break

        if 1 <= choice <= len(modules):
            selected_module = modules[choice - 1]
            while True:
                clear_screen()
                print(f"🚀 Loading {selected_module.__name__} Module...\n")
                selected_module()

                repeat_prompt = random.choice([
                    "\n🔁 Want to rerun this module? (y/N): ",
                    "\n🔄 Try this one again? (y/N): ",
                    "\n⏱️ Repeat this challenge? (y/N): ",
                ])
                again = input(repeat_prompt).strip().lower()
                if again != 'y':
                    break
        else:
            print(random.choice([
                "\n❗ Whoops, that number isn't in the list.",
                "\n❗ Invalid pick. Please choose an available module.",
                "\n❗ Try selecting from the options shown.",
            ]))
            sleep(1.5)

if __name__ == "__main__":
    main()
# endregion
