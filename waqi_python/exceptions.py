class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class ApiError(Error):
    """Exception raised for errors returned by the WAQI servers."""
    pass

class UnknownError(Error):
    """
    Exception raised for 200 responses with unrecognizable format
    returned by the WAQI servers.
    """
    pass
