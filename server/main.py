from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model import TODO

from database import *

app = FastAPI()

origins = ['http://localhost:3000',]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.get('/healthCheck')
async def healthCheck():
    return {"message":"working"}


@app.get('/todo-list')
async def get_todo():
    
    resp = await find_all_doc()
    return resp


@app.get('/todo-list/{todo}',response_model=TODO)
async def get_todo_by_title(todo):
    
    response = await find_one_doc(todo)
    if response:
        return response
    raise HTTPException(404, f"There is no todo with the title {todo}")


@app.post("/todo-list", response_model=TODO)
async def post_todo(todo: TODO):
    response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong")

@app.put("/todo-list/{todo}",response_model=TODO)
async def put_todo(todo:str,desc:str):
    # todo_item = dict(todo_item)
    # print(todo_item)
    # todo = todo_item['todo']
    # print(todo)
    # desc = todo_item['description']
    # print(desc)

    response = await update_todo_desc(todo,desc)
    if response:
        return response
    raise HTTPException(404,f'there is no {todo}')

@app.delete('/todo-list/{todo}')
async def delete_todo(todo):
    response = await remove_todo(todo)
    if response:
        return "Successfully deleted todo"
    raise HTTPException(404, f"There is no todo with the title {todo}")