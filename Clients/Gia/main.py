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

# region Set Theory
class SetTheory:
    """A simple class for set theory operations."""

    def __init__(self):
        clear_screen()
        print("Set Theory function opened!")
        sleep(1)
        self.start()

    def start(self):
        print("Welcome to the Set Theory class!")
        self.perform_operations()

    def perform_operations(self):
        print("Let's begin by reading two sets from the user.")
        sleep(1)
        A = self.read_set('A')
        B = self.read_set('B')
        print("\nYou have entered:")
        print(f"Set A: {A}")
        print(f"Set B: {B}")

        print("Performing set operations...")
        sleep(1)

        print("\nResults of set operations:")
        print(f"Union (A ∪ B): {A | B}")
        print(f"Intersection (A ∩ B): {A & B}")
        print(f"Difference (A - B): {A - B}")
        print(f"Is A a subset of B? {'Yes' if A <= B else 'No'}")
        print(f"Are A and B equal? {'Yes' if A == B else 'No'}")

    def read_set(self, name):
        elements = input(f"Enter the elements of set {name} (space separated): ")
        return set(elements.split())
# endregion

# region Ciphers
class Ciphers:
    """A simple class for encrypting text using basic ciphers."""

    def __init__(self):
        clear_screen()
        print("Ciphers class opened!")
        sleep(1)
        self.start()

    def start(self):
        print("Pick your desired encryption method:")
        print("1. Caesar Cipher")
        print("2. Vigenère Cipher")
        print("3. Playfair Cipher")
        print("4. Vernam Cipher")
        print("5. One time pad Cipher")
        print("6. Hill Cipher")
        print("7. Rail Fence Cipher")
        print("8. Columnar Cipher")
        choice = int(input("Enter the number of the method you want to use: "))
        match choice:
            case 1:
                self.caesar_cipher()
            case 2:
                self.vigenere_cipher()
            case 3:
                self.playfair_cipher()
            case 4:
                self.vernam_cipher()
            case 5:
                self.one_time_pad()
            case 6:
                self.hill_cipher()
            case 7:
                self.rail_fence_cipher()
            case 8:
                self.columnar_cipher()
            case _:
                print("invalid")

    def caesar_cipher(self):
        text = input("Enter the text to encrypt: ")
        shift = int(input("Enter the shift value (1-25): "))
        result = ""
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - base + shift) % 26 + base)
            else:
                result += char
        print(f"Encrypted text: {result}")

    def vigenere_cipher(self):
        text = input("Enter the text to encrypt: ")
        keyword = input("Enter the key: ")
        result = ""
        keyword = (keyword * (len(text) // len(keyword) + 1))[:len(text)]
        for i, char in enumerate(text):
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                key_char = keyword[i].upper() if char.isupper() else keyword[i].lower()
                shift = ord(key_char) - base
                result += chr((ord(char) - base + shift) % 26 + base)
            else:
                result += char
        print(f"Encrypted text: {result}")
    
    def playfair_cipher(self):
        plain_text = input("Enter the text to encrypt: ")
        keyword = input("Enter the Keyword: ")

        def generate_key_matrix(keyword):
            keyword = keyword.upper().replace("J", "I")
            seen = set()
            key = ""
            for char in keyword:
                if char not in seen and char.isalpha():
                    seen.add(char)
                    key += char
            for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
                if char not in seen:
                    key += char
            matrix = [list(key[i:i+5]) for i in range(0, 25, 5)]
            return matrix

        def prepare_text(text):
            text = text.upper().replace("J", "I")
            prepared = ""
            i = 0
            while i < len(text):
                char1 = text[i]
                char2 = text[i+1] if i+1 < len(text) else "X"
                if char1 == char2:
                    prepared += char1 + "X"
                    i += 1
                else:
                    prepared += char1 + char2
                    i += 2
            if len(prepared) % 2 != 0:
                prepared += "X"
            return prepared

        def find_position(matrix, char):
            for i in range(5):
                for j in range(5):
                    if matrix[i][j] == char:
                        return i, j
            return None, None

        def encrypt_pair(matrix, a, b):
            row1, col1 = find_position(matrix, a)
            row2, col2 = find_position(matrix, b)
            if row1 == row2:
                return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:
                return matrix[row1][col2] + matrix[row2][col1]

        matrix = generate_key_matrix(keyword)
        prepared = prepare_text(plain_text)
        ciphertext = ""
        for i in range(0, len(prepared), 2):
            ciphertext += encrypt_pair(matrix, prepared[i], prepared[i+1])
        
        print(f"Encrypted text: {ciphertext}")

    def vernam_cipher(self):
        text = input("Enter the text to encrypt: ")
        key = input("Enter the keyword: ")
        key_repeated = (key * (len(text) // len(key) + 1))[:len(text)]
        result = ""
        for i in range(len(text)):
            encrypted_char = chr(ord(text[i]) ^ ord(key[i]))
            result += encrypted_char
        print(f"Encrypted text: {result}")
        print(f"Encrypted text in hex: {result.encode().hex()}")
    
    def one_time_pad(self):
        text = input("Enter the text to encrypt: ")
        key = os.urandom(len(text))
        encrypted_bytes = bytearray()
        for char, key_byte in zip(text, key):
            encrypted_char = ord(char) ^ key_byte
            encrypted_bytes.append(encrypted_char)
        print(f"Random Key (hex): {key.hex()}")
        print(f"Encrypted text (hex): {encrypted_bytes.hex()}")

    def hill_cipher(self):
        text = input("Enter the plaintext to encrypt: ")
        key_matrix_input = input("Enter the key matrix (3x3) as space-separated values (e.g., '1 2 3 4 5 6 7 8 9'): ")
        try:
            key_matrix_values = list(map(int, key_matrix_input.split()))
            if len(key_matrix_values) != 9:
                print("Key matrix must have 9 values for a 3x3 matrix.")
                return
            key_matrix = [key_matrix_values[i:i+3] for i in range(0, 9, 3)]
        except ValueError as e:
            print(f"Invalid input for key matrix: {e}")
            return

        small = [chr(i) for i in range(ord('a'), ord('z')+1)]
        big = [chr(i) for i in range(ord('A'), ord('Z')+1)]

        filtered = [c for c in text if c.isalpha()]
        while len(filtered) % 3 != 0:
            filtered.append('x')

        numbers = []
        for c in filtered:
            if c in small:
                numbers.append(small.index(c))
            elif c in big:
                numbers.append(big.index(c))
            else:
                numbers.append(0)

        ciphertext = ""
        for i in range(0, len(numbers), 3):
            block = numbers[i:i+3]
            result = []
            for col in range(3):
                value = 0
                for row in range(3):
                    value += key_matrix[row][col] * block[row]
                result.append(value % 26)
            for idx, num in enumerate(result):
                orig_char = filtered[i + idx]
                if orig_char in big:
                    ciphertext += big[num]
                else:
                    ciphertext += small[num]

        print("Key matrix:")
        for row in key_matrix:
            print(" ".join(map(str, row)))
        print(f"Encrypted text: {ciphertext}")

    def rail_fence_cipher(self):
        text = input("Enter the text to encrypt: ")
        if any(char.isdigit() for char in text):
            print("Error: Text should not contain numbers.")
            return
        try:
            rails = int(input("Enter the number of rails (2-10): "))
        except ValueError:
            print("Invalid input. Please enter a number between 2 and 10.")
            return
        if not (2 <= rails <= 10):
            print("Invalid number of rails. Please enter a number between 2 and 10.")
            return

        fence = [''] * rails
        rail = 0
        direction = 1

        for char in text:
            fence[rail] += char
            rail += direction
            if rail == 0 or rail == rails - 1:
                direction *= -1

        encrypted_text = ''.join(fence)
        print(f"Encrypted text: {encrypted_text}")

    def columnar_cipher(self):
        text = input("Enter the text to encrypt: ")
        print(f"Need {len(text)} cells for the given text.")
        try:
            rows = int(input("Enter the number of rows for the matrix: "))
            cols = int(input("Enter the number of columns for the matrix: "))
        except ValueError:
            print("Rows and columns must be positive integers.")
            return
        key_input = input(f"Enter the key as {cols} numbers (1 to {cols}) separated by spaces (e.g., '3 1 2'): ")
        try:
            key = [int(k) for k in key_input.strip().split()]
        except ValueError:
            print("Key must be numbers.")
            return
        if len(key) != cols or sorted(key) != list(range(1, cols + 1)):
            print(f"Key must be {cols} unique numbers from 1 to {cols}.")
            return
        if rows <= 0 or cols <= 0:
            print("Rows and columns must be positive integers.")
            return

        padded_length = rows * cols
        padded_text = text.ljust(padded_length, 'x')[:padded_length]
        matrix = []
        idx = 0
        for r in range(rows):
            row = []
            for c in range(cols):
                row.append(padded_text[idx])
                idx += 1
            matrix.append(row)
        ciphertext = ""
        for k in key:
            col_idx = k - 1
            for r in range(rows):
                ciphertext += matrix[r][col_idx]
        print(f"Encrypted text: {ciphertext}")

# endregion

# region Sorting
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
            left = arr[:mid] #get all elements sa left
            right = arr[mid:] #get all elements sa right
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
        
        while i < len(left): #add remaining left side
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right): #add remaining right side
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

        # 10 buckets for tenths place (0-9)
        bucket_count = 10
        buckets = [[] for _ in range(bucket_count)]

        for num in arr:
            # Find the bucket index based on the tenths place of the normalized value
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
# endregion

# region Conversion
class Conversion:
    """A simple class for number base conversions."""

    def __init__(self):
        clear_screen()
        print("Conversion class opened!")
        sleep(1)
        self.start()

    def start(self):
        print("Pick a conversion method:")
        print("1. Decimal to Binary")
        print("2. Binary to Decimal")
        print("3. Decimal to Octal")
        print("4. Decimal to Hexadecimal")
        print("5. Octal to Decimal")
        print("6. Hexadecimal to Decimal")
        print("7. Binary to Octal")
        print("8. Binary to Hexadecimal")
        print("9. Octal to Binary")
        print("10. Octal to Hexadecimal")
        print("11. Hexadecimal to Binary")
        print("12. Hexadecimal to Octal")
        choice = int(input("Enter the number of your choice: "))

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
                print("Invalid choice.")

    def decimal_to_binary(self):
        decimal = int(input("Enter decimal number: "))
        binary = ""
        if decimal == 0:
            binary = "0"
        else:
            while decimal > 0:
                binary = str(decimal % 2) + binary
                decimal //= 2
        print(f"Binary: {binary}")

    def binary_to_decimal(self):
        binary = input("Enter binary number: ")
        decimal = 0
        for digit in binary:
            decimal = decimal * 2 + int(digit)
        print(f"Decimal: {decimal}")

    def decimal_to_binary(self):
        decimal = int(input("Enter decimal number: "))
        output = ""
        sub = 2

        while True:
            r = decimal % sub  # remainder
            decimal //= sub
            output = str(r) + output
            if decimal == 0:
                break

        print(f"Binary: {output}")

    def decimal_to_octal(self):
        decimal = int(input("Enter decimal number: "))
        output = ""
        sub = 8

        while True:
            r = decimal % sub  # remainder
            decimal //= sub
            output = str(r) + output
            if decimal == 0:
                break

        print(f"Octal: {output}")

    def decimal_to_hex(self):
        decimal = int(input("Enter decimal number: "))
        output = ""
        sub = 16

        while True:
            r = decimal % sub  # remainder
            match r:
                case 10:
                    r = "A"
                case 11:
                    r = "B"
                case 12:
                    r = "C"
                case 13:
                    r = "D"
                case 14:
                    r = "E"
                case 15:
                    r = "F"
            decimal //= sub
            output = str(r) + output
            if decimal == 0:
                break

        print(f"Hexadecimal: {output}")

    def binary_to_decimal(self):
        binary = input("Enter binary number: ")
        r_binary = ""
        output = 0
        sub = 2

        for char in binary:
            r_binary = char + r_binary

        for i in range(0, len(r_binary)):
            output += int(r_binary[i]) * sub ** i

        print(f"Decimal: {output}")

    def octal_to_decimal(self):
        octal = input("Enter octal number: ")
        r_octal = ""
        output = 0
        sub = 8

        for char in octal:
            r_octal = char + r_octal

        for i in range(0, len(r_octal)):
            output += int(r_octal[i]) * sub ** i

        print(f"Decimal: {output}")

    def hex_to_decimal(self):
        hex_str = input("Enter hexadecimal number: ")
        r_hex = ""
        output = 0
        sub = 16

        for char in hex_str:
            r_hex = char + r_hex

        for i in range(0, len(r_hex)):
            to_out = 0
            match r_hex[i].upper():
                case "A":
                    to_out = 10
                case "B":
                    to_out = 11
                case "C":
                    to_out = 12
                case "D":
                    to_out = 13
                case "E":
                    to_out = 14
                case "F":
                    to_out = 15
                case _:
                    to_out = int(r_hex[i])
            output += to_out * sub ** i

        print(f"Decimal: {output}")

    def binary_to_octal(self):
        binary = input("Enter binary number: ")
        decimal = 0
        r_binary = ""
        sub = 2

        for char in binary:
            r_binary = char + r_binary

        for i in range(0, len(r_binary)):
            decimal += int(r_binary[i]) * sub ** i

        output = ""
        sub_octal = 8
        temp_decimal = decimal
        while True:
            r = temp_decimal % sub_octal
            temp_decimal //= sub_octal
            output = str(r) + output
            if temp_decimal == 0:
                break

        print(f"Octal: {output}")

    def binary_to_hex(self):
        binary = input("Enter binary number: ")
        decimal = 0
        r_binary = ""
        sub = 2

        for char in binary:
            r_binary = char + r_binary

        for i in range(0, len(r_binary)):
            decimal += int(r_binary[i]) * sub ** i

        output = ""
        sub_hex = 16
        temp_decimal = decimal
        while True:
            r = temp_decimal % sub_hex
            match r:
                case 10:
                    r = "A"
                case 11:
                    r = "B"
                case 12:
                    r = "C"
                case 13:
                    r = "D"
                case 14:
                    r = "E"
                case 15:
                    r = "F"
            temp_decimal //= sub_hex
            output = str(r) + output
            if temp_decimal == 0:
                break

        print(f"Hexadecimal: {output}")

    def octal_to_binary(self):
        octal = input("Enter octal number: ")
        decimal = 0
        r_octal = ""
        sub = 8

        for char in octal:
            r_octal = char + r_octal

        for i in range(0, len(r_octal)):
            decimal += int(r_octal[i]) * sub ** i

        output = ""
        sub_bin = 2
        temp_decimal = decimal
        while True:
            r = temp_decimal % sub_bin
            temp_decimal //= sub_bin
            output = str(r) + output
            if temp_decimal == 0:
                break

        print(f"Binary: {output}")

    def octal_to_hex(self):
        octal = input("Enter octal number: ")
        decimal = 0
        r_octal = ""
        sub = 8

        for char in octal:
            r_octal = char + r_octal

        for i in range(0, len(r_octal)):
            decimal += int(r_octal[i]) * sub ** i

        output = ""
        sub_hex = 16
        temp_decimal = decimal
        while True:
            r = temp_decimal % sub_hex
            match r:
                case 10:
                    r = "A"
                case 11:
                    r = "B"
                case 12:
                    r = "C"
                case 13:
                    r = "D"
                case 14:
                    r = "E"
                case 15:
                    r = "F"
            temp_decimal //= sub_hex
            output = str(r) + output
            if temp_decimal == 0:
                break

        print(f"Hexadecimal: {output}")

    def hex_to_binary(self):
        hex_str = input("Enter hexadecimal number: ")
        r_hex = ""
        decimal = 0
        sub = 16

        for char in hex_str:
            r_hex = char + r_hex

        for i in range(0, len(r_hex)):
            to_out = 0
            match r_hex[i].upper():
                case "A":
                    to_out = 10
                case "B":
                    to_out = 11
                case "C":
                    to_out = 12
                case "D":
                    to_out = 13
                case "E":
                    to_out = 14
                case "F":
                    to_out = 15
                case _:
                    to_out = int(r_hex[i])
            decimal += to_out * sub ** i

        output = ""
        sub_bin = 2
        temp_decimal = decimal
        while True:
            r = temp_decimal % sub_bin
            temp_decimal //= sub_bin
            output = str(r) + output
            if temp_decimal == 0:
                break

        print(f"Binary: {output}")

    def hex_to_octal(self):
        hex_str = input("Enter hexadecimal number: ")
        r_hex = ""
        decimal = 0
        sub = 16

        for char in hex_str:
            r_hex = char + r_hex

        for i in range(0, len(r_hex)):
            to_out = 0
            match r_hex[i].upper():
                case "A":
                    to_out = 10
                case "B":
                    to_out = 11
                case "C":
                    to_out = 12
                case "D":
                    to_out = 13
                case "E":
                    to_out = 14
                case "F":
                    to_out = 15
                case _:
                    to_out = int(r_hex[i])
            decimal += to_out * sub ** i

        output = ""
        sub_octal = 8
        temp_decimal = decimal
        while True:
            r = temp_decimal % sub_octal
            temp_decimal //= sub_octal
            output = str(r) + output
            if temp_decimal == 0:
                break

        print(f"Octal: {output}")
# endregion

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
        # else:
        #     print("Invalid choice.")

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
        # Calculate GCD first
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
        print("Searching class opened!")
        sleep(1)
        self.start()

    def start(self):
        print("Pick a searching method:")
        print("1. Linear Search")
        print("2. Binary Search")
        print("3. interpolation search")
        choice = int(input("Enter the number of your choice: "))
        
        match choice:
            case 1:
                self.linear_search()
            case 2:
                self.binary_search()
            case 3:
                self.interpolation_search()
            case _:
                print("invalid")

    def linear_search(self):
        arr = list(map(int, input("Enter the elements of the array (space separated): ").split()))
        target = int(input("Enter the number to search for: "))
        found = False
        for i, num in enumerate(arr):
            if num == target:
                print(f"Found {target} at index {i}.")
                found = True
                break
        if not found:
            print(f"{target} not found in the array.")

    def binary_search(self):
        arr = list(map(int, input("Enter the elements of the array (space separated): ").split()))
        arr.sort()
        print(f"Sorted array: {arr}")
        target = int(input("Enter the number to search for: "))
        left, right = 0, len(arr) - 1
        found = False
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                print(f"Found {target} at index {mid}.")
                found = True
                break
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if not found:
            print(f"{target} not found in the array.")

    def interpolation_search(self):
        arr = list(map(int, input("Enter the elements of the array (space separated): ").split()))
        arr.sort()
        print(f"Sorted array: {arr}")

        target = int(input("Enter the number to search for: "))
        key = target
        low = 0
        high = len(arr) - 1

        while low <= high and arr[low] <= key <= arr[high]:


            if arr[high] == arr[low]:
                if arr[low] == key:
                    return low
                else:
                    break
            pos = low + int(((key - arr[low]) * (high - low)) / (arr[high] - arr[low]))
            
            #text
            displayed_arr = ""
            for i in range(len(arr)):
                # if i = 0:
                #     displayed_arr += f"{arr[i]}"
                #     continue
                if i == pos:
                    displayed_arr += f", \033[93m{arr[pos]}\033[0m"
                elif i == low:
                    displayed_arr += f", \033[94m{arr[low]}\033[0m"
                elif i == high:
                    displayed_arr += f", \033[92m{arr[high]}\033[0m"
                
                else:
                    displayed_arr += f", {arr[i]}"
            displayed_arr = f"[{displayed_arr[2:]}]"
            
            print(displayed_arr)
            sleep(0.1)
            if pos < low or pos > high:
                break
            if arr[pos] < key:
                low = pos + 1
            elif arr[pos] > key:
                high = pos - 1
            else:
                return pos
        return -1
# endregion

# region Main Program Loop
def main():
    classes = [
        SetTheory,
        Ciphers,
        Sorting,
        Conversion,
        Prime,
        GCD_LCM,
        Searching,
    ]

    while True:
        clear_screen()
        print("Pick a number to open:")
        for i, cls in enumerate(classes):
            print(f"{i + 1}. {cls.__name__}")
        print("0. Exit")
        try:
            picked = int(input("Enter the number of the class you want to open: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            sleep(1)
            continue
        if picked == 0:
            print("Goodbye!")
            break
        if 1 <= picked <= len(classes):
            classes[picked - 1]()
            again = input("Would you like to restart the class? (y/N): ")
            if again.lower() == 'y':
                classes[picked - 1]()
        else:
            print("Invalid choice. Please try again.")
            sleep(1)

if __name__ == "__main__":
    main()
# endregion
