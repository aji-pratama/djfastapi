from typing import List
from fastapi import APIRouter

from api import models, schemas

api_router = APIRouter()


@api_router.post("/posts", response_model=schemas.PostSchema)
def create_post(post: schemas.PostSchema):
    return models.Post.objects.create(**post.dict())


@api_router.get("/posts", response_model=List[schemas.PostSchema])
def posts():
    return list(models.Post.objects.all())
