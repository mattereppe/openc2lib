from openc2lib import Response, StatusCode
import logging

logger = logging.getLogger(__name__)

def log_and_respond(status, status_text, error=None, res=None):
    """
    Logs the error if present and returns a standardized response.

    Args:
        status (StatusCode): The status code for the response.
        status_text (str): A descriptive message for the response.
        error (Exception, optional): The error message or exception details. Defaults to None.
        res (object, optional): The response results. Defaults to None.

    Returns:
        Response: A standardized OpenC2 response object.
    """
    if error:
        logger.error(f"Error: {error}")
    if res:
        return Response(status=status, status_text=status_text, results=res)
    return Response(status=status, status_text=status_text)

def servererror(status_text, error=None, res=None):
    """Returns an Internal Server Error response (500)."""
    return log_and_respond(StatusCode.INTERNALERROR, status_text, error, res)

def notimplemented(status_text, error=None, res=None):
    """Returns a Not Implemented response (501) for unsupported commands."""
    return log_and_respond(StatusCode.NOTIMPLEMENTED, status_text, error, res)

def notfound(status_text, error=None, res=None):
    """Returns a Not Found response (404) when requested data is unavailable."""
    return log_and_respond(StatusCode.NOTFOUND, status_text, error, res)

def forbidden(status_text, error=None, res=None):
    """Returns a Forbidden response (403) for unauthorized resource access."""
    return log_and_respond(StatusCode.FORBIDDEN, status_text, error, res)

def unauthorized(status_text, error=None, res=None):
    """Returns an Unauthorized response (401) when authentication fails."""
    return log_and_respond(StatusCode.UNAUTHORIZED, status_text, error, res)

def badrequest(status_text, error=None, res=None):
    """Returns a Bad Request response (400) for malformed or invalid requests."""
    return log_and_respond(StatusCode.BADREQUEST, status_text, error, res)

def processing(status_text):
    """Returns a Processing response (102) indicating an ongoing process."""
    logger.info(status_text)
    return log_and_respond(status=StatusCode.PROCESSING, status_text=status_text)

def ok(status_text, res=None):
    """Returns an OK response (200) for successful operations."""
    logger.info(status_text)
    return log_and_respond(status=StatusCode.OK, status_text=status_text,error=None, res=res)
