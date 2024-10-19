from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def get_category():
  return "Tra ve category"