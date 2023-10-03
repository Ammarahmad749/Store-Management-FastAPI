from fastapi import APIRouter

main_router = APIRouter(prefix="/api")

@main_router.get("/health")
def get_health():
    return 'Healthy System!'
