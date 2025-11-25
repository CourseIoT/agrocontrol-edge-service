from sensor.domain.entities import SensorRecord
from sensor.infrastructure.models import SensorDataRecord as SensorDataRecordModel

class SensorRecordRepository:

    @staticmethod
    def save(sensor_record) -> SensorRecord:
        record = SensorDataRecordModel.create(
            device_id=sensor_record.device_id,
            temperature=sensor_record.temperature,
            humidityAir=sensor_record.humidityAir,
            humidityFloor=sensor_record.humidityFloor,
            levelWaterOk=sensor_record.levelWaterOk,
            bombWaterOk=sensor_record.bombWaterOk,
            created_at=sensor_record.created_at
        )
        return SensorRecord(
            device_id=record.device_id,
            temperature=record.temperature,
            humidityAir=record.humidityAir,
            humidityFloor=record.humidityFloor,
            levelWaterOk=record.levelWaterOk,
            bombWaterOk=record.bombWaterOk,
            created_at=record.created_at
        )