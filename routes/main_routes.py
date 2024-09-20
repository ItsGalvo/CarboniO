from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates("templates")

@router.get("/")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/index.html", view_model)

@router.get("/login")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/login.html", view_model)

@router.get("/termosdeuso")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/termosdeuso.html", view_model)

@router.get("/politicaprivacidade")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/politicaprivacidade.html", view_model)

@router.get("/loginusuario")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/loginusuario.html", view_model)

@router.get("/loginempresa")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/loginempresa.html", view_model)

@router.get("/login_admin")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/login_admin.html", view_model)

@router.get("/centrodecoleta")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/centrodecoleta.html", view_model)