from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import FileResponse

from database import SessionLocal
from models import LandRecord
from pdf_generator import generate_pdf

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/search/")
def search_land_record(query: str, db: Session = Depends(get_db)):
    record = db.query(LandRecord).filter(
        (LandRecord.parcel_id == query) |
        (LandRecord.plot_number == query) |
        (LandRecord.owner_name == query)
    ).first()

    if not record:
        raise HTTPException(status_code=404, detail="Record not found")

   
    record_dict = {
        "Parcel ID": record.parcel_id,
        "Plot Number": record.plot_number,
        "Owner Name": record.owner_name,
        "Area": record.area,
        "Location": record.location
    }

    pdf_path = generate_pdf(record_dict)
    return FileResponse(pdf_path, media_type='application/pdf', filename="land_record.pdf")
