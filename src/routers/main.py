from fastapi import APIRouter

from routers.categories import category_router
from routers.products import product_router
from routers.inventory import inventory_rotuer
from routers.sales import sales_router

main_router = APIRouter(prefix="/api")
main_router.include_router(category_router)
main_router.include_router(product_router)
main_router.include_router(inventory_rotuer)
main_router.include_router(sales_router)
