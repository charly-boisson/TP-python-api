from sqlalchemy import Column, String, Integer, ForeignKey, Numeric, Date
from sqlalchemy.orm import relationship
from Models.Model import Model

class Position(Model):

    __tablename__ = 'positions'
    id = Column(Integer, primary_key=True, nullable=False,autoincrement=True)
    name = Column(String(200), nullable=True)
    description = Column(String(200), nullable=True)
    tech_skills = Column(String(200), nullable=True)
    years_of_experience = Column(Integer, nullable=True)
    salary = Column(Integer, nullable=True)
    client = Column(Integer, ForeignKey('clients.id'))
    recruiter = Column(Integer, ForeignKey('recruiters.id'))
    interviews = relationship("Interview")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "tech_skills": self.tech_skills,
            "years_of_experience": self.years_of_experience,
            "salary": self.salary,
            "client": self.client,
            "recruiter": self.recruiter,
            "interviews": [itv.serialize() for itv in self.interviews],
        }
