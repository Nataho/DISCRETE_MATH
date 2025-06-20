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

# region set theory
class SetTheory:
    """Handles user interaction and operations related to basic set theory."""

    def __init__(self):
        self.set_a = set()
        self.set_b = set()
        clear_screen()
        print("Set Theory Module Activated 📘")
        sleep(1)
        self.run()

    def run(self):
        self.display_welcome()
        self.get_sets()
        self.display_sets()
        self.compute_results()

    def display_welcome(self):
        print("Let's explore your sets A and B 🔎")

    def get_sets(self):
        self.set_a = self.input_set("A")
        self.set_b = self.input_set("B")

    def input_set(self, label):
        raw = input(f"Enter elements of set {label} (space-separated) 🧩: ")
        return set(raw.strip().split())

    def display_sets(self):
        print("\nYou entered ✅")
        print(f"  • Set A: {self.set_a}")
        print(f"  • Set B: {self.set_b}")

    def compute_results(self):
        print("\nComputing set operations ⚙️")
        sleep(1)
        print("\nResults 📊")
        print(f"  A ∪ B = {self.set_a | self.set_b}")
        print(f"  A ∩ B = {self.set_a & self.set_b}")
        print(f"  A \\ B = {self.set_a - self.set_b}")
        print(f"  A ⊆ B? {'Yes' if self.set_a <= self.set_b else 'No'}")
        print(f"  A = B? {'Yes' if self.set_a == self.set_b else 'No'}")
# endregion set theory


