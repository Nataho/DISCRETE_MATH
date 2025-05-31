from basic_math import bMath
from Advanced.encryption.playfair import PlayfairCipher
from TOOLS import TOOLS
import os

class Ciphers:
    """a class to encrypt and decrypt text using various ciphers."""
    
    def __init__(self,):
        TOOLS.clear_screen()
        self.methods = [
            "Caesar Cipher",
            "Vigenère Cipher",
            "Playfair Cipher",
            "Vernam Cipher",
            "One Time Pad Cipher",
            "Hill Cipher"
        ]
        self.start()
        
    def start(self):
        print("pick your desired encryption method.")
        for i, method in enumerate(self.methods):
            print(f"{i + 1}. {method}")
        print()
        choice = int(input("Enter the number of the method you want to use: ")) - 1
        print()
        if choice < 0 or choice >= len(self.methods):
            print("Invalid choice. Please run the program again.")
            exit()
        picked_method = self.methods[choice]
        print(f"You have selected: {picked_method}")
        match picked_method:
            case "Caesar Cipher":
                self._caesar()
            case "Vigenère Cipher":
                self._vigenere()
            case "Playfair Cipher":
                self._playfair()
            case "Vernam Cipher":
                self._vernam_cipher()
            case "One Time Pad Cipher":
                self._one_time_pad()
            case "Hill Cipher":
                self._hill_cipher()
            case _:
                print("This method is not implemented yet.")

#region caesar cipher
    def _caesar(self):
        print()
        text = input("Enter the text to encrypt: ")
        if any(char.isdigit() for char in text):
            print("Error: Text should not contain numbers.")
            return
        shift = int(input("Enter the shift value (1-25): "))
        if 1 <= shift <= 25:
            encrypted_text = self.caesar(text, shift)
            print(f"Encrypted text: {encrypted_text}")
        else:
            print("Invalid shift value. Please enter a number between 1 and 25.")
    
    def caesar(self, text, shift):
        small = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        big = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        encrypted_text = ""
        for char in text:
            if char in small: # check if the character is in the lowercase alphabet
                index = small.index(char)
                new_index = (index + shift) % 26
                encrypted_text += small[new_index]
            elif char in big: # check if the character is in the uppercase alphabet
                index = big.index(char)
                new_index = (index + shift) % 26
                encrypted_text += big[new_index]
            else: # if the character is not in the alphabet, keep it unchanged
                encrypted_text += char
        return encrypted_text
#endregion caesar cipher

