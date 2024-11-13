from pydantic import BaseModel
from typing import List, Optional, Dict

class UserCreate(BaseModel):
    email: str
    password: str
    role: str


class LoginRequest(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    email: str
    role: str

class ReportCreate(BaseModel):
    title: str
    content: str
    tags: Optional[str]
    geo_codes: Optional[Dict]
    category_id: int

class ReportUpdate(BaseModel):
    title: Optional[str]
    content: Optional[str]
    tags: Optional[str]
    geo_codes: Optional[Dict]
    category_id: Optional[int]

class ReportResponse(BaseModel):
    id: int
    title: str
    content: str
    tags: Optional[str]
    geo_codes: Optional[Dict]
    category_id: int

class StaffCreate(BaseModel):
    name: str
    role: str
    user_id: int

class StaffResponse(BaseModel):
    id: int
    name: str
    role: str
    user_id: int
