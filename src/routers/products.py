from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from data_model.interface import ProductModel
from models.products import Products

from settings import get_session

product_router = APIRouter(prefix="/products",
                           tags=["Product Management"])


@product_router.post("",
                     summary="Create Product",
                     description="Create Product")
def create_product(
        model: ProductModel,
        db: Session = Depends(get_session)):
    return Products().create_product(model, db)


@product_router.get("",
                    summary="Get Product",
                    description="Get Product")
def get_products(
        db: Session = Depends(get_session)):
    return Products.get_products(db)


@product_router.get("/{product_id}",
                    summary="Get Product Details By Id",
                    description="Get Product Details By Id.")
def get_product_by_id(
        product_id: int,
        db: Session = Depends(get_session)):
    return Products.get_product_by_id(product_id, db)
