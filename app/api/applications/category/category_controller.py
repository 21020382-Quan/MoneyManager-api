import base64
from fastapi import File, HTTPException, UploadFile
from models.categories import Category
from sqlmodel import Session, select
from core.config import settings

def read_category(session: Session, category_id: int) -> Category:
  db_category = session.get(Category, category_id)
  if not db_category:
    raise HTTPException(status_code=404, detail="Category not found")
  return db_category

def delete_category(session: Session, category_id: int):
  db_category = session.delete(Category, category_id)
  if not db_category:
    raise HTTPException(status_code=404, detail="Category not found")
  return db_category