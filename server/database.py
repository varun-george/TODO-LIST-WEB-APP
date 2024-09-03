from model import TODO

import motor.motor_asyncio as driver#-> driver for mongoDB


connection_string = "mongodb://localhost:27017/"

client = driver.AsyncIOMotorClient(connection_string)

db = client.TodoList

collection = db.Collection_1_Todo


async def find_one_doc(todo):
    document = await collection.find_one({"todo":todo})
    return document

async def find_all_doc():
    todo_list = []
    documents = collection.find({})
    async for document in documents:
        todo_list.append(TODO(**document))
    return todo_list



async def create_todo(todo):
    document = todo
    result = await collection.insert_one(document)
    return document


async def update_todo_desc(todo, desc):
    await collection.update_one({"todo": todo}, {"$set": {"description": desc}})
    document = await collection.find_one({"todo": todo})
    return document

async def update_todo(todo, upt_todo):
    await collection.update_one({"todo": todo}, {"$set": {"todo": upt_todo}})
    document = await collection.find_one({"todo": upt_todo})
    return document

async def remove_todo(todo):
    await collection.delete_one({"todo": todo})
    return True
    






