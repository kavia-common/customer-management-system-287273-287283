from datetime import datetime
from typing import Dict, List, Optional

from fastapi import APIRouter, HTTPException, status

from src.api.models import Customer, CustomerCreate, CustomerUpdate

router = APIRouter(
    tags=["Customers"],
    responses={404: {"description": "Customer not found"}},
)


# In-memory storage for customers
# Note: This is a simple in-memory store for demo purposes only.
_CUSTOMERS: Dict[int, Customer] = {}
_NEXT_ID: int = 1


def _get_next_id() -> int:
    global _NEXT_ID
    next_id = _NEXT_ID
    _NEXT_ID += 1
    return next_id


def _find_customer(customer_id: int) -> Optional[Customer]:
    return _CUSTOMERS.get(customer_id)


# PUBLIC_INTERFACE
@router.get(
    "/customers",
    response_model=List[Customer],
    summary="List customers",
    description="Retrieve all customers currently stored.",
    operation_id="list_customers",
)
def get_all_customers() -> List[Customer]:
    """Return a list of all customers."""
    return list(_CUSTOMERS.values())


# PUBLIC_INTERFACE
@router.get(
    "/customers/{customer_id}",
    response_model=Customer,
    summary="Get customer by ID",
    description="Retrieve a single customer by its unique ID.",
    operation_id="get_customer_by_id",
)
def get_customer_by_id(customer_id: int) -> Customer:
    """Return a customer by ID, or 404 if not found."""
    customer = _find_customer(customer_id)
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
    return customer


# PUBLIC_INTERFACE
@router.post(
    "/customers",
    response_model=Customer,
    status_code=status.HTTP_201_CREATED,
    summary="Create customer",
    description="Create a new customer with the provided details.",
    operation_id="create_customer",
)
def create_customer(payload: CustomerCreate) -> Customer:
    """Create a new customer and return it."""
    new_id = _get_next_id()
    customer = Customer(
        id=new_id,
        name=payload.name,
        email=payload.email,
        phone=payload.phone,
        created_at=datetime.utcnow(),
    )
    _CUSTOMERS[new_id] = customer
    return customer


# PUBLIC_INTERFACE
@router.put(
    "/customers/{customer_id}",
    response_model=Customer,
    summary="Update customer",
    description="Replace the customer data for a given ID using the provided payload.",
    operation_id="update_customer",
)
def update_customer(customer_id: int, payload: CustomerUpdate) -> Customer:
    """Update an existing customer. Returns 404 if not found."""
    existing = _find_customer(customer_id)
    if not existing:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")

    updated = existing.model_copy(update={})
    if payload.name is not None:
        updated = updated.model_copy(update={"name": payload.name})
    if payload.email is not None:
        updated = updated.model_copy(update={"email": payload.email})
    if payload.phone is not None:
        updated = updated.model_copy(update={"phone": payload.phone})

    _CUSTOMERS[customer_id] = updated
    return updated


# PUBLIC_INTERFACE
@router.delete(
    "/customers/{customer_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete customer",
    description="Delete a customer by ID.",
    operation_id="delete_customer",
)
def delete_customer(customer_id: int) -> None:
    """Delete a customer. Returns 404 if not found."""
    if customer_id not in _CUSTOMERS:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
    del _CUSTOMERS[customer_id]
    return None
