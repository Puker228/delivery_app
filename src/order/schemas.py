from datetime import datetime

from typing import Optional
from pydantic import BaseModel

from selling_point.schemas import SellingPointGet
from cart.schemas import CartGet
from order_status.schemas import StatusGet


class OrderGet(BaseModel):

    id: int
    selling_point_id: Optional[SellingPointGet] = None
    cart: Optional[CartGet] = None

    amount: int
    sum: float

    created_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None

    status_id: Optional[StatusGet] = None
    is_active: Optional[bool] = True


class OrderCreate(BaseModel):
    selling_point_id: int

    amount: int
    sum: float

    status_id: int
    is_active: Optional[bool] = True


class OrderUpdate(BaseModel):
    selling_point_id: int

    amount: int
    sum: float

    completed_at: Optional[datetime] = None

    status_id: int
    is_active: Optional[bool] = True

