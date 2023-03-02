from .tables import db , Trade,ConfigTrade


def create():
    db.connect()
    db.create_tables([Trade, ConfigTrade])
