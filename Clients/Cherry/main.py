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

# region Ciphers
class Ciphers:
    """Encrypts text using various classical ciphers."""

    def __init__(self):
        clear_screen()
        print(">> Cipher Station Activated!")
        sleep(1)
        self.run_menu()

    def run_menu(self):
        print("\nSelect a cryptographic method to explore:")
        options = [
            ("Rail Fence Cipher", self.rail_fence),
            ("Playfair Cipher", self.playfair),
            ("Hill Cipher", self.hill),
            ("Columnar Cipher", self.columnar),
            ("Caesar Cipher", self.caesar),
            ("Vernam Cipher", self.vernam),
            ("Vigenère Cipher", self.vigenere),
            ("One-Time Pad Cipher", self.one_time_pad)
        ]
        random.shuffle(options)
        for i, (label, _) in enumerate(options, start=1):
            print(f" {i}. {label}")
        try:
            choice = int(input("Your pick (number): "))
            options[choice - 1][1]()
        except (ValueError, IndexError):
            print("Hmm, invalid choice. Please select a valid number.")

    def caesar(self):
        text = input("Type your message: ")
        shift = int(input("By how many positions should we shift? (1–25): "))
        encrypted = ""
        print("\n[Process]")
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                shifted = chr((ord(char) - base + shift) % 26 + base)
                print(f"{char} -> {shifted}")
                encrypted += shifted
            else:
                encrypted += char
        print(f"\nEncrypted Message → {encrypted}")

    def vigenere(self):
        text = input("Enter the text: ")
        key = input("Enter the keyword: ")
        key_extended = (key * ((len(text) // len(key)) + 1))[:len(text)]
        result = ""
        print("\n[Process]")
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
        print(f"\nVigenère Encryption → {result}")

    def playfair(self):
        text = input("Message to encrypt: ")
        keyword = input("Keyword to construct matrix: ")
        matrix = self._generate_playfair_matrix(keyword)
        prepared = self._prepare_playfair_text(text)
        encrypted = ""
        print("\n[Matrix]")
        for row in matrix:
            print(" ".join(row))
        print("\n[Pairs]")
        for i in range(0, len(prepared), 2):
            pair = prepared[i], prepared[i + 1]
            cipher_pair = self._playfair_encrypt_pair(matrix, *pair)
            print(f"{pair[0]}{pair[1]} -> {cipher_pair}")
            encrypted += cipher_pair
        print(f"\nCiphertext → {encrypted}")

    def _generate_playfair_matrix(self, keyword):
        keyword = keyword.upper().replace("J", "I")
        seen, key = set(), ""
        for char in keyword:
            if char.isalpha() and char not in seen:
                seen.add(char)
                key += char
        for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
            if char not in seen:
                key += char
        return [list(key[i:i+5]) for i in range(0, 25, 5)]

    def _prepare_playfair_text(self, text):
        text = text.upper().replace("J", "I")
        i, prepared = 0, ""
        while i < len(text):
            char1 = text[i]
            char2 = text[i + 1] if i + 1 < len(text) else "X"
            if char1 == char2:
                prepared += char1 + "X"
                i += 1
            else:
                prepared += char1 + char2
                i += 2
        return prepared if len(prepared) % 2 == 0 else prepared + "X"

    def _playfair_encrypt_pair(self, matrix, a, b):
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == a:
                    row1, col1 = i, j
                if matrix[i][j] == b:
                    row2, col2 = i, j
        if row1 == row2:
            return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            return matrix[row1][col2] + matrix[row2][col1]

    def vernam(self):
        text = input("Input text: ")
        key = input("Key (same length as text): ")
        key = (key * ((len(text) // len(key)) + 1))[:len(text)]
        print("\n[Process]")
        for c, k in zip(text, key):
            print(f"{c} ^ {k} = {chr(ord(c) ^ ord(k))}")
        result = "".join(chr(ord(c) ^ ord(k)) for c, k in zip(text, key))
        print(f"\nEncrypted: {result}")
        print(f"As hex: {result.encode().hex()}")

    def one_time_pad(self):
        text = input("Message: ")
        key = os.urandom(len(text))
        encrypted = bytes([ord(c) ^ k for c, k in zip(text, key)])
        print("\n[Process]")
        for c, k in zip(text, key):
            print(f"{c} ^ {k} = {ord(c) ^ k}")
        print(f"Generated key (hex): {key.hex()}")
        print(f"Encrypted output (hex): {encrypted.hex()}")

    def hill(self):
        text = input("Text to encode: ")
        key_input = input("Provide 3x3 key matrix (space-separated 9 numbers): ")
        try:
            values = list(map(int, key_input.split()))
            if len(values) != 9:
                print("Error: Expected exactly 9 numbers.")
                return
            matrix = [values[i:i+3] for i in range(0, 9, 3)]
        except:
            print("Matrix input couldn't be processed.")
            return

        small = [chr(i) for i in range(97, 123)]
        big = [chr(i) for i in range(65, 91)]
        chars = [c for c in text if c.isalpha()]
        while len(chars) % 3 != 0:
            chars.append('x')
        nums = [(small + big).index(c.lower()) % 26 for c in chars]
        print("\n[Process]")
        result = ""
        for i in range(0, len(nums), 3):
            block = nums[i:i+3]
            res = [(sum(matrix[r][c] * block[r] for r in range(3)) % 26) for c in range(3)]
            for j, val in enumerate(res):
                orig = chars[i + j]
                print(f"Block: {block} * Col {j} → {val}")
                result += big[val] if orig.isupper() else small[val]
        print("\nMatrix used:")
        for row in matrix:
            print(row)
        print(f"Hill Cipher Result → {result}")

    def rail_fence(self):
        text = input("Message: ")
        if any(c.isdigit() for c in text):
            print("Numbers aren't allowed here.")
            return
        try:
            rails = int(input("Rails to zigzag across (2–10): "))
            if not (2 <= rails <= 10):
                raise ValueError
        except:
            print("Bad input for rail count.")
            return

        fence = [''] * rails
        rail, direction = 0, 1
        print("\n[Zigzag Process]")
        for char in text:
            print(f"Char {char} → Rail {rail}")
            fence[rail] += char
            rail += direction
            if rail == 0 or rail == rails - 1:
                direction *= -1
        print(f"\nEncoded Message → {''.join(fence)}")

    def columnar(self):
        text = input("Plaintext to scramble: ")
        print(f"You’ll need enough cells for {len(text)} characters.")
        try:
            rows = int(input("Rows: "))
            cols = int(input("Columns: "))
            key = list(map(int, input(f"Key order for {cols} columns (e.g. 3 1 2): ").split()))
            if len(key) != cols or sorted(key) != list(range(1, cols + 1)):
                raise ValueError
        except:
            print("Column key setup failed.")
            return

        padded = text.ljust(rows * cols, 'x')[:rows * cols]
        matrix = [list(padded[i * cols:(i + 1) * cols]) for i in range(rows)]
        print("\n[Matrix]")
        for row in matrix:
            print(" ".join(row))
        result = ""
        print("\n[Columnar Read Order]")
        for k in key:
            print(f"Reading column {k}:")
            for r in matrix:
                print(f" → {r[k - 1]}")
                result += r[k - 1]
        print(f"\nColumnar Encrypted Output → {result}")
# endregion

# region set theory
class SetTheory:
    """Handles user interaction and operations related to basic set theory."""

    def __init__(self):
        self.set_a = set()
        self.set_b = set()
        clear_screen()
        print(">> Set Theory Function Activated!")
        sleep(1)
        self.run()

    def run(self):
        self.display_welcome()
        self.get_sets()
        self.display_sets()
        self.compute_results()

    def display_welcome(self):
        print("Welcome to the Set Theory Console!")

    def get_sets(self):
        self.set_a = self.input_set("A")
        self.set_b = self.input_set("B")

    def input_set(self, label):
        raw = input(f"Enter the elements of set {label} (space-separated): ")
        return set(raw.strip().split())

    def display_sets(self):
        print("\nYou entered the following sets:")
        print(f"Set A → {self.set_a}")
        print(f"Set B → {self.set_b}")

    def compute_results(self):
        print("\nInitiating set operations...\n")
        sleep(1)

        operations = [
            ("Union", self._union),
            ("Intersection", self._intersection),
            ("Difference (A - B)", self._difference),
            ("Subset Check", self._subset_check),
            ("Equality Check", self._equality_check),
        ]
        random.shuffle(operations)  # Shuffle operation order

        for label, func in operations:
            print(f"--- {label} ---")
            func()
            print()

    def _union(self):
        result = self.set_a.copy()
        for item in self.set_b:
            if item not in result:
                print(f"Adding {item} to union set")
                result.add(item)
            else:
                print(f"{item} already present in union")
        print(f"→ Union Result: {result}")

    def _intersection(self):
        result = set()
        for item in self.set_a:
            if item in self.set_b:
                print(f"{item} found in both sets")
                result.add(item)
            else:
                print(f"{item} is unique to A")
        print(f"→ Intersection Result: {result}")

    def _difference(self):
        result = set()
        for item in self.set_a:
            if item not in self.set_b:
                print(f"Keeping {item} (not in B)")
                result.add(item)
            else:
                print(f"Discarding {item} (exists in B)")
        print(f"→ A - B Result: {result}")

    def _subset_check(self):
        print("Checking if A is a subset of B...")
        for item in self.set_a:
            if item not in self.set_b:
                print(f"{item} is missing in B → Not a subset")
                print("→ Result: No")
                return
            else:
                print(f"{item} found in B")
        print("→ Result: Yes (A ⊆ B)")

    def _equality_check(self):
        print("Validating if sets A and B are equal...")
        all_items = self.set_a.union(self.set_b)
        same = True
        for item in all_items:
            in_a = item in self.set_a
            in_b = item in self.set_b
            symbol = "✓" if in_a and in_b else "✗"
            print(f"{symbol} {item}: A={in_a}, B={in_b}")
            if in_a != in_b:
                same = False
        print(f"→ Result: {'Yes' if same else 'No'} (A == B)")
# endregion set theory

# region conversion
class Conversion:
    """A flexible number base converter with detailed, step-by-step tracing."""

    def __init__(self):
        clear_screen()
        print(">> Number Base Conversion Utility Initialized!")
        sleep(1)
        self.start()

    def start(self):
        print("\nPick the type of conversion you'd like to perform:\n")

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

        # Show randomized menu
        for i, (label, _) in enumerate(options, 1):
            print(f" {i}. {label}")

        try:
            choice = int(input("\nEnter your choice (1–12): "))
            if 1 <= choice <= 12:
                options[choice - 1][1]()
            else:
                print("⚠️ Hmm... that option's out of range. Try again.")
        except ValueError:
            print("⚠️ That doesn't look like a number. Please enter digits only.")

    def decimal_to_binary(self):
        num = int(input("Enter a decimal number: "))
        self._decimal_to_base(num, 2, "Binary")

    def binary_to_decimal(self):
        binary = input("Type a binary number (0s and 1s): ")
        steps = [f"{digit} × 2^{i} = {int(digit)*(2**i)}"
                 for i, digit in enumerate(binary[::-1])]
        print("Step-by-step:\n" + "\n".join(steps))
        print(f"→ Decimal: {int(binary, 2)}")

    def decimal_to_octal(self):
        num = int(input("Enter a decimal number: "))
        self._decimal_to_base(num, 8, "Octal")

    def decimal_to_hex(self):
        num = int(input("Enter a decimal number: "))
        self._decimal_to_base(num, 16, "Hexadecimal")

    def octal_to_decimal(self):
        octal = input("Input an octal number (0–7 digits): ")
        steps = [f"{digit} × 8^{i} = {int(digit)*(8**i)}"
                 for i, digit in enumerate(octal[::-1])]
        print("Step-by-step:\n" + "\n".join(steps))
        print(f"→ Decimal: {int(octal, 8)}")

    def hex_to_decimal(self):
        hex_str = input("Input a hexadecimal value (0–9, A–F): ").upper()
        digits = "0123456789ABCDEF"
        steps = [f"{char} × 16^{i} = {digits.index(char)*(16**i)}"
                 for i, char in enumerate(hex_str[::-1])]
        print("Step-by-step:\n" + "\n".join(steps))
        print(f"→ Decimal: {int(hex_str, 16)}")

    def binary_to_octal(self):
        binary = input("Enter a binary number: ")
        dec = int(binary, 2)
        print(f"→ Intermediate decimal: {dec}")
        self._decimal_to_base(dec, 8, "Octal")

    def binary_to_hex(self):
        binary = input("Enter a binary number: ")
        dec = int(binary, 2)
        print(f"→ Intermediate decimal: {dec}")
        self._decimal_to_base(dec, 16, "Hexadecimal")

    def octal_to_binary(self):
        octal = input("Enter an octal number: ")
        dec = int(octal, 8)
        print(f"→ Intermediate decimal: {dec}")
        self._decimal_to_base(dec, 2, "Binary")

    def octal_to_hex(self):
        octal = input("Enter an octal number: ")
        dec = int(octal, 8)
        print(f"→ Intermediate decimal: {dec}")
        self._decimal_to_base(dec, 16, "Hexadecimal")

    def hex_to_binary(self):
        hex_str = input("Enter a hexadecimal number: ")
        dec = int(hex_str, 16)
        print(f"→ Intermediate decimal: {dec}")
        self._decimal_to_base(dec, 2, "Binary")

    def hex_to_octal(self):
        hex_str = input("Enter a hexadecimal number: ")
        dec = int(hex_str, 16)
        print(f"→ Intermediate decimal: {dec}")
        self._decimal_to_base(dec, 8, "Octal")

    def _decimal_to_base(self, decimal, base, label):
        digits = "0123456789ABCDEF"
        original = decimal
        steps = []
        while decimal > 0:
            r = decimal % base
            q = decimal // base
            step = f"{decimal} ÷ {base} = {q} remainder {r}"
            if base == 16:
                step += f" ({digits[r]})"
            steps.append(step)
            decimal = q
        print("Conversion Steps:\n" + "\n".join(reversed(steps)))
        if base == 2:
            converted = bin(original)[2:]
        elif base == 8:
            converted = oct(original)[2:]
        else:
            converted = hex(original)[2:].upper()
        print(f"→ {label}: {converted}")
# endregion conversion

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
        try:
            choice = int(input("Choose (1 or 2): "))
            match choice:
                case 1: self.gcd()
                case 2: self.lcm()
                case _: print("⚠️ That’s not a valid option.")
        except ValueError:
            print("⚠️ Only numeric input is accepted.")

    def gcd(self):
        try:
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            x, y = a, b
            print(f"Finding GCD of {a} and {b}...\n")
            while y != 0:
                print(f"{x} % {y} = {x % y}")
                x, y = y, x % y
            print(f"→ GCD({a}, {b}) = {x}")
        except ValueError:
            print("⚠️ Invalid input. Use integers only.")

    def lcm(self):
        try:
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            print(f"Calculating LCM of {a} and {b}...")
            x, y = a, b
            while y != 0:
                x, y = y, x % y
            gcd = x
            print(f"GCD = {gcd}")
            lcm = (a * b) // gcd
            print(f"→ LCM({a}, {b}) = {lcm}")
        except ValueError:
            print("⚠️ Please enter valid integers.")
# endregion

# region Prime
class Prime:
    """A simple class for prime number operations."""

    def __init__(self):
        clear_screen()
        print(">> You've entered the Prime Numbers Module.")
        sleep(1)
        self.start()

    def start(self):
        print("\nChoose an operation:")
        print(" 1. Check if a number is prime")
        print(" 2. Generate primes (Sieve of Eratosthenes)")
        print(" 3. Get prime factors of a number")
        print(" 4. Apply Fermat's Little Theorem")
        print(" 5. Explore primitive roots")
        try:
            choice = int(input("Pick an option (1–5): "))
        except ValueError:
            print("⚠️ That's not a number.")
            return

        match choice:
            case 1: self.check_prime()
            case 2: self.sieve()
            case 3: self.prime_factors()
            case 4: self.fermats()
            case 5: self.primitive_roots()
            case _: print("⚠️ Option out of range.")

    def check_prime(self):
        try:
            n = int(input("\nEnter the number to test: "))
        except ValueError:
            print("⚠️ Invalid input. Try an integer.")
            return

        if n < 2:
            print(f"{n} is not a prime number.")
            return

        for i in range(2, int(n ** 0.5) + 1):
            print(f"Checking: {n} % {i} = {n % i}")
            if n % i == 0:
                print(f"{n} is divisible by {i}, so it's not prime.")
                return

        print(f"{n} is a prime number.")

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
            n = int(input("\nEnter a number: "))
        except ValueError:
            print("⚠️ Not a valid number.")
            return

        original = n
        factors = []

        print(f"Starting factorization of {original}:")

        while n % 2 == 0:
            print(f"{n} is even → factor 2")
            factors.append(2)
            n //= 2

        i = 3
        while i * i <= n:
            while n % i == 0:
                print(f"{n} is divisible by {i} → factor {i}")
                factors.append(i)
                n //= i
            i += 2

        if n > 2:
            print(f"Remaining prime factor: {n}")
            factors.append(n)

        print(f"→ Prime factors of {original}: {factors}")

    def sieve(self):
        print("\nGenerate primes using the Sieve of Eratosthenes.")
        try:
            start = int(input("Start from (inclusive): "))
            end = int(input("End at (exclusive): "))
        except ValueError:
            print("⚠️ Use integers only.")
            return

        if end <= start:
            print("⚠️ Make sure end is greater than start.")
            return

        print(f"Finding primes from {start} to {end}...")
        primes = [i for i in range(start, end) if self._check_prime(i)]

        print(f"→ Primes between {start} and {end}:")
        print(primes)

    def fermats(self):
        print("\nFermat’s Little Theorem: a^(p−1) ≡ 1 mod p, if p is prime.")
        try:
            a = int(input("Enter value for a: "))
            k = int(input("Enter exponent k: "))
            p = int(input("Enter a prime number p: "))
        except ValueError:
            print("⚠️ Input must be numeric.")
            return

        if not self._check_prime(p):
            print("⚠️ p must be a prime number.")
            return

        result = pow(a, k, p)
        print(f"→ {a}^{k} mod {p} = {result}")

    def primitive_roots(self):
        print("\nCheck if a number is a primitive root modulo a prime p.")
        try:
            p = int(input("Enter a prime number p: "))
            a = int(input("Enter number to test as primitive root: "))
        except ValueError:
            print("⚠️ Use integers only.")
            return

        if p <= 0 or a <= 0:
            print("⚠️ Enter positive integers.")
            return

        if not self._check_prime(p):
            print("⚠️ p must be a prime number.")
            return

        required = set(range(1, p))
        actual = set(pow(a, k, p) for k in range(1, p))

        if actual == required:
            print(f"→ Yes, {a} is a primitive root modulo {p}.")
        else:
            print(f"→ No, {a} is not a primitive root modulo {p}.")

        roots = []
        for g in range(2, p):
            if set(pow(g, k, p) for k in range(1, p)) == required:
                roots.append(g)

        print(f"→ All primitive roots of {p}: {roots}")
# endregion

# region Searching
class Searching:
    """A tool to demonstrate various search algorithms interactively."""

    def __init__(self):
        clear_screen()
        print("🔍 Welcome to the Interactive Search Tool!")
        sleep(1)
        self.menu()

    def menu(self):
        print("\nWhich search algorithm would you like to explore today?")
        print(" 1. Interpolation Search")
        print(" 2. Linear Search")
        print(" 3. Binary Search")

        try:
            choice = int(input("Your choice (1–3): "))
        except ValueError:
            print("⚠️ Please enter a number between 1 and 3.")
            return self.menu()

        if choice == 2:
            self.linear_search()
        elif choice == 3:
            self.binary_search()
        elif choice == 1:
            self.interpolation_search()
        else:
            print("⚠️ Not a valid selection. Try again.")
            self.menu()

    def get_array_and_target(self, sort_array=False):
        try:
            values = list(map(int, input("\nEnter the list of numbers (space-separated): ").split()))
            if sort_array:
                values.sort()
                print(f"🔢 Sorted array: {values}")
            target = int(input("🔍 Enter the number to find: "))
            return values, target
        except ValueError:
            print("⚠️ Invalid input. Use only integers.")
            return self.get_array_and_target(sort_array)

    def linear_search(self):
        arr, target = self.get_array_and_target()
        print("\n🔎 Starting linear search...\n")
        sleep(0.5)

        for idx, val in enumerate(arr):
            print(f"Checking index {idx}: value = {val}")
            if val == target:
                print(f"✅ Found {target} at index {idx}.")
                return
            print("→ Not a match.")
        print(f"❌ {target} was not found in the list.")

    def binary_search(self):
        arr, target = self.get_array_and_target(sort_array=True)
        print("\n🔎 Starting binary search...\n")
        sleep(0.5)

        left, right = 0, len(arr) - 1
        step = 1

        while left <= right:
            mid = (left + right) // 2
            print(f"Step {step}: left = {left}, right = {right}, mid = {mid}, value = {arr[mid]}")
            step += 1

            if arr[mid] == target:
                print(f"✅ Found {target} at index {mid}.")
                return
            elif arr[mid] < target:
                print(f"{arr[mid]} < {target} → Searching right half")
                left = mid + 1
            else:
                print(f"{arr[mid]} > {target} → Searching left half")
                right = mid - 1

        print(f"❌ {target} could not be located in the array.")

    def interpolation_search(self):
        arr, target = self.get_array_and_target(sort_array=True)
        print("\n🔎 Starting interpolation search...\n")
        sleep(0.5)

        low, high = 0, len(arr) - 1
        step = 1

        while low <= high and arr[low] <= target <= arr[high]:
            if arr[high] == arr[low]:
                if arr[low] == target:
                    print(f"✅ Found {target} at index {low}.")
                    return
                break

            pos = low + int(((target - arr[low]) * (high - low)) / (arr[high] - arr[low]))

            if pos < low or pos > high:
                break

            print(f"Step {step}: low = {low}, high = {high}, pos = {pos}, value = {arr[pos]}")
            step += 1

            if arr[pos] == target:
                print(f"✅ Success! {target} is at index {pos}.")
                return
            elif arr[pos] < target:
                print(f"{arr[pos]} < {target} → Moving right")
                low = pos + 1
            else:
                print(f"{arr[pos]} > {target} → Moving left")
                high = pos - 1

        print(f"❌ {target} is not in the array.")
# endregion

#region test
class test:
    pass
#endregion test

# region Main Program Loop
def main():
    modules = [
        Sorting,
        Ciphers,
        SetTheory,
        Conversion,
        GCD_LCM,
        Prime,
        Searching,
        test
    ]

    while True:
        clear_screen()
        print("👑 Enter Rica Mae Sabanal’s Algorithm kingdom Where Logic Reigns! 👑\n")
        print("📚 Pick a module to explore:")

        for idx, module in enumerate(modules, start=1):
            print(f" {idx}. 🔹 {module.__name__}")
        print(" 0. 🔚 Exit Explorer")

        try:
            choice = int(input("\n📥 Your pick (0 to quit): "))
        except ValueError:
            print("\n⚠️ Oops! That's not a number. Try again...")
            sleep(1.5)
            continue

        if choice == 0:
            print("\n👋 Thank you for exploring algorithms with me. Until next time!")
            break

        if 1 <= choice <= len(modules):
            selected_module = modules[choice - 1]
            while True:
                clear_screen()
                print(f"🚀 Now launching: {selected_module.__name__}\n")
                selected_module()

                again = input("\n🔄 Try this module again? (y/N): ").strip().lower()
                if again != 'y':
                    break
        else:
            print("\n❗ Invalid option. Please select from the list.")
            sleep(1.5)

if __name__ == "__main__":
    main()
# endregion
