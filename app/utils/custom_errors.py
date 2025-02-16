class Error(Exception):
    def __init__(self, value=''):
        if not hasattr(self, 'value'):
            self.value = value

    def __str__(self):
        return repr(self.value)


class InternalDbError(Error):
    message = 'Sorry, we had a problem with that request.'  # noqa: E501
    internal_error_code = 50001
