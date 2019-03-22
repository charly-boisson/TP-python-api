from sqlalchemy import Column, String, Integer, ForeignKey, Numeric, Date
from sqlalchemy.orm import relationship
from Models.Model import Model

class Candidate(Model):

    __tablename__ = 'candidates'
    id = Column(Integer, primary_key=True, nullable=False,autoincrement=True)
    first_name = Column(String(200), nullable=False)
    last_name = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)
    birthday = Column(Date, nullable=True)
    phone = Column(String(30), nullable=True)
    languages = Column(String(500), default="")
    skills = Column(String(1000), default="")
    interviews = relationship("Interview")
    reviews = relationship("Review")

    def serialize(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "birthday": self.birthday,
            "phone": self.phone,
            "languages": self.languages,
            "skills": self.skills,
            "interviews": [itv.serialize() for itv in self.interviews],
            "reviews": [rev.serialize() for rev in self.reviews],
        }
