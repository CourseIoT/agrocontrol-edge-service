from typing import Optional
from iam.domain.entites import Device

class AuthService:
    
    @staticmethod
    def autenticate_device(device: Optional[Device]):
        return device is not None