from datetime import datetime
from typing import Union
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from models.sales import Sales
from data_model.enums import Durations

from settings import get_session

sales_router = APIRouter(prefix="/sales",
                           tags=["Sales Management"])


@sales_router.get("",
                    summary="Get Sales order",
                    description="Get Sales order")
def get_sales(
        db: Session = Depends(get_session),
        duration: Union[Durations,None] = None,
        product_name: Union[str,None] = None,
        category_name: Union[str,None] = None,
        period_start_date: Union[datetime, None]= None,
        period_end_date: Union[datetime, None]= None):
    return Sales.get_sales(db,
                           duration,
                           product_name,
                           category_name,
                           period_start_date,
                           period_end_date)


@sales_router.get("/{sales_id}",
                    summary="Get Sales order Details By Id",
                    description="Get Sales order Details By Id.")
def get_sale_by_id(
        sales_id: int,
        db: Session = Depends(get_session)):
    return Sales().get_sale_by_id(sales_id, db)
