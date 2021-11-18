from typing import List, Optional


from pydantic import BaseModel




class DisciplineBase(BaseModel):

	discipline: str
	professor: Optional[str] 


class NoteBase(BaseModel):

	note: Optional[str]




class DisciplineCreate(DisciplineBase):

	pass

class NoteCreate(NoteBase):

	pass


class DisciplineUpdate(DisciplineBase): 

	discipline: Optional[str] = None
	professor: Optional[str] = None

class NoteUpdate(NoteBase):
	note: Optional[str]
	
class Discipline(DisciplineBase):
	
	id : int
	class Config:
		orm_mode = True

class Note(NoteBase):
	id: int
	discipline_id : int
	class Config:
		orm_mode = True


	
# class Item(ItemBase):
#     id: int
#     owner_id: int

#     class Config:
#         orm_mode = True



# class UserBase(BaseModel):

#     email: str




# class UserCreate(UserBase):

#     password: str



# class User(UserBase):
#     id: int
#     is_active: bool
#     items: List[Item] = []

#     class Config:
#         orm_mode = True
