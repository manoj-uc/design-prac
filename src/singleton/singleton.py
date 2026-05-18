# Singleton Pattern in Python
# This ensures only one instance of a class is created""
"""
================================================================================
                    SINGLETON vs NORMAL CLASS COMPARISON
================================================================================

| Feature                  | NormalClass                  | Singleton                     |
|--------------------------|------------------------------|-------------------------------|
| Number of objects        | Multiple                     | Only 1                        |
| s1 is s2                 | False                        | True                          |
| New object created?      | Every time                   | Only first time               |
| Memory usage             | More objects                 | Only one object               |
| Data Consistency         | Each object has own data     | All share same data           |
| Use Case                 | Regular objects              | Shared resource (Logger, DB)  |

================================================================================

"""

class Singleton:
    """
    Singleton class using __new__ method.
    """
    
    _INSTANCE = None
    
    def __new__(cls, *args, **kwargs):
        if cls._INSTANCE is None:
            print("Creating the singleton instance.")
            cls._INSTANCE = super().__new__(cls)
        else:
            print("Returning existing singleton instance...")
        
        return cls._INSTANCE
    
    def __init__(self, value=None):
        # Note: __init__ will be called every time, so we guard it
        if not hasattr(self, 'initialized'):
            self.value = value
            self.initialized = True
            print(f"Initialized with value: {value}")
        else:
            print("Already initialized. Ignoring new parameters.")


# Example usage
if __name__ == "__main__":
    print("=== Singleton Pattern Demo ===\n")
    
    # Create first instance
    s1 = Singleton("Hello World")
    print(f"s1 value: {s1.value}\n")
    
    # Create second instance (should return the same object)
    s2 = Singleton("New Value")  # This won't change the value
    print(f"s2 value: {s2.value}\n")
    
    # Check if they are the same object
    print(f"Are s1 and s2 the same object? {s1 is s2}")
    print(f"Object ID s1: {id(s1)}")
    print(f"Object ID s2: {id(s2)}")