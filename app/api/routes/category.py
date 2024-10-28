from fastapi import APIRouter
from api.deps import SessionDep
import api.applications.category.category_controller as CategoryController
from models.categories import Category

router = APIRouter()

@router.get('/{category_id}')
def get_category(session: SessionDep, category_id: int):
  return CategoryController.read_category(session, category_id)

@router.post('/')
def create_category(session: SessionDep, category: Category):
  return CategoryController.create_category(session, category)

@router.delete('/{category_id}')
def delete_category(session: SessionDep, category_id: int):
  return CategoryController.delete_category(session, category_id)

@router.put('/{category_id}')
def update_category(session: SessionDep, category_id: int, category: Category):
  return CategoryController.update_category(session, category_id, category)