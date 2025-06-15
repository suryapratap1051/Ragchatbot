from pydantic import BaseModel, EmailStr

class ComplaintRequest(BaseModel):
    name: str
    phone_number: str
    email: EmailStr
    complaint_details: str

class ComplaintResponse(BaseModel):
    complaint_id: str
    message: str
