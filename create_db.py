from sqlalchemy import create_engine,  Table, Column, Integer, String, MetaData

engine = create_engine('sqlite:///foo.db')

metadata = MetaData()
users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String),
    Column('description', String),
    Column('choices', String)
)

metadata.create_all(engine)
