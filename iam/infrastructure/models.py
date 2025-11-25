from peewee import Model, CharField, DateTimeField
from shared.infastructure.database import database as edge_database

class Device(Model):
    device_id = CharField(primary_key=True)
    api_key = CharField()
    created_at = DateTimeField()

    class Meta:
        database = edge_database
        table_name = 'devices'    