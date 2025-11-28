from peewee import Model, FloatField, IntegerField, BooleanField, CharField, DateTimeField

from shared.infastructure.database import database as edge_database

class SensorDataRecord(Model):
    device_id = CharField()
    airHumidity = FloatField()
    airTemperature = FloatField()
    soilMoisture1 = IntegerField()
    soilMoisture2 = IntegerField()
    soilMoisture3 = IntegerField()
    avgSoilMoisture = IntegerField()
    pumpState = BooleanField()
    created_at = DateTimeField()

    class Meta:
        database = edge_database
        table_name = 'sensor_data'