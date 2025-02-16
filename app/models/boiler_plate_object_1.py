from sqlalchemy import (
    Column,
    DateTime,
    func,
)

from app import db_manager

Base = db_manager.base


class BoilerPlateObject1(Base):
    __tablename__ = 'boiler_plate_object_1'
    created_at = Column(DateTime, server_default=func.now())
