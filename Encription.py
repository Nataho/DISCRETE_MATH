from basic_math import bMath
from Advanced.encryption.playfair import PlayfairCipher
from TOOLS import TOOLS

class Ciphers:
    """a class to encrypt and decrypt text using various ciphers."""
    
    def __init__(self,):
        TOOLS.clear_screen()
        self.methods = [
            "Caesar Cipher",
            "Vigenère Cipher",
            "Playfair Cipher",
        ]
        self.start()
        
    def start(self):
        """hi ciar"""
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
                self.caesar()
            case "Vigenère Cipher":
                self.vigenere()
            case "Playfair Cipher":
                self.playfair()
            case _:
                print("This method is not implemented yet.")
        
    def caesar(self):
        print()
        text = input("Enter the text to encrypt: ")
        shift = int(input("Enter the shift value (1-25): "))
        if 1 <= shift <= 25:
            encrypted_text = self._caesar(text, shift)
            print(f"Encrypted text: {encrypted_text}")
        else:
            print("Invalid shift value. Please enter a number between 1 and 25.")
    
    def _caesar(self, text, shift):
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
    
    def vigenere(self):
        print()
        text = input("Enter the text to encrypt: ")
        keyword = input("Enter the keyword: ")
        encrypted_text = self._vigenere(text, keyword)
        print(f"Encrypted text: {encrypted_text}")

    def _vigenere(self, text, keyword):
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

    def playfair(self):
        print()
        text = input("Enter the text to encrypt: ")
        keyword = input("Enter the keyword: ")
        encrypted_text = self._playfair(text, keyword)
        print(f"Encrypted text: {encrypted_text}")
    
    def _playfair(self, text, keyword):
        cipher = PlayfairCipher(text,keyword)

        return cipher.ciphertext