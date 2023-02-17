from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import postgres_password, postgres_user, postgres_port
SQLALCHEMY_DATABASE_URL = f'postgresql://{postgres_user}:{postgres_password}@host.docker.internal:{postgres_port}/mango'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
