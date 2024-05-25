from pydantic import BaseModel
from typing import List

class Doc(BaseModel):
    name: str
    description: str
    tags: List[str]
    bin: bytearray
