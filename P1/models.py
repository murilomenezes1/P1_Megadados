from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import VARCHAR

from .database import Base

class Disciplines(Base):

	__tablename__ = "Disciplines"


	id = Column(Integer, primary_key=True, index=True)
	discipline = Column(VARCHAR(100), unique=True, index=True)
	professor = Column(VARCHAR(100))

	note_db = relationship("Notes", back_populates = "discipline_db")


class Notes(Base):

	__tablename__ = "Notes"
	id = Column(Integer, primary_key=True, index=True)
	note = Column(VARCHAR(500), index=True)
	discipline_id = Column(Integer, ForeignKey("Disciplines.id", ondelete="CASCADE"))

	discipline_db = relationship("Disciplines", back_populates="note_db")






