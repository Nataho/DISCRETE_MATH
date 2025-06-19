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
    """An interactive console for sorting algorithms with style."""

    def __init__(self):
        clear_screen()
        print("🔧 Booting up the Sorting Suite...")
        sleep(1)
        self.start()

    def start(self):
        methods = [
            ("⚡ Quick Sort", self.quick_sort),
            ("🌲 Tree Sort", self.tree_sort),
            ("📝 Insertion Sort", self.insertion_sort),
            ("🔗 Merge Sort", self.merge_sort),
            ("🫧 Bubble Sort", self.bubble_sort),
            ("🪣 Bucket Sort", self.bucket_sort),
            ("🧹 Comb Sort", self.comb_sort),
            ("🛠️ Shell Sort", self.shell_sort),
            ("📊 Radix Sort", self.radix_sort),
            ("🎯 Selection Sort", self.selection_sort),
        ]

        while True:
            clear_screen()
            print("\n📦 Choose your sorting strategy:")
            for idx, (name, _) in enumerate(methods, 1):
                print(f" {idx}. {name}")
            print(" 0. 🔙 Back to Main Menu")

            try:
                choice = int(input("\n🎮 Your move: "))
                if choice == 0:
                    return
                _, func = methods[choice - 1]
                func()
                input("\n🕹️ Press Enter to return to menu...")
            except (ValueError, IndexError):
                print("⚠️ That’s not a valid selection. Try again!")
                sleep(1.5)

    def bubble_sort(self):
        arr = self._get_input()
        print("\n🫧 Starting Bubble Sort... brace yourself!")
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    print(f"🔁 Swap: {arr}")
                    sleep(0.01)
        print(f"\n🎉 Final Result: {arr}")

    def selection_sort(self):
        arr = self._get_input()
        print("\n🎯 Starting Selection Sort...")
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            print(f"🔢 Step {i+1}: {arr}")
            sleep(0.01)
        print(f"\n✅ Sorted: {arr}")

    def insertion_sort(self):
        arr = self._get_input()
        print("\n📝 Deploying Insertion Sort...")
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
            print(f"📥 Inserted {key} ➝ {arr}")
            sleep(0.01)
        print(f"\n✔️ Done: {arr}")

    def merge_sort(self):
        arr = self._get_input()
        print("\n🔗 Merging begins...")
        self._merge_sort(arr)
        print(f"\n🥂 Sorted Output: {arr}")

    def _merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]
            print(f"🪓 Split ➡️ {L} | {R}")
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
            print(f"🧬 Merged 🔄 {arr}")
            sleep(0.05)

    def quick_sort(self):
        arr = self._get_input()
        print("\n✂️ Slicing with Quick Sort...")
        self._quick_sort(arr, 0, len(arr) - 1)
        print(f"\n🏁 Final Sort: {arr}")

    def _quick_sort(self, arr, low, high):
        if low < high:
            pi = self._partition(arr, low, high)
            self._quick_sort(arr, low, pi - 1)
            self._quick_sort(arr, pi + 1, high)

    def _partition(self, arr, low, high):
        pivot = arr[high]
        print(f"🎯 Pivot: {pivot}")
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                print(f"🔁 Swap: {arr}")
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def bucket_sort(self):
        arr = self._get_input()
        if not arr:
            print("⚠️ Nothing to sort!")
            return
        print("\n🪣 Bucketing numbers...")
        bucket_count = 10
        max_val, min_val = max(arr), min(arr)
        buckets = [[] for _ in range(bucket_count)]
        for num in arr:
            idx = int((num - min_val) / (max_val - min_val + 1) * (bucket_count - 1))
            buckets[idx].append(num)
        for i, b in enumerate(buckets):
            b.sort()
            print(f"📂 Bucket {i}: {b}")
        sorted_arr = [num for b in buckets for num in b]
        print(f"\n🎊 All Sorted: {sorted_arr}")

    def shell_sort(self):
        arr = self._get_input()
        print("\n🛠️ Running Shell Sort...")
        gap = len(arr) // 2
        while gap > 0:
            for i in range(gap, len(arr)):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            print(f"🔧 Gap {gap} ➝ {arr}")
            gap //= 2
        print(f"\n📦 Final Form: {arr}")

    def comb_sort(self):
        arr = self._get_input()
        print("\n🧼 Scrubbing with Comb Sort...")
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
                    print(f"🧽 Swap: {arr}")
        print(f"\n✨ Cleaned Up: {arr}")

    def radix_sort(self):
        arr = self._get_input()
        print("\n📊 Launching Radix Sort...")
        max_val = max(arr)
        exp = 1
        while max_val // exp > 0:
            self._counting_sort(arr, exp)
            print(f"🔁 Exp={exp}: {arr}")
            exp *= 10
        print(f"\n🏆 Fully Sorted: {arr}")

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
        print("\n🌲 Tree Sort module coming soon... Stay tuned!")

    def _get_input(self):
        try:
            return list(map(int, input("\n🔢 Enter numbers (space-separated): ").split()))
        except ValueError:
            print("🚫 Invalid input. Integers only!")
            return self._get_input()
