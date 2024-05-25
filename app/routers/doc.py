from pydantic import BaseModel
from typing import List
from fastapi import APIRouter


class Doc(BaseModel):
    name: str
    description: str
    tags: List[str]
    bin: bytearray


router = APIRouter(
    prefix='/doc',
    tags=['doc']
)

@router.post('/')
async def create_document(doc: Doc):
    return { 'message': 'Docs created' }

