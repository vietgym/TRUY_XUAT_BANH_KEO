from fastapi import Request, APIRouter, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.services.service_login import LoginService

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/")
def load_rood(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.get("/home/")
def login(request: Request):
    return templates.TemplateResponse("addPic.html", {"request": request})


@router.post("/login_user/")
async def get_info_user(username: str = Form(...),
                        password: str = Form(...),
                        db: Session = Depends(get_db)):
    print(f"Received username: {username}, password: {password}")
    login_service = LoginService(db=db)
    login_response = await login_service.login_user(user_lg=username, password=password)
    return login_response


@router.get("/load_register/")
def load_register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})
