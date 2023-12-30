from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.schemas.schemas import Trans, TransBase
from app.db.database import get_db
from app.services.service_trans import TransService
from app.api.current.current import get_session

router = APIRouter()


@router.post("/creat_trans/")
async def creat_user(user_id: str, product_id: str,
                     db: Session = Depends(get_db)):
    trans_service = TransService(db=db)
    trans_response = await trans_service.creat_trans(user_id=user_id,
                                                     product_id=product_id)
    return trans_response


@router.post("/creat_trans_FE/")
async def creat_trans_fe(request: Request,
                         db: Session = Depends(get_db),
                         session: Session = Depends(get_session)):
    data = await request.json()
    product_id = data.get("product_id")
    user_id = session.get("current_user_id")
    print(f"Nhận được user_id: {user_id}, product_id: {product_id}")
    trans_service = TransService(db=db)
    trans_response = await trans_service.creat_trans(user_id=user_id,
                                                     product_id=product_id)
    return trans_response


@router.get("/get_trans/{trans_id}/")
async def get_trans_by_id(trans_id: str,
                          db: Session = Depends(get_db)):
    trans_service = TransService(db=db)
    trans_response = await trans_service.get_trans(trans_id=trans_id)
    return trans_response


@router.get("/get_full_info_trans/{trans_id}/")
async def get_trans_by_id(trans_id: str,
                          db: Session = Depends(get_db)):
    trans_service = TransService(db=db)
    trans_response = await trans_service.get_full_info_trans(trans_id=trans_id)
    return trans_response


@router.get("/get_all_trans/{skip}/{limit}/")
async def get_all_trans(skip: int,
                        limit: int,
                        db: Session = Depends(get_db)):
    trans_service = TransService(db=db)
    trans_response = await trans_service.get_all_trans(skip=skip, limit=limit)
    return trans_response


@router.get("/get_all_trans_by_user_id/")
async def get_all_trans_by_user_id(user_id: str,
                                   db: Session = Depends(get_db)):
    trans_service = TransService(db=db)
    trans_response = await trans_service.get_all_trans_by_user_id(user_id=user_id)
    return trans_response


@router.delete("/delete_trans/{trans_id}/")
async def get_all_trans(trans_id: str,
                        db: Session = Depends(get_db)):
    trans_service = TransService(db=db)
    trans_response = await trans_service.delete_trans(trans_id=trans_id)
    return trans_response
