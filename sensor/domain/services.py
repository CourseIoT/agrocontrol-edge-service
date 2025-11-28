from datetime import datetime, timezone
from dateutil.parser import parse

from sensor.domain.entities import SensorRecord

class SensorRecordService:

    def create_sensor_record(self, 
                             device_id: str, 
                             airHumidity: float, 
                             airTemperature: float, 
                             soilMoisture1: int, 
                             soilMoisture2: int, 
                             soilMoisture3: int, 
                             avgSoilMoisture: int, 
                             pumpState: bool, 
                             created_at_str: str) -> SensorRecord:
        
        created_at = parse(created_at_str)
        
        return SensorRecord(
            device_id=device_id,
            airHumidity=airHumidity,
            airTemperature=airTemperature,
            soilMoisture1=soilMoisture1,
            soilMoisture2=soilMoisture2,
            soilMoisture3=soilMoisture3,
            avgSoilMoisture=avgSoilMoisture,
            pumpState=pumpState,
            created_at=created_at
        )