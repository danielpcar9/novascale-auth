from typing import Any

class AnomalyDetector:
    """Base class for anomaly detection."""
    
    def is_anomaly(self, data: Any) -> bool:
        """Verifies if the provided data represents an anomaly."""
        return False
