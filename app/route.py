from fastapi import APIRouter
from app.api.endpoint import login, user, product, trans, user_current

router = APIRouter()
router.include_router(login.router, tags=["login"])
router.include_router(user.router, tags=["User"])
router.include_router(product.router, tags=["Product"])
router.include_router(trans.router, tags=["Trans"])
router.include_router(user_current.router, tags=["User_current"])
