class HttpInternalServerError(Exception):
    def __init__(self, message: str = "Internal Server Error"):
        super().__init__(message)
        self.message = message
        self.status_code = 500
