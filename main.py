from fastapi import FastAPI, Depends, HTTPException,status
from sqlalchemy.orm import Session
from . import crud, models, schemas, auth
from .dependencies import get_db
from auth import create_access_token,authenticate_user
app = FastAPI()

# User registration endpoint
@app.post("/register", response_model=schemas.UserResponse)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user.email, user.password, user.role)
@app.post("/login")
async def login(info:schemas.LoginRequest , db: Session = Depends(get_db)):
    user = authenticate_user(db, info.email, info.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.email, "role": user.role})
    return {"access_token": access_token, "token_type": "bearer"}
# Get user by ID
@app.get("/users/{user_id}", response_model=schemas.UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Create a new report
@app.post("/reports/", response_model=schemas.ReportResponse)
def create_report(report: schemas.ReportCreate, db: Session = Depends(get_db)):
    return crud.create_report(db, report.title, report.content, report.tags, report.geo_codes, report.category_id)

# Update a report
@app.put("/reports/{report_id}", response_model=schemas.ReportResponse)
def update_report(report_id: int, report: schemas.ReportUpdate, db: Session = Depends(get_db)):
    updated_report = crud.update_report(db, report_id, report.dict(exclude_unset=True))
    if updated_report is None:
        raise HTTPException(status_code=404, detail="Report not found")
    return updated_report

# Delete a report
@app.delete("/reports/{report_id}", response_model=schemas.ReportResponse)
def delete_report(report_id: int, db: Session = Depends(get_db)):
    deleted_report = crud.delete_report(db, report_id)
    if deleted_report is None:
        raise HTTPException(status_code=404, detail="Report not found")
    return deleted_report

# Create staff
@app.post("/staff/", response_model=schemas.StaffResponse)
def create_staff(staff: schemas.StaffCreate, db: Session = Depends(get_db)):
    return crud.create_staff(db, staff.name, staff.role, staff.user_id)

# Delete staff
@app.delete("/staff/{staff_id}", response_model=schemas.StaffResponse)
def delete_staff(staff_id: int, db: Session = Depends(get_db)):
    deleted_staff = crud.delete_staff(db, staff_id)
    if deleted_staff is None:
        raise HTTPException(status_code=404, detail="Staff not found")
    return deleted_staff
