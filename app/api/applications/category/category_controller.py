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

def update_category(session: Session, category_id: int, data: Category) -> Category:
  db_category = session.get(Category, category_id)
  if not db_category:
    raise HTTPException(status_code=404, detail="category not found") 
  db_category.sqlmodel_update(data.model_dump(exclude_unset=True))

  session.commit()
  session.refresh(db_category)

  return db_category

def create_category(session: Session, data: Category) -> Category: 
  category = session.exec(select(Category).where(Category.category_name == data.category_name)).first()
  category = Category(
    user_name=data.user_name,
    category_name=data.category_name,
    created_at=data.created_at, 
    updated_at=data.updated_at,
  )
  session.add(category)
  session.commit()
  session.refresh(category)

  return category