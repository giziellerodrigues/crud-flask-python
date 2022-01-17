from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(os.getenv('DB_CONFIG_URI'))
session_factory = sessionmaker(bind=engine)