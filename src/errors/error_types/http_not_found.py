class HttpNotFoundError(Exception):
    def __init__(self, message: str = "Not Found"):
        super().__init__(message)
        self.message = message
        self.status_code = 404
