from datetime import datetime

from sqlmodel import Field, Relationship, SQLModel

class CategoryBase(SQLModel):
    pass

# Database model, database table inferred from class name
class Category(CategoryBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_name: str = Field(unique=True, index=True)
    category_name: str 
    created_at: datetime | None = Field(default_factory=datetime.now)
    updated_at: datetime | None = Field(default_factory=datetime.now)

    class Config:
        from_attributes = True
