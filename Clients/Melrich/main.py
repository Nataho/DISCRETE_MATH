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

# region set theory
class SetTheory:
    """Handles user interaction and operations related to basic set theory."""

    def __init__(self):
        self.set_a = set()
        self.set_b = set()
        clear_screen()
        print("🔬 Entering Set Theory Explorer!")
        sleep(1)
        self.run()

    def run(self):
        self.display_welcome()
        self.get_sets()
        self.display_sets()
        self.compute_results()

    def display_welcome(self):
        print("🙌 Welcome! Ready to play with sets?")

    def get_sets(self):
        self.set_a = self.input_set("A")
        self.set_b = self.input_set("B")

    def input_set(self, label):
        raw = input(f"📝 Please provide elements for set {label}, separated by spaces: ")
        return set(raw.strip().split())

    def display_sets(self):
        print("\n📂 You’ve defined the following sets:")
        print(f"• Set A = {self.set_a}")
        print(f"• Set B = {self.set_b}")

    def compute_results(self):
        print("\n🔢 Let’s calculate set operations now...\n")
        sleep(1)

        operations = [
            ("Union", self._union),
            ("Intersection", self._intersection),
            ("Difference (A − B)", self._difference),
            ("Subset Check", self._subset_check),
            ("Equality Check", self._equality_check),
        ]
        random.shuffle(operations)

        for label, func in operations:
            print(f"=== ➕ {label} ===")
            func()
            print()
            
    def _union(self):
        result = self.set_a.copy()
        for item in self.set_b:
            if item not in result:
                print(f"🌟 Including {item} in the union")
                result.add(item)
            else:
                print(f"🔄 {item} is already present")
        print(f"🧮 Union outcome: {result}")

    def _intersection(self):
        result = set()
        for item in self.set_a:
            if item in self.set_b:
                print(f"🤝 {item} appears in both sets")
                result.add(item)
            else:
                print(f"🚧 {item} exists only in A")
        print(f"🧮 Intersection outcome: {result}")

    def _difference(self):
        result = set()
        for item in self.set_a:
            if item not in self.set_b:
                print(f"🛡️ Keeping {item} (not in B)")
                result.add(item)
            else:
                print(f"🗑️ Discarding {item} (found in B)")
        print(f"🧮 A minus B = {result}")

    def _subset_check(self):
        print("🔍 Let’s see if A is contained within B...")
        for item in self.set_a:
            if item not in self.set_b:
                print(f"🚫 {item} isn't in B — not a subset")
                print("✅ Conclusion: A ⊈ B")
                return
            else:
                print(f"✅ {item} is inside B")
        print("✅ Conclusion: Yes, A ⊆ B")

    def _equality_check(self):
        print("⚖️ Comparing A and B for equality...")
        all_items = self.set_a.union(self.set_b)
        same = True
        for item in all_items:
            in_a = item in self.set_a
            in_b = item in self.set_b
            emoji = "✅" if in_a and in_b else "❌"
            print(f"{emoji} {item} → A: {in_a}, B: {in_b}")
            if in_a != in_b:
                same = False
        print(f"🧮 Equality check result: {'A == B' if same else 'A != B'}")
