from fastapi import Request, APIRouter, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.services.service_login import LoginService

router = APIRouter()
templates = Jinja2Templates(directory="templates")


# @router.post("/login_user/")
# async def get_info_user(username: str = Form(...),
#                         password: str = Form(...),
#                         db: Session = Depends(get_db)):
#     print(f"Received username: {username}, password: {password}")
#     login_service = LoginService(db=db)
#     login_response = await login_service.login_user(name=username, password=password)
#     return login_response

@router.post("/login_user/")
async def get_info_user(username: str,
                        password: str,
                        db: Session = Depends(get_db)):
    print(f"Received username: {username}, password: {password}")
    login_service = LoginService(db=db)
    login_response = await login_service.login_user(user_lg=username, password=password)
    return login_response
