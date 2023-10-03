from sqlalchemy.orm import Session
from pydantic import BaseModel

from data_model.models import Inventory, ProductInventoryAssociation


class Inventories(BaseModel):

    def create_inventory(self, payload, db: Session):
        product = Inventory(**payload.dict())
        db.begin()
        db.add(product)
        db.commit()
        db.refresh(product)
        return product

    def add_product_to_inventory(self, payload, db: Session):
        product_inventory = ProductInventoryAssociation(**payload.dict())
        db.begin()
        db.add(product_inventory)
        db.commit()
        db.refresh(product_inventory)
        return product_inventory

    def update_product_inventory_stock(self, payload, db: Session):

        db.query(ProductInventoryAssociation).filter(
            ProductInventoryAssociation.product_id == payload.product_id,
            ProductInventoryAssociation.inventory_id == payload.inventory_id
        ).update(
            values=dict(
                current_stock=ProductInventoryAssociation.current_stock + payload.current_stock
            )
        )
        db.commit()
        return 'Record Updated'

    @staticmethod
    def get_all_inventories(db: Session):
        return db.query(Inventory).all()

    @staticmethod
    def get_inventory_by_id(inventory_id: int, db: Session):
        return db.query(Inventory).filter(Inventory.id == inventory_id).first()
