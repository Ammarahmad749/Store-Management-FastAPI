from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    types,
    Boolean,
    BIGINT,
    String,
    ForeignKey,
    Table,
    Float,
    func,
    Index,
    ARRAY,
    JSON
)
from sqlalchemy.orm import relationship

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    created_at = Column(types.TIMESTAMP, server_default=func.now())
    updated_at = Column(
        types.TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp()
    )
    is_active = Column(Boolean, nullable=False, server_default="1")

class ProductInventoryAssociation(BaseModel):
    __tablename__ = 'product_inventory_association'
    id = Column(BIGINT, primary_key=True)
    product_id = Column(BIGINT, ForeignKey('products.id'))
    inventory_id = Column(BIGINT, ForeignKey('inventory.id'))
    current_stock = Column(BIGINT, nullable=False)
    low_stock_alert_threshold = Column(BIGINT, nullable=False)
    update_transition_history = Column(ARRAY(JSON), nullable=True)


class Category(BaseModel):
    __tablename__ = 'categories'
    id = Column(BIGINT, primary_key=True)
    category_name = Column(String, nullable=False)
    products = relationship('Product', backref='category', lazy='dynamic')

    __table_args__ = (Index('idx_category', 'id', 'category_name'),)


class Product(BaseModel):
    __tablename__ = 'products'
    id = Column(BIGINT, primary_key=True)
    product_name = Column(String, nullable=False)
    price = Column(BIGINT, nullable=False)
    description = Column(String)
    category_id = Column(BIGINT, ForeignKey('categories.id'), nullable=False)
    inventories = relationship(
        'Inventory', secondary=ProductInventoryAssociation.__tablename__, back_populates='products')
    sales = relationship('Sale', backref='product', lazy='dynamic')

    __table_args__ = (
        Index('idx_product', 'id', 'category_id', 'product_name'),)


class Inventory(BaseModel):
    __tablename__ = 'inventory'
    id = Column(BIGINT, primary_key=True)
    inventory_name = Column(String, nullable=False)
    products = relationship(
        'Product', secondary=ProductInventoryAssociation.__tablename__, back_populates='inventories')

    __table_args__ = (Index('idx_inventory', 'id', 'inventory_name'),)


class Sale(BaseModel):
    __tablename__ = 'sales'

    id = Column(BIGINT, primary_key=True)
    product_id = Column(BIGINT, ForeignKey(
        'products.id'), nullable=False)
    quantity = Column(BIGINT, nullable=False)
    revenue = Column(Float, nullable=False)

    __table_args__ = (Index('idx_sale', 'id', 'product_id', 'revenue'),)
