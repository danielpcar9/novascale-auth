class AuthService:
    def __init__(self, detector):
        self.detector = detector

    def register(self, user):
        self.detector.record_attempt(user.username, success=True)
        return {"message": "Usuario registrado", "data": user.model_dump()}