from sqlalchemy.orm import Session
from pydantic import BaseModel

from data_model.models import Category


class Categories(BaseModel):

    def create_category(self, payload, db: Session):
        category = Category(**payload.dict())
        db.begin()
        db.add(category)
        db.commit()
        db.refresh(category)
        return category

    @staticmethod
    def get_categories(db: Session):
        return db.query(Category).all()

    @staticmethod
    def get_category_by_id(category_id: int,db: Session):
        return db.query(Category).filter(Category.id == category_id).first()
