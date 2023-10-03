from pydantic import BaseModel, Field


class CategoriesModel(BaseModel):
    category_name: str = Field(description="Name of category")


class ProductModel(BaseModel):
    product_name: str = Field(description="Name of Product")
    price: int = Field(description="Price of Product")
    description: str = Field(description="Description of Product")
    category_id: int = Field(description="Category id for product")


class InventoryModel(BaseModel):

    inventory_name: str = Field(description="Name of inventory")


class ProductInventoryModel(BaseModel):
    product_id: int = Field(description="Id of Product")
    inventory_id: int = Field(description="Id of inventory")
    current_stock: int = Field(description="No of stock")
    low_stock_alert_threshold: int = Field(description="Alert threshold")


class ProductStockUpdate(BaseModel):
    product_id: int = Field(description="Id of Product")
    inventory_id: int = Field(description="Id of inventory")
    current_stock: int = Field(description="New No of stock")
