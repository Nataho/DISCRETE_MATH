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

#region set theory
class SetTheory:
    """Handles user interaction and operations related to basic set theory."""

    def __init__(self):
        self.set_a = set()
        self.set_b = set()
        clear_screen()
        print("📘 Set Theory Module Activated!")
        sleep(1)
        self.run()

    def run(self):
        self.display_welcome()
        self.get_sets()
        self.display_sets()
        self.compute_results()

    def display_welcome(self):
        print("🔎 Let's explore your sets A and B!")

    def get_sets(self):
        self.set_a = self.input_set("A")
        self.set_b = self.input_set("B")

    def input_set(self, label):
        raw = input(f"🧩 Enter elements of set {label} (separated by spaces): ")
        return set(raw.strip().split())

    def display_sets(self):
        print("\n✅ You entered:")
        print(f"  • Set A: {self.set_a}")
        print(f"  • Set B: {self.set_b}")

    def compute_results(self):
        print("\n⚙️ Computing set operations...")
        sleep(1)
        print("\n📊 Results:")
        print(f"  A ∪ B = {self.set_a | self.set_b}")
        print(f"  A ∩ B = {self.set_a & self.set_b}")
        print(f"  A \\ B = {self.set_a - self.set_b}")
        print(f"  A ⊆ B? {'Yes' if self.set_a <= self.set_b else 'No'}")
        print(f"  A = B? {'Yes' if self.set_a == self.set_b else 'No'}")
#endregion set theory


