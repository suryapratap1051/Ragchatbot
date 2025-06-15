from fastapi import FastAPI, HTTPException
from backend.database import create_complaint, get_complaint_by_id
from backend.models import ComplaintRequest, ComplaintResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.post("/complaints", response_model=ComplaintResponse)
def post_complaint(data: ComplaintRequest):
    complaint = create_complaint(data.dict())
    return {"complaint_id": complaint.complaint_id, "message": "Complaint created successfully"}

@app.get("/complaints/{complaint_id}")
def get_complaint(complaint_id: str):
    complaint = get_complaint_by_id(complaint_id)
    if complaint is None:
        raise HTTPException(status_code=404, detail="Complaint not found")
    return {
        "complaint_id": complaint.complaint_id,
        "name": complaint.name,
        "phone_number": complaint.phone_number,
        "email": complaint.email,
        "complaint_details": complaint.complaint_details,
        "created_at": complaint.created_at
    }
