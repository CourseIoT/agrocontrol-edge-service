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

    def create_and_save_sensor_record(self, 
                                      device_id: str, 
                                      api_key: str, 
                                      airHumidity: float, 
                                      airTemperature: float, 
                                      soilMoisture1: int,
                                      soilMoisture2: int,
                                      soilMoisture3: int,
                                      avgSoilMoisture: int,
                                      pumpState: bool, 
                                      created_at: str) -> SensorRecord:
            
        device = self.device_repository.find_by_id_and_api_key(device_id, api_key)
        if device is None:
            raise ValueError("Authentication failed: Invalid device ID or API key")
        
        # 2. Validación de Datos (Negocio)
        try:
            self.validate_values(airTemperature, airHumidity, avgSoilMoisture)
        except ValueError as ve:
            raise ValueError(f"Validation error: {str(ve)}")
        
        saved_sensor_record = self.sensor_record_service.create_sensor_record(
            device_id=device_id, 
            airHumidity=airHumidity, 
            airTemperature=airTemperature, 
            soilMoisture1=soilMoisture1,
            soilMoisture2=soilMoisture2,
            soilMoisture3=soilMoisture3,
            avgSoilMoisture=avgSoilMoisture,
            pumpState=pumpState, 
            created_at_str=created_at
        )

        print(f"eee {saved_sensor_record.device_id}, {soilMoisture2}, {soilMoisture3}")

        return self.sensor_record_repository.save(saved_sensor_record)
    
        # 5. Envío a API Externa (Cloud)
        try:
             pass 
        except Exception as e:
            print(f"Warning: Failed to sync with cloud: {e}")
            return self.sensor_record_repository.save(saved_sensor_record)
    
    def validate_values(self, airTemperature: float, airHumidity: float, avgSoilMoisture: int) -> None:
        return None