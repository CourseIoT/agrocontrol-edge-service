from typing import Optional
from iam.domain.entites import Device
from iam.infrastructure.models import Device as DeviceModel
from datetime import datetime, timezone

import peewee

class DeviceRepository:
    @staticmethod
    def find_by_id_and_api_key(device_id: str, api_key: str) -> Optional[Device]:
        try:
            # Get the device from the database if device_id and api_key match
            device = DeviceModel.get(
                (DeviceModel.device_id == device_id) & (DeviceModel.api_key == api_key))
        
            return Device(device.device_id, device.api_key, device.created_at)
        except peewee.DoesNotExist:
            return None
    
    @staticmethod
    def insert_device(device_id, api_key) -> None:

        now=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ");
        # Insert a new device into the database
        DeviceModel.create(
            device_id=device_id,
            api_key=api_key,
            created_at=now
        )
    @staticmethod
    def get_or_create_test_device() -> Device:
        # Creates a test device if it does not exist
        device, _ = DeviceModel.get_or_create(
            device_id="smart-band-001",
            defaults={"api_key": "test-api-key-123", "created_at": "2025-06-04T23:23:00Z"}
        )
        return Device(device.device_id, device.api_key, device.created_at)