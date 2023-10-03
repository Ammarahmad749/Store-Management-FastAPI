from typing import Union
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from sqlalchemy import func
from sqlalchemy.orm import Session
from pydantic import BaseModel

from data_model.models import Sale, Product, Category
from data_model.enums import Durations


class Sales(BaseModel):

    @staticmethod
    def get_sales(
        db: Session,
        duration: Union[Durations, None],
        product_name: Union[str,None] = None,
        category_name: Union[str,None] = None,
        period_start_date: Union[datetime, None]= None,
        period_end_date: Union[datetime, None]= None
    ):

        filters_params = [Product.id == Sale.product_id,Product.category_id == Category.id]

        if duration is not None and (period_end_date is None and period_start_date is None):
            start_date, end_date = Sales.get_start_and_end_date(duration)

            filters_params.append(
                Sale.created_at <= start_date
            )
            filters_params.append(
                Sale.created_at >= end_date
            )

        elif period_start_date and period_end_date:

            filters_params.append(
                Sale.created_at <= period_start_date
            )
            filters_params.append(
                Sale.created_at >= period_end_date
            )

        if product_name is not None:
            filters_params.append(
                func.lower(Product.product_name) == func.lower(product_name)
            )

        if category_name is not None:
            filters_params.append(
                func.lower(Category.category_name) == func.lower(category_name)
            )

        return db.query(Sale).join(Product).join(Category).filter(*filters_params).all()

    @staticmethod
    def get_start_and_end_date(duration):
        if duration == Durations.DAILY:
            start_date = datetime.utcnow()
            return start_date, start_date
        elif duration == Durations.WEEKLY:
            start_date = datetime.utcnow()
            end_date = start_date - timedelta(days=7)
            return start_date, end_date
        elif duration == Durations.MONTHLY:
            start_date = datetime.utcnow()
            end_date = start_date - relativedelta(months=1)
            return start_date, end_date
        elif duration == Durations.ANNUAL:
            start_date = datetime.utcnow()
            end_date = start_date - relativedelta(years=1)
            return start_date, end_date
        return datetime.utcnow(), datetime.utcnow()

    @staticmethod
    def get_sale_by_id(sale_id: int, db: Session):
        return db.query(Sale).filter(Sale.id == sale_id).first()