# region ciphers
class Ciphers:
    """Encrypts and decrypts text using various classical ciphers."""

    def __init__(self):
        clear_screen()
        print("🛡️ Cipher Station Activated!")
        sleep(1)
        self.mode_menu()

    def mode_menu(self):
        print("\n🔐 Choose Mode:")
        modes = [("Encrypt 🔒", self.run_menu_encrypt), ("Decrypt 🔓", self.run_menu_decrypt)]
        random.shuffle(modes)
        for i, (label, _) in enumerate(modes, start=1):
            print(f" {i}. {label}")
        try:
            choice = int(input("Your pick (1 or 2): "))
            modes[choice - 1][1]()
        except (ValueError, IndexError):
            print("⚠️ Invalid choice — please try again.")
            self.mode_menu()

    def run_menu_encrypt(self):
        print("\n🧩 Select a cipher to encrypt with:")
        options = [
            ("Rail Fence Cipher", self.rail_fence_encrypt),
            ("Playfair Cipher", self.playfair_encrypt),
            ("Hill Cipher", self.hill_encrypt),
            ("Columnar Cipher", self.columnar_encrypt),
            ("Caesar Cipher", self.caesar_encrypt),
            ("Vernam Cipher", self.vernam_encrypt),
            ("Vigenère Cipher", self.vigenere_encrypt),
            ("One-Time Pad Cipher", self.one_time_pad_encrypt),
        ]
        random.shuffle(options)
        for i, (label, _) in enumerate(options, start=1):
            print(f" {i}. {label}")
        try:
            choice = int(input("Enter cipher number: "))
            options[choice - 1][1]()
        except (ValueError, IndexError):
            print("⚠️ That wasn't a valid option. Please try again.")

    def run_menu_decrypt(self):
        print("\n🧩 Select a cipher to decrypt with:")
        options = [
            ("Rail Fence Cipher", self.rail_fence_decrypt),
            ("Playfair Cipher", self.playfair_decrypt),
            ("Hill Cipher", self.hill_decrypt),
            ("Columnar Cipher", self.columnar_decrypt),
            ("Caesar Cipher", self.caesar_decrypt),
            ("Vernam Cipher", self.vernam_decrypt),
            ("Vigenère Cipher", self.vigenere_decrypt),
            ("One-Time Pad Cipher", self.one_time_pad_decrypt),
        ]
        random.shuffle(options)
        for i, (label, _) in enumerate(options, start=1):
            print(f" {i}. {label}")
        try:
            choice = int(input("Enter cipher number: "))
            options[choice - 1][1]()
        except (ValueError, IndexError):
            print("⚠️ Invalid selection. Please try again.")

    def caesar_encrypt(self):
        text = input("Enter message to encrypt: ")
        shift = int(input("Shift (1–25): "))
        encrypted = ""
        print("\n[🔒 Encrypting]")
        for char in text:
            ...
        print(f"\nEncrypted → {encrypted}")

    def caesar_decrypt(self):
        text = input("Enter message to decrypt: ")
        shift = int(input("Shift used (1–25): "))
        decrypted = ""
        print("\n[🔓 Decrypting]")
        for char in text:
            ...
        print(f"\nDecrypted → {decrypted}")

    def vigenere_encrypt(self):
        text = input("Enter message to encrypt: ")
        key = input("Keyword: ")
        print("\n[🔒 Encrypting]")
        ...
        print(f"\nEncrypted → {result}")

    def vigenere_decrypt(self):
        text = input("Enter encrypted text: ")
        key = input("Keyword used: ")
        print("\n[🔓 Decrypting]")
        ...
        print(f"\nDecrypted → {result}")

    def playfair_encrypt(self):
        text = input("Enter message to encrypt: ")
        keyword = input("Keyword: ")
        print("\n[🧩 Matrix]")
        ...
        print("\n[🔒 Encrypting Pairs]")
        ...
        print(f"\nEncrypted → {encrypted}")

    def playfair_decrypt(self):
        text = input("Enter ciphertext to decrypt: ")
        keyword = input("Keyword: ")
        print("\n[🧩 Matrix]")
        ...
        print("\n[🔓 Decrypting Pairs]")
        ...
        print(f"\nDecrypted → {decrypted}")

    # Playfair Encrypt & Decrypt
    def playfair_encrypt(self):
        text = input("Enter message to encrypt: ")
        keyword = input("Keyword for matrix: ")
        matrix = self._generate_playfair_matrix(keyword)
        prepared = self._prepare_playfair_text(text)
        encrypted = ""
        print("\n[🧩 Matrix]")
        for row in matrix:
            print(" ".join(row))
        print("\n🔒 Encrypting pairs …")
        for i in range(0, len(prepared), 2):
            pair = prepared[i], prepared[i + 1]
            cipher_pair = self._playfair_encrypt_pair(matrix, *pair)
            print(f"{pair[0]}{pair[1]} → {cipher_pair}")
            encrypted += cipher_pair
        print(f"\n✅ Encrypted text → {encrypted}")

    def playfair_decrypt(self):
        text = input("Enter ciphertext to decrypt: ")
        keyword = input("Keyword for matrix: ")
        matrix = self._generate_playfair_matrix(keyword)
        decrypted = ""
        print("\n[🧩 Matrix]")
        for row in matrix:
            print(" ".join(row))
        print("\n🔓 Decrypting pairs …")
        for i in range(0, len(text), 2):
            pair = text[i], text[i + 1]
            plain_pair = self._playfair_decrypt_pair(matrix, *pair)
            print(f"{pair[0]}{pair[1]} → {plain_pair}")
            decrypted += plain_pair
        print(f"\n✅ Decrypted text → {decrypted}")


    # Playfair Encrypt & Decrypt
    def playfair_encrypt(self):
        text = input("Enter message to encrypt: ")
        keyword = input("Keyword for matrix: ")
        matrix = self._generate_playfair_matrix(keyword)
        prepared = self._prepare_playfair_text(text)
        encrypted = ""
        print("\n[🧩 Matrix]")
        for row in matrix:
            print(" ".join(row))
        print("\n[🔒 Encrypting Pairs]")
        for i in range(0, len(prepared), 2):
            pair = prepared[i], prepared[i + 1]
            cipher_pair = self._playfair_encrypt_pair(matrix, *pair)
            print(f"{pair[0]}{pair[1]} → {cipher_pair}")
            encrypted += cipher_pair
        print(f"\n✅ Encrypted Text → {encrypted}")

    def playfair_decrypt(self):
        text = input("Enter ciphertext to decrypt: ")
        keyword = input("Keyword for matrix: ")
        matrix = self._generate_playfair_matrix(keyword)
        decrypted = ""
        print("\n[🧩 Matrix]")
        for row in matrix:
            print(" ".join(row))
        print("\n[🔓 Decrypting Pairs]")
        for i in range(0, len(text), 2):
            pair = text[i], text[i + 1]
            plain_pair = self._playfair_decrypt_pair(matrix, *pair)
            print(f"{pair[0]}{pair[1]} → {plain_pair}")
            decrypted += plain_pair
        print(f"\n✅ Decrypted Text → {decrypted}")

    # Vernam Encrypt & Decrypt
    def vernam_encrypt(self):
        text = input("Plaintext input: ")
        key = input("Key (same length): ")
        key = (key * ((len(text) // len(key)) + 1))[:len(text)]
        print("\n[🔒 Encrypting]")
        for c, k in zip(text, key):
            print(f"{c} ⊕ {k} = {chr(ord(c) ^ ord(k))}")
        result = "".join(chr(ord(c) ^ ord(k)) for c, k in zip(text, key))
        print(f"\n✅ Encrypted → {result}")
        print(f"(Hex) → {result.encode().hex()}")

    def vernam_decrypt(self):
        text = input("Ciphertext input: ")
        key = input("Key used (same length): ")
        key = (key * ((len(text) // len(key)) + 1))[:len(text)]
        print("\n[🔓 Decrypting]")
        for c, k in zip(text, key):
            print(f"{c} ⊕ {k} = {chr(ord(c) ^ ord(k))}")
        result = "".join(chr(ord(c) ^ ord(k)) for c, k in zip(text, key))
        print(f"\n✅ Decrypted → {result}")
        print(f"(Hex) → {result.encode().hex()}")

    # One-Time Pad Encrypt & Decrypt
    def one_time_pad_encrypt(self):
        text = input("Enter your message: ")
        key = os.urandom(len(text))
        encrypted = bytes([ord(c) ^ k for c, k in zip(text, key)])
        print("\n[🔒 Encrypting via One‑Time Pad]")
        for c, k in zip(text, key):
            print(f"{c} ⊕ {k} = {ord(c) ^ k}")
        print(f"\n🔑 Key (hex): {key.hex()}")
        print(f"🔐 Encrypted (hex): {encrypted.hex()}")

    def one_time_pad_decrypt(self):
        encrypted_hex = input("Paste encrypted message (hex): ")
        key_hex = input("Paste key used (hex): ")
        try:
            encrypted = bytes.fromhex(encrypted_hex)
            key = bytes.fromhex(key_hex)
        except ValueError:
            print("⚠️ Invalid hex input — please try again.")
            return
        decrypted = "".join(chr(e ^ k) for e, k in zip(encrypted, key))
        print("\n[🔓 Decrypting via One‑Time Pad]")
        for e, k in zip(encrypted, key):
            print(f"{e} ⊕ {k} = {e ^ k}")
        print(f"\n📨 Decrypted message → {decrypted}")

    # Hill Cipher Encrypt & Decrypt
    def hill_encrypt(self):
        text = input("Enter text to encrypt: ")
        key_input = input("Enter 3×3 key matrix (9 numbers space-separated): ")
        try:
            vals = list(map(int, key_input.split()))
            if len(vals) != 9:
                print("⚠️ Expected exactly 9 numbers.")
                return
            matrix = [vals[i:i+3] for i in range(0, 9, 3)]
        except ValueError:
            print("⚠️ Invalid matrix input — enter 9 integers.")
            return

        small = [chr(i) for i in range(97, 123)]
        big = [chr(i) for i in range(65, 91)]
        chars = [c for c in text if c.isalpha()]
        while len(chars) % 3 != 0:
            chars.append('x')
        nums = [(small + big).index(c.lower()) % 26 for c in chars]
        print("\n[🔒 Encrypting with Hill Cipher]")
        result = ""
        for i in range(0, len(nums), 3):
            block = nums[i:i+3]
            res = [(sum(matrix[r][c] * block[r] for r in range(3)) % 26) for c in range(3)]
            for j, val in enumerate(res):
                orig = chars[i + j]
                print(f"Block {block} → Col {j} = {val}")
                result += big[val] if orig.isupper() else small[val]
        print("\n🧮 Key matrix:")
        for row in matrix:
            print(row)
        print(f"\n🔐 Hill Cipher Encrypted → {result}")

    def hill_decrypt(self):
        text = input("Enter encrypted text: ")
        key_input = input("Enter 3×3 key matrix (9 numbers space-separated): ")
        try:
            vals = list(map(int, key_input.split()))
            if len(vals) != 9:
                print("⚠️ Expected exactly 9 numbers.")
                return
            matrix = [vals[i:i+3] for i in range(0, 9, 3)]
        except ValueError:
            print("⚠️ Invalid matrix input — enter 9 integers.")
            return

        inv_matrix = self._hill_matrix_inverse(matrix)
        if inv_matrix is None:
            print("⚠️ Matrix not invertible mod 26 — can't decrypt.")
            return

        small = [chr(i) for i in range(97, 123)]
        big = [chr(i) for i in range(65, 91)]
        chars = [c for c in text if c.isalpha()]
        while len(chars) % 3 != 0:
            chars.append('x')
        nums = [(small + big).index(c.lower()) % 26 for c in chars]
        print("\n[🔓 Decrypting with Hill Cipher]")
        result = ""
        for i in range(0, len(nums), 3):
            block = nums[i:i+3]
            res = [(sum(inv_matrix[r][c] * block[r] for r in range(3)) % 26) for c in range(3)]
            for j, val in enumerate(res):
                orig = chars[i + j]
                print(f"Block {block} → InvCol {j} = {val}")
                result += big[val] if orig.isupper() else small[val]
        print("\n🧮 Inverse matrix:")
        for row in inv_matrix:
            print(row)
        print(f"\n📨 Hill Cipher Decrypted → {result}")

#endregion cipher

# region Searching
class Searching:
    """A tool to demonstrate various search algorithms interactively."""

    def __init__(self):
        clear_screen()
        print("🔍 Welcome to the Interactive Search Tool!")
        sleep(1)
        self.menu()

    def menu(self):
        print("\nWhich search adventure shall we take on today?")
        print(" 1. Interpolation Search")
        print(" 2. Linear Search")
        print(" 3. Binary Search")
        print(" 4. Ternary Search")
        print(" 5. Jump Search")
        print(" 6. Interval Search")

        try:
            choice = int(input("Pick a number (1–3) to dive in: "))
        except ValueError:
            print("⚠️ Oops! That’s not a number between 1 and 3. Try again.")
            return self.menu()

        if choice == 1:
            self.interpolation_search()
        elif choice == 2:
            self.linear_search()
        elif choice == 3:
            self.binary_search()
        elif choice == 4:
            self.ternary_search()
        elif choice == 5:
            self.jump_search()
        elif choice == 6:
            self.interval_search()
        else:
            print("⚠️ That choice isn’t on the menu. Give it another go!")
            self.menu()

    def get_array_and_target(self, sort_array=False):
        try:
            values = list(map(int, input("\nEnter your list of numbers (space-separated): ").split()))
            if sort_array:
                values.sort()
                print(f"🔢 Here’s the sorted array we’ll work with: {values}")
            target = int(input("🔍 Now, what number are you searching for? "))
            return values, target
        except ValueError:
            print("⚠️ Hmmm, looks like some input wasn’t an integer. Try again please!")
            return self.get_array_and_target(sort_array)

    def linear_search(self):
        arr, target = self.get_array_and_target()
        print("\n🔎 Starting linear search…\n")
        sleep(0.5)

        for idx, val in enumerate(arr):
            print(f"Checking index {idx} — value: {val}")
            if val == target:
                print(f"🎉 Got it! {target} found at index {idx}.")
                return
            print("→ Nope, not here. Moving on…")
        print(f"😞 Sorry, {target} isn’t in this list.")

    def binary_search(self):
        arr, target = self.get_array_and_target(sort_array=True)
        print("\n🔎 Starting binary search…\n")
        sleep(0.5)

        left, right = 0, len(arr) - 1
        step = 1

        while left <= right:
            mid = (left + right) // 2
            print(f"Step {step}: left = {left}, right = {right}, mid = {mid} (value: {arr[mid]})")
            step += 1

            if arr[mid] == target:
                print(f"🎉 Found {target} right here at index {mid}!")
                return
            elif arr[mid] < target:
                print(f"{arr[mid]} is less than {target}, searching the right half...")
                left = mid + 1
            else:
                print(f"{arr[mid]} is greater than {target}, searching the left half...")
                right = mid - 1

        print(f"😞 No luck! {target} isn’t in the array.")

    def interpolation_search(self):
        arr, target = self.get_array_and_target(sort_array=True)
        print("\n🔎 Starting interpolation search…\n")
        sleep(0.5)

        low, high = 0, len(arr) - 1
        step = 1

        while low <= high and arr[low] <= target <= arr[high]:
            if arr[high] == arr[low]:
                if arr[low] == target:
                    print(f"🎉 Found {target} at index {low}!")
                    return
                break

            pos = low + int(((target - arr[low]) * (high - low)) / (arr[high] - arr[low]))

            if pos < low or pos > high:
                break

            print(f"Step {step}: low = {low}, high = {high}, pos = {pos} (value: {arr[pos]})")
            step += 1

            if arr[pos] == target:
                print(f"🎯 Bullseye! {target} found at index {pos}.")
                return
            elif arr[pos] < target:
                print(f"{arr[pos]} is less than {target}, shifting right...")
                low = pos + 1
            else:
                print(f"{arr[pos]} is greater than {target}, shifting left...")
                high = pos - 1

        print(f"😔 {target} wasn’t found this time.")
    
    def ternary_search(self):
        arr, target = self.get_array_and_target(sort_array=True)
        print("\n🔍 Launching Ternary Search...\n")
        sleep(0.5)
        left, right = 0, len(arr) - 1
        step = 1
        while left <= right:
            third = (right - left) // 3
            mid1 = left + third
            mid2 = right - third
            print(f"Step {step}: mid1={mid1}({arr[mid1]}), mid2={mid2}({arr[mid2]})")
            step += 1
            if arr[mid1] == target:
                print(f"🎯 Found at index {mid1}")
                return
            if arr[mid2] == target:
                print(f"🎯 Found at index {mid2}")
                return
            if target < arr[mid1]:
                right = mid1 - 1
            elif target > arr[mid2]:
                left = mid2 + 1
            else:
                left = mid1 + 1
                right = mid2 - 1
        print(f"❌ {target} not discovered.")

    def jump_search(self):
        arr, target = self.get_array_and_target(sort_array=True)
        print("\n🏃 Executing Jump Search...\n")
        sleep(0.5)
        import math
        n = len(arr)
        step = int(math.sqrt(n))
        prev = 0
        while prev < n and arr[min(step, n) - 1] < target:
            print(f"Jumping from {prev} to {min(step, n) - 1}")
            prev = step
            step += int(math.sqrt(n))
            if prev >= n:
                print("🚫 Overshot the list!")
                return
        for i in range(prev, min(step, n)):
            print(f"Scanning index {i}: {arr[i]}")
            if arr[i] == target:
                print(f"🎯 Found at index {i}")
                return
        print(f"❌ {target} not found after jumping.")

    def interval_search(self):
        arr, target = self.get_array_and_target(sort_array=True)
        print("\n📈 Interval (Exponential) Search Engaged...\n")
        sleep(0.5)
        if len(arr) == 0:
            print("📭 Empty array!")
            return
        if arr[0] == target:
            print("🎯 Found at index 0")
            return
        index = 1
        while index < len(arr) and arr[index] <= target:
            print(f"Interval check: index={index}, value={arr[index]}")
            index *= 2
        left = index // 2
        right = min(index, len(arr) - 1)
        print(f"🔎 Binary search between {left} and {right}")
        while left <= right:
            mid = (left + right) // 2
            print(f"Checking mid={mid}: {arr[mid]}")
            if arr[mid] == target:
                print(f"🎯 Found at index {mid}")
                return
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        print(f"❌ {target} not located in exponential search window.")
# endregion

#region conversion
class Conversion:
    """A simple class for number base conversions."""

    def __init__(self):
        clear_screen()
        print("🔧 Welcome to the Base Conversion Tool!")
        sleep(1)
        self.start()

    def start(self):
        print("\n✨ Choose a conversion type:")
        print(" 1️⃣ Decimal → Binary")
        print(" 2️⃣ Binary → Decimal")
        print(" 3️⃣ Decimal → Octal")
        print(" 4️⃣ Decimal → Hexadecimal")
        print(" 5️⃣ Octal → Decimal")
        print(" 6️⃣ Hexadecimal → Decimal")
        print(" 7️⃣ Binary → Octal")
        print(" 8️⃣ Binary → Hexadecimal")
        print(" 9️⃣ Octal → Binary")
        print("🔟 Octal → Hexadecimal")
        print("🟰 Hexadecimal → Binary")
        print("🧮 Hexadecimal → Octal")
        choice = int(input("\nYour choice (1–12): "))

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
                print("❗ Oops—that's not a valid choice.")

    def decimal_to_binary(self):
        decimal = int(input("🔢 Enter a decimal number: "))
        output = ""
        base = 2

        while True:
            remainder = decimal % base
            decimal //= base
            output = str(remainder) + output
            if decimal == 0:
                break

        print(f"✅ Result in Binary: {output}")

    def binary_to_decimal(self):
        binary = input("🔢 Enter a binary number: ")
        reversed_bin = binary[::-1]
        decimal = sum(int(digit) * 2 ** idx for idx, digit in enumerate(reversed_bin))
        print(f"✅ Converted to Decimal: {decimal}")

    def decimal_to_octal(self):
        decimal = int(input("🔢 Enter a decimal number: "))
        output = ""
        base = 8

        while True:
            remainder = decimal % base
            decimal //= base
            output = str(remainder) + output
            if decimal == 0:
                break

        print(f"✅ Octal value: {output}")

    def decimal_to_hex(self):
        decimal = int(input("🔢 Enter a decimal number: "))
        output = ""
        base = 16

        while True:
            remainder = decimal % base
            hex_digit = "0123456789ABCDEF"[remainder]
            decimal //= base
            output = hex_digit + output
            if decimal == 0:
                break

        print(f"✅ Hexadecimal: {output}")

    def octal_to_decimal(self):
        octal = input("🔢 Enter an octal number: ")
        reversed_octal = octal[::-1]
        decimal = sum(int(digit) * 8 ** idx for idx, digit in enumerate(reversed_octal))
        print(f"✅ Decimal result: {decimal}")

    def hex_to_decimal(self):
        hex_str = input("🔢 Enter a hexadecimal number: ")
        reversed_hex = hex_str[::-1].upper()
        hex_digits = "0123456789ABCDEF"
        decimal = sum(hex_digits.index(char) * 16 ** idx for idx, char in enumerate(reversed_hex))
        print(f"✅ Decimal result: {decimal}")

    def binary_to_octal(self):
        binary = input("🔢 Enter a binary number: ")
        decimal = int(binary, 2)
        octal = ""
        while decimal:
            octal = str(decimal % 8) + octal
            decimal //= 8
        print(f"✅ Octal value: {octal or '0'}")

    def binary_to_hex(self):
        binary = input("🔢 Enter a binary number: ")
        decimal = int(binary, 2)
        hex_value = ""
        while decimal:
            hex_value = "0123456789ABCDEF"[decimal % 16] + hex_value
            decimal //= 16
        print(f"✅ Hexadecimal: {hex_value or '0'}")

    def octal_to_binary(self):
        octal = input("🔢 Enter an octal number: ")
        decimal = int(octal, 8)
        binary = ""
        while decimal:
            binary = str(decimal % 2) + binary
            decimal //= 2
        print(f"✅ Binary value: {binary or '0'}")

    def octal_to_hex(self):
        octal = input("🔢 Enter an octal number: ")
        decimal = int(octal, 8)
        hex_value = ""
        while decimal:
            hex_value = "0123456789ABCDEF"[decimal % 16] + hex_value
            decimal //= 16
        print(f"✅ Hexadecimal: {hex_value or '0'}")

    def hex_to_binary(self):
        hex_str = input("🔢 Enter a hexadecimal number: ")
        decimal = int(hex_str, 16)
        binary = ""
        while decimal:
            binary = str(decimal % 2) + binary
            decimal //= 2
        print(f"✅ Binary value: {binary or '0'}")

    def hex_to_octal(self):
        hex_str = input("🔢 Enter a hexadecimal number: ")
        decimal = int(hex_str, 16)
        octal = ""
        while decimal:
            octal = str(decimal % 8) + octal
            decimal //= 8
        print(f"✅ Octal value: {octal or '0'}")
#endregion conversion

# region Prime
class Prime:
    """A simple class for prime number operations."""

    def __init__(self):
        clear_screen()
        print("🔎 Prime Number Toolkit is ready!")
        sleep(1)
        self.start()

    def start(self):
        print("\n🧮 What would you like to do?")
        print(" 1️⃣  Check if a number is prime")
        print(" 2️⃣  Generate primes (Sieve of Eratosthenes)")
        print(" 3️⃣  Compute prime factors")
        print(" 4️⃣  Fermat’s little theorem")
        print(" 5️⃣  Find primitive roots")
        choice = int(input("Select option (1–5): "))
        
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
                print("❗ Oops—that's not a valid option.")

    def check_prime(self):
        n = int(input("🔢 Enter a number to test: "))
        if n < 2:
            print("❌ Not prime.")
            return
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                print("❌ Not prime.")
                return
        print("✅ Prime!")

    @staticmethod
    def _check_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def prime_factors(self):
        num = int(input("🔢 Enter a number to factor: "))
        factors = []
        while n % 2 == 0:
            factors.append(2)
            n //= 2
        for i in range(3, int(n**0.5) + 1, 2):
            while n % i == 0:
                if Prime._check_prime(i):
                    factors.append(i)
                n //= i
        if n > 2:
            factors.append(n)
        print(f"🔍 Prime factors of {num}: {factors}")

    def sieve(self):
        low = int(input("📏 Enter the lower bound: "))
        high = int(input("📏 Enter the upper bound: "))
        primes = [i for i in range(low, high) if self._check_prime(i)]
        print(f"✅ Primes between {low} and {high}: {primes}")
    
    def fermats(self):
        print("🧠 Fermat’s little theorem: a^(p–1) ≡ 1 (mod p)")
        a = int(input("🔢 Enter a (base): "))
        k = int(input("🔢 Enter k (exponent): "))
        p = int(input("🔢 Enter p (prime): "))
        if not self._check_prime(p):
            print("❗ p must be prime.")
        answer = pow(a, k) % p
        print(f"📊 {a}^{k} mod {p} = {answer}")

    def primitive_roots(self):
        p = int(input("🔢 Enter a prime p: "))
        a = int(input("🔢 Enter a candidate for primitive root: "))
        if a <= 0 or p <= 0:
            print("❗ a and p must be positive.")
        if not self._check_prime(p):
            print("❗ p must be prime.")
        
        required = set(range(1, p))
        roots = [
            g for g in range(2, p)
            if set(pow(g, k, p) for k in range(1, p)) == required
        ]
        is_prim = a in roots
        print(f"🔑 Is {a} a primitive root mod {p}? {'Yes' if is_prim else 'No'}")
        print(f"🌟 Primitive roots of {p}: {roots}")
# endregion


# region GCD & LCM
class GCD_LCM:
    """A simple class for GCD and LCM calculations."""

    def __init__(self):
        clear_screen()
        print("🔢 GCD & LCM Calculator is ready!")
        sleep(1)
        self.start()

    def start(self):
        print("\n🛠️ Choose an operation:")
        print(" 1️⃣  Compute GCD (Euclidean method)")
        print(" 2️⃣  Compute LCM (via GCD)")
        choice = int(input("Your selection (1 or 2): "))
        
        match choice:
            case 1:
                self.gcd()
            case 2:
                self.lcm()
            case _:
                print("❗ Invalid choice, please restart.")

    def gcd(self):
        a = int(input("📌 Enter the first number: "))
        b = int(input("📌 Enter the second number: "))
        while b:
            a, b = b, a % b
        print(f"✅ GCD result: {a}")

    def lcm(self):
        a = int(input("📌 Enter the first number: "))
        b = int(input("📌 Enter the second number: "))
        orig_a, orig_b = a, b
        while b:
            a, b = b, a % b
        gcd = a
        lcm = (orig_a * orig_b) // gcd
        print(f"✅ LCM result: {lcm}")
# endregion


# region Searching
class Searching:
    """A tool to explore different search algorithms interactively."""

    def __init__(self):
        clear_screen()
        print("✨ Hello there! Welcome to the Search Algorithm Playground!")
        sleep(1)
        self.menu()

    def menu(self):
        print("\nWhich search path would you like to explore today?")
        print(" 1. Interpolation Search 🚀")
        print(" 2. Linear Search 🧭")
        print(" 3. Binary Search 🧠")
        print(" 4. Ternary Search 🔱")
        print(" 5. Jump Search 🏃")
        print(" 6. Interval Search 📏")

        try:
            choice = int(input("Enter a number between 1 and 6: "))
        except ValueError:
            print("⚠️ Uh-oh—that wasn't a number 1–6. Let's try again!")
            return self.menu()

        {
            1: self.interpolation_search,
            2: self.linear_search,
            3: self.binary_search,
            4: self.ternary_search,
            5: self.jump_search,
            6: self.interval_search,
        }.get(choice, lambda: (print("⚠️ Oops—that option isn't on the list. Give it another shot!"), self.menu()))()

    def get_array_and_target(self, sort_array=False):
        try:
            values = list(map(int, input("\nType in a series of numbers (space-separated): ").split()))
            if sort_array:
                values.sort()
                print(f"📊 Sorted array: {values}")
            target = int(input("🔍 What number are we searching for? "))
            return values, target
        except ValueError:
            print("⚠️ Whoops! All inputs must be integers. Let's try that again.")
            return self.get_array_and_target(sort_array)

    def linear_search(self):
        arr, target = self.get_array_and_target()
        print("\n🔎 Launching linear search…\n")
        sleep(0.5)

        for idx, val in enumerate(arr):
            print(f"Checking index {idx} (value: {val})")
            if val == target:
                print(f"🎉 Success! Found {target} at index {idx}.")
                return
            print("…not here, moving on.")
        print(f"❌ Nope, {target} isn't in this list.")

    def binary_search(self):
        arr, target = self.get_array_and_target(sort_array=True)
        print("\n🔎 Running binary search…\n")
        sleep(0.5)

        left, right = 0, len(arr) - 1
        step = 1

        while left <= right:
            mid = (left + right) // 2
            print(f"Step {step}: left={left}, right={right}, mid={mid} (value: {arr[mid]})")
            step += 1

            if arr[mid] == target:
                print(f"🎯 Found {target}! It's at index {mid}.")
                return
            elif arr[mid] < target:
                print("Going right—current is smaller than target.")
                left = mid + 1
            else:
                print("Going left—current is bigger than target.")
                right = mid - 1

        print(f"❌ No luck—{target} isn't present.")

    def interpolation_search(self):
        arr, target = self.get_array_and_target(sort_array=True)
        print("\n🔎 Performing interpolation search…\n")
        sleep(0.5)

        low, high = 0, len(arr) - 1
        step = 1

        while low <= high and arr[low] <= target <= arr[high]:
            if arr[high] == arr[low]:
                if arr[low] == target:
                    print(f"🎉 Found {target} at index {low}!")
                    return
                break

            pos = low + int(((target - arr[low]) * (high - low)) / (arr[high] - arr[low]))
            if pos < low or pos > high:
                break

            print(f"Step {step}: low={low}, high={high}, pos={pos} (value: {arr[pos]})")
            step += 1

            if arr[pos] == target:
                print(f"🎯 Hit! {target} is at index {pos}.")
                return
            elif arr[pos] < target:
                print("Target's higher—shifting right.")
                low = pos + 1
            else:
                print("Target's lower—shifting left.")
                high = pos - 1

        print(f"❌ {target} wasn't found this time.")

    def ternary_search(self):
        arr, target = self.get_array_and_target(sort_array=True)
        print("\n🔎 Kicking off ternary search…\n")
        sleep(0.5)

        left, right = 0, len(arr) - 1
        step = 1
        while left <= right:
            mid1 = left + (right - left) // 3
            mid2 = right - (right - left) // 3
            print(f"Step {step}: left={left}, mid1={mid1}, mid2={mid2}, right={right} (vals: {arr[mid1]}, {arr[mid2]})")
            step += 1

            if arr[mid1] == target:
                print(f"🎉 Found it at mid1 (index {mid1})!")
                return
            if arr[mid2] == target:
                print(f"🎉 Found it at mid2 (index {mid2})!")
                return

            if target < arr[mid1]:
                print("Going left third.")
                right = mid1 - 1
            elif target > arr[mid2]:
                print("Going right third.")
                left = mid2 + 1
            else:
                print("Going middle third.")
                left = mid1 + 1
                right = mid2 - 1

        print(f"❌ Couldn't locate {target}.")

    def jump_search(self):
        arr, target = self.get_array_and_target(sort_array=True)
        print("\n🔎 Starting jump search…\n")
        sleep(0.5)

        import math
        n = len(arr)
        step_size = int(math.sqrt(n))
        prev = 0
        step = 1

        # Jumping blocks
        while prev < n and arr[min(prev + step_size, n) - 1] < target:
            print(f"Step {step}: jumped to block ending at index {min(prev+step_size, n)-1}")
            prev += step_size
            step += 1

        print(f"🔍 Now linearly scanning from index {prev}…")
        for idx in range(prev, min(prev + step_size, n)):
            print(f"Checking index {idx} (value: {arr[idx]})")
            if arr[idx] == target:
                print(f"🎉 Found {target} at index {idx}!")
                return

        print(f"❌ {target} not found in the list.")

    def interval_search(self):
        arr, target = self.get_array_and_target(sort_array=False)
        print("\n🔎 Launching interval search…\n")
        sleep(0.5)

        left, right = 0, len(arr) - 1
        step = 1
        while left <= right:
            print(f"Step {step}: examining interval {left}–{right}")
            mini = min(arr[left:right+1])
            maxi = max(arr[left:right+1])
            print(f"Range is {mini} to {maxi}")
            if target < mini or target > maxi:
                print("Target out of this slice—shrinking the window.")
                left += 1
                right -= 1
            else:
                for idx in range(left, right+1):
                    print(f"Scanning index {idx} — value {arr[idx]}")
                    if arr[idx] == target:
                        print(f"🎉 Found {target} at index {idx}!")
                        return
                break
            step += 1

        print(f"❌ {target} isn’t in this list.")
# endregion



# region Main Program Loop
def main():
    modules = [
        Prime,
        GCD_LCM,
        Ciphers,
        Conversion,
        Searching,
        SetTheory,
        Sorting,
    ]

    while True:
        clear_screen()
        print("✨ Welcome to Jason Hangalay's Algorithm Explorer ✨")
        print("\n🧭 Select a module to launch:")
        for index, mod in enumerate(modules, start=1):
            print(f" {index}. {mod.__name__}")
        print(" 0. 🚪 Quit")

        try:
            selection = int(input("\nEnter module number (0 to quit): "))
        except ValueError:
            print("\n⚠️ That wasn't a valid number. Try again!")
            sleep(1.2)
            continue

        if selection == 0:
            print("\n👋 Thanks for exploring! See you next time.")
            break

        if 1 <= selection <= len(modules):
            while True:
                clear_screen()
                print(f"▶️ Launching: {modules[selection - 1].__name__}\n")
                modules[selection - 1]()  # Instantiate and run
                retry = input("\n🔁 Would you like to run this module again? (y/N): ")
                if retry.strip().lower() != 'y':
                    break
        else:
            print("\n❗ Not a valid choice—please choose from the list!")
            sleep(1.2)

if __name__ == "__main__":
    main()
# endregion
#