from sqlalchemy import Column, String, Integer, ForeignKey, Numeric, Date
from sqlalchemy.orm import relationship
from Models.Model import Model

class Review(Model):

    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True, nullable=False,autoincrement=True)
    review_date = Column(Date, nullable=True)
    content = Column(String(200), nullable=True)
    reviewer = Column(String(200), nullable=True)
    candidate = Column(Integer, ForeignKey('candidates.id'))

    def serialize(self):
        return {
            "id": self.id,
            "review_date": self.review_date,
            "content": self.content,
            "reviewer": self.reviewer,
            "candidate": self.candidate,
        }
