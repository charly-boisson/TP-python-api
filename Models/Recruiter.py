from sqlalchemy import Column, String, Integer, ForeignKey, Numeric, Date
from sqlalchemy.orm import relationship
from Models.Model import Model

class Recruiter(Model):

    __tablename__ = 'recruiters'
    id = Column(Integer, primary_key=True, nullable=False,autoincrement=True)
    first_name = Column(String(200), nullable=False)
    last_name = Column(String(200), nullable=False)
    phone = Column(String(30), nullable=True)
    interviews = relationship("Interview")
    positions = relationship("Position")

    def serialize(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone": self.phone,
            "interviews": [itv.serialize() for itv in self.interviews],
            "positions": [pos.serialize() for pos in self.positions],
        }
