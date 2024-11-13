from sqlalchemy import Column, Integer, String, ForeignKey, Text, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Staff(Base):
    __tablename__ = "staff"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    role = Column(String)  # Can be 'editor', 'reporter', or 'desk_head'
    user_id = Column(Integer, ForeignKey("users.id"))
    
    user = relationship("User", back_populates="staff")

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(String)  # Can be 'admin', 'editor', 'reporter'
    
    staff = relationship("Staff", back_populates="user")

class Report(Base):
    __tablename__ = "reports"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(Text)
    tags = Column(String)  # Comma-separated string of tags
    geo_codes = Column(JSON)  # Store latitude/longitude as JSON
    category_id = Column(Integer, ForeignKey("categories.id"))
    attachments = Column(JSON)  # Store file paths or URLs of attachments
    category = relationship("Category", back_populates="reports")

class ReportDesk(Base):
    __tablename__ = "report_desks"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    desk_head_id = Column(Integer, ForeignKey("staff.id"))
    staff = relationship("Staff", backref="report_desks")

class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    reports = relationship("Report", back_populates="category")

class Tag(Base):
    __tablename__ = "tags"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    reports = relationship("Report", secondary="report_tags")

class ReportTag(Base):
    __tablename__ = "report_tags"
    
    report_id = Column(Integer, ForeignKey("reports.id"), primary_key=True)
    tag_id = Column(Integer, ForeignKey("tags.id"), primary_key=True)
