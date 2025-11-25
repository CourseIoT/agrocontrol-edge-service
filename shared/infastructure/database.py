from peewee import SqliteDatabase

database = SqliteDatabase('agrocontrol_edge_database.db')

def init_database() -> None:
    database.connect()
    from iam.infrastructure.models import Device
    database.create_tables([Device])
    database.close()
    