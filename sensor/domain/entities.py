from datetime import datetime

class SensorRecord:

    def __init__(self, device_id: str, airHumidity: float, airTemperature: float, soilMoisture1: int, soilMoisture2: int, soilMoisture3: int, avgSoilMoisture: int, pumpState: bool, created_at: datetime):
        self.device_id = device_id
        self.airHumidity = airHumidity
        self.airTemperature = airTemperature
        self.soilMoisture1 = soilMoisture1
        self.soilMoisture2 = soilMoisture2
        self.soilMoisture3 = soilMoisture3
        self.avgSoilMoisture = avgSoilMoisture
        self.pumpState = pumpState
        self.created_at = created_at