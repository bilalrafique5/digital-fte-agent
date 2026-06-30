from pydantic import BaseModel
from typing import List, Dict

class ContentRequest(BaseModel):
    topic:str
    platforms:List[str] = ["LinkedIn","Twitter"]

class PlatformResult(BaseModel):
    draft:str
    final_post:str
    critic_feedback:str

class ContentResponse(BaseModel):
    status:str
    strategy:str
    results:Dict[str, PlatformResult]
