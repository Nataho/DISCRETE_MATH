import os
import time

# region Helper Functions
# Helper function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Helper function to simulate a delay (in seconds)
def sleep(seconds):
    time.sleep(seconds)
# endregion

#region set theory
class SetTheory:
    """Handles user interaction and operations related to basic set theory."""

    def __init__(self):
        self.set_a = set()
        self.set_b = set()
        clear_screen()
        print("Set Theory function opened!")
        sleep(1)
        self.run()

    def run(self):
        self.display_welcome()
        self.get_sets()
        self.display_sets()
        self.compute_results()

    def display_welcome(self):
        print("Welcome to the Set Theory class!")

    def get_sets(self):
        self.set_a = self.input_set("A")
        self.set_b = self.input_set("B")

    def input_set(self, label):
        raw = input(f"Enter the elements of set {label} (space-separated): ")
        return set(raw.strip().split())

    def display_sets(self):
        print("\nYou have entered:")
        print(f"Set A: {self.set_a}")
        print(f"Set B: {self.set_b}")

    def compute_results(self):
        print("\nPerforming set operations...")
        sleep(1)
        print("\nResults of set operations:")
        print(f"Union (A ∪ B): {self.set_a | self.set_b}")
        print(f"Intersection (A ∩ B): {self.set_a & self.set_b}")
        print(f"Difference (A - B): {self.set_a - self.set_b}")
        print(f"Is A a subset of B? {'Yes' if self.set_a <= self.set_b else 'No'}")
        print(f"Are A and B equal? {'Yes' if self.set_a == self.set_b else 'No'}")
#endregion set theory

