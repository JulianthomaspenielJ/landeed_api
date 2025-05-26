from sqlalchemy import Column, Integer, String, Float
from database import Base

class LandRecord(Base):
    __tablename__ = "land_records"
    
    id = Column(Integer, primary_key=True, index=True)
    parcel_id = Column(String(100), index=True)
    plot_number = Column(String(100), index=True)
    owner_name = Column(String(255), index=True)
    area = Column(Float)
    location = Column(String(255))
