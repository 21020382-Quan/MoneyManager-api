from datetime import datetime

from sqlmodel import Field, Relationship, SQLModel


# Shared properties
class UserBase(SQLModel):
    user_name: str = Field(unique=True, index=True)
    hashed_password: str

# Database model, database table inferred from class name
class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime | None = Field(default_factory=datetime.now)
    updated_at: datetime | None = Field(default_factory=datetime.now)

    class Config:
        from_attributes = True