# endregion set theory #######


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
            choice = int(input("Your pick (enter number): "))
            modes[choice - 1][1]()
        except (ValueError, IndexError):
            print("⚠️ Invalid choice — please try again.")
            self.mode_menu()

    def run_menu_encrypt(self):
        print("\n🧩 Select a cipher to Encrypt with:")
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
            choice = int(input("Enter number for your cipher: "))
            options[choice - 1][1]()
        except (ValueError, IndexError):
            print("⚠️ That wasn't a valid option. Try again.")

    def run_menu_decrypt(self):
        print("\n🧩 Select a cipher to Decrypt with:")
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
            choice = int(input("Enter number for decryption: "))
            options[choice - 1][1]()
        except (ValueError, IndexError):
            print("⚠️ That wasn't valid. Please try again.")

    # Caesar Encrypt and Decrypt
    def caesar_encrypt(self):
        text = input("Enter your message to encrypt: ")
        shift = int(input("Shift amount (1–25): "))
        encrypted = ""
        print("\n[🔒 Encrypting]")
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                shifted = chr((ord(char) - base + shift) % 26 + base)
                print(f"{char} → {shifted}")
                encrypted += shifted
            else:
                encrypted += char
        print(f"\nEncrypted Result → {encrypted}")

    def caesar_decrypt(self):
        text = input("Enter the encrypted text: ")
        shift = int(input("Shift amount used (1–25): "))
        decrypted = ""
        print("\n[🔓 Decrypting]")
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                shifted = chr((ord(char) - base - shift) % 26 + base)
                print(f"{char} → {shifted}")
                decrypted += shifted
            else:
                decrypted += char
        print(f"\nDecrypted Result → {decrypted}")

    # Vigenère Encrypt and Decrypt
    def vigenere_encrypt(self):
        text = input("Message to encrypt: ")
        key = input("Keyword: ")
        key_extended = (key * ((len(text) // len(key)) + 1))[:len(text)]
        result = ""
        print("\n[🔒 Encrypting]")
        for i, char in enumerate(text):
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                key_char = key_extended[i].upper() if char.isupper() else key_extended[i].lower()
                shift = ord(key_char) - base
                encrypted = chr((ord(char) - base + shift) % 26 + base)
                print(f"{char} + {key_char} → {encrypted}")
                result += encrypted
            else:
                result += char
        print(f"\nEncrypted Result → {result}")

    def vigenere_decrypt(self):
        text = input("Encrypted text to decrypt: ")
        key = input("Keyword used: ")
        key_extended = (key * ((len(text) // len(key)) + 1))[:len(text)]
        result = ""
        print("\n[🔓 Decrypting]")
        for i, char in enumerate(text):
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                key_char = key_extended[i].upper() if char.isupper() else key_extended[i].lower()
                shift = ord(key_char) - base
                decrypted = chr((ord(char) - base - shift) % 26 + base)
                print(f"{char} - {key_char} → {decrypted}")
                result += decrypted
            else:
                result += char
        print(f"\nDecrypted Result → {result}")

    # Playfair Encrypt and Decrypt
    def playfair_encrypt(self):
        text = input("Enter message to encrypt: ")
        keyword = input("Keyword for matrix: ")
        matrix = self._generate_playfair_matrix(keyword)
        prepared = self._prepare_playfair_text(text)
        encrypted = ""
        print("\n[🧩 Matrix]")
        for row in matrix:
            print(" ".join(row))
        print("\n[Encrypting Pairs]")
        for i in range(0, len(prepared), 2):
            pair = prepared[i], prepared[i + 1]
            cipher_pair = self._playfair_encrypt_pair(matrix, *pair)
            print(f"{pair[0]}{pair[1]} → {cipher_pair}")
            encrypted += cipher_pair
        print(f"\nEncrypted Text → {encrypted}")

    def playfair_decrypt(self):
        text = input("Enter ciphertext to decrypt: ")
        keyword = input("Keyword for matrix: ")
        matrix = self._generate_playfair_matrix(keyword)
        decrypted = ""
        print("\n[🧩 Matrix]")
        for row in matrix:
            print(" ".join(row))
        print("\n[Decrypting Pairs]")
        for i in range(0, len(text), 2):
            pair = text[i], text[i + 1]
            plain_pair = self._playfair_decrypt_pair(matrix, *pair)
            print(f"{pair[0]}{pair[1]} → {plain_pair}")
            decrypted += plain_pair
        print(f"\nDecrypted Text → {decrypted}")

    # Vernam encrypt/decrypt
    def vernam_encrypt(self):
        text = input("Plaintext input: ")
        key = input("Key (same length): ")
        key = (key * ((len(text) // len(key)) + 1))[:len(text)]
        print("\n[🔒 Encrypting]")
        for c, k in zip(text, key):
            print(f"{c} ⊕ {k} = {chr(ord(c) ^ ord(k))}")
        result = "".join(chr(ord(c) ^ ord(k)) for c, k in zip(text, key))
        print(f"\nEncrypted → {result}")
        print(f"(Hex) → {result.encode().hex()}")

    def vernam_decrypt(self):
        text = input("Ciphertext input: ")
        key = input("Key used (same length): ")
        key = (key * ((len(text) // len(key)) + 1))[:len(text)]
        print("\n[🔓 Decrypting]")
        for c, k in zip(text, key):
            print(f"{c} ⊕ {k} = {chr(ord(c) ^ ord(k))}")
        result = "".join(chr(ord(c) ^ ord(k)) for c, k in zip(text, key))
        print(f"\nDecrypted → {result}")
        print(f"(Hex) → {result.encode().hex()}")

    # One-Time Pad encrypt/decrypt (same operation)
    def one_time_pad_encrypt(self):
        text = input("Enter your message: ")
        key = os.urandom(len(text))
        encrypted = bytes([ord(c) ^ k for c, k in zip(text, key)])
        print("\n[🔒 Encrypting via One-Time Pad]")
        for c, k in zip(text, key):
            print(f"{c} ⊕ {k} = {ord(c) ^ k}")
        print(f"🔑 Generated key (hex): {key.hex()}")
        print(f"🔐 Encrypted output (hex): {encrypted.hex()}")

    def one_time_pad_decrypt(self):
        encrypted_hex = input("Paste encrypted message (hex): ")
        key_hex = input("Paste key used (hex): ")
        try:
            encrypted = bytes.fromhex(encrypted_hex)
            key = bytes.fromhex(key_hex)
        except Exception:
            print("⚠️ Invalid hex input—please try again.")
            return
        decrypted = "".join(chr(e ^ k) for e, k in zip(encrypted, key))
        print("\n[🔓 Decrypting via One-Time Pad]")
        for e, k in zip(encrypted, key):
            print(f"{e} ⊕ {k} = {e ^ k}")
        print(f"\n📨 Decrypted message → {decrypted}")

    # Hill cipher encrypt/decrypt
    def hill_encrypt(self):
        text = input("Enter text to encrypt: ")
        key_input = input("Enter 3×3 key matrix (9 numbers space-separated): ")
        try:
            values = list(map(int, key_input.split()))
            if len(values) != 9:
                print("⚠️ Expected exactly 9 numbers.")
                return
            matrix = [values[i:i+3] for i in range(0, 9, 3)]
        except:
            print("⚠️ Invalid matrix input—please enter 9 integers.")
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
        print("\n🧮 Key matrix used:")
        for row in matrix:
            print(row)
        print(f"\n🔐 Hill Cipher Encrypted result → {result}")

    def hill_decrypt(self):
        text = input("Enter encrypted text: ")
        key_input = input("Enter 3×3 key matrix (9 numbers space-separated): ")
        try:
            values = list(map(int, key_input.split()))
            if len(values) != 9:
                print("⚠️ Expected exactly 9 numbers.")
                return
            matrix = [values[i:i+3] for i in range(0, 9, 3)]
        except:
            print("⚠️ Invalid matrix input—please enter 9 integers.")
            return

        inv_matrix = self._hill_matrix_inverse(matrix)
        if inv_matrix is None:
            print("⚠️ Matrix not invertible mod 26—cannot decrypt.")
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
        print("\n🧮 Inverse matrix used:")
        for row in inv_matrix:
            print(row)
        print(f"\n📨 Hill Cipher Decrypted result → {result}")

    def _hill_matrix_inverse(self, matrix):
        # Calculate determinant mod 26
        def det3(m):
            return (m[0][0]*m[1][1]*m[2][2] + m[0][1]*m[1][2]*m[2][0] + m[0][2]*m[1][0]*m[2][1]
                    - m[0][2]*m[1][1]*m[2][0] - m[0][1]*m[1][0]*m[2][2] - m[0][0]*m[1][2]*m[2][1]) % 26
        det = det3(matrix)
        det_inv = self._modular_inverse(det, 26)
        if det_inv is None:
            return None
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
        adj = [[cof[j][i] % 26 for j in range(3)] for i in range(3)]
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
        text = input("🚂 Plaintext message: ")
        if any(c.isdigit() for c in text):
            print("⚠️ Digits are not allowed in this cipher.")
            return
        try:
            rails = int(input("Specify number of rails (2–10): "))
            if rails < 2 or rails > 10:
                raise ValueError
        except:
            print("⚠️ Invalid rails—please enter 2 to 10.")
            return

        fence = [''] * rails
        rail, direction = 0, 1
        print("\n[🔒 Encrypting Zigzag]")
        for char in text:
            print(f"{char} → rail {rail}")
            fence[rail] += char
            rail += direction
            if rail == 0 or rail == rails - 1:
                direction *= -1
        encrypted = ''.join(fence)
        print(f"\n🔐 Encrypted text → {encrypted}")

    def rail_fence_decrypt(self):
        ciphertext = input("🚂 Ciphertext: ")
        try:
            rails = int(input("Rails used (2–10): "))
            if rails < 2 or rails > 10:
                raise ValueError
        except:
            print("⚠️ Invalid rails—please enter 2 to 10.")
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
        print("\n[🗺️ Marking positions]")
        for r in range(rails):
            for c in range(n):
                if fence[r][c] == '*' and index < n:
                    fence[r][c] = ciphertext[index]
                    print(f"Placing {ciphertext[index]} at rail {r}, pos {c}")
                    index += 1

        result = []
        rail, direction = 0, 1
        print("\n[🔓 Reading zigzag]")
        for i in range(n):
            result.append(fence[rail][i])
            print(f"rail {rail}, pos {i} → {fence[rail][i]}")
            rail += direction
            if rail == 0 or rail == rails - 1:
                direction *= -1
        decrypted = ''.join(result)
        print(f"\n📨 Decrypted text → {decrypted}")

    # Columnar encrypt/decrypt
    def columnar_encrypt(self):
        text = input("📋 Plaintext (spaces removed automatically): ").replace(" ", "")
        key = input("🔑 Keyword: ").lower()
        n = len(key)
        matrix = [list(text[i:i+n]) for i in range(0, len(text), n)]
        while len(matrix[-1]) < n:
            matrix[-1].append('x')
        print("\n[🧩 Matrix layout]")
        for row in matrix:
            print("".join(row))

        sorted_key = sorted(list(set(key)))
        order = [sorted_key.index(k) for k in key]
        print(f"Column order based on key: {order}")

        result = ""
        for col_num in sorted(order):
            col_idx = order.index(col_num)
            col_text = "".join(matrix[row][col_idx] for row in range(len(matrix)))
            print(f"Column {col_idx} ('{key[col_idx]}') → {col_text}")
            result += col_text
        print(f"\n✅ Encrypted → {result}")

    def columnar_decrypt(self):
        ciphertext = input("🔐 Ciphertext: ")
        key = input("🔑 Keyword used: ").lower()
        n = len(key)
        num_rows = len(ciphertext) // n
        sorted_key = sorted(list(set(key)))
        order = [sorted_key.index(k) for k in key]

        cols = {}
        start = 0
        print("\n[📦 Extracting columns]")
        for col_num in sorted(order):
            length = num_rows
            cols[col_num] = ciphertext[start:start+length]
            print(f"Column {col_num} → {cols[col_num]}")
            start += length

        matrix = [[""]*n for _ in range(num_rows)]
        for col_idx, col_num in enumerate(order):
            col_text = cols[col_num]
            for row in range(num_rows):
                matrix[row][col_idx] = col_text[row]

        print("\n[🧱 Reconstructed matrix]")
        for row in matrix:
            print("".join(row))

        result = "".join(matrix[row][col] for row in range(num_rows) for col in range(n))
        print(f"\n📨 Decrypted → {result}")
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
    """A tool to explore different search algorithms interactively."""

    def __init__(self):
        clear_screen()
        print("🌟 Hey! Welcome to the Search Algorithm Playground!")
        sleep(1)
        self.menu()

    def menu(self):
        print("\nReady to explore? Pick a search method:")
        print(" 1. Interpolation Search 🌍")
        print(" 2. Linear Search 🧭")
        print(" 3. Binary Search 🧠")
        print(" 4. Ternary Search ⚛️")
        print(" 5. Jump Search 🚀")
        print(" 6. Interval Search 📏")

        try:
            choice = int(input("Enter your choice (1–6): "))
        except ValueError:
            print("⚠️ That wasn’t a number from 1 to 6. Let’s try again!")
            return self.menu()

        {
            1: self.interpolation_search,
            2: self.linear_search,
            3: self.binary_search,
            4: self.ternary_search,
            5: self.jump_search,
            6: self.interval_search,
        }.get(choice, lambda: (print("⚠️ Hm, that option’s not in the list—try again!"), self.menu()))()

    def get_array_and_target(self, sort_array=False):
        try:
            values = list(map(int, input("\nType a series of numbers (space-separated): ").split()))
            if sort_array:
                values.sort()
                print(f"📈 Sorted array is: {values}")
            target = int(input("🔎 What number would you like to find? "))
            return values, target
        except ValueError:
            print("⚠️ Whoops! Please enter valid integers.")
            return self.get_array_and_target(sort_array)

    def linear_search(self):
        arr, target = self.get_array_and_target()
        print("\n🔍 Launching linear search…\n")
        sleep(0.5)
        for idx, val in enumerate(arr):
            print(f"Checking index {idx}: {val}")
            if val == target:
                print(f"🎉 Found {target} at index {idx}!")
                return
            print("…not here, moving on.")
        print(f"❌ {target} isn’t in the list.")

    def binary_search(self):
        arr, target = self.get_array_and_target(sort_array=True)
        print("\n🔍 Starting binary search…\n")
        sleep(0.5)
        left, right = 0, len(arr) - 1
        step = 1
        while left <= right:
            mid = (left + right) // 2
            print(f"Step {step}: left={left}, mid={mid}, right={right} | value={arr[mid]}")
            step += 1
            if arr[mid] == target:
                print(f"🎯 {target} found at index {mid}!")
                return
            if arr[mid] < target:
                print("Going right half.")
                left = mid + 1
            else:
                print("Going left half.")
                right = mid - 1
        print(f"❌ {target} not found.")

    def interpolation_search(self):
        arr, target = self.get_array_and_target(sort_array=True)
        print("\n🔍 Running interpolation search…\n")
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
            print(f"Step {step}: low={low}, pos={pos}, high={high} | value={arr[pos]}")
            step += 1
            if arr[pos] == target:
                print(f"🎯 {target} at index {pos}—nailed it!")
                return
            if arr[pos] < target:
                print("Target's higher—going right.")
                low = pos + 1
            else:
                print("Target's lower—going left.")
                high = pos - 1
        print(f"❌ {target} wasn't found.")

    def ternary_search(self):
        arr, target = self.get_array_and_target(sort_array=True)
        print("\n🔍 Kicking off ternary search…\n")
        sleep(0.5)
        left, right = 0, len(arr) - 1
        step = 1
        while left <= right:
            mid1 = left + (right - left)//3
            mid2 = right - (right - left)//3
            print(f"Step {step}: left={left}, mid1={mid1}, mid2={mid2}, right={right}")
            step += 1
            if arr[mid1] == target:
                print(f"🎉 Found at mid1 (index {mid1})!")
                return
            if arr[mid2] == target:
                print(f"🎉 Found at mid2 (index {mid2})!")
                return
            if target < arr[mid1]:
                print("Searching left third.")
                right = mid1 - 1
            elif target > arr[mid2]:
                print("Searching right third.")
                left = mid2 + 1
            else:
                print("Searching middle third.")
                left = mid1 + 1
                right = mid2 - 1
        print(f"❌ Didn’t find {target}.")

    def jump_search(self):
        arr, target = self.get_array_and_target(sort_array=True)
        print("\n🔍 Starting jump search…\n")
        sleep(0.5)
        import math
        n = len(arr)
        step_size = int(math.sqrt(n))
        prev, step = 0, 1
        while prev < n and arr[min(prev+step_size, n)-1] < target:
            print(f"Step {step}: jumping to index {min(prev+step_size,n)-1}")
            prev += step_size
            step += 1
        print(f"🔎 Linear scan from index {prev}…")
        for idx in range(prev, min(prev+step_size, n)):
            print(f"Index {idx}: {arr[idx]}")
            if arr[idx] == target:
                print(f"🎉 Found {target} at {idx}!")
                return
        print(f"❌ {target} not found.")

    def interval_search(self):
        arr, target = self.get_array_and_target(sort_array=False)
        print("\n🔍 Launching interval search…\n")
        sleep(0.5)
        left, right, step = 0, len(arr)-1, 1
        while left <= right:
            print(f"Step {step}: window {left}–{right}")
            mini, maxi = min(arr[left:right+1]), max(arr[left:right+1])
            print(f"Slice min={mini}, max={maxi}")
            if target < mini or target > maxi:
                print("Outside window—shrinking.")
                left += 1
                right -= 1
            else:
                for idx in range(left, right+1):
                    print(f"Scanning idx {idx}: {arr[idx]}")
                    if arr[idx] == target:
                        print(f"🎉 Found {target} at {idx}!")
                        return
                break
            step += 1
        print(f"❌ {target} missing from list.")
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