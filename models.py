from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from database import Base

class Url(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    short_code = Column(String, unique=True, index=True)
    original_url = Column(String, nullable=False)