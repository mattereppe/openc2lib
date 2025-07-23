class AuthEndpoint(str):
    """ Define oauth2 Authentication Endpoint

        This field indicates the URI where the Producer can obtain authorization credentials
    """

    def __new__(cls, value):
        if not isinstance(value, str) or not value.startswith(('http://', 'https://')):
            raise ValueError("AuthEndpoint must be a string starting with http:// or https://")
        return str.__new__(cls, value)
