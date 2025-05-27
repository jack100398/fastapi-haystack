from pydantic import BaseModel

class SyncRequest(BaseModel):
    id: int