from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from models.categories import Categories
from data_model.interface import CategoriesModel

from settings import get_session

category_router = APIRouter(prefix="/categories",
                            tags=["Category Management"])


@category_router.post("",
                      summary="Create Categories",
                      description="Create Categories")
def create_category(
        model: CategoriesModel,
        db: Session = Depends(get_session)):
    return Categories().create_category(model, db)


@category_router.get("",
                     summary="Get Categories",
                     description="Get Categories")
def get_categories(
        db: Session = Depends(get_session)):
    return Categories.get_categories(db)


@category_router.get("/{category_id}",
                     summary="Get Category Details By Id",
                     description="Get Category Details By Id.")
def get_product_by_id(
        category_id: int,
        db: Session = Depends(get_session)):
    return Categories.get_category_by_id(category_id, db)