# region ciphers
class Ciphers:
    """Encrypts and decrypts text using various classical ciphers."""

    def __init__(self):
        clear_screen()
        print("🛡️ Cipher Station: Ready for action!")
        sleep(1)
        self.mode_menu()

    def mode_menu(self):
        print("\n🔐 Choose your mode:")
        modes = [("Encrypt 🔒", self.run_menu_encrypt), ("Decrypt 🔓", self.run_menu_decrypt)]
        random.shuffle(modes)
        for i, (label, _) in enumerate(modes, start=1):
            print(f" {i}. {label}")
        try:
            choice = int(input("Your pick (1 or 2): "))
            modes[choice - 1][1]()
        except (ValueError, IndexError):
            print("⚠️ Invalid choice—let’s try again.")
            self.mode_menu()

    def run_menu_encrypt(self):
        print("\n🧩 Pick a cipher to encrypt with:")
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
            print("⚠️ Not a valid option—please try again.")

    def run_menu_decrypt(self):
        print("\n🧩 Pick a cipher to decrypt with:")
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
            print("⚠️ Oops—invalid selection, please try again.")

    def caesar_encrypt(self):
        text = input("Enter text to encrypt: ")
        shift = int(input("Shift amount (1–25): "))
        encrypted = ""
        print("\n[🔒 Encrypting...]")
        for char in text:
            ...
        print(f"\nEncrypted → {encrypted}")

    def caesar_decrypt(self):
        text = input("Enter text to decrypt: ")
        shift = int(input("Shift used (1–25): "))
        decrypted = ""
        print("\n[🔓 Decrypting...]")
        for char in text:
            ...
        print(f"\nDecrypted → {decrypted}")

    def vigenere_encrypt(self):
        text = input("Enter text to encrypt: ")
        key = input("Keyword: ")
        print("\n[🔒 Encrypting...]")
        ...
        print(f"\nEncrypted → {result}")

    def vigenere_decrypt(self):
        text = input("Enter encrypted text: ")
        key = input("Keyword: ")
        print("\n[🔓 Decrypting...]")
        ...
        print(f"\nDecrypted → {result}")

    def playfair_encrypt(self):
        text = input("Enter text to encrypt: ")
        keyword = input("Keyword: ")
        print("\n[🧩 Setting up matrix...]")
        ...
        print("\n[🔒 Encrypting pairs...]")
        ...
        print(f"\nEncrypted → {encrypted}")

    def playfair_decrypt(self):
        text = input("Enter ciphertext to decrypt: ")
        keyword = input("Keyword: ")
        print("\n[🧩 Setting up matrix...]")
        ...
        print("\n[🔓 Decrypting pairs...]")
        ...
        print(f"\nDecrypted → {decrypted}")

    # Playfair Encrypt & Decrypt
    def playfair_encrypt(self):
        text = input("Enter message to encrypt: ")
        keyword = input("Keyword for matrix: ")
        matrix = self._generate_playfair_matrix(keyword)
        prepared = self._prepare_playfair_text(text)
        encrypted = ""
        print("\n[🧩 Playfair Matrix]")
        for row in matrix:
            print(" ".join(row))
        print("\n🔒 Encrypting digraphs …")
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
        print("\n[🧩 Playfair Matrix]")
        for row in matrix:
            print(" ".join(row))
        print("\n🔓 Decrypting digraphs …")
        for i in range(0, len(text), 2):
            pair = text[i], text[i + 1]
            plain_pair = self._playfair_decrypt_pair(matrix, *pair)
            print(f"{pair[0]}{pair[1]} → {plain_pair}")
            decrypted += plain_pair
        print(f"\n✅ Decrypted text → {decrypted}")

    # Vernam Encrypt & Decrypt
    def vernam_encrypt(self):
        text = input("Plaintext input: ")
        key = input("Key (matching length): ")
        key = (key * ((len(text) // len(key)) + 1))[:len(text)]
        print("\n🔒 Encrypting with Vernam …")
        for c, k in zip(text, key):
            print(f"{c} ⊕ {k} = {chr(ord(c) ^ ord(k))}")
        result = "".join(chr(ord(c) ^ ord(k)) for c, k in zip(text, key))
        print(f"\n✅ Encrypted → {result}")
        print(f"(hex) → {result.encode().hex()}")

    def vernam_decrypt(self):
        text = input("Ciphertext input: ")
        key = input("Key used (same length): ")
        key = (key * ((len(text) // len(key)) + 1))[:len(text)]
        print("\n🔓 Decrypting with Vernam …")
        for c, k in zip(text, key):
            print(f"{c} ⊕ {k} = {chr(ord(c) ^ ord(k))}")
        result = "".join(chr(ord(c) ^ ord(k)) for c, k in zip(text, key))
        print(f"\n✅ Decrypted → {result}")
        print(f"(hex) → {result.encode().hex()}")

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
            print("⚠️ Invalid hex input—please try again.")
            return
        decrypted = "".join(chr(e ^ k) for e, k in zip(encrypted, key))
        print("\n[🔓 Decrypting via One‑Time Pad]")
        for e, k in zip(encrypted, key):
            print(f"{e} ⊕ {k} = {e ^ k}")
        print(f"\n📨 Decrypted message → {decrypted}")

    # Hill Cipher Encrypt & Decrypt
    def hill_encrypt(self):
        text = input("Enter text to encrypt: ")
        key_input = input("Enter 3×3 key matrix (9 numbers space‑separated): ")
        try:
            vals = list(map(int, key_input.split()))
            if len(vals) != 9:
                print("⚠️ Expected exactly 9 numbers.")
                return
            matrix = [vals[i:i+3] for i in range(0, 9, 3)]
        except ValueError:
            print("⚠️ Invalid matrix input—enter 9 integers.")
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
        key_input = input("Enter 3×3 key matrix (9 numbers space‑separated): ")
        try:
            vals = list(map(int, key_input.split()))
            if len(vals) != 9:
                print("⚠️ Expected exactly 9 numbers.")
                return
            matrix = [vals[i:i+3] for i in range(0, 9, 3)]
        except ValueError:
            print("⚠️ Invalid matrix input—enter 9 integers.")
            return

        inv_matrix = self._hill_matrix_inverse(matrix)
        if inv_matrix is None:
            print("⚠️ Matrix not invertible mod 26—can't decrypt.")
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


# region sorting
class Sorting:
    """A simple class for sorting algorithms."""

    def __init__(self):
        clear_screen()
        print("📊 Sorting Algorithm Explorer is primed!")
        sleep(1)
        self.start()

    def start(self):
        print("\n⚙️ Pick a sorting method to run:")
        print(" 1. 🫧 Bubble Sort")
        print(" 2. 📍 Selection Sort")
        print(" 3. 📝 Insertion Sort")
        print(" 4. 🔀 Merge Sort")
        print(" 5. 🚀 Quick Sort")
        print(" 6. 🪣 Bucket Sort")
        print(" 7. 🐚 Shell Sort")
        print(" 8. ⚙️ Comb Sort")
        print(" 9. 🧮 Radix Sort")
        print("10. 🌳 Tree Sort")
        choice = int(input("Enter your choice (1–10): "))

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
                print("❗ That choice is invalid—please try again.")
#endregion


# region conversion
class Conversion:
    """A simple class for number base conversions."""

    def __init__(self):
        clear_screen()
        print("Base Conversion Toolkit is ready 🛠️")
        sleep(1)
        self.start()

    def start(self):
        print("\nSelect a conversion type:")
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
        choice = int(input("\nEnter your choice (1–12): "))

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
                print("That isn’t a valid option ❗ Please restart the tool.")
    ...
#endregion conversion




# region Prime
class Prime:
    """A simple class for prime number operations."""

    def __init__(self):
        clear_screen()
        print("Prime Number Toolkit: Ready to dive in 🎯")
        sleep(1)
        self.start()

    def start(self):
        print("\nWhat would you like to explore today?")
        print(" 1️⃣ Test if a number is prime")
        print(" 2️⃣ Generate primes (Sieve of Eratosthenes)")
        print(" 3️⃣ Compute prime factors")
        print(" 4️⃣ Apply Fermat’s little theorem")
        print(" 5️⃣ Discover primitive roots")
        choice = int(input("Enter your choice (1–5): "))

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
                print("That option isn’t valid—please try again ❗")
    ...
# endregion



# region GCD & LCM
class GCD_LCM:
    """A simple class for GCD and LCM calculations."""

    def __init__(self):
        clear_screen()
        print("🎯 GCD & LCM Calculator is primed and ready!")
        sleep(1)
        self.start()

    def start(self):
        print("\n⚙️ Let’s crunch some numbers—pick an operation:")
        print(" 1️⃣  Calculate GCD (Euclidean algorithm)")
        print(" 2️⃣  Calculate LCM (deriving via GCD)")
        choice = int(input("Enter your selection (1 or 2): "))

        match choice:
            case 1:
                self.gcd()
            case 2:
                self.lcm()
            case _:
                print("❗ That wasn’t a valid choice—please restart the tool.")

    def gcd(self):
        a = int(input("🧮 First number, please: "))
        b = int(input("🧮 Now a second number: "))
        while b:
            a, b = b, a % b
        print(f"✅ Your GCD is {a}!")

    def lcm(self):
        a = int(input("🧮 First number, please: "))
        b = int(input("🧮 Now a second number: "))
        orig_a, orig_b = a, b
        while b:
            a, b = b, a % b
        gcd = a
        lcm = (orig_a * orig_b) // gcd
        print(f"✅ The LCM is {lcm}!")
# endregion



# region Searching
class Searching:
    """A tool to demonstrate various search algorithms interactively."""

    def __init__(self):
        clear_screen()
        print("Dive into the Search Algorithm Explorer 🔎")
        sleep(1)
        self.menu()

    def menu(self):
        print("\nPick your search adventure:")
        print(" 1. Interpolation Search 🌐")
        print(" 2. Linear Search 🚶")
        print(" 3. Binary Search 🧠")
        print(" 4. Ternary Search 🔺")
        print(" 5. Jump Search 🏃")
        print(" 6. Interval Search 📐")

        try:
            choice = int(input("Your pick (1–6): "))
        except ValueError:
            print("That’s not a number. ⚠️ Please choose between 1 and 6.")
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
            print("Oops! ❗ Pick a number from 1 to 6.")
            self.menu()
# endregion



def main():
    modules = [
        Conversion,
        Searching,
        SetTheory,
        Sorting,
        GCD_LCM,
        Ciphers,
        Prime,
    ]

    while True:
        clear_screen()
        print("🌟 Welcome to Melrich Catipay's Algorithm Adventure 🌟")
        print("\n🧭 Choose a module to explore:")
        for index, mod in enumerate(modules, start=1):
            print(f" {index}. {mod.__name__}")
        print(" 0. 🚪 Exit")

        try:
            selection = int(input("\nEnter your choice (0 to exit): "))
        except ValueError:
            print("\n⚠️ Oops, that input wasn't a number. Give it another try!")
            sleep(1.2)
            continue

        if selection == 0:
            print("\n👋 Thanks for joining the exploration! Farewell!")
            break

        if 1 <= selection <= len(modules):
            while True:
                clear_screen()
                chosen = modules[selection - 1]
                print(f"▶️ Now running: {chosen.__name__}\n")
                chosen()  # Instantiate and run
                again = input("\n🔁 Run this module again? (y/N): ")
                if again.strip().lower() != 'y':
                    break
        else:
            print("\n❗ Invalid selection—please pick a valid option!")
            sleep(1.2)

if __name__ == "__main__":
    main()
# endregion