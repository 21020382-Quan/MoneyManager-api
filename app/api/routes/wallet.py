from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def get_transaction():
  return "Tra ve transaction"

@router.post('/')
def create_transaction():
  return "Create transaction"

@router.delete('/')
def delete_transaction():
  return "Delete transaction" 

@router.put('/')
def update_transaction():
  return "Update transaction"

