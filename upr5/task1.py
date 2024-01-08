import os

class InvalidLineError(Exception):
    def __init__(self, line):
        self.line = line
        super().__init__(f"Invalid line: {line}")

class InvalidItemError(Exception):
    def __init__(self, item_name):
        self.item_name = item_name
        super().__init__(f"Invalid item name: {item_name}")

class InvalidQuantityError(Exception):
    def __init__(self, quantity):
        self.quantity = quantity
        super().__init__(f"Invalid quantity: {quantity}")

class InvalidPriceError(Exception):
    def __init__(self, price):
        self.price = price
        super().__init__(f"Invalid price: {price}")

class ListFileError(Exception):
    def __init__(self, file_path):
        self.file_path = file_path
        super().__init__(f"File error at path: {file_path}")

def validate_list(file_path: str) -> float:
        try:
            file = open(file_path, 'r', encoding='utf-8')
        except FileNotFoundError:
            raise ListFileError(f"File not found: {file_path}")
        except IOError:
            raise ListFileError(f"Unable to read file: {file_path}")
        
        total_cost = 0
        for line in file:
            line = line.strip()
            
            if not line.startswith('-'):
                raise InvalidLineError(f"Invalid line: {line}")
            parts = line[1:].split(':')

            if len(parts) != 3:
                raise InvalidLineError(f"Invalid line structure: {line}")
            
            item_name, quantity, price = parts
            if not item_name or item_name.isdigit():
                raise InvalidItemError(f"Invalid item name: {item_name}")     
            try:
                quantity = int(quantity)
                if quantity <= 0:
                    raise InvalidQuantityError(f"Invalid quantity: {quantity}")
            except ValueError:
                    raise InvalidQuantityError(f"Invalid quantity: {quantity}")
                
            try:
                price = float(price)
                if price < 0:
                    raise InvalidPriceError(f"Invalid price: {price}")
            except ValueError:
                    raise InvalidPriceError(f"Invalid price: {price}")

            total_cost += quantity * price
            return total_cost


assert abs(validate_list(os.path.join("lab04_files", "task_1", "list1.txt")) - 11.25) < 0.001

assert int(validate_list(os.path.join("lab04_files", "task_1", "list2.txt"))) == 0, "Empty files should return 0"

try:
    validate_list(os.path.join("lab04_files", "task_1", "list3.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidLineError:
    pass

try:
    validate_list(os.path.join("lab04_files", "task_1", "list4.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidLineError:
    pass

try:
    validate_list(os.path.join("lab04_files", "task_1", "list5.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidItemError:
    pass

try:
    validate_list(os.path.join("lab04_files", "task_1", "list6.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidQuantityError:
    pass

try:
    validate_list(os.path.join("lab04_files", "task_1", "list7.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidQuantityError:
    pass

try:
    validate_list(os.path.join("lab04_files", "task_1", "list8.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidQuantityError:
    pass

try:
    validate_list(os.path.join("lab04_files", "task_1", "list9.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidPriceError:
    pass

try:
    validate_list(os.path.join("lab04_files", "task_1", "list10.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidPriceError:
    pass

try:
    validate_list(os.path.join("lab04_files", "task_1", "list11.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidLineError:
    pass