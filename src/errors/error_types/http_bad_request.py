class HttpBadRequestError(Exception):
    def __init__(self, message: str = "Bad Request"):
        super().__init__(message)
        self.message = message
        self.status_code = 400
