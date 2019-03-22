from sqlalchemy import Column, String, Integer, ForeignKey, Numeric, Date
from sqlalchemy.orm import relationship
from Models.Model import Model

class Client(Model):

    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True, nullable=False,autoincrement=True)
    name = Column(String(200), nullable=True)
    phone = Column(String(30), nullable=True)
    email = Column(String(200), nullable=True)
    positions = relationship("Position")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "positions": [pos.serialize() for pos in self.positions],
        }
