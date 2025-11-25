from typing import Optional

from iam.domain.entites import Device
from iam.domain.services import AuthService

from iam.infrastructure.repositories import DeviceRepository

class AuthApplicationService:

    def __init__(self):
        self.auth_service = AuthService()
        self.device_repository = DeviceRepository()

    def authenticate_device(self, device_id: str, api_key: str) -> bool:
        device: Optional[Device] = self.device_repository.find_by_id_and_api_key(device_id , api_key)
        return self.auth_service.autenticate_device(device)

    def get_or_create_test_device(self) -> Device:
        return self.device_repository.get_or_create_test_device()