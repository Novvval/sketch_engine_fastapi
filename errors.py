from fastapi import HTTPException


class ApiException(HTTPException):
    def __init__(self, status_code, message):
        self.message = message
        super().__init__(status_code=status_code, detail=message)


class InvalidLangError(ApiException):
    def __init__(self):
        message = "Language does not exist"
        super().__init__(400, message)


class InvalidQueryError(ApiException):
    def __init__(self, query):
        message = f"Invalid query: {query}"
        super().__init__(400, message)
