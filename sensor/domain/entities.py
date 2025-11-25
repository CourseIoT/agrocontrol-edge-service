from datetime import datetime

class SensorRecord:

    def __init__(self, device_id: str, temperature: float, humidityAir: float, humidityFloor: float, levelWaterOk: bool, bombWaterOk: bool, created_at: datetime):
        self.device_id = device_id
        self.temperature = temperature
        self.humidityAir = humidityAir
        self.humidityFloor = humidityFloor
        self.levelWaterOk = levelWaterOk
        self.bombWaterOk = bombWaterOk
        self.created_at = created_at