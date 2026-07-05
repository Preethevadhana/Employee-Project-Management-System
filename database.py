from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# MySQL Database URL
DATABASE_URL = "mysql+pymysql://root:password@localhost/enterprise_db"

# Create Engine
engine = create_engine(DATABASE_URL, echo=False)

# Create Session
SessionLocal = sessionmaker(bind=engine)

def get_db():
    return SessionLocal()