class IE(str):
    """ 
    IE Class

    Represents a IE that can be stopped.
    
    This class extends `str`, meaning it behaves like a string while 
    semantically representing an IE.
    """
    def __new__(cls, value):
        if not isinstance(value, str):
            raise TypeError("IE must be initialized with a string")
        return super().__new__(cls, value)
