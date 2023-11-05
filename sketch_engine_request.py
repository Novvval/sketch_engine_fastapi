import requests

from errors import InvalidLangError, InvalidQueryError

ALLOWED_PARAMS = ["lang", "query"]
COUNTRY_CODES = {"en": "English", "de": "German", "it": "Italian", "et": "Estonian", "ru": "Russian", "cz": "Czech"}


class SketchEngineRequest:
    def __init__(self, type, lang, query):
        self.type = type
        self.lang = lang
        self.query = query

    def validate_request(self):
        if self.lang not in COUNTRY_CODES:
            raise InvalidLangError()
        if self.query == "":
            raise InvalidQueryError(self.query)
        if self.query.isspace():
            raise InvalidQueryError(self.query)
        if len(self.query) > 1000:
            raise InvalidQueryError(self.query)
        return True

    def send(self):
        if self.validate_request():
            lang = COUNTRY_CODES[self.lang]
            request = requests.get(
                f"https://skell.sketchengine.eu/api/run.cgi/{self.type}?lang={lang}&query={self.query}&format=json"
            ).json()

            return request
