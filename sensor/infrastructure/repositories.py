from sensor.domain.entities import SensorRecord
from sensor.infrastructure.models import SensorDataRecord as SensorDataRecordModel

# SensorRecord Repository
# Handle sensor data
class SensorRecordRepository:

    @staticmethod
    def save(sensor_record: SensorRecord) -> SensorRecord:
        record = SensorDataRecordModel.create(
            device_id = sensor_record.device_id,
            airHumidity = sensor_record.airHumidity,
            airTemperature = sensor_record.airTemperature,
            soilMoisture1 = sensor_record.soilMoisture1,
            soilMoisture2 = sensor_record.soilMoisture2,
            soilMoisture3 = sensor_record.soilMoisture3,
            avgSoilMoisture = sensor_record.avgSoilMoisture,
            pumpState = sensor_record.pumpState,
            created_at = sensor_record.created_at
        )

        return SensorRecord(
            device_id = record.device_id,
            airHumidity = record.airHumidity,
            airTemperature = record.airTemperature,
            soilMoisture1 = record.soilMoisture1,
            soilMoisture2 = record.soilMoisture2,
            soilMoisture3 = record.soilMoisture3,
            avgSoilMoisture = record.avgSoilMoisture,
            pumpState = record.pumpState,
            created_at = record.created_at
        )