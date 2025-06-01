import os
import time

_delay = 0.01  # Default delay for typewriter effect
class TOOLS: 
    @staticmethod
    def simulate_sleep(delay:int, message):
        print("simulating delay...")
        time.sleep(delay)
        print(message)
    def sleep(delay:int):
        time.sleep(delay)
    
    @staticmethod
    def clear_screen():
        os.system("clear")
    
    def set_delay(self, delay:float):
        if isinstance(delay, (int, float)):
            _delay = delay
            self._delay = _delay
        else:
            raise TypeError("Delay must be a number (int or float).")

    @staticmethod
    def print_type(text, delay = _delay):
        for letter in text:
            print(letter, end='', flush=True)
            # print(delay)
            time.sleep(delay)
        print()  # for newline

    @staticmethod
    def input_type(prompt="", delay = _delay):
        for letter in prompt:
            print(letter, end='', flush=True)
            time.sleep(delay)
        return input()