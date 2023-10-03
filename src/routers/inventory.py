from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from data_model.interface import InventoryModel, ProductInventoryModel, ProductStockUpdate
from models.inventory import Inventories

from settings import get_session

inventory_rotuer = APIRouter(prefix="/inventory",
                             tags=["Inventory Management"])


@inventory_rotuer.post("",
                       summary="Create Inventory",
                       description="Create Inventory")
def create_inventory(
        model: InventoryModel,
        db: Session = Depends(get_session)):
    return Inventories().create_inventory(model, db)


@inventory_rotuer.post("/add-product",
                       summary="Add product to Inventory",
                       description="Add product to Inventory")
def add_product_to_inventory(
        model: ProductInventoryModel,
        db: Session = Depends(get_session)):
    return Inventories().add_product_to_inventory(model, db)


@inventory_rotuer.get("",
                      summary="Get Inventories",
                      description="Get Inventories")
def get_inventories(
        db: Session = Depends(get_session)):
    return Inventories.get_all_inventories(db)


@inventory_rotuer.get("/{inventory_id}",
                      summary="Get Inventory Details By Id",
                      description="Get Inventory Details By Id along with product in it.")
def get_inventory_by_id(
        inventory_id: int,
        db: Session = Depends(get_session)):
    return Inventories.get_inventory_by_id(inventory_id, db)

@inventory_rotuer.patch("",
                      summary="Update Inventory Stock",
                      description="Update Inventory Stock.")
def update_stock(
        model: ProductStockUpdate,
        db: Session = Depends(get_session)):
    return Inventories().update_product_inventory_stock(model, db)
