from peewee import *

db = PostgresqlDatabase('adventures', user='postgres', password='',
                        host='localhost', port=5432)


class BaseModel (Model):
    class Meta:
        database = db

class Trash (BaseModel):
    name = CharField()
    health = IntegerField()
    attack = IntegerField()

class Boss (BaseModel):
    name = CharField()
    health = IntegerField()
    attack = IntegerField()


db.connect()
db.drop_tables([Trash])
db.create_tables([Trash])
db.drop_tables([Boss])
db.create_tables([Boss])