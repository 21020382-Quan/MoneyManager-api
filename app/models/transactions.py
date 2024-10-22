from datetime import datetime

from sqlmodel import Field, Relationship, SQLModel

class TransactionBase(SQLModel):
    pass

# Database model, database table inferred from class name
class Transaction(TransactionBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    description: str
    date: datetime
    value: int
    category_id: int
    is_notified: bool
    user_id: int
    wallet_id: int
    name: str
    image: str

    class Config:
        from_attributes = True