#endregion sorting

#region ciphers
class Ciphers: 
    """🔐 Encrypts and decrypts text using various classical ciphers with flair."""

    def __init__(self):
        clear_screen()
        print("🧠 Cipher Station Activated!")
        sleep(1)
        self.mode_menu()

    def mode_menu(self):
        print("\n🧭 Choose Mode:")
        modes = [
            ("🔒 Encrypt", self.run_menu_encrypt),
            ("🔓 Decrypt", self.run_menu_decrypt)
        ]
        random.shuffle(modes)
        for i, (label, _) in enumerate(modes, start=1):
            print(f" {i}. {label}")
        try:
            choice = int(input("🎮 Your pick (number): "))
            modes[choice - 1][1]()
        except (ValueError, IndexError):
            print("⚠️ Invalid choice. Try again!")
            self.mode_menu()

    def run_menu_encrypt(self):
        print("\n🔐 Select a cipher to encrypt with:")
        options = [
            ("🚆 Rail Fence Cipher", self.rail_fence_encrypt),
            ("🔳 Playfair Cipher", self.playfair_encrypt),
            ("📐 Hill Cipher", self.hill_encrypt),
            ("🏛️ Columnar Cipher", self.columnar_encrypt),
            ("🏰 Caesar Cipher", self.caesar_encrypt),
            ("🧢 Vernam Cipher", self.vernam_encrypt),
            ("📜 Vigenère Cipher", self.vigenere_encrypt),
            ("🎲 One-Time Pad Cipher", self.one_time_pad_encrypt)
        ]
        random.shuffle(options)
        for i, (label, _) in enumerate(options, start=1):
            print(f" {i}. {label}")
        try:
            choice = int(input("📌 Your pick (number): "))
            options[choice - 1][1]()
        except (ValueError, IndexError):
            print("⚠️ Invalid choice. Try again!")

    def run_menu_decrypt(self):
        print("\n🔓 Select a cipher to decrypt with:")
        options = [
            ("🚆 Rail Fence Cipher", self.rail_fence_decrypt),
            ("🔳 Playfair Cipher", self.playfair_decrypt),
            ("📐 Hill Cipher", self.hill_decrypt),
            ("🏛️ Columnar Cipher", self.columnar_decrypt),
            ("🏰 Caesar Cipher", self.caesar_decrypt),
            ("🧢 Vernam Cipher", self.vernam_decrypt),
            ("📜 Vigenère Cipher", self.vigenere_decrypt),
            ("🎲 One-Time Pad Cipher", self.one_time_pad_decrypt)
        ]
        random.shuffle(options)
        for i, (label, _) in enumerate(options, start=1):
            print(f" {i}. {label}")
        try:
            choice = int(input("📌 Your pick (number): "))
            options[choice - 1][1]()
        except (ValueError, IndexError):
            print("⚠️ Invalid choice. Try again!")

    # Caesar Encrypt and Decrypt
    def caesar_encrypt(self):
        text = input("📝 Type your message: ")
        shift = int(input("🔁 Shift positions (1–25): "))
        encrypted = ""
        print("\n🔧 [Encrypting...]")
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                shifted = chr((ord(char) - base + shift) % 26 + base)
                print(f"{char} ➡️ {shifted}")
                encrypted += shifted
            else:
                encrypted += char
        print(f"\n✅ Encrypted → {encrypted}")

    def caesar_decrypt(self):
        text = input("🔐 Type encrypted message: ")
        shift = int(input("🔁 Shift positions used (1–25): "))
        decrypted = ""
        print("\n🔓 Decrypting...")
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                shifted = chr((ord(char) - base - shift) % 26 + base)
                print(f"{char} 🔽 {shifted}")
                decrypted += shifted
            else:
                decrypted += char
        print(f"\n✅ Decrypted → {decrypted}")

    def vigenere_encrypt(self):
        text = input("📝 Enter the text: ")
        key = input("🔑 Enter the keyword: ")
        key_extended = (key * ((len(text) // len(key)) + 1))[:len(text)]
        result = ""
        print("\n🔐 Encrypting...")
        for i, char in enumerate(text):
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                key_char = key_extended[i].upper() if char.isupper() else key_extended[i].lower()
                shift = ord(key_char) - base
                encrypted = chr((ord(char) - base + shift) % 26 + base)
                print(f"{char} ➕ {key_char} → {encrypted}")
                result += encrypted
            else:
                result += char
        print(f"\n✅ Encrypted → {result}")

    def vigenere_decrypt(self):
        text = input("🔐 Enter encrypted text: ")
        key = input("🔑 Enter keyword used: ")
        key_extended = (key * ((len(text) // len(key)) + 1))[:len(text)]
        result = ""
        print("\n🔓 Decrypting...")
        for i, char in enumerate(text):
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                key_char = key_extended[i].upper() if char.isupper() else key_extended[i].lower()
                shift = ord(key_char) - base
                decrypted = chr((ord(char) - base - shift) % 26 + base)
                print(f"{char} ➖ {key_char} → {decrypted}")
                result += decrypted
            else:
                result += char
        print(f"\n✅ Decrypted → {result}")

    def playfair_encrypt(self):
        text = input("📝 Message to encrypt: ")
        keyword = input("🔑 Keyword to construct matrix: ")
        matrix = self._generate_playfair_matrix(keyword)
        prepared = self._prepare_playfair_text(text)
        encrypted = ""
        print("\n🧮 Matrix:")
        for row in matrix:
            print(" ".join(row))
        print("\n🔗 Pairs:")
        for i in range(0, len(prepared), 2):
            pair = prepared[i], prepared[i + 1]
            cipher_pair = self._playfair_encrypt_pair(matrix, *pair)
            print(f"{pair[0]}{pair[1]} → {cipher_pair}")
            encrypted += cipher_pair
        print(f"\n🔐 Ciphertext → {encrypted}")

    def playfair_decrypt(self):
        text = input("🔐 Ciphertext to decrypt: ")
        keyword = input("🔑 Keyword to reconstruct matrix: ")
        matrix = self._generate_playfair_matrix(keyword)
        decrypted = ""
        print("\n🧮 Matrix:")
        for row in matrix:
            print(" ".join(row))
        print("\n🔓 Pairs:")
        for i in range(0, len(text), 2):
            pair = text[i], text[i + 1]
            plain_pair = self._playfair_decrypt_pair(matrix, *pair)
            print(f"{pair[0]}{pair[1]} → {plain_pair}")
            decrypted += plain_pair
        print(f"\n✅ Decrypted Text → {decrypted}")

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
        text = input("📝 Input text: ")
        key = input("🔑 Key (same length as text): ")
        key = (key * ((len(text) // len(key)) + 1))[:len(text)]
        print("\n🔐 [Encrypting with Vernam Cipher]")
        for c, k in zip(text, key):
            print(f"{c} ^ {k} = {chr(ord(c) ^ ord(k))}")
        result = "".join(chr(ord(c) ^ ord(k)) for c, k in zip(text, key))
        print(f"\n🔒 Encrypted → {result}")
        print(f"🧾 As hex: {result.encode().hex()}")

    def vernam_decrypt(self):
        text = input("🧩 Encrypted text: ")
        key = input("🔑 Key used (same length): ")
        key = (key * ((len(text) // len(key)) + 1))[:len(text)]
        print("\n🔓 [Decrypting with Vernam Cipher]")
        for c, k in zip(text, key):
            print(f"{c} ^ {k} = {chr(ord(c) ^ ord(k))}")
        result = "".join(chr(ord(c) ^ ord(k)) for c, k in zip(text, key))
        print(f"\n📜 Decrypted → {result}")
        print(f"🧾 As hex: {result.encode().hex()}")

    # One-Time Pad encrypt/decrypt (same operation)
    def one_time_pad_encrypt(self):
        text = input("💬 Message: ")
        key = os.urandom(len(text))
        encrypted = bytes([ord(c) ^ k for c, k in zip(text, key)])
        print("\n🔐 [Encrypting with One-Time Pad]")
        for c, k in zip(text, key):
            print(f"{c} ^ {k} = {ord(c) ^ k}")
        print(f"🧾 Generated key (hex): {key.hex()}")
        print(f"🔒 Encrypted output (hex): {encrypted.hex()}")

    def one_time_pad_decrypt(self):
        encrypted_hex = input("🧩 Encrypted message (hex): ")
        key_hex = input("🔑 Key used (hex): ")
        try:
            encrypted = bytes.fromhex(encrypted_hex)
            key = bytes.fromhex(key_hex)
        except Exception:
            print("🚫 Invalid hex input.")
            return
        decrypted = "".join(chr(e ^ k) for e, k in zip(encrypted, key))
        print("\n🔓 [Decrypting with One-Time Pad]")
        for e, k in zip(encrypted, key):
            print(f"{e} ^ {k} = {e ^ k}")
        print(f"\n📜 Decrypted message → {decrypted}")

    # Hill cipher encrypt/decrypt
    def hill_encrypt(self):
        text = input("📨 Text to encode: ")
        key_input = input("🔢 3x3 key matrix (space-separated 9 numbers): ")
        try:
            values = list(map(int, key_input.split()))
            if len(values) != 9:
                print("⚠️ Expected 9 numbers.")
                return
            matrix = [values[i:i+3] for i in range(0, 9, 3)]
        except:
            print("🚫 Invalid matrix input.")
            return

        small = [chr(i) for i in range(97, 123)]
        big = [chr(i) for i in range(65, 91)]
        chars = [c for c in text if c.isalpha()]
        while len(chars) % 3 != 0:
            chars.append('x')
        nums = [(small + big).index(c.lower()) % 26 for c in chars]
        print("\n🔐 [Encrypting with Hill Cipher]")
        result = ""
        for i in range(0, len(nums), 3):
            block = nums[i:i+3]
            res = [(sum(matrix[r][c] * block[r] for r in range(3)) % 26) for c in range(3)]
            for j, val in enumerate(res):
                orig = chars[i + j]
                print(f"Block: {block} * Col {j} → {val}")
                result += big[val] if orig.isupper() else small[val]
        print("\n🧮 Matrix used:")
        for row in matrix:
            print(row)
        print(f"📜 Hill Cipher Encrypted → {result}")

    def hill_decrypt(self):
        text = input("🧩 Encrypted text: ")
        key_input = input("🔢 3x3 key matrix (space-separated 9 numbers): ")
        try:
            values = list(map(int, key_input.split()))
            if len(values) != 9:
                print("⚠️ Expected 9 numbers.")
                return
            matrix = [values[i:i+3] for i in range(0, 9, 3)]
        except:
            print("🚫 Invalid matrix input.")
            return

        inv_matrix = self._hill_matrix_inverse(matrix)
        if inv_matrix is None:
            print("🚫 Matrix not invertible mod 26. Can't decrypt.")
            return

        small = [chr(i) for i in range(97, 123)]
        big = [chr(i) for i in range(65, 91)]
        chars = [c for c in text if c.isalpha()]
        while len(chars) % 3 != 0:
            chars.append('x')
        nums = [(small + big).index(c.lower()) % 26 for c in chars]
        print("\n🔓 [Decrypting with Hill Cipher]")
        result = ""
        for i in range(0, len(nums), 3):
            block = nums[i:i+3]
            res = [(sum(inv_matrix[r][c] * block[r] for r in range(3)) % 26) for c in range(3)]
            for j, val in enumerate(res):
                orig = chars[i + j]
                print(f"Block: {block} * InvCol {j} → {val}")
                result += big[val] if orig.isupper() else small[val]
        print("\n🧮 Inverse matrix:")
        for row in inv_matrix:
            print(row)
        print(f"📜 Hill Cipher Decrypted → {result}")

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

    def rail_fence_encrypt(self):
        text = input("📨 Message: ")
        if any(c.isdigit() for c in text):
            print("🚫 Digits not allowed.")
            return
        try:
            rails = int(input("🚉 Rails (2–10): "))
            if rails < 2 or rails > 10:
                raise ValueError
        except:
            print("⚠️ Invalid number of rails.")
            return

        fence = [''] * rails
        rail, direction = 0, 1
        print("\n🌀 [Encrypting in Zigzag]")
        for char in text:
            print(f"{char} ➝ Rail {rail}")
            fence[rail] += char
            rail += direction
            if rail == 0 or rail == rails - 1:
                direction *= -1
        encrypted = ''.join(fence)
        print(f"\n🔒 Encrypted → {encrypted}")

    def rail_fence_decrypt(self):
        ciphertext = input("🧩 Ciphertext: ")
        try:
            rails = int(input("🚉 Rails used (2–10): "))
            if rails < 2 or rails > 10:
                raise ValueError
        except:
            print("⚠️ Invalid number of rails.")
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
        print("\n📍 [Marking positions]")
        for r in range(rails):
            for c in range(n):
                if fence[r][c] == '*' and index < n:
                    fence[r][c] = ciphertext[index]
                    print(f"Placing {ciphertext[index]} at rail {r}, pos {c}")
                    index += 1

        result = []
        rail, direction = 0, 1
        print("\n🔄 [Reading Zigzag]")
        for i in range(n):
            result.append(fence[rail][i])
            print(f"Rail {rail}, pos {i} ➝ {fence[rail][i]}")
            rail += direction
            if rail == 0 or rail == rails - 1:
                direction *= -1
        decrypted = ''.join(result)
        print(f"\n📜 Decrypted → {decrypted}")

    def columnar_encrypt(self):
        text = input("💬 Plaintext: ").replace(" ", "")
        key = input("🔑 Keyword: ").lower()
        n = len(key)
        matrix = [list(text[i:i+n]) for i in range(0, len(text), n)]
        while len(matrix[-1]) < n:
            matrix[-1].append('x')
        print("\n🧮 [Matrix Representation]")
        for row in matrix:
            print("".join(row))

        sorted_key = sorted(list(set(key)))
        order = [sorted_key.index(k) for k in key]
        print(f"🔢 Column order: {order}")

        result = ""
        for col_num in sorted(order):
            col_idx = order.index(col_num)
            col_text = "".join(matrix[row][col_idx] for row in range(len(matrix)))
            print(f"Column {col_idx} ({key[col_idx]}) ➝ {col_text}")
            result += col_text
        print(f"\n🔐 Encrypted → {result}")

    def columnar_decrypt(self):
        ciphertext = input("🧩 Ciphertext: ")
        key = input("🔑 Keyword: ").lower()
        n = len(key)
        num_rows = len(ciphertext) // n
        sorted_key = sorted(list(set(key)))
        order = [sorted_key.index(k) for k in key]

        cols = {}
        start = 0
        for col_num in sorted(order):
            length = num_rows
            cols[col_num] = ciphertext[start:start+length]
            start += length
        print("\n📤 [Columns Extracted]")
        for k, v in cols.items():
            print(f"Col {k}: {v}")

        matrix = [[""]*n for _ in range(num_rows)]
        for col_idx, col_num in enumerate(order):
            col_text = cols[col_num]
            for row in range(num_rows):
                matrix[row][col_idx] = col_text[row]

        print("\n📥 [Reconstructed Matrix]")
        for row in matrix:
            print("".join(row))

        result = "".join(matrix[row][col] for row in range(num_rows) for col in range(n))
        print(f"\n📜 Decrypted → {result}")
#endregion ciphers
# 1 by 1 paste please

# region set theory
class SetTheory: 
    """Handles user interaction and operations related to basic set theory."""

    def __init__(self):
        self.set_a = set()
        self.set_b = set()
        clear_screen()
        print("🔧 Activating Set Operations Terminal...")
        sleep(1)
        self.run()

    def run(self):
        self.display_intro()
        self.get_sets()
        self.display_sets()
        self.perform_operations()

    def display_intro(self):
        print("📚 Welcome to the Set Theory Playground")
        print("🧪 Time to discover the magic between two sets!")

    def get_sets(self):
        self.set_a = self.input_set("A")
        self.set_b = self.input_set("B")

    def input_set(self, label):
        raw = input(f"\n📨 Enter elements for Set {label} (space-separated): ")
        cleaned = set(raw.strip().split())
        print(f"🎉 Set {label} saved: {cleaned}")
        return cleaned

    def display_sets(self):
        print("\n📦 Your Sets:")
        print(f"🅰️ Set A → {self.set_a}")
        print(f"🅱️ Set B → {self.set_b}")

    def perform_operations(self):
        print("\n🛠️ Performing set operations...\n")
        sleep(1)

        operations = [
            ("🔗 UNION", self._union),
            ("🎯 INTERSECTION", self._intersection),
            ("➖ DIFFERENCE (A - B)", self._difference),
            ("📎 SUBSET CHECK (A ⊆ B)", self._subset_check),
            ("🧾 EQUALITY CHECK (A == B)", self._equality_check),
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
                print(f"➕ Adding '{item}' to union set")
                result.add(item)
            else:
                print(f"🔄 '{item}' already included")
        print(f"📊 Union Output: {result}")

    def _intersection(self):
        result = set()
        for item in self.set_a:
            if item in self.set_b:
                print(f"🎯 Match found: '{item}'")
                result.add(item)
            else:
                print(f"🚫 '{item}' is unique to A")
        print(f"📊 Intersection Output: {result}")

    def _difference(self):
        result = set()
        for item in self.set_a:
            if item not in self.set_b:
                print(f"➖ Keeping '{item}' (not in B)")
                result.add(item)
            else:
                print(f"❌ Excluding '{item}' (found in B)")
        print(f"📊 Difference (A - B) Output: {result}")

    def _subset_check(self):
        print("🔍 Checking if A is a subset of B...")
        for item in self.set_a:
            if item not in self.set_b:
                print(f"❌ '{item}' is missing in B")
                print("📊 Verdict: A is *not* a subset of B")
                return
            print(f"✅ '{item}' is present in B")
        print("📊 Verdict: Yes, A is a subset of B")

    def _equality_check(self):
        print("🧪 Testing if Set A and B are equal...")
        all_items = self.set_a.union(self.set_b)
        equal = True
        for item in sorted(all_items):
            in_a = item in self.set_a
            in_b = item in self.set_b
            status = "✅" if in_a and in_b else "❌"
            print(f"{status} '{item}' → A: {in_a}, B: {in_b}")
            if in_a != in_b:
                equal = False
        print(f"📊 Equality Result: {'Yes (A = B)' if equal else 'No (A ≠ B)'}")
# endregion set theory
# region conversion

class Conversion: 
    """A flexible number base converter with detailed, step-by-step tracing and emoji-enhanced UI."""

    def __init__(self):
        clear_screen()
        print("🧮 Number Base Conversion Utility Initialized!")
        sleep(1)
        self.start()

    def start(self):
        print("\n🎛️ Pick the type of conversion you'd like to perform:\n")

        options = [
            ("🔢 Decimal → Binary", self.decimal_to_binary),
            ("💡 Binary → Decimal", self.binary_to_decimal),
            ("🔢 Decimal → Octal", self.decimal_to_octal),
            ("🔢 Decimal → Hexadecimal", self.decimal_to_hex),
            ("🧾 Octal → Decimal", self.octal_to_decimal),
            ("🧾 Hexadecimal → Decimal", self.hex_to_decimal),
            ("💡 Binary → Octal", self.binary_to_octal),
            ("💡 Binary → Hexadecimal", self.binary_to_hex),
            ("🧾 Octal → Binary", self.octal_to_binary),
            ("🧾 Octal → Hexadecimal", self.octal_to_hex),
            ("🧾 Hexadecimal → Binary", self.hex_to_binary),
            ("🧾 Hexadecimal → Octal", self.hex_to_octal),
        ]

        random.shuffle(options)

        for i, (label, _) in enumerate(options, 1):
            print(f" {i}. {label}")

        try:
            choice = int(input("\n🔎 Enter your choice (1–12): "))
            if 1 <= choice <= 12:
                options[choice - 1][1]()
            else:
                print("⚠️ Hmm... that option's out of range. Try again.")
        except ValueError:
            print("⚠️ That doesn't look like a number. Please enter digits only.")

    def decimal_to_binary(self):
        num = int(input("🔢 Enter a decimal number: "))
        self._decimal_to_base(num, 2, "Binary")

    def binary_to_decimal(self):
        binary = input("💡 Type a binary number (0s and 1s): ")
        steps = [f"{digit} × 2^{i} = {int(digit)*(2**i)}"
                 for i, digit in enumerate(binary[::-1])]
        print("📘 Step-by-step:\n" + "\n".join(steps))
        print(f"➡️ Decimal: {int(binary, 2)}")

    def decimal_to_octal(self):
        num = int(input("🔢 Enter a decimal number: "))
        self._decimal_to_base(num, 8, "Octal")

    def decimal_to_hex(self):
        num = int(input("🔢 Enter a decimal number: "))
        self._decimal_to_base(num, 16, "Hexadecimal")

    def octal_to_decimal(self):
        octal = input("🧾 Input an octal number (0–7 digits): ")
        steps = [f"{digit} × 8^{i} = {int(digit)*(8**i)}"
                 for i, digit in enumerate(octal[::-1])]
        print("📘 Step-by-step:\n" + "\n".join(steps))
        print(f"➡️ Decimal: {int(octal, 8)}")

    def hex_to_decimal(self):
        hex_str = input("🧾 Input a hexadecimal value (0–9, A–F): ").upper()
        digits = "0123456789ABCDEF"
        steps = [f"{char} × 16^{i} = {digits.index(char)*(16**i)}"
                 for i, char in enumerate(hex_str[::-1])]
        print("📘 Step-by-step:\n" + "\n".join(steps))
        print(f"➡️ Decimal: {int(hex_str, 16)}")

    def binary_to_octal(self):
        binary = input("💡 Enter a binary number: ")
        dec = int(binary, 2)
        print(f"🛠️ Intermediate decimal: {dec}")
        self._decimal_to_base(dec, 8, "Octal")

    def binary_to_hex(self):
        binary = input("💡 Enter a binary number: ")
        dec = int(binary, 2)
        print(f"🛠️ Intermediate decimal: {dec}")
        self._decimal_to_base(dec, 16, "Hexadecimal")

    def octal_to_binary(self):
        octal = input("🧾 Enter an octal number: ")
        dec = int(octal, 8)
        print(f"🛠️ Intermediate decimal: {dec}")
        self._decimal_to_base(dec, 2, "Binary")

    def octal_to_hex(self):
        octal = input("🧾 Enter an octal number: ")
        dec = int(octal, 8)
        print(f"🛠️ Intermediate decimal: {dec}")
        self._decimal_to_base(dec, 16, "Hexadecimal")

    def hex_to_binary(self):
        hex_str = input("🧾 Enter a hexadecimal number: ")
        dec = int(hex_str, 16)
        print(f"🛠️ Intermediate decimal: {dec}")
        self._decimal_to_base(dec, 2, "Binary")

    def hex_to_octal(self):
        hex_str = input("🧾 Enter a hexadecimal number: ")
        dec = int(hex_str, 16)
        print(f"🛠️ Intermediate decimal: {dec}")
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
        print("📘 Conversion Steps:\n" + "\n".join(reversed(steps)))
        if base == 2:
            converted = bin(original)[2:]
        elif base == 8:
            converted = oct(original)[2:]
        else:
            converted = hex(original)[2:].upper()
        print(f"✅ {label}: {converted}")
# endregion conversion

# region GCD & LCM
class GCD_LCM: 
    """Performs GCD and LCM calculations using classic number theory."""

    def __init__(self):
        clear_screen()
        print("⚙️ Launching the GCD & LCM Calculation Center...")
        sleep(1)
        self.start()

    def start(self):
        print("\n🧭 Choose the operation you wish to perform:")
        print(" 1. 🔍 Determine GCD (Greatest Common Divisor)")
        print(" 2. 🔄 Determine LCM (Least Common Multiple)")
        print(" 3. 🚪 Exit to Main Menu")

        choice = input("👉 Enter your selection (1-3): ").strip()

        if choice == '1':
            self.gcd()
        elif choice == '2':
            self.lcm()
        elif choice == '3':
            print("👋 Heading back to the Main Menu...")
            sleep(1)
        else:
            print("❗ Invalid selection. Restarting menu...")
            sleep(1)
            self.start()

    def gcd(self):
        try:
            a = int(input("\n🔢 First number: "))
            b = int(input("🔢 Second number: "))
        except ValueError:
            print("🚫 Please input valid whole numbers only.")
            return

        print(f"\n🔧 Using Euclid's Algorithm to find GCD({a}, {b}):")
        while b != 0:
            print(f"   ➡️ {a} % {b} = {a % b}")
            a, b = b, a % b

        print(f"\n✅ Success! The GCD is {a}")

    def lcm(self):
        try:
            a = int(input("\n🔢 First number: "))
            b = int(input("🔢 Second number: "))
        except ValueError:
            print("🚫 Invalid input. Please enter whole numbers only.")
            return

        original_a, original_b = a, b
        print(f"\n📊 Computing LCM of {a} and {b} via their GCD...")

        # GCD Calculation
        while b != 0:
            a, b = b, a % b
        gcd = a

        # LCM Formula
        lcm = abs(original_a * original_b) // gcd
        print(f"\n📘 Step 1: GCD({original_a}, {original_b}) = {gcd}")
        print(f"📘 Step 2: LCM = |{original_a} × {original_b}| ÷ {gcd} = {lcm}")
        print(f"\n🎉 Finished! The LCM is {lcm}")
# endregion

# region Prime
class Prime: 
    """Prime number toolkit: discovery, factorization, and modular fun."""

    def __init__(self):
        clear_screen()
        print("🧮 Entering the Prime Number Chamber!")
        sleep(1)
        self.start()

    def start(self):
        print("\n🧭 What prime adventure shall we go on?")
        print(" 1. Check if a Number is Prime 🔍")
        print(" 2. Display All Primes in a Range 📈")
        print(" 3. Factor a Number into Primes 🧱")
        print(" 4. Fermat’s Power Mod Calculator 📐")
        print(" 5. Find Primitive Roots 🔑")
        try:
            choice = int(input("\n🎯 Pick an option (1–5): "))
        except ValueError:
            print("🚫 That’s not a number. Try again!")
            return

        match choice:
            case 1: self.check_prime()
            case 2: self.sieve()
            case 3: self.prime_factors()
            case 4: self.fermats()
            case 5: self.primitive_roots()
            case _: print("⚠️ That’s not a valid option. Give it another shot!")

    def check_prime(self):
        try:
            n = int(input("\n🔢 Enter the number to verify: "))
        except ValueError:
            print("🚫 Use whole numbers only.")
            return

        if n < 2:
            print(f"❌ {n} is not a prime number.")
            return

        for i in range(2, int(n ** 0.5) + 1):
            print(f"🔍 Checking if divisible by {i} → {n} % {i} = {n % i}")
            if n % i == 0:
                print(f"❌ {n} is divisible by {i}, so it’s not prime.")
                return

        print(f"✅ Yes! {n} is a prime number!")

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
            n = int(input("\n🔢 Number to factorize: "))
        except ValueError:
            print("⚠️ Please provide a valid whole number.")
            return

        original = n
        factors = []

        print(f"\n🔧 Decomposing {original} into its prime parts:")

        while n % 2 == 0:
            print(f"{n} is even → adding factor: 2")
            factors.append(2)
            n //= 2

        i = 3
        while i * i <= n:
            while n % i == 0:
                print(f"{n} ÷ {i} has no remainder → factor: {i}")
                factors.append(i)
                n //= i
            i += 2

        if n > 2:
            print(f"🟢 Final prime: {n}")
            factors.append(n)

        print(f"\n📦 Prime factor list of {original}: {factors}")

    def sieve(self):
        print("\n🔬 Prime Number Detector (Sieve of Eratosthenes)")
        try:
            start = int(input("🔹 Starting value: "))
            end = int(input("🔸 Ending value: "))
        except ValueError:
            print("⚠️ Use valid numbers.")
            return

        if end <= start:
            print("⚠️ Ending value must be greater than the starting value.")
            return

        print(f"\n🧠 Finding primes between {start} and {end}...")
        primes = [i for i in range(start, end) if self._check_prime(i)]

        print(f"\n📃 List of primes in [{start}, {end}):")
        print(primes)

    def fermats(self):
        print("\n📊 Fermat's Exponentiation Mod Tool")
        try:
            a = int(input("🔸 Base (a): "))
            k = int(input("🔺 Exponent (k): "))
            p = int(input("🔻 Modulus (p, must be prime): "))
        except ValueError:
            print("🚫 All values must be integers.")
            return

        if not self._check_prime(p):
            print("❌ The modulus must be a prime number.")
            return

        result = pow(a, k, p)
        print(f"\n📈 Result: {a}^{k} mod {p} = {result}")

    def primitive_roots(self):
        print("\n🔑 Primitive Root Finder")
        try:
            p = int(input("🔹 Enter a prime number (p): "))
            a = int(input("🔸 Value to test (a): "))
        except ValueError:
            print("⚠️ Both inputs must be positive integers.")
            return

        if p <= 0 or a <= 0:
            print("⚠️ Values must be greater than zero.")
            return

        if not self._check_prime(p):
            print("❌ The number p must be a prime.")
            return

        required = set(range(1, p))
        actual = set(pow(a, k, p) for k in range(1, p))

        if actual == required:
            print(f"🎉 Success! {a} is a primitive root modulo {p}.")
        else:
            print(f"❌ {a} is not a primitive root modulo {p}.")

        print(f"\n🔍 Scanning all primitive roots of {p}...")
        roots = []
        for g in range(2, p):
            if set(pow(g, k, p) for k in range(1, p)) == required:
                roots.append(g)

        print(f"🌟 Primitive roots: {roots}")

# endregion

# region Searching
class Searching: 
    """An interactive explorer of popular search algorithms."""

    def __init__(self):
        clear_screen()
        print("🕵️‍♂️ Step into the Search Explorer!")
        sleep(1)
        self.menu()

    def menu(self):
        print("\n🔍 Which search path shall we take today?")
        print(" 1. 🧮 Interpolation Search")
        print(" 2. 📏 Linear Search")
        print(" 3. 🧠 Binary Search")

        try:
            choice = int(input("🎯 Enter option (1–3): "))
        except ValueError:
            print("🚫 Only numbers from 1 to 3 are allowed. Try again!")
            return self.menu()

        if choice == 2:
            self.linear_search()
        elif choice == 3:
            self.binary_search()
        elif choice == 1:
            self.interpolation_search()
        else:
            print("❗ That’s not one of the choices. Let’s try again.")
            self.menu()

    def get_array_and_target(self, sort_array=False):
        try:
            values = list(map(int, input("\n🔢 Type the list of numbers (separated by spaces): ").split()))
            if sort_array:
                values.sort()
                print(f"📊 Sorted numbers: {values}")
            target = int(input("🎯 What number do you want to search for?: "))
            return values, target
        except ValueError:
            print("🚫 Please enter valid integers only.")
            return self.get_array_and_target(sort_array)

    def linear_search(self):
        arr, target = self.get_array_and_target()
        print("\n📍 Beginning linear search...\n")
        sleep(0.5)

        for idx, val in enumerate(arr):
            print(f"🔎 Looking at index {idx}: value = {val}")
            if val == target:
                print(f"🎉 Match found! {target} is at index {idx}.")
                return
            print("➡️ No match. Moving on...")
        print(f"❌ Sorry, {target} wasn’t found in the list.")

    def binary_search(self):
        arr, target = self.get_array_and_target(sort_array=True)
        print("\n📍 Initiating binary search...\n")
        sleep(0.5)

        left, right = 0, len(arr) - 1
        step = 1

        while left <= right:
            mid = (left + right) // 2
            print(f"🔎 Step {step}: left = {left}, right = {right}, mid = {mid}, value = {arr[mid]}")
            step += 1

            if arr[mid] == target:
                print(f"🎯 Found it! {target} is at index {mid}.")
                return
            elif arr[mid] < target:
                print(f"{arr[mid]} < {target} → Shifting right")
                left = mid + 1
            else:
                print(f"{arr[mid]} > {target} → Shifting left")
                right = mid - 1

        print(f"❌ {target} couldn’t be found in the list.")

    def interpolation_search(self):
        arr, target = self.get_array_and_target(sort_array=True)
        print("\n📍 Running interpolation search...\n")
        sleep(0.5)

        low, high = 0, len(arr) - 1
        step = 1

        while low <= high and arr[low] <= target <= arr[high]:
            if arr[high] == arr[low]:
                if arr[low] == target:
                    print(f"🎯 Found {target} at index {low}.")
                    return
                break

            pos = low + int(((target - arr[low]) * (high - low)) / (arr[high] - arr[low]))

            if pos < low or pos > high:
                break

            print(f"🔎 Step {step}: low = {low}, high = {high}, pos = {pos}, value = {arr[pos]}")
            step += 1

            if arr[pos] == target:
                print(f"🏆 Success! {target} is at index {pos}.")
                return
            elif arr[pos] < target:
                print(f"{arr[pos]} < {target} → Heading right")
                low = pos + 1
            else:
                print(f"{arr[pos]} > {target} → Heading left")
                high = pos - 1

        print(f"❌ No luck! {target} isn’t in the array.")
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
        print("🏰 Welcome to the Algorithm Adventure Zone – Led by Cherry Albia! 🏰\n")
        print("🧠 Choose a journey to challenge your brain:")

        for idx, module in enumerate(modules, start=1):
            print(f" {idx}. ✨ {module.__name__}")
        print(" 0. ❌ Leave the Realm")

        try:
            choice = int(input("\n🎯 Select your option (0 to exit): "))
        except ValueError:
            print("\n🚫 That doesn't seem like a valid number. Give it another shot!")
            sleep(1.5)
            continue

        if choice == 0:
            print("\n👋 Farewell, brave explorer! Come back soon for more algorithmic quests.")
            break

        if 1 <= choice <= len(modules):
            selected_module = modules[choice - 1]
            while True:
                clear_screen()
                print(f"⚙️ Launching Module: {selected_module.__name__}\n")
                selected_module()

                again = input("\n🔁 Would you like to run this module again? (y/N): ").strip().lower()
                if again != 'y':
                    break
        else:
            print("\n❗ That choice isn't on the list. Try picking a valid one.")
            sleep(1.5)

if __name__ == "__main__":
    main()
# endregion