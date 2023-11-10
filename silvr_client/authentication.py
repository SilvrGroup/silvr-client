class AuthenticationBackend:
    @property
    def headers(self):
        raise NotImplementedError


class TokenAuth(AuthenticationBackend):
    api_key: str

    def __init__(self, api_key):
        self.api_key = api_key

    @property
    def headers(self):
        return {"X-API-KEY": self.api_key}
