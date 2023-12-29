from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime
from sqlalchemy.orm import Session

from app.schemas.schemas import User, UserBase
from app.db.database import get_db
from app.services.service_user import UserService
from app.api.current.current import get_session

router = APIRouter()


@router.post("/creat_user/")
async def creat_user(user: UserBase,
                     db: Session = Depends(get_db)):
    user_service = UserService(db=db)
    user_service = await user_service.creat_user(user=user)
    return user_service


@router.post("/update_user_by_id/{user_id}/")
async def update_user_by_id(user_id: str,
                            user_update: UserBase,
                            db: Session = Depends(get_db)):
    user_service = UserService(db=db)
    user_response = await user_service.update_user(user_id=user_id, user_update=user_update)
    return user_response


@router.post("/update_user_test_2/")
async def update_user_test_2(name: str, email: str,
                             session: Session = Depends(get_session),
                             db: Session = Depends(get_db)):
    user_id = session.get("current_user_id")
    user_service = UserService(db=db)
    user_response = await user_service.update_info_user(user_id=user_id, user_name=name, user_email=email)
    return user_response


@router.get("/get_user_by_id/{user_id}/")
async def get_user_by_id(user_id: str,
                         db: Session = Depends(get_db)):
    user_service = UserService(db=db)
    user_response = await user_service.get_user(user_id=user_id)
    return user_response


# @router.get("/get_full_trans_user/{user_id}/")
# async def get_user_by_id(user_id: str,
#                          db: Session = Depends(get_db)):
#     pro_service = UserService(db=db)
#     pro_response = await pro_service.get_full_trans_user(user_id=user_id)
#     return pro_response


@router.get("/get_all_users/{skip}/{limit}/")
async def get_all_users(skip: int,
                        limit: int,
                        db: Session = Depends(get_db)):
    user_service = UserService(db=db)
    user_response = await user_service.get_all_user(skip=skip, limit=limit)
    return user_response


@router.delete("/delete_user/{pro_id}/")
async def delete_user_by_id(user_id: str,
                            db: Session = Depends(get_db)):
    user_service = UserService(db=db)
    user_response = await user_service.delete_user_by_id(user_id=user_id)
    return user_response
