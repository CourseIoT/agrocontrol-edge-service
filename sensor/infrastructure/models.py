from peewee import Model, AutoField, FloatField, BooleanField, CharField, DateTimeField

from shared.infastructure.database import database as edge_database

class SensorDataRecord(Model):
    device_id = CharField()
    temperature = FloatField()
    humidityAir = FloatField()
    humidityFloor = FloatField()
    levelWaterOk = BooleanField()
    bombWaterOk = BooleanField()
    created_at = DateTimeField()

    class Meta:
        database = edge_database
        table_name = 'sensor_data'