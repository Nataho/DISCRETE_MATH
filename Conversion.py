from TOOLS import TOOLS
class Conversion: #class for conversion
    def __init__(self):
        print("what the fuck bro")
        TOOLS.clear_screen()
        self.methods = [
            "binary to octal",
            "binary to decimal",
            "binary to hex",

            "decimal to binary",
            "decimal to octal",
            "decimal to hex",

            "octal to binary",
            "octal to decimal",
            "octal to hex",

            "hex to binary",
            "hex to octal",
            "hex to decimal",
        ]
        self.start()
        # raise NotImplementedError("This class cannot be instantiated directly.")

    def start(self):
        print("Pick a conversion method:")
        for i, method in enumerate(self.methods):
            print(f"{i + 1}. {method}")
        choice = int(TOOLS.input_type("Enter the number of your choice: ")) - 1
        if choice < 0 or choice >= len(self.methods):
            print("Invalid choice. Please try again.")
            return
        method_name = self.methods[choice]
        print()
        print(f"You chose: {method_name}")
        match method_name:
            case "binary to octal":
                binary = TOOLS.input_type("Enter binary number: ")
                result = self.btoo(binary)
                TOOLS.print_type(f"Octal: {result}")
            case "binary to decimal":
                binary = TOOLS.input_type("Enter binary number: ")
                result = self.btod(binary)
                TOOLS.print_type(f"Decimal: {result}")
            case "binary to hex":
                binary = TOOLS.input_type("Enter binary number: ")
                result = self.btoh(binary)
                TOOLS.print_type(f"Hex: {result}")
            case "decimal to binary":
                decimal = int(TOOLS.input_type("Enter decimal number: "))
                result = self.dtob(decimal)
                TOOLS.print_type(f"Binary: {result}")
            case "decimal to octal":
                decimal = int(TOOLS.input_type("Enter decimal number: "))
                result = self.dtoo(decimal)
                TOOLS.print_type(f"Octal: {result}")
            case "decimal to hex":
                decimal = int(TOOLS.input_type("Enter decimal number: "))
                result = self.dtoh(decimal)
                TOOLS.print_type(f"Hex: {result}")
            case "octal to binary":
                octal = TOOLS.input_type("Enter octal number: ")
                result = self.otob(octal)
                TOOLS.print_type(f"Binary: {result}")
            case "octal to decimal":
                octal = TOOLS.input_type("Enter octal number: ")
                result = self.otod(octal)
                TOOLS.print_type(f"Decimal: {result}")
            case "octal to hex":
                octal = TOOLS.input_type("Enter octal number: ")
                result = self.otoh(octal)
                TOOLS.print_type(f"Hex: {result}")
            case "hex to binary":
                hex_num = TOOLS.input_type("Enter hex number: ")
                result = self.htob(hex_num)
                TOOLS.print_type(f"Binary: {result}")
            case "hex to octal":
                hex_num = TOOLS.input_type("Enter hex number: ")
                result = self.htoo(hex_num)
                TOOLS.print_type(f"Octal: {result}")
            case "hex to decimal":
                hex_num = TOOLS.input_type("Enter hex number: ")
                result = self.htod(hex_num)
                TOOLS.print_type(f"Decimal: {result}")
    
    #decimal to binary
    # @staticmethod
    def dtob(self, decimal:int):
        output = ""
        sub = 2

        while True:
            r = decimal % sub #remainder
            decimal //= sub 
            output = str(r) + output
            if decimal == 0: break

        return output
    
    #decimal to octal
    # @staticmethod
    def dtoo(self, decimal:int):
        output = ""
        sub = 8

        while True:
            r = decimal % sub #remainder
            decimal //= sub
            output = str(r) + output
            if decimal == 0: break

        return output

    #decimal to hex
    # @staticmethod
    def dtoh(self, decimal:int):
        output = ""
        sub = 16

        while True:
            r = decimal % sub #remainder
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
            if decimal == 0: break

        return output
    
    #binary to decimal
    # @staticmethod
    def btod(self, binary:str):
        binary = str(binary)
        r_binary = ""
        output = 0
        sub = 2
        
        for char in binary:
            r_binary = char + r_binary

        for i in range(0,len(r_binary)):
            output += int(r_binary[i]) * sub ** i

        return output

    #octal to decimal
    # @staticmethod
    def otod(self, octal:str):
        octal = str(octal)
        r_octal = ""
        output = 0
        sub = 8

        for char in octal:
            r_octal = char + r_octal

        for i in range(0,len(r_octal)):
            output += int(r_octal[i]) * sub ** i

        return output

    #hex to decimal
    # @staticmethod
    def htod(self, hex:str):
        """converts hex to decimal"""
        hex = str(hex)
        r_hex = ""
        output = 0
        sub = 16

        for char in hex:
            r_hex = char + r_hex
        
        for i in range(0,len(r_hex)):
            to_out = 0
            match r_hex[i]:
                case "A": to_out = 10
                case "B": to_out = 11
                case "c": to_out = 12
                case "D": to_out = 13
                case "E": to_out = 14
                case "F": to_out = 15
                case _: to_out = int(r_hex[i])
            
            output += to_out * sub ** i
        
        return output

    #binary to octal
    # @staticmethod
    def btoo(self, binary:str):
        binary = str(binary)
        decimal = self.btod(binary)
        return self.dtoo(decimal)

    #binary to hex
    # @staticmethod
    def btoh(self, binary:str):
        binary = str(binary)
        decimal = self.btod(binary)
        return self.dtoh(decimal)
    
    #octal to binary
    # @staticmethod
    def otob(self, octal:str):
        octal = str(octal)
        decimal = self.otod(octal)
        return self.dtob(decimal)

    #octal to hex
    # @staticmethod
    def otoh(self, octal:str):
        octal = str(octal)
        decimal = self.otod(octal)
        return self.dtoh(decimal)

    #hex to binary
    # @staticmethod
    def htob(self, hex:str):
        hex = str(hex)
        decimal = self.htod(hex)
        return self.dtob(decimal)

    #hex to octal
    def htoo(self, hex:str):
        hex = str(hex)
        decimal = self.htod(hex)
        return self.dtoo(decimal)
    

