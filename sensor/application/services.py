from sensor.domain.services import SensorRecordService
from sensor.domain.entities import SensorRecord
from sensor.infrastructure.repositories import SensorRecordRepository
from iam.infrastructure.repositories import DeviceRepository
import requests

class SensorRecordApplicationService:
    
    def __init__(self):
        self.sensor_record_service = SensorRecordService()
        self.sensor_record_repository = SensorRecordRepository()
        self.device_repository = DeviceRepository()

    def create_and_save_sensor_record(self, device_id: str, api_key: str, temperature: float, humidityAir: float, humidityFloor: float, levelWaterOk: bool, bombWaterOk: bool, created_at: str) -> SensorRecord:
            
        device = self.device_repository.find_by_id_and_api_key(device_id, api_key)
        if device is None:
            raise ValueError("Authentication failed: Invalid device ID or API key")
        
        try:
            self.validate_values(temperature, humidityAir, humidityFloor)
        except ValueError as ve:
            raise ValueError(f"Validation error: {str(ve)}")
        
        saved_sensor_record = self.sensor_record_service.create_sensor_record(device_id, temperature, humidityAir, humidityFloor, levelWaterOk, bombWaterOk, created_at)

        sensor_data_record = {
            "device_id": saved_sensor_record.device_id,
            "temperature": saved_sensor_record.temperature,
            "humidityAir": saved_sensor_record.humidityAir,
            "humidityFloor": saved_sensor_record.humidityFloor,
            "levelWaterOk": saved_sensor_record.levelWaterOk,
            "bombWaterOk": saved_sensor_record.bombWaterOk,
            "created_at": created_at}

        # Todo: Put endpoint URL
        requests.post("/", json=sensor_data_record)
        return self.sensor_record_repository.save(sensor_data_record)
    
    # Validate the sensor values
    def validate_values(self, temperature: float, humidityAir: float, humidityFloor: float) -> None:
        if -10.0 > temperature < 60.0:
            raise ValueError(f"Invalid temperature: {temperature}")
        if 0.0 > humidityAir < 100.0:
            raise ValueError(f"Invalid humidityAir: {humidityAir}")
        if 0.0 > humidityFloor < 100.0:
            raise ValueError(f"Invalid humidityFloor: {humidityFloor}")