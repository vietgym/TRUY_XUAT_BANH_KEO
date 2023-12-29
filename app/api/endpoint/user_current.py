from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime
from sqlalchemy.orm import Session

from app.schemas.schemas import User, UserBase, UserUpdate
from app.db.database import get_db
from app.services.service_user import UserService
from app.api.current.current import set_current_user, get_session

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/user_profile/")
async def get_info_current_user(session: Session = Depends(get_session),
                                db: Session = Depends(get_db)):
    user_id = session.get("current_user_id")
    user_service = UserService(db=db)
    user_response = await user_service.get_user(user_id=user_id)
    return user_response


@router.get("/user_profile/")
async def get_info_current_user(session: Session = Depends(get_session),
                                db: Session = Depends(get_db)):
    user_id = session.get("current_user_id")
    user_service = UserService(db=db)
    user_response = await user_service.get_user(user_id=user_id)
    return user_response


# @router.post("/update_info_user/")
# async def update_info_user(data: dict, request: Request,
#                            session: Session = Depends(get_session),
#                            db: Session = Depends(get_db)):
#     user_name = data.get("editUserName")
#     email = data.get("editUserEmail")
#     print(f"Nhận được tên người dùng: {user_name}, email: {email}")
#     user_id = session.get("current_user_id")
#     user_service = UserService(db=db)
#     user_response = await user_service.update_info_user(user_id=user_id, user_name=user_name, user_email=email)
#     return user_response


@router.post("/update_info_user/")
async def update_info_user(request: Request,
                           session: Session = Depends(get_session),
                           db: Session = Depends(get_db)):
    form = await request.form()
    name = form.get("editUserName")
    email = form.get("editUserEmail")
    user_id = session.get("current_user_id")
    print(f"Nhận được tên người dùng: {name}, email: {email}")
    user_service = UserService(db=db)
    user_response = await user_service.update_info_user(user_id=user_id, user_name=name, user_email=email)
    return user_response
