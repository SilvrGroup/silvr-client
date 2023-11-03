from .authentication import AuthenticationBackend

class Client:
    def __init__(self, authentication: AuthenticationBakend, base_url="https://app.silvr.co"):
        self.authentication = authentication
        
