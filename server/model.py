from pydantic import BaseModel

class TODO(BaseModel):
    todo : str
    description : str

