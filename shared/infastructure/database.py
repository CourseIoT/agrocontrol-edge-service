from peewee import SqliteDatabase

database = SqliteDatabase('agrocontrol_edge_database.db')

def init_database() -> None:
    database.connect()
    from iam.infrastructure.models import Device
    from sensor.infrastructure.models import SensorDataRecord
    database.create_tables([Device, SensorDataRecord])
    database.close()
    