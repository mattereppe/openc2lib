class EF(str):
    """ 
    EF Class

    Represents an export field.
    
    This class extends `str`, meaning it behaves like a string while 
    semantically representing an EF.
    """

    def __new__(cls, value):
        if not isinstance(value, str):
            raise TypeError("EF must be initialized with a string")
        return super().__new__(cls, value)
