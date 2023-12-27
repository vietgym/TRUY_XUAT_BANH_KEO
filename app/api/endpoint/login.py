from fastapi import Request, APIRouter, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.api.current.current import set_current_user, get_session
from app.services.service_login import LoginService
# from app.services.se

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/")
def load_rood(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.get("/login/", response_class=HTMLResponse)
def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.get("/home/")
def login(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@router.get("/example/")
async def example(request: Request, session: Session = Depends(get_session)):
    session["example_key"] = "example_value"
    return {"message": "Example route", "key": session["example_key"]}


@router.post("/login_user/")
async def get_info_user(username: str = Form(...),
                        password: str = Form(...),
                        db: Session = Depends(get_db),
                        session: Session = Depends(get_session)):
    print(f"Received username: {username}, password: {password}")
    login_service = LoginService(db=db)
    login_response = await login_service.login_user(user_lg=username, password=password)
    if login_response != "SAITKMK":
        set_current_user(session, str(login_response.userID))
        return {"result": "success", "user_id": str(login_response.userID)}
    return login_response


@router.get("/get_current_user/")
async def get_current_user(session: Session = Depends(get_session)):
    user_id = session.get("current_user_id")
    return {"user_id": user_id, "message": "Welcome to the home page!"}


@router.get("/load_register/")
def load_register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@router.post("/register_user/")
async def register_user(request: Request, db: Session = Depends(get_db)):
    form = await request.form()
    userLg = form.get("username")
    userPass = form.get("password")
    re_password = form.get("re_password")
    userName = form.get("name")
    userEmail = form.get("email")
    print(f"Received username: {userLg}, password: {userPass}, name: {userName}, email: {userEmail}")
    user_service = LoginService(db=db)
    user_new = await user_service.ck_register_user(userLg=userLg, userPass=userPass, re_password=re_password,
                                                   userName=userName, userEmail=userEmail)
    if user_new == {"message": "mat khau nhap lai khong giong"}:
        return user_new
    crt_user = await user_service.creat_user(user=user_new)
    return crt_user
