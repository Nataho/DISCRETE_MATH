from TOOLS import TOOLS
from Prime import Prime

class GCD_LCM():
    def __init__(self):
        TOOLS.clear_screen()
        self.GCD_methods = [
            "Euclidean algorithm",
            # "Prime factorization",
            # "Binary GCD algorithm",
        ]
        self.LCM_methods = [
            # "Using GCD",
            # "Prime factorization",
            # "Listing multiples",
        ]
        self.start()

    def start(self):
        TOOLS.print_type("Pick a method to calculate GCD:")
        for i, method in enumerate(self.GCD_methods):
            TOOLS.print_type(f"{i + 1}. {method}")
        choice = int(TOOLS.input_type("Enter the number of your choice: ")) - 1
        if choice < 0 or choice >= len(self.GCD_methods):
            TOOLS.print_type("Invalid choice. Please try again.")
            return
        method_name = self.GCD_methods[choice]
        TOOLS.print_type("")
        TOOLS.print_type(f"You chose: {method_name}")

        if method_name == "Euclidean algorithm":
            a = int(TOOLS.input_type("Enter first number (a): "))
            b = int(TOOLS.input_type("Enter second number (b): "))
            result = self.eucledian(a, b)
            TOOLS.sleep(0.5)
            print()
            TOOLS.print_type(f"GCD({a}, {b}) = {result}")

    def eucledian(self, a, b):
        """Calculate GCD using the Euclidean algorithm."""
        print()
        while b: #runs when b is not zero
            TOOLS.print_type(f"{a} = {b}({a // b}) + {a % b}")
            a, b = b, a % b #swap
        return a
    # def