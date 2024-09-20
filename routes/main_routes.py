from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/")
templates = Jinja2Templates("templates/main")

@router.get("/")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/index.html", view_model)

@router.get("/login")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/login.html", view_model)

@router.get("/termosdeuso")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/termosdeuso.html", view_model)

@router.get("/politicaprivacidade")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/politicaprivacidade.html", view_model)
