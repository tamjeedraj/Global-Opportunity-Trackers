
# from sqlalchemy import create_engine
# from models import Base

# # SQLite database file
# engine = create_engine("sqlite:///data.db")

# # Create all tables defined in models.py
# Base.metadata.create_all(engine)

# print("Database tables created successfully!")

# # from sqlalchemy import create_engine
# # from models import Base

# # engine = create_engine("sqlite:///./data.db", connect_args={"check_same_thread": False})

# # Base.metadata.create_all(engine)
# # print("Database tables created successfully!")



from sqlalchemy import create_engine
from models import Base

# SQLite database file (relative path)
engine = create_engine("sqlite:///./data.db", connect_args={"check_same_thread": False})

# Create all tables defined in models.py
Base.metadata.create_all(bind=engine)

print("Database tables created successfully!")
