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

# region GCD & LCM
class GCD_LCM:
    """Performs GCD and LCM calculations using classic number theory."""

    def __init__(self):
        clear_screen()
        print(">> Welcome to the GCD & LCM Utility!")
        sleep(1)
        self.start()

    def start(self):
        print("\nWhich operation would you like to perform?")
        print(" 1. Compute GCD (Greatest Common Divisor)")
        print(" 2. Compute LCM (Least Common Multiple)")
        try:
            choice = int(input("Make a selection (1 or 2): "))
            match choice:
                case 1:
                    self.gcd()
                case 2:
                    self.lcm()
                case _:
                    print("⚠️ Invalid selection. Try 1 or 2 next time.")
        except ValueError:
            print("⚠️ Please enter a valid number.")

    def gcd(self):
        try:
            a = int(input("First integer: "))
            b = int(input("Second integer: "))
            orig_a, orig_b = a, b
            while b != 0:
                a, b = b, a % b
            print(f"GCD of {orig_a} and {orig_b} is → {a}")
        except ValueError:
            print("Invalid input. Please enter integers only.")

    def lcm(self):
        try:
            a = int(input("Enter the first integer: "))
            b = int(input("Enter the second integer: "))
            orig_a, orig_b = a, b
            # GCD computation
            x, y = a, b
            while y != 0:
                x, y = y, x % y
            gcd = x
            lcm = (orig_a * orig_b) // gcd
            print(f"LCM of {orig_a} and {orig_b} is → {lcm}")
        except ValueError:
            print("Oops! Only integers are allowed here.")
# endregion

# region Prime
class Prime:
    """A simple class for prime number operations."""

    def __init__(self):
        clear_screen()
        print("You've entered the Prime Numbers Module.")
        sleep(1)
        self.start()

    def start(self):
        print("\nWhat would you like to do?")
        print(" 1. Test if a number is prime")
        print(" 2. List primes using the Sieve of Eratosthenes")
        print(" 3. Get prime factors of a number")
        print(" 4. Apply Fermat's Little Theorem")
        print(" 5. Explore primitive roots")

        try:
            choice = int(input("Pick an option (1–5): "))
        except ValueError:
            print("That doesn't seem to be a number.")
            return

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
                print("That’s not one of the listed options.")

    def check_prime(self):
        n = int(input("\nEnter the number you'd like to test: "))
        if n < 2:
            print(f"{n} is not a prime number.")
            return
        for i in range(2, int(n ** 0.5) + 1):
            print(f"Checking divisibility: {n} % {i} = {n % i}")
            if n % i == 0:
                print(f"{n} is divisible by {i}, so it’s not prime.")
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
        n = int(input("\nEnter a number to find its prime factors: "))
        original = n
        factors = []

        print(f"Starting factorization for: {original}")

        while n % 2 == 0:
            print(f"{n} is divisible by 2 → factor added: 2")
            factors.append(2)
            n //= 2
            print(f"Dividing by 2, new n = {n}")

        i = 3
        while i * i <= n:
            while n % i == 0:
                print(f"{n} is divisible by {i} → factor added: {i}")
                if Prime._check_prime(i):
                    factors.append(i)
                n //= i
                print(f"Dividing by {i}, new n = {n}")
            i += 2

        if n > 2:
            print(f"Remaining number is prime: {n} → factor added")
            factors.append(n)

        print(f"Prime factors of {original}: {factors}")

    def sieve(self):
        print("\nGenerate all prime numbers in a given range.")
        min_val = int(input("Enter the starting number (inclusive): "))
        max_val = int(input("Enter the ending number (exclusive): "))

        if max_val <= min_val:
            print("Make sure the max is greater than the min.")
            return

        primes = []
        for i in range(min_val, max_val):
            if self._check_prime(i):
                primes.append(i)

        print(f"Primes between {min_val} and {max_val}:")
        print(primes)

    def fermats(self):
        print("\nFermat’s Little Theorem says: a^(p-1) ≡ 1 (mod p), where p is prime.")
        a = int(input("Enter value for a: "))
        k = int(input("Enter an exponent value k (you’ll compute a^k mod p): "))
        p = int(input("Enter a prime number p: "))

        if not self._check_prime(p):
            print("The value of p must be a prime number.")
            return

        result = pow(a, k, p)
        print(f"{a}^{k} mod {p} = {result}")

    def primitive_roots(self):
        print("\nLet’s check for primitive roots modulo a prime number.")
        p = int(input("Enter a prime number p: "))
        a = int(input("Enter a number to test if it's a primitive root: "))

        if a <= 0 or p <= 0:
            print("Please enter positive integers for both values.")
            return

        if not self._check_prime(p):
            print("p must be a prime number.")
            return

        required_set = set(range(1, p))
        roots = []

        for g in range(2, p):
            actual_set = set(pow(g, k, p) for k in range(1, p))
            if actual_set == required_set:
                roots.append(g)

        print(f"\nIs {a} a primitive root modulo {p}? {'Yes' if a in roots else 'No'}")
        print(f"All primitive roots of {p}: {roots}")
