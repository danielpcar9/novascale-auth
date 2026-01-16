from app.services.auth_service import AuthService
from app.ml.anomaly import AnomalyDetector

def get_auth_service():
    detector = AnomalyDetector()
    return AuthService(detector=detector)