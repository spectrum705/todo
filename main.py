from typing import Optional
from fastapi import FastAPI
import uvicorn
from crud import Database
# from model import Note
import random
app = FastAPI()
db = Database()

@app.get("/add/{note}")
async def  add_note(note):
    try:
        db.add(note,str(random.randint(1,1000)))
        return {"status": "success"}, 200
    except:
        return {"status": "failed"}, 500
@app.get("/all")
def show_notes():
    try:
        note = db.show()
        return {"notes": note}, 200
    except:
        return {"status": "failed"}, 500
    
@app.get("/search/{id}")
def search_notes(id):
    try:
        note = db.search(id)
        if note:
            return {"notes": note}, 200
        else:
            return {"status": "No notes found"}, 400
    except:
        return {"status": "failed"}, 500    


@app.get("/update/{id}/{note}")
def update_note(id, note):
    try:
        db.update(id, note)
        return {"status": "success"}, 200
    except:
        return {"status": "failed"}, 500


      
@app.get("/delete/{id}")
def delete(id):
    try:
        note = db.delete(id)
        if note:
            return  note, 200
        else:
            return {"status": "No notes found"}, 400
    except:
        return {"status": "failed"}, 500    




