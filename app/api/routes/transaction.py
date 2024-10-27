from fastapi import APIRouter
from api.deps import SessionDep
import api.applications.transaction.transaction_controller as TransactionController

router = APIRouter()

@router.get('/{transaction_id}')
def get_transaction(session: SessionDep, transaction_id: int):
  return TransactionController.read_transaction(session, transaction_id)

@router.post('/')
def create_transaction():
  return "Create transaction"

@router.delete('/{transaction_id}')
def delete_transaction(session: SessionDep, transaction_id: int):
  return TransactionController.delete_transaction(session, transaction_id)

@router.put('/')
def update_transaction():
  return "Update transaction"