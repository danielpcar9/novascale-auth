# app/deeps.py
from app.services.auth_service import AuthService
from app.ml.anomaly import AnomalyDetector
from app.database import get_session as get_session


def get_auth_service() -> AuthService:
    """Factory to inject the authentication service with its detector."""
    detector = AnomalyDetector()
    return AuthService(detector=detector)
