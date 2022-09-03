from src.models.base import Base
from sqlalchemy import Column, Integer, Float


class WineResult(Base):
    __tablename__ = "wine_results"
    id = Column(Integer, primary_key=True)
    quality = Column(Integer, nullable=False)
    fixed_acidity = Column(Float)
    volatile_acidity = Column(Float)
    citric_acid = Column(Float)
    residual_sugar = Column(Float)
    chlorides = Column(Float)
    free_sulfur_dioxide = Column(Float)
    total_sulfur_dioxide = Column(Float)
    density = Column(Float)
    ph = Column(Float)
    sulphates = Column(Float)
    alcohol = Column(Float)
