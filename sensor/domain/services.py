
from datetime import datetime, timezone
from dateutil.parser import parse

from sensor.domain.entities import SensorRecord

class SensorRecordService:

    def create_sensor_record(self, device_id: str, temperature: float, humidityAir: float, humidityFloor: float, levelWaterOk: bool, bombWaterOk: bool, created_at_str: str) -> SensorRecord:
        
        created_at = parse(created_at_str)
        return SensorRecord(
            device_id=device_id,
            temperature=temperature,
            humidityAir=humidityAir,
            humidityFloor=humidityFloor,
            levelWaterOk=levelWaterOk,
            bombWaterOk=bombWaterOk,
            created_at=created_at
        )