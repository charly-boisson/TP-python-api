from sqlalchemy import Column, String, Integer, ForeignKey, Numeric, Date
from sqlalchemy.orm import relationship
from Models.Model import Model

class Interview(Model):

    __tablename__ = 'interviews'
    id = Column(Integer, primary_key=True, nullable=False,autoincrement=True)
    date = Column(Date, nullable=True)
    feedback = Column(String(200), nullable=True)
    position = Column(Integer, ForeignKey('positions.id'))
    recruiter_id = Column(Integer, ForeignKey('recruiters.id'))
    candidate = Column(Integer, ForeignKey('candidates.id'))

    def serialize(self):
        return {
            "id": self.id,
            "date": self.date,
            "feedback": self.feedback,
            "position": self.position,
            "recruiter_id": self.recruiter_id,
            "candidate": self.candidate,
        }
