from pydantic import BaseModel


class PostSchema(BaseModel):
    title: str
    body: str = None

    class Config:
        orm_mode = True