#region vigenere cipher
    def _vigenere(self):
        print()
        text = input("Enter the text to encrypt: ")
        if any(char.isdigit() for char in text):
            print("Error: Text should not contain numbers.")
            return
        keyword = input("Enter the keyword: ")
        if any(char.isdigit() for char in keyword):
            print("Error: Keyword should not contain numbers.")
            return
        encrypted_text = self.vigenere(text, keyword)
        print(f"Encrypted text: {encrypted_text}")

    def vigenere(self, text, keyword):
        small = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        big = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        keyword_repeated = (keyword * (len(text) // len(keyword) + 1))[:len(text)] # Repeat the keyword to match the length of the text
        encrypted_text = ""
        
        for i, char in enumerate(text):
            if char in small:
                index = small.index(char)
                shift = small.index(keyword_repeated[i].lower())
                new_index = (index + shift) % 26
                encrypted_text += small[new_index]
            elif char in big:
                index = big.index(char)
                shift = big.index(keyword_repeated[i].upper())
                new_index = (index + shift) % 26
                encrypted_text += big[new_index]
            else:
                encrypted_text += char
        
        return encrypted_text
#endregion vigenere cipher

#region playfair cipher
    def _playfair(self):
        print()
        text = input("Enter the text to encrypt: ")
        keyword = input("Enter the keyword: ")
        encrypted_text = self.playfair(text, keyword)
        print(f"Encrypted text: {encrypted_text}")
    
    def playfair(self, text, keyword):
        cipher = PlayfairCipher(text,keyword)

        return cipher.ciphertext
#endregion playfair cipher

#region vernam cipher
    def _vernam_cipher(self):
        print()
        text = input("Enter the text to encrypt: ")
        key = input("Enter the key: ")
        
        # Repeat or trim the key to match the length of the text
        key_repeated = (key * (len(text) // len(key) + 1))[:len(text)]
        
        encrypted_text = self.vernam_cipher(text, key_repeated)
        print(f"Encrypted text(ascii): {encrypted_text}")
        print(f"Encrypted text(hex): {encrypted_text.encode().hex()}")  # Display in hex format

    def vernam_cipher(self, text, key):
        encrypted_text = ""
        for i in range(len(text)):
            # XOR operation between the ASCII values of the characters
            encrypted_char = chr(ord(text[i]) ^ ord(key[i]))
            encrypted_text += encrypted_char
            # encrypted_text = encrypted_text.encode().hex()  # Ensure the encrypted character is in hex format
        return encrypted_text
#endregion vernam cipher

#region one time pad ciphers
    def _one_time_pad(self):
        print()
        text = input("Enter the text to encrypt: ")
        # Generate a random key (as bytes) with the same length as the text
        key = os.urandom(len(text))
        
        # Encrypt the text: for each character, XOR its ASCII value with the corresponding key byte
        encrypted_bytes = bytearray()
        for char, key_byte in zip(text, key): #combine text and key
            encrypted_char = ord(char) ^ key_byte #XOR operation
            encrypted_bytes.append(encrypted_char) #append character to encrypted bytes
        
        # Show the key and encrypted text in hexadecimal format for easy copying
        print(f"Random Key (hex): {key.hex()}")
        print(f"Encrypted text (hex): {encrypted_bytes.hex()}")

    def one_time_pad(self, text, key):
        # key should be bytes of the same length as text
        return bytes([ord(c) ^ k for c, k in zip(text, key)])
#endregion one time pad cipher

#region hill cipher
    def _hill_cipher(self):
        text = input("Enter the plaintext to encrypt: ")
        key_matrix_input = input("Enter the key matrix (3x3) as space-separated values (e.g., '1 2 3 4 5 6 7 8 9'): ")
        key_matrix = []
        try:
            key_matrix_values = list(map(int, key_matrix_input.split()))
            if len(key_matrix_values) != 9:
                raise ValueError("Key matrix must have 9 values for a 3x3 matrix.")
            key_matrix = [key_matrix_values[i:i+3] for i in range(0, 9, 3)]
        except ValueError as e:
            print(f"Invalid input for key matrix: {e}")
            return
        encrypted_text = self.hill_cipher(key_matrix, text)
        for row in key_matrix:
            print(" ".join(map(str, row)))
        print(f"Encrypted text: {encrypted_text}")

    def hill_cipher(self,key_matrix, plaintext):
        small = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        big = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

        # Make sure the key_matrix is 3x3 (Hill cipher requires a 3x3 matrix for 3-letter blocks)
        if len(key_matrix) != 3 or any(len(row) != 3 for row in key_matrix):
            raise ValueError("Key matrix must be 3x3.")

        # Prepare the plaintext:
        # 1. Remove any characters that are not letters.
        # 2. don't Convert all letters to lowercase.
        # 3. Pad the plaintext with 'x' so its length is a multiple of 3.
        filtered = [c for c in plaintext if c.isalpha()]
        while len(filtered) % 3 != 0:
            filtered.append('x')
        # filtered = ''.join(filtered).lower()

        # Convert each letter to a number (a=0, b=1, ..., z=25)
        numbers = []
        for c in filtered:
            if c in small:
                numbers.append(small.index(c))
            elif c in big:
                numbers.append(big.index(c))
            else:
            # Should not happen since we filtered isalpha(), but just in case
                numbers.append(0)

        # # Encrypt the plaintext in blocks of 3 letters
        ciphertext = ""
        # print(key_matrix)
        for i in range(0, len(numbers), 3):
            block = numbers[i:i+3]
            # print(f"Processing block: {block}")
            # Multiply the key matrix by the block vector, then take mod 26 for each result
            result = []
            for col in range(3):
                value = 0
                # print(key_matrix[col])
                for row in range(3):
                    # print(f"Multiplying {key_matrix[row][col]} (key) with {block[col]} (block)")
                    value += key_matrix[row][col] * block[row]
                    # print(f"{block[row]} * {key_matrix[row][col]}")
                    # print(block[col])
                # print(f"Value before mod: {value}")
                result.append(value % 26)
            # Convert the resulting numbers back to letters
            # Preserve original case: use uppercase if original block letter was uppercase, else lowercase
            for idx, num in enumerate(result):
                orig_char = filtered[i + idx]
                if orig_char in big:
                    ciphertext += big[num]
                else:
                    ciphertext += small[num]

        return ciphertext
        
#endregion hill cipher