# endregion

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
            "Caesar Cipher", "Vigenère Cipher", "Playfair Cipher",
            "Vernam Cipher", "One-Time Pad Cipher", "Hill Cipher",
            "Rail Fence Cipher", "Columnar Cipher"
        ]
        for i, option in enumerate(options, start=1):
            print(f" {i}. {option}")
        try:
            choice = int(input("Your pick (number): "))
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
            print("Hmm, that didn't look like a number.")

    def invalid_option(self):
        print("That choice doesn't exist in our cipher vault.")

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
        print("\nPerforming set operations...\n")
        sleep(1)

        print("Union (A ∪ B):")
        union = self.set_a.copy()
        for elem in self.set_b:
            if elem not in union:
                print(f"Adding {elem} from B to A")
                union.add(elem)
            else:
                print(f"{elem} already in A")
        print(f"→ {union}\n")

        print("Intersection (A ∩ B):")
        intersection = set()
        for elem in self.set_a:
            if elem in self.set_b:
                print(f"{elem} is in both A and B")
                intersection.add(elem)
            else:
                print(f"{elem} is only in A")
        print(f"→ {intersection}\n")

        print("Difference (A - B):")
        difference = set()
        for elem in self.set_a:
            if elem not in self.set_b:
                print(f"{elem} is in A but not in B, keeping it")
                difference.add(elem)
            else:
                print(f"{elem} is also in B, removing it from result")
        print(f"→ {difference}\n")

        print("Subset check (Is A ⊆ B?):")
        is_subset = True
        for elem in self.set_a:
            if elem not in self.set_b:
                print(f"{elem} is not in B → A is not a subset of B")
                is_subset = False
                break
            else:
                print(f"{elem} is in B")
        print(f"→ {'Yes' if is_subset else 'No'}\n")

        print("Equality check (A == B):")
        all_in_a = all(elem in self.set_b for elem in self.set_a)
        all_in_b = all(elem in self.set_a for elem in self.set_b)
        for elem in self.set_a.union(self.set_b):
            state = "✓" if elem in self.set_a and elem in self.set_b else "✗"
            print(f"{state} {elem} in A: {elem in self.set_a}, in B: {elem in self.set_b}")
        print(f"→ {'Yes' if all_in_a and all_in_b else 'No'}")
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
        print("\nPlease select a search algorithm to use:")
        print(" 1. Linear Search")
        print(" 2. Binary Search")
        print(" 3. Interpolation Search")

        try:
            choice = int(input("Your choice (1–3): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")
            return self.menu()

        match choice:
            case 1:
                self.linear_search()
            case 2:
                self.binary_search()
            case 3:
                self.interpolation_search()
            case _:
                print("Oops! That's not a valid option. Try again.")
                self.menu()

    def get_array_and_target(self, sort_array=False):
        try:
            values = list(map(int, input("\nEnter the array values (space-separated): ").split()))
            if sort_array:
                values.sort()
                print(f"Sorted array: {values}")
            target = int(input("Enter the number you're looking for: "))
            return values, target
        except ValueError:
            print("Invalid input. Please enter integers only.")
            return self.get_array_and_target(sort_array)

    def linear_search(self):
        arr, target = self.get_array_and_target()
        print("\nRunning linear search...\n")
        sleep(0.5)

        for idx, val in enumerate(arr):
            print(f"Checking index {idx}: value = {val}")
            if val == target:
                print(f"✅ Match found! {target} is at index {idx}.")
                return
            else:
                print(f"→ {val} does not match {target}")
        print(f"❌ {target} was not found in the provided list.")

    def binary_search(self):
        arr, target = self.get_array_and_target(sort_array=True)
        print("\nRunning binary search...\n")
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
                print(f"{arr[mid]} < {target} → Move right")
                left = mid + 1
            else:
                print(f"{arr[mid]} > {target} → Move left")
                right = mid - 1

        print(f"❌ {target} could not be located in the array.")

    def interpolation_search(self):
        arr, target = self.get_array_and_target(sort_array=True)
        print("\nRunning interpolation search...\n")
        sleep(0.5)

        low, high = 0, len(arr) - 1
        step = 1

        while low <= high and arr[low] <= target <= arr[high]:
            if arr[high] == arr[low]:
                if arr[low] == target:
                    print(f"✅ Found {target} at index {low}.")
                    return
                else:
                    break

            pos = low + int(((target - arr[low]) * (high - low)) / (arr[high] - arr[low]))

            if pos < low or pos > high:
                break

            print(f"Step {step}: low = {low}, high = {high}, pos = {pos}, value = {arr[pos]}")
            step += 1

            if arr[pos] < target:
                print(f"{arr[pos]} < {target} → Move right")
                low = pos + 1
            elif arr[pos] > target:
                print(f"{arr[pos]} > {target} → Move left")
                high = pos - 1
            else:
                print(f"✅ Success! {target} was located at index {pos}.")
                return

        print(f"❌ {target} is not in the array.")
# endregion

# region conversion
class Conversion:
    """A simple class for number base conversions, with detailed step-by-step process."""

    def __init__(self):
        clear_screen()
        print(">> Number Base Conversion Utility Initialized!")
        sleep(1)
        self.start()

    def start(self):
        print("\nWhat kind of conversion do you need?")
        print(" 1. Decimal to Binary")
        print(" 2. Binary to Decimal")
        print(" 3. Decimal to Octal")
        print(" 4. Decimal to Hexadecimal")
        print(" 5. Octal to Decimal")
        print(" 6. Hexadecimal to Decimal")
        print(" 7. Binary to Octal")
        print(" 8. Binary to Hexadecimal")
        print(" 9. Octal to Binary")
        print("10. Octal to Hexadecimal")
        print("11. Hexadecimal to Binary")
        print("12. Hexadecimal to Octal")
        try:
            choice = int(input("\nSelect an option (1–12): "))
            match choice:
                case 1: self.decimal_to_binary()
                case 2: self.binary_to_decimal()
                case 3: self.decimal_to_octal()
                case 4: self.decimal_to_hex()
                case 5: self.octal_to_decimal()
                case 6: self.hex_to_decimal()
                case 7: self.binary_to_octal()
                case 8: self.binary_to_hex()
                case 9: self.octal_to_binary()
                case 10: self.octal_to_hex()
                case 11: self.hex_to_binary()
                case 12: self.hex_to_octal()
                case _: print("⚠️ That number doesn't match any of the options.")
        except ValueError:
            print("⚠️ Invalid input. Numbers only, please.")

    def decimal_to_binary(self):
        decimal = int(input("Decimal input: "))
        original = decimal
        steps = []
        while decimal:
            steps.append(f"{decimal} ÷ 2 = {decimal // 2} remainder {decimal % 2}")
            decimal //= 2
        print("Steps:\n" + "\n".join(reversed(steps)))
        print(f"→ Binary: {bin(original)[2:]}")

    def binary_to_decimal(self):
        binary = input("Binary input: ")
        steps = [f"{digit} × 2^{i} = {int(digit)*(2**i)}"
                 for i, digit in enumerate(binary[::-1])]
        print("Steps:\n" + "\n".join(steps))
        print(f"→ Decimal: {int(binary, 2)}")

    def decimal_to_octal(self):
        decimal = int(input("Decimal input: "))
        original = decimal
        steps = []
        while decimal:
            steps.append(f"{decimal} ÷ 8 = {decimal // 8} remainder {decimal % 8}")
            decimal //= 8
        print("Steps:\n" + "\n".join(reversed(steps)))
        print(f"→ Octal: {oct(original)[2:]}")

    def decimal_to_hex(self):
        decimal = int(input("Decimal input: "))
        original = decimal
        digits = "0123456789ABCDEF"
        steps = []
        while decimal:
            r = decimal % 16
            steps.append(f"{decimal} ÷ 16 = {decimal // 16} remainder {r} ({digits[r]})")
            decimal //= 16
        print("Steps:\n" + "\n".join(reversed(steps)))
        print(f"→ Hexadecimal: {hex(original)[2:].upper()}")

    def octal_to_decimal(self):
        octal = input("Octal input: ")
        steps = [f"{digit} × 8^{i} = {int(digit)*(8**i)}"
                 for i, digit in enumerate(octal[::-1])]
        print("Steps:\n" + "\n".join(steps))
        print(f"→ Decimal: {int(octal, 8)}")

    def hex_to_decimal(self):
        hex_str = input("Hex input: ").upper()
        digits = "0123456789ABCDEF"
        steps = [f"{char} × 16^{i} = {digits.index(char)*(16**i)}"
                 for i, char in enumerate(hex_str[::-1])]
        print("Steps:\n" + "\n".join(steps))
        print(f"→ Decimal: {int(hex_str, 16)}")

    def binary_to_octal(self):
        binary = input("Binary input: ")
        decimal = int(binary, 2)
        print(f"Intermediate decimal: {decimal}")
        self._decimal_to_octal_steps(decimal)

    def binary_to_hex(self):
        binary = input("Binary input: ")
        decimal = int(binary, 2)
        print(f"Intermediate decimal: {decimal}")
        self._decimal_to_hex_steps(decimal)

    def octal_to_binary(self):
        octal = input("Octal input: ")
        decimal = int(octal, 8)
        print(f"Intermediate decimal: {decimal}")
        self._decimal_to_binary_steps(decimal)

    def octal_to_hex(self):
        octal = input("Octal input: ")
        decimal = int(octal, 8)
        print(f"Intermediate decimal: {decimal}")
        self._decimal_to_hex_steps(decimal)

    def hex_to_binary(self):
        hex_str = input("Hex input: ")
        decimal = int(hex_str, 16)
        print(f"Intermediate decimal: {decimal}")
        self._decimal_to_binary_steps(decimal)

    def hex_to_octal(self):
        hex_str = input("Hex input: ")
        decimal = int(hex_str, 16)
        print(f"Intermediate decimal: {decimal}")
        self._decimal_to_octal_steps(decimal)

    def _decimal_to_binary_steps(self, decimal):
        steps = []
        original = decimal
        while decimal:
            steps.append(f"{decimal} ÷ 2 = {decimal // 2} remainder {decimal % 2}")
            decimal //= 2
        print("Steps:\n" + "\n".join(reversed(steps)))
        print(f"→ Binary: {bin(original)[2:]}")

    def _decimal_to_octal_steps(self, decimal):
        steps = []
        original = decimal
        while decimal:
            steps.append(f"{decimal} ÷ 8 = {decimal // 8} remainder {decimal % 8}")
            decimal //= 8
        print("Steps:\n" + "\n".join(reversed(steps)))
        print(f"→ Octal: {oct(original)[2:]}")

    def _decimal_to_hex_steps(self, decimal):
        digits = "0123456789ABCDEF"
        steps = []
        original = decimal
        while decimal:
            r = decimal % 16
            steps.append(f"{decimal} ÷ 16 = {decimal // 16} remainder {r} ({digits[r]})")
            decimal //= 16
        print("Steps:\n" + "\n".join(reversed(steps)))
        print(f"→ Hexadecimal: {hex(original)[2:].upper()}")
# endregion conversion

#region sorting
class Sorting:
    """A simple class for sorting algorithms."""

    def __init__(self):
        clear_screen()
        print("› Sorting algorithm initialized")
        sleep(1)
        self.start()

    def start(self):
        print("Choose a sorting method:")
        print("1. Bubble Sort")
        print("2. Selection Sort")
        print("3. Insertion Sort")
        print("4. Merge Sort")
        print("5. Quick Sort")
        print("6. Bucket Sort")
        print("7. Shell Sort")
        print("8. Comb Sort")
        print("9. Radix Sort")
        print("10. Tree Sort")
        try:
            choice = int(input(">> "))
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
                    print("⚠️ Invalid option")
        except ValueError:
            print("⚠️ Numbers only")

    def bubble_sort(self):
        arr = list(map(int, input("enter elements (space)>> ").split()))
        n = len(arr)
        comparisons = 0
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    print(f"{arr} [{arr[j]} > {arr[j+1]}]")
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    print(f"{arr} [{arr[j]} <=> {arr[j+1]}]")
                    comparisons += 1
                    sleep(0.01)
        print(f"→ Sorted: {arr} | Comparisons: {comparisons}")

    def selection_sort(self):
        arr = list(map(int, input("enter elements (space)>> ").split()))
        n = len(arr)
        comparisons = 0
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
                    comparisons += 1
                    sleep(0.01)
                    print(f"{arr} [{arr[j]} < {arr[min_idx]}]")
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f"→ Sorted: {arr}")

    def insertion_sort(self):
        arr = list(map(int, input("enter elements (space)>> ").split()))
        self._insertion_sort(arr)
        print(f"→ Sorted: {arr}")

    @staticmethod
    def _insertion_sort(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                sleep(0.01)
                print(f"{arr} [{key} < {arr[j]}]")
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    def merge_sort(self):
        arr = list(map(int, input("enter elements (space)>> ").split()))
        self._merge_sort(arr)
        print(f"→ Sorted: {arr}")

    def _merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]
            sleep(0.05)
            print(f"Split: {left} | {right}")
            self._merge_sort(left)
            self._merge_sort(right)
            self._merge(arr, left, right)

    def _merge(self, arr, left, right):
        i = j = k = 0
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
        print(f"Merged: {left} + {right} → {arr}")

    def quick_sort(self):
        arr = list(map(int, input("enter elements (space)>> ").split()))
        self._quick_sort(arr, 0, len(arr) - 1)
        print(f"→ Sorted: {arr}")

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
                print(f"{arr[j]} < pivot({pivot})")
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                print(f"Swapped: {arr}")
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def bucket_sort(self):
        arr = list(map(int, input("enter elements (space)>> ").split()))
        if not arr:
            print("⚠️ Empty input")
            return
        min_val = min(arr)
        max_val = max(arr)
        range_val = max_val - min_val + 1
        bucket_count = 10
        buckets = [[] for _ in range(bucket_count)]
        for num in arr:
            index = 0 if range_val == 1 else int(((num - min_val) / range_val) * (bucket_count - 1))
            buckets[index].append(num)
            print(f"Buckets: {buckets}")
        for i in range(bucket_count):
            self._insertion_sort(buckets[i])
            print(f"Bucket {i}: {buckets[i]}")
        sorted_arr = []
        for b in buckets:
            sorted_arr.extend(b)
            print(f"Merged: {sorted_arr}")
        print(f"→ Sorted: {sorted_arr}")

    def shell_sort(self):
        arr = list(map(int, input("enter elements (space)>> ").split()))
        length = len(arr)
        gap = length // 2
        while gap > 0:
            for start in range(gap):
                indices = list(range(start, length, gap))
                subarray = [arr[i] for i in indices]
                self._insertion_sort(subarray)
                print(f"Gap {gap}: {subarray}")
                sleep(0.2)
            for idx, val in zip(indices, subarray):
                arr[idx] = val
            gap //= 2
        print(f"→ Sorted: {arr}")

    def comb_sort(self):
        arr = list(map(int, input("enter elements (space)>> ").split()))
        gap = len(arr)
        shrink = 1.3
        sorted_flag = False
        while gap > 1 or not sorted_flag:
            gap = max(1, int(gap / shrink))
            sorted_flag = True
            for i in range(len(arr) - gap):
                if arr[i] > arr[i + gap]:
                    print(f"{arr} [{arr[i]} > {arr[i + gap]}]; gap={gap}")
                    sleep(0.01)
                    arr[i], arr[i + gap] = arr[i + gap], arr[i]
                    print(f"{arr} [{arr[i]} <=> {arr[i + gap]}]")
                    sleep(0.01)
                    sorted_flag = False
        print(f"→ Sorted: {arr}")

    def radix_sort(self):
        arr = list(map(int, input("enter elements (space)>> ").split()))
        max_num = max(arr)
        exp = 1
        pass_num = 1
        while max_num // exp > 0:
            self._counting_sort(arr, exp)
            print(f"Pass {pass_num}: {arr}")
            sleep(0.1)
            pass_num += 1
            exp *= 10
        print(f"→ Sorted: {arr}")

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
#endregion sorting

# region Main Program Loop
def main():
    modules = [
        GCD_LCM,
        Prime,
        Ciphers,
        SetTheory,
        Searching,
        Conversion,
        Sorting,
    ]

    while True:
        clear_screen()
        print("🧠 === John Lloyd Gutib Algorithm Explorer === 🧠\n")
        print("📦 Available Modules:")
        for idx, module in enumerate(modules, start=1):
            print(f" {idx}. {module.__name__}")
        print(" 0. Exit Program")

        try:
            choice = int(input("\nEnter your choice (0 to exit): "))
        except ValueError:
            print("\n⚠️ Please enter a valid number.")
            sleep(1.5)
            continue

        if choice == 0:
            print("\n👋 Thanks for using the Algorithm Explorer. Goodbye!")
            break

        if 1 <= choice <= len(modules):
            while True:
                clear_screen()
                selected_module = modules[choice - 1]
                print(f"🚀 Launching: {selected_module.__name__}\n")
                selected_module()  # Run the selected module

                again = input("\nWould you like to run this module again? (y/N): ").strip().lower()
                if again != 'y':
                    break
        else:
            print("\n❌ That option doesn't exist. Please try again.")
            sleep(1.5)

if __name__ == "__main__":
    main()
# endregion

