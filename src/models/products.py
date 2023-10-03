from sqlalchemy.orm import Session
from pydantic import BaseModel

from data_model.models import Product


class Products(BaseModel):

    def create_product(self, payload, db: Session):
        product = Product(**payload.dict())
        db.begin()
        db.add(product)
        db.commit()
        db.refresh(product)
        return product

    @staticmethod
    def get_products(db: Session):
        return db.query(Product).all()

    @staticmethod
    def get_product_by_id(product_id: int, db: Session):
        return db.query(Product).filter(Product.id == product_id).first()
