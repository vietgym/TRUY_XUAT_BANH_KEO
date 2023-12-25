from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime
from sqlalchemy.orm import Session

from app.schemas.schemas import Product, ProductBase
from app.db.database import get_db
from app.services.service_product import ProductService

router = APIRouter()


@router.post("/creat_product/")
async def creat_user(product: ProductBase,
                     db: Session = Depends(get_db)):
    pro_service = ProductService(db=db)
    pro_response = await pro_service.creat_product(product=product)
    return pro_response


@router.put("/update_product_by_id/{pro_id}/")
async def update_product_by_id(pro_id: str,
                               pro_update: ProductBase,
                               db: Session = Depends(get_db)):
    pro_service = ProductService(db=db)
    pro_response = await pro_service.update_product(pro_id=pro_id, pro_update=pro_update)
    return pro_response


@router.get("/get_product_by_id/{pro_id}/")
async def get_product_by_id(pro_id: str,
                            db: Session = Depends(get_db)):
    pro_service = ProductService(db=db)
    pro_response = await pro_service.get_product(pro_id=pro_id)
    return pro_response


@router.get("/get_all_products/{skip}/{limit}/")
async def get_all_products(skip: int,
                           limit: int,
                           db: Session = Depends(get_db)):
    pro_service = ProductService(db=db)
    pro_response = await pro_service.get_all_product(skip=skip, limit=limit)
    return pro_response


@router.delete("/delete_product/{pro_id}/")
async def delete_product_by_id(pro_id: str,
                               db: Session = Depends(get_db)):
    pro_service = ProductService(db=db)
    pro_response = await pro_service.delete_product_by_id(pro_id=pro_id)
    return pro_response