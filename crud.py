from sqlalchemy.orm import Session
from . import models

# User CRUD
def create_user(db: Session, email: str, password: str, role: str):
    db_user = models.User(email=email, password=password, role=role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def delete_user(db: Session, user_id: int):
    user = get_user(db, user_id)
    if user:
        db.delete(user)
        db.commit()
        return user
    return None

# Report CRUD
def create_report(db: Session, title: str, content: str, tags: str, geo_codes: dict, category_id: int):
    db_report = models.Report(title=title, content=content, tags=tags, geo_codes=geo_codes, category_id=category_id)
    db.add(db_report)
    db.commit()
    db.refresh(db_report)
    return db_report

def get_report(db: Session, report_id: int):
    return db.query(models.Report).filter(models.Report.id == report_id).first()

def update_report(db: Session, report_id: int, update_data: dict):
    db_report = get_report(db, report_id)
    if db_report:
        for key, value in update_data.items():
            setattr(db_report, key, value)
        db.commit()
        db.refresh(db_report)
        return db_report
    return None

def delete_report(db: Session, report_id: int):
    report = get_report(db, report_id)
    if report:
        db.delete(report)
        db.commit()
        return report
    return None

# Staff CRUD
def create_staff(db: Session, name: str, role: str, user_id: int):
    db_staff = models.Staff(name=name, role=role, user_id=user_id)
    db.add(db_staff)
    db.commit()
    db.refresh(db_staff)
    return db_staff

def get_staff(db: Session, staff_id: int):
    return db.query(models.Staff).filter(models.Staff.id == staff_id).first()

def delete_staff(db: Session, staff_id: int):
    staff = get_staff(db, staff_id)
    if staff:
        db.delete(staff)
        db.commit()
        return staff
    return None
