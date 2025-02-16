from sqlalchemy import (
    Integer,
    Column,
    String,
    DateTime,
    ForeignKey,
    func,
)
from sqlalchemy.orm import relationship

from app import db_manager

Base = db_manager.base


class BoilerPlateObject2(Base):
    __tablename__ = 'boiler_plate_object_2'
    parent_id = Column(Integer, ForeignKey('boiler_plate_object_1.id'))
    created_at = Column(DateTime, server_default=func.now())
    name = Column(String, nullable=False)

    # ORM-level relationship for easier access
    parent_obj = relationship('BoilerPlateObject1', back_populates='boiler_plate_object_2')

    def __repr__(self):
        return f'<BoilerPlateObject2 {self.name}>'
