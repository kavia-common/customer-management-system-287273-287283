from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field


# PUBLIC_INTERFACE
class CustomerBase(BaseModel):
    """Base fields shared by Customer models."""
    name: str = Field(..., description="Full name of the customer", min_length=1)
    email: EmailStr = Field(..., description="Customer email address")
    phone: str = Field(..., description="Customer phone number", min_length=3)


# PUBLIC_INTERFACE
class CustomerCreate(CustomerBase):
    """Payload to create a new customer."""
    pass


# PUBLIC_INTERFACE
class CustomerUpdate(BaseModel):
    """Payload to update an existing customer. All fields are optional."""
    name: Optional[str] = Field(None, description="Full name of the customer", min_length=1)
    email: Optional[EmailStr] = Field(None, description="Customer email address")
    phone: Optional[str] = Field(None, description="Customer phone number", min_length=3)


# PUBLIC_INTERFACE
class Customer(CustomerBase):
    """Customer model returned by the API, includes server-managed fields."""
    id: int = Field(..., description="Unique identifier for the customer")
    created_at: datetime = Field(..., description="Timestamp when the customer was created")

    class Config:
        from_attributes = True
