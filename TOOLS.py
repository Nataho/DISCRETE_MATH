import os
import time
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
