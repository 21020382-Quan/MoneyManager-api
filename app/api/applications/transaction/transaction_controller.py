import base64
from fastapi import File, HTTPException, UploadFile
from models.transactions import Transaction
from sqlmodel import Session, select
from core.config import settings

def read_transaction(session: Session, transaction_id: int) -> Transaction:
  db_transaction = session.get(Transaction, transaction_id)
  if not db_transaction:
    raise HTTPException(status_code=404, detail="Transaction not found")
  return db_transaction

def delete_transaction(session: Session, transaction_id: int):
  db_transaction = session.delete(Transaction, transaction_id)
  if not db_transaction:
    raise HTTPException(status_code=404, detail="Transaction not found")
  return db_transaction