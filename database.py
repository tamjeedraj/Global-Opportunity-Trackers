
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, Session
# from models import Base

# engine = create_engine("sqlite:///data.db", connect_args={"check_same_thread": False})

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base.metadata.create_all(bind=engine)


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

## def save_opportunity(opportunity, db: Session):
#     db.add(opportunity)
#     db.commit()
#     db.refresh(opportunity)
#     return opportunity


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./opportunities.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 🔹 नया function: Opportunity को DB में save करने के लिए
def save_opportunity(opportunity, db):
    db.add(opportunity)
    db.commit()
    db.refresh(opportunity)
    return opportunity
