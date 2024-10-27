from fastapi import APIRouter
from api.deps import SessionDep
import api.applications.category.category_controller as CategoryController

router = APIRouter()

@router.get('/{category_id}')
def get_category(session: SessionDep, category_id: int):
  return CategoryController.read_category(session, category_id)

@router.post('/')
def create_category():
  return "Create category"

@router.delete('/{category_id}')
def delete_category(session: SessionDep, category_id: int):
  return CategoryController.delete_category(session, category_id)

@router.put('/')
def update_category():
  return "Update category"