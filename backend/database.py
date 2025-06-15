from sqlalchemy import create_engine, Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
import uuid

DATABASE_URL = "sqlite:///./complaints.db"
Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

class Complaint(Base):
    __tablename__ = "complaints"
    complaint_id = Column(String, primary_key=True, index=True)
    name = Column(String)
    phone_number = Column(String)
    email = Column(String)
    complaint_details = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

Base.metadata.create_all(bind=engine)

def create_complaint(data):
    db = SessionLocal()
    complaint_id = str(uuid.uuid4())[:8].upper()
    complaint = Complaint(complaint_id=complaint_id, **data)
    db.add(complaint)
    db.commit()
    db.refresh(complaint)
    db.close()
    return complaint

def get_complaint_by_id(complaint_id):
    db = SessionLocal()
    complaint = db.query(Complaint).filter(Complaint.complaint_id == complaint_id).first()
    db.close()
    return complaint