# region Ciphers
class Ciphers:
    """Encrypts text using various classical ciphers."""

    def __init__(self):
        clear_screen()
        print("Ciphers class opened!")
        sleep(1)
        self.run_menu()

    def run_menu(self):
        print("Choose an encryption method:")
        options = [
            "Caesar Cipher", "Vigenère Cipher", "Playfair Cipher",
            "Vernam Cipher", "One-Time Pad Cipher", "Hill Cipher",
            "Rail Fence Cipher", "Columnar Cipher"
        ]
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")
        try:
            choice = int(input("Enter the number of your choice: "))
            methods = {
                1: self.caesar,
                2: self.vigenere,
                3: self.playfair,
                4: self.vernam,
                5: self.one_time_pad,
                6: self.hill,
                7: self.rail_fence,
                8: self.columnar
            }
            methods.get(choice, self.invalid_option)()
        except ValueError:
            print("Invalid input. Please enter a number.")

    def invalid_option(self):
        print("Invalid option selected.")

    def caesar(self):
        text = input("Enter text: ")
        shift = int(input("Shift (1–25): "))
        encrypted = ""
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                encrypted += chr((ord(char) - base + shift) % 26 + base)
            else:
                encrypted += char
        print(f"Encrypted: {encrypted}")

    def vigenere(self):
        text = input("Enter text: ")
        key = input("Enter keyword: ")
        key_extended = (key * ((len(text) // len(key)) + 1))[:len(text)]
        result = ""
        for i, char in enumerate(text):
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                key_char = key_extended[i].upper() if char.isupper() else key_extended[i].lower()
                shift = ord(key_char) - base
                result += chr((ord(char) - base + shift) % 26 + base)
            else:
                result += char
        print(f"Encrypted: {result}")

    def playfair(self):
        text = input("Enter text: ")
        keyword = input("Keyword: ")
        matrix = self._generate_playfair_matrix(keyword)
        prepared = self._prepare_playfair_text(text)
        encrypted = ""
        for i in range(0, len(prepared), 2):
            encrypted += self._playfair_encrypt_pair(matrix, prepared[i], prepared[i + 1])
        print(f"Encrypted: {encrypted}")

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
        text = input("Text: ")
        key = input("Key: ")
        key = (key * ((len(text) // len(key)) + 1))[:len(text)]
        result = "".join(chr(ord(c) ^ ord(k)) for c, k in zip(text, key))
        print(f"Encrypted: {result}")
        print(f"Hex: {result.encode().hex()}")

    def one_time_pad(self):
        text = input("Text: ")
        key = os.urandom(len(text))
        encrypted = bytes([ord(c) ^ k for c, k in zip(text, key)])
        print(f"Key (hex): {key.hex()}")
        print(f"Encrypted (hex): {encrypted.hex()}")

    def hill(self):
        text = input("Plaintext: ")
        key_input = input("3x3 key matrix (space-separated): ")
        try:
            values = list(map(int, key_input.split()))
            if len(values) != 9:
                print("Error: Matrix needs 9 numbers.")
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
        result = ""
        for i in range(0, len(nums), 3):
            block = nums[i:i+3]
            res = [(sum(matrix[r][c] * block[r] for r in range(3)) % 26) for c in range(3)]
            for j, val in enumerate(res):
                orig = chars[i + j]
                result += big[val] if orig.isupper() else small[val]
        print("Key Matrix:")
        for row in matrix:
            print(row)
        print(f"Encrypted: {result}")

    def rail_fence(self):
        text = input("Text: ")
        if any(c.isdigit() for c in text):
            print("Digits are not allowed.")
            return
        try:
            rails = int(input("Number of rails (2-10): "))
            if not (2 <= rails <= 10):
                raise ValueError
        except:
            print("Invalid rail number.")
            return

        fence = [''] * rails
        rail, direction = 0, 1
        for char in text:
            fence[rail] += char
            rail += direction
            if rail == 0 or rail == rails - 1:
                direction *= -1
        print(f"Encrypted: {''.join(fence)}")

    def columnar(self):
        text = input("Text: ")
        print(f"Matrix needs {len(text)} cells.")
        try:
            rows = int(input("Rows: "))
            cols = int(input("Columns: "))
            key = list(map(int, input(f"Enter {cols} column key numbers: ").split()))
            if len(key) != cols or sorted(key) != list(range(1, cols + 1)):
                raise ValueError
        except:
            print("Invalid input.")
            return

        padded = text.ljust(rows * cols, 'x')[:rows * cols]
        matrix = [list(padded[i * cols:(i + 1) * cols]) for i in range(rows)]
        result = ""
        for k in key:
            for r in matrix:
                result += r[k - 1]
        print(f"Encrypted: {result}")
# endregion

#region sorting
class Sorting:
    """A simple class for sorting algorithms."""

    def __init__(self):
        clear_screen()
        print("Sorting class opened!")
        sleep(1)
        self.start()

    def start(self):
        print("Pick your desired sorting method:")
        print("1. Bubble Sort")
        print("2. Selection Sort")
        print("3. Insertion sort")
        print("4. Merge Sort")
        print("5. Quick Sort")
        print("6. Bucket Sort")
        print("7. Shell Sort")
        print("8. Comb Sort")
        print("9. Radix Sort")
        print("10. Tree Sort")
        choice = int(input("Enter the number of the method you want to use: "))
        
        match choice:
            case 1:
                self.bubble_sort()
            case 2:
                self.selection_sort()
            case 3:
                self.insertion_sort()
            case 4:
                self.merge_sort()
            case 5:
                self.quick_sort()
            case 6:
                self.bucket_sort()
            case 7:
                self.shell_sort()
            case 8:
                self.comb_sort()
            case 9:
                self.radix_sort()
            case _:
                print("Invalid Choice.")

    def bubble_sort(self):
        arr = list(map(int, input("Enter the items to sort (space-separated): ").split()))
        n = len(arr)
        comparisons = 0

        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    print(f"compare: \t {arr} [{arr[j]} > {arr[j+1]}]" )
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    print(f"swap: \t {arr} [{arr[j]} <=> {arr[j+1]}]" )
                    comparisons += 1
                    sleep(0.01)

        print(f"Sorted array: {arr}| comparisons: {comparisons}")

    def selection_sort(self):
        arr = list(map(int, input("Enter the items to sort (space-separated): ").split()))
        n = len(arr)
        comparisons = 0

        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
                    comparisons += 1
                    sleep(0.01)
                    print(f"sorting.. {arr} [{arr[j]} < {arr[min_idx]}]" )
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

        print(f"Sorted array: {arr}")
    
    def insertion_sort(self):
        arr = list(map(int, input("Enter the items to sort (space-separated): ").split()))
        self._insertion_sort(arr)
        print(f"sorted array: {arr}")
    
    @staticmethod
    def _insertion_sort(arr):
        length = len(arr)

        for i in range(1, length):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                sleep(0.01)
                print(f"sorting.. {arr} [{key} < {arr[j]}]")
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    def merge_sort(self):
        arr = list(map(int, input("Enter the items to sort (space-separated): ").split()))
        self._merge_sort(arr)
        print()
        print(f"Sorted array: {arr}")
        
    def _merge_sort(self, arr):
        length = len(arr)

        if length > 1:
            mid = length // 2
            left = arr[:mid]
            right = arr[mid:]
            sleep(0.05)
            print(f"left: \t{left}; right: {right}")

            self._merge_sort(left)
            self._merge_sort(right)

            self._merge(arr, left, right)

    def _merge(self, arr, left, right):
        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

        sleep(0.05)
        print(f"merge: \t{left}{right} = {arr}")

    def quick_sort(self):
        arr = list(map(int, input("Enter the items to sort (space-separated): ").split()))
        self._quick_sort(arr, 0, len(arr) - 1)
        print(f"Sorted array: {arr}")
    
    def _quick_sort(self, arr, low, high):
        if low < high:
            pi = self._partition(arr, low, high)
            self._quick_sort(arr, low, pi - 1)
            self._quick_sort(arr, pi + 1, high)
    
    def _partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] < pivot:
                print(f"sorting: arr[j]({arr[j]}) < pivot({pivot})")
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                print(arr)

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def bucket_sort(self):
        arr = list(map(int, input("Enter the items to sort (space-separated): ").split()))

        if not arr:
            print("Empty array.")
            return

        min_val = min(arr)
        max_val = max(arr)
        range_val = max_val - min_val + 1

        bucket_count = 10
        buckets = [[] for _ in range(bucket_count)]

        for num in arr:
            if range_val == 1:
                index = 0
            else:
                index = int(((num - min_val) / range_val) * (bucket_count - 1))
            buckets[index].append(num)
            print(f"buckets: {buckets}")

        for i in range(bucket_count):
            self._insertion_sort(buckets[i])
            print(f"sort bucket {i}: {buckets[i]}")

        sorted_arr = []
        for i in range(bucket_count):
            sorted_arr.extend(buckets[i])
            print(f"combine buckets: {sorted_arr}")

        print(f"Sorted array: {sorted_arr}")
    
    def shell_sort(self):
        arr = list(map(int, input("Enter the items to sort (space-separated): ").split()))
        length = len(arr)
        gap = length // 2

        while gap > 0:
            for start in range(gap):
                subarray_indices = list(range(start, length, gap))
                subarray = [arr[i] for i in subarray_indices]
                self._insertion_sort(subarray)
                print(subarray)
                sleep(0.2)

            for idx, val in zip(subarray_indices, subarray):
                arr[idx] = val

            gap //= 2

        print(f"sorted array: {arr}")
    
    def comb_sort(self):
        arr = list(map(int, input("Enter the items to sort (space-separated): ").split()))
        length = len(arr)
        gap = length
        shrink = 1.3
        sorted_flag = False

        while gap > 1 or not sorted_flag:
            gap = int(gap / shrink)
            if gap < 1:
                gap = 1
            sorted_flag = True

            for i in range(length - gap):
                if arr[i] > arr[i + gap]:
                    print(f"compare:{arr} [{arr[i]} > {arr[i + gap]}]; gap = {gap}")
                    sleep(0.01)
                    arr[i], arr[i + gap] = arr[i + gap], arr[i]
                    print(f"swap:\t{arr} [{arr[i]} <=> {arr[i + gap]}]")
                    sleep(0.01)
                    sorted_flag = False

        print(f"sorted array: {arr}")

    def radix_sort(self):
        arr = list(map(int, input("Enter the items to sort (space-separated): ").split()))
        max_num = max(arr)
        exp = 1
        passes = 1

        while max_num // exp > 0:
            self._counting_sort(arr, exp)
            print(f"pass {passes}: {arr}")
            sleep(0.1)
            passes += 1
            exp *= 10

        print(f"sorted array: {arr}")
    
    def _counting_sort(self, arr, exp):
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
#endregion sorting

#region conversion
class Conversion:
    """A simple class for number base conversions."""

    def __init__(self):
        clear_screen()
        print("Welcome to the Base Conversion Tool!")
        sleep(1)
        self.start()

    def start(self):
        print("\nChoose a conversion type:")
        print(" 1. Decimal → Binary")
        print(" 2. Binary → Decimal")
        print(" 3. Decimal → Octal")
        print(" 4. Decimal → Hexadecimal")
        print(" 5. Octal → Decimal")
        print(" 6. Hexadecimal → Decimal")
        print(" 7. Binary → Octal")
        print(" 8. Binary → Hexadecimal")
        print(" 9. Octal → Binary")
        print("10. Octal → Hexadecimal")
        print("11. Hexadecimal → Binary")
        print("12. Hexadecimal → Octal")
        choice = int(input("\nEnter the number of your choice: "))

        match choice:
            case 1:
                self.decimal_to_binary()
            case 2:
                self.binary_to_decimal()
            case 3:
                self.decimal_to_octal()
            case 4:
                self.decimal_to_hex()
            case 5:
                self.octal_to_decimal()
            case 6:
                self.hex_to_decimal()
            case 7:
                self.binary_to_octal()
            case 8:
                self.binary_to_hex()
            case 9:
                self.octal_to_binary()
            case 10:
                self.octal_to_hex()
            case 11:
                self.hex_to_binary()
            case 12:
                self.hex_to_octal()
            case _:
                print("Oops! That's not a valid choice. Please try again.")

    def decimal_to_binary(self):
        decimal = int(input("Enter a decimal number: "))
        output = ""
        base = 2

        while True:
            remainder = decimal % base
            decimal //= base
            output = str(remainder) + output
            if decimal == 0:
                break

        print(f"Result in Binary: {output}")

    def binary_to_decimal(self):
        binary = input("Enter a binary number: ")
        reversed_bin = binary[::-1]
        decimal = sum(int(digit) * 2 ** idx for idx, digit in enumerate(reversed_bin))
        print(f"Converted to Decimal: {decimal}")

    def decimal_to_octal(self):
        decimal = int(input("Enter a decimal number: "))
        output = ""
        base = 8

        while True:
            remainder = decimal % base
            decimal //= base
            output = str(remainder) + output
            if decimal == 0:
                break

        print(f"Octal value: {output}")

    def decimal_to_hex(self):
        decimal = int(input("Enter a decimal number: "))
        output = ""
        base = 16

        while True:
            remainder = decimal % base
            hex_digit = "0123456789ABCDEF"[remainder]
            decimal //= base
            output = hex_digit + output
            if decimal == 0:
                break

        print(f"Hexadecimal: {output}")

    def octal_to_decimal(self):
        octal = input("Enter an octal number: ")
        reversed_octal = octal[::-1]
        decimal = sum(int(digit) * 8 ** idx for idx, digit in enumerate(reversed_octal))
        print(f"Decimal result: {decimal}")

    def hex_to_decimal(self):
        hex_str = input("Enter a hexadecimal number: ")
        reversed_hex = hex_str[::-1].upper()
        hex_digits = "0123456789ABCDEF"
        decimal = sum(hex_digits.index(char) * 16 ** idx for idx, char in enumerate(reversed_hex))
        print(f"Decimal result: {decimal}")

    def binary_to_octal(self):
        binary = input("Enter a binary number: ")
        decimal = int(binary, 2)
        octal = ""
        while decimal:
            octal = str(decimal % 8) + octal
            decimal //= 8
        print(f"Octal value: {octal or '0'}")

    def binary_to_hex(self):
        binary = input("Enter a binary number: ")
        decimal = int(binary, 2)
        hex_value = ""
        while decimal:
            hex_value = "0123456789ABCDEF"[decimal % 16] + hex_value
            decimal //= 16
        print(f"Hexadecimal: {hex_value or '0'}")

    def octal_to_binary(self):
        octal = input("Enter an octal number: ")
        decimal = int(octal, 8)
        binary = ""
        while decimal:
            binary = str(decimal % 2) + binary
            decimal //= 2
        print(f"Binary value: {binary or '0'}")

    def octal_to_hex(self):
        octal = input("Enter an octal number: ")
        decimal = int(octal, 8)
        hex_value = ""
        while decimal:
            hex_value = "0123456789ABCDEF"[decimal % 16] + hex_value
            decimal //= 16
        print(f"Hexadecimal: {hex_value or '0'}")

    def hex_to_binary(self):
        hex_str = input("Enter a hexadecimal number: ")
        decimal = int(hex_str, 16)
        binary = ""
        while decimal:
            binary = str(decimal % 2) + binary
            decimal //= 2
        print(f"Binary value: {binary or '0'}")

    def hex_to_octal(self):
        hex_str = input("Enter a hexadecimal number: ")
        decimal = int(hex_str, 16)
        octal = ""
        while decimal:
            octal = str(decimal % 8) + octal
            decimal //= 8
        print(f"Octal value: {octal or '0'}")
#endregion conversion

# region Prime
class Prime:
    """A simple class for prime number operations."""

    def __init__(self):
        clear_screen()
        print("Prime class opened!")
        sleep(1)
        self.start()

    def start(self):
        print("Pick a method:")
        print("1. Check if a number is prime")
        print("2. Sieve of Eratosthenes")
        print("3. prime factors")
        print("4. fermat's little theorem")
        print("5. primitive roots")
        choice = int(input("Enter the number of your choice: "))
        
        match choice:
            case 1:
                self.check_prime()
            case 2:
                self.sieve()
            case 3:
                self.prime_factors()
            case 4:
                self.fermats()
            case 5:
                self.primitive_roots()
            case _:
                print("invalid")
        # if choice == 1:
        #     self.check_prime()
        # elif choice == 2:
        #     self.sieve()
        
        # else:
        #     print("Invalid choice.")

    def check_prime(self):
        n = int(input("Enter a number: "))
        if n < 2:
            print("Not prime.")
            return
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                print("Not prime.")
                return
        print("Prime!")

    @staticmethod
    def _check_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def prime_factors(self):
        num = int(input("Enter a number to check for primality: "))
        factors = []
        while n % 2 == 0:
            factors.append(2)
            n //= 2
        # Check odd numbers
        for i in range(3, int(n**0.5) + 1, 2):
            while n % i == 0:
                if Prime._check_prime(i):
                    factors.append(i)
                n //= i
        if n > 2:
            factors.append(n)
        
        print(f"Prime factors of {num}: {factors}")

    def sieve(self):
        min = int(input("enter minimum: "))
        max = int(input("enter maximum: "))
        primes = []
        for i in range(min, max):
            if self._check_prime(i):
                primes.append(i)
        print(f"primes in {min} to {max}: {primes}")
    
    def fermats(self):
        print("formula: a^(p-1) ≡ 1 (mod p) for prime p")
        print("use this: a^k mod p")

        a = int(input("Enter a number for a: "))
        k = int(input("Enter a number for k: "))
        p = int(input("Enter a prime number for p: "))

        if not self._check_prime(p):
            print("p needs to be prime")
        
        exponent_result = pow(a, k)
        answer = exponent_result % p
        print(f"{a}^{k} mod {p} = {answer} mod {p}")

    def primitive_roots(self):
        p = int(input("Enter a prime number: "))
        a = int(input("Enter a number to check if it is a primitive root: "))

        if a <= 0 or p <= 0:
            print("a and p must be positive integers")
        if not self._check_prime(p):
            print("p needs to be prime")
        
        required_set = set(range(1,p))
        roots =[]

        for g in range(2, p):
            actual_set = set(pow(g, k, p) for k in range(1, p))
            if actual_set == required_set:
                roots.append(g)

        # Check if 'a' is a primitive root of p
        is_primitive = a in roots
        print(f"Is {a} a primitive root of {p}? {'Yes' if is_primitive else 'No'}")
        print(f"Primitive roots of {p}: {roots}")
# endregion

# region GCD & LCM
class GCD_LCM:
    """A simple class for GCD and LCM calculations."""

    def __init__(self):
        clear_screen()
        print("GCD/LCM class opened!")
        sleep(1)
        self.start()

    def start(self):
        print("Pick a method:")
        print("1. GCD (Euclidean algorithm)")
        print("2. LCM (using GCD)")
        choice = int(input("Enter the number of your choice: "))
        
        match choice:
            case 1:
                self.gcd()
            case 2:
                self.lcm()
            case _:
                print("invalid")

    def gcd(self):
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        while b:
            a, b = b, a % b
        print(f"GCD: {a}")

    def lcm(self):
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        orig_a, orig_b = a, b
        while b:
            a, b = b, a % b
        gcd = a
        lcm = (orig_a * orig_b) // gcd
        print(f"LCM: {lcm}")
# endregion

# region Searching
class Searching:
    """A simple class for searching algorithms."""

    def __init__(self):
        clear_screen()
        print("Welcome to the Searching Algorithm Tool!")
        sleep(1)
        self.start()

    def start(self):
        print("\nSelect a search technique:")
        print(" 1. Linear Search")
        print(" 2. Binary Search")
        print(" 3. Interpolation Search")
        choice = int(input("Enter your choice (1–3): "))

        match choice:
            case 1:
                self.linear_search()
            case 2:
                self.binary_search()
            case 3:
                self.interpolation_search()
            case _:
                print("That doesn't seem to be a valid choice.")

    def linear_search(self):
        arr = list(map(int, input("\nEnter the array elements (space-separated): ").split()))
        target = int(input("Enter the number you're searching for: "))
        print("\nSearching...\n")
        sleep(0.5)
        for i, num in enumerate(arr):
            if num == target:
                print(f"Success! Found {target} at index {i}.")
                return
        print(f"{target} was not found in the array.")

    def binary_search(self):
        arr = list(map(int, input("\nEnter the array elements (space-separated): ").split()))
        arr.sort()
        print(f"Sorted array: {arr}")
        target = int(input("Enter the number you're searching for: "))
        print("\nPerforming binary search...\n")
        sleep(0.5)

        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                print(f"Success! Found {target} at index {mid}.")
                return
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        print(f"{target} was not found in the array.")

    def interpolation_search(self):
        arr = list(map(int, input("\nEnter the array elements (space-separated): ").split()))
        arr.sort()
        print(f"Sorted array: {arr}")
        target = int(input("Enter the number you're searching for: "))

        print("\nPerforming interpolation search...\n")
        sleep(0.5)

        low = 0
        high = len(arr) - 1

        while low <= high and arr[low] <= target <= arr[high]:
            if arr[high] == arr[low]:
                if arr[low] == target:
                    print(f"Success! Found {target} at index {low}.")
                    return
                else:
                    break

            pos = low + int(((target - arr[low]) * (high - low)) / (arr[high] - arr[low]))

            # Display array with highlights
            displayed_arr = ""
            for i in range(len(arr)):
                if i == pos:
                    displayed_arr += f", \033[93m{arr[i]}\033[0m"
                elif i == low:
                    displayed_arr += f", \033[94m{arr[i]}\033[0m"
                elif i == high:
                    displayed_arr += f", \033[92m{arr[i]}\033[0m"
                else:
                    displayed_arr += f", {arr[i]}"
            displayed_arr = f"[{displayed_arr[2:]}]"
            print(displayed_arr)
            sleep(0.1)

            if pos < low or pos > high:
                break
            if arr[pos] < target:
                low = pos + 1
            elif arr[pos] > target:
                high = pos - 1
            else:
                print(f"Success! Found {target} at index {pos}.")
                return

        print(f"{target} was not found in the array.")
# endregion


# region Main Program Loop
def main():
    modules = [
        Prime,
        Sorting,
        Ciphers,
        SetTheory,
        Conversion,
        Searching,
        GCD_LCM,
    ]

    while True:
        clear_screen()
        print("== Welcome to Jason Hangalay's Algorithm Explorer ==")
        print("\nAvailable Modules:")
        for index, mod in enumerate(modules, start=1):
            print(f" {index}. {mod.__name__}")
        print(" 0. Quit")

        try:
            selection = int(input("\nChoose a module to launch (0 to quit): "))
        except ValueError:
            print("\nOops! That's not a valid number.")
            sleep(1.2)
            continue

        if selection == 0:
            print("\nThanks for exploring! See you next time.")
            break

        if 1 <= selection <= len(modules):
            while True:
                clear_screen()
                print(f">>> Starting: {modules[selection - 1].__name__}\n")
                modules[selection - 1]()  # Instantiate and run
                retry = input("\nRun this module again? (y/N): ")
                if retry.strip().lower() != 'y':
                    break
        else:
            print("\nThat's not one of the options. Try again!")
            sleep(1.2)



if __name__ == "__main__":
    main()
# endregion
