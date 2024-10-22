from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def get_wallet():
  return "Tra ve wallet"

