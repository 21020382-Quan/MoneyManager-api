from datetime import datetime

from sqlmodel import Field, Relationship, SQLModel

class CategoryBase(SQLModel):
    user_name: str = Field(unique=True, index=True)
    category_name: str 

# Database model, database table inferred from class name
class Category(CategoryBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime | None = Field(default_factory=datetime.now)
    updated_at: datetime | None = Field(default_factory=datetime.now)

    class Config:
        from_attributes = True
