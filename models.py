
# from sqlalchemy import Column, Integer, String, Date, create_engine
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()

# class Opportunity(Base):
#     __tablename__ = "opportunities"
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String)
#     link = Column(String)
#     deadline = Column(Date)
#     category = Column(String)
#     tags = Column(String)
    

# from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import declarative_base

# Base = declarative_base()

# class Opportunity(Base):
#     __tablename__ = "opportunities"
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String)
#     description = Column(String)
#     category = Column(String)


# from sqlalchemy import Column, Integer, String, Date
# from database import Base

# class Opportunity(Base):
#     __tablename__ = "opportunities"

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, nullable=False)        # Opportunity का नाम
#     description = Column(String, nullable=True)   # Details/Notes
#     country = Column(String, nullable=True)       # Country field
#     deadline = Column(Date, nullable=True)        # Deadline (Date format)
#     status = Column(String, nullable=True)        # Status (Saved, Applied, Planning, etc.)

from sqlalchemy import Column, Integer, String, Date
from database import Base

class Opportunity(Base):
    __tablename__ = "opportunities"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)        # Opportunity का नाम
    description = Column(String, nullable=True)   # Details/Notes
    country = Column(String, nullable=True)       # Country field
    deadline = Column(Date, nullable=True)        # Deadline (Date format)
    status = Column(String, nullable=True)        # Status (Saved, Applied, Planning, etc.)
