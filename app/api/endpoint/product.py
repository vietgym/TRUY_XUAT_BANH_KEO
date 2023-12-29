from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime
from sqlalchemy.orm import Session

from app.schemas.schemas import Product, ProductBase
from app.db.database import get_db
from app.services.service_product import ProductService
from app.api.current.current import set_current_user, get_session

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


@router.post("/edit_product/")
async def edit_product(request: Request):
    data = await request.json()
    product_id = data.get("productId")
    print("Received productId:", product_id)
    return {"message": "Product ID received successfully"}


@router.post("/edit_info_product/")
async def edit_product(request: Request,
                       session: Session = Depends(get_session),
                       db: Session = Depends(get_db)):
    form = await request.form()
    product = ProductBase(proName=form.get("productName"),
                          manufacturerAdd=form.get("manufacturerAdd"),
                          manufacturerName=form.get("manufacturerName"),
                          manufacturerCont=form.get("manufacturerCont"),
                          distributorAdd=form.get("distributorAdd"),
                          distributorName=form.get("distributorName"),
                          distributorCont=form.get("distributorCont"),
                          otherDetails=form.get("otherDetails"))
    product_id = form.get("productId")
    print(f"Nhận được Product: {product_id}")

    pro_service = ProductService(db=db)
    pro_response = await pro_service.update_product(pro_id=product_id, pro_update=product)
    return pro_response


@router.get("/get_product_by_id/{pro_id}/")
async def get_product_by_id(pro_id: str,
                            db: Session = Depends(get_db)):
    pro_service = ProductService(db=db)
    pro_response = await pro_service.get_product(pro_id=pro_id)
    return pro_response


@router.get("/get_all_products/")
async def get_all_products(db: Session = Depends(get_db)):
    pro_service = ProductService(db=db)
    pro_response = await pro_service.get_all_product(skip=0, limit=99)
    return pro_response


@router.delete("/delete_product/{pro_id}/")
async def delete_product_by_id(pro_id: str,
                               db: Session = Depends(get_db)):
    pro_service = ProductService(db=db)
    pro_response = await pro_service.delete_product_by_id(pro_id=pro_id)
    return pro_response