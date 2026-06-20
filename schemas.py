from pydantic import BaseModel

class CreateRequest(BaseModel):
    original_url: str

class CreateResponse(BaseModel):
    short_code: str
    original_url: str
    class Config:
        from_attributes = True