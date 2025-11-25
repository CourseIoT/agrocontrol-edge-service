from sensor.domain.services import SensorRecordService
from sensor.domain.entities import SensorRecord
from sensor.infrastructure.repositories import SensorRecordRepository
from iam.infrastructure.repositories import DeviceRepository

class SensorRecordApplicationService:

    def __init__(self):
        self.sensor_record_service = SensorRecordService()
        self.sensor_record_repository = SensorRecordRepository()
        self.device_repository = DeviceRepository()

    def create_and_save_sensor_record(self, device_id: str, api_key: str, temperature: float, humidityAir: float, humidityFloor: float, levelWaterOk: bool, bombWaterOk: bool, created_at: str) -> SensorRecord:
        device = self.device_repository.find_by_id_and_api_key(device_id, api_key)

        if device is None:
            raise ValueError("Device not found")

        saved_record = self.sensor_record_service.create_sensor_record(device_id, temperature, humidityAir, humidityFloor, levelWaterOk, bombWaterOk, created_at)
        return self.sensor_record_repository.save(saved_record)

    