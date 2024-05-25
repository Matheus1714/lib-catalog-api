from fastapi import APIRouter
from .schemas import Doc

router = APIRouter(
    prefix='/doc',
    tags=['doc']
)

router.post('/')
async def create_document(doc: Doc):
    return { 'message': 'Docs created' }


