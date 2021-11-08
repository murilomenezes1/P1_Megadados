from typing import Optional, List

from fastapi import FastAPI, Query, Form

from pydantic import BaseModel

from fastapi.encoders import jsonable_encoder



class Discipline(BaseModel):
	name: str
	professor: Optional[str] = None
	notes: List[Optional[str]] = None


app = FastAPI()

classes = {}
discipline_list = set()
notes_list = []
disc_notes_list = []


@app.post("/AddDiscipline/",
	response_model=Discipline)
async def create_item(item: Discipline):

	discipline_dict = item.dict()
	if discipline_dict['name'] not in discipline_list and (discipline_dict['professor'] != ("string" or "")) and (discipline_dict['notes'] != ("string" or "")) :
		classes[discipline_dict['name']] = {'professor': discipline_dict['professor'], 'notes':discipline_dict['notes']}
	else: 
		classes[discipline_dict['name']] = {'professor': None , 'notes': []}

	return discipline_dict

@app.get("/ReadDisciplines/")
async def read_items():

	for i in classes.keys():
		discipline_list.add(i)

	return discipline_list

@app.delete("/DeleteDiscipline")
async def delete_item(discipline_name: str):

	del classes[name]

	return classes

@app.put("/UpdateDiscipline")
async def update_item(name: str, new_name: str = Query(None), professor: str = Query(None), notes: str = Query(None)):

	if professor:
		classes[name]['professor'] = professor
	if notes:
		classes[name]['notes'] = notes
		notes_list.append(notes)
	if new_name: 
		classes[new_name] = classes[name]
		del classes[name]
		discipline_list.remove(name)



	return classes

@app.delete("/DeleteNotes")
async def delete_notes(name: str, index: int):

	del classes[name]['notes'][index]

	return classes

@app.get("/ReadNotes")
async def read_notes(name: str):

	
	disc_notes_list.append(classes[name]['notes'])

	return disc_notes_list

@app.put("/AddNotes")
async def add_notes(name: str, note: str):

	notes_list.append(note)
	classes[name]['notes'].append(note)

	return classes