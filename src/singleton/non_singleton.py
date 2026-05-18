# Non-Singleton Class in Python (WITHOUT Singleton Pattern)
# This allows multiple instances of the class to be created

class NonSingletonClass:
    """
    Regular class - every time you create an object, 
    a new instance is made.
    """
    
    def __init__(self, value=None):
        # __init__ runs fresh every time a new object is created
        self.value = value
        print(f"New object created with value: {value}")


# Example usage
if __name__ == "__main__":
    print("=== Normal Class Demo (WITHOUT Singleton) ===\n")
    
    # Create first instance
    s1 = NonSingletonClass("Hello World")
    print(f"s1 value: {s1.value}\n")
    
    # Create second instance (this creates a completely new object)
    s2 = NonSingletonClass("New Value")
    print(f"s2 value: {s2.value}\n")
    
    # Check if they are the same object
    print(f"Are s1 and s2 the same object? {s1 is s2}")
    print(f"Object ID s1: {id(s1)}")
    print(f"Object ID s2: {id(s2)}")