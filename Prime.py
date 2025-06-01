from TOOLS import TOOLS
from basic_math import bMath
class Prime:
    def __init__(self):
        TOOLS.clear_screen()
        self.methods = [
            "prime factors (trial by division)",
            "Sieve of Eratosthenes",
            "Fermat's little theorem",
        ]
        self.start()

    def start(self):
        TOOLS.print_type("Pick a method to check for primality:")
        for i, method in enumerate(self.methods):
            TOOLS.print_type(f"{i + 1}. {method}")
        choice = int(TOOLS.input_type("Enter the number of your choice: ")) - 1
        if choice < 0 or choice >= len(self.methods):
            TOOLS.print_type("Invalid choice. Please try again.")
            return
        method_name = self.methods[choice]
        TOOLS.print_type("")
        TOOLS.print_type(f"You chose: {method_name}")
        
        if method_name == "prime factors (trial by division)":
            num = int(TOOLS.input_type("Enter a number to check for primality: "))
            result = self.prime_factors(num)
            TOOLS.print_type(f"Prime factors of {num}: {result}")
        elif method_name == "Sieve of Eratosthenes":
            min_limit = int(TOOLS.input_type("Enter the lower limit for prime numbers: "))
            max_limit = int(TOOLS.input_type("Enter the upper limit for prime numbers: "))
            primes = self.sieve_of_eratosthenes(min_limit, max_limit)
            TOOLS.print_type(f"Prime numbers from {min_limit} to {max_limit}: {primes}")
        elif method_name == "Fermat's little theorem":
            TOOLS.print_type("formula: a^(p-1) ≡ 1 (mod p) for prime p")
            TOOLS.print_type("use this: a^k mod p")
            a = int(TOOLS.input_type("Enter a number for a: "))
            k = int(TOOLS.input_type("Enter a number for k: "))
            p = int(TOOLS.input_type("Enter a prime number for p: "))
            result = self.fermats(a, k, p)
            TOOLS.print_type(f"{a}^{k} mod {p} = {result} mod {p}")
    
    def prime_factors(self, n):
        """Return the list of prime factors of n."""
        factors = []
        # Handle 2 separately
        while n % 2 == 0:
            factors.append(2)
            n //= 2
        # Check odd numbers
        for i in range(3, int(n**0.5) + 1, 2):
            while n % i == 0:
                if self.is_prime(i):
                    factors.append(i)
                n //= i
        if n > 2:
            factors.append(n)
        return factors

    def sieve_of_eratosthenes(self, min, max):
        """Return a list of prime numbers in the range [min, max] using the Sieve of Eratosthenes."""
        if max < 2 or min > max:
            return []
        sieve = [True] * (max + 1)
        sieve[0] = sieve[1] = False
        for start in range(2, int(max**0.5) + 1):
            if sieve[start]:
                for multiple in range(start*start, max + 1, start):
                    sieve[multiple] = False
        return [num for num in range(min, max + 1) if sieve[num]]
    
    def fermats(self, a, k, p):
        if not self.is_prime(p):
            TOOLS.print_type("Error: p must be a prime number.")
            raise ValueError("p must be a prime number.")

        exponent_result = pow(a, k)
        return bMath().modulo(exponent_result,p)

    def is_prime(self, n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
