from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/empresa")
templates = Jinja2Templates("templates/main")

@router.get("/editarperfilempresa")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/editarperfilempresa.html", view_model)

@router.get("/cuponsativos")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/cuponsativos.html", view_model)

@router.get("/perfilempresa")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/perfilempresa.html", view_model)

@router.get("/loginempresa")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/loginempresa.html", view_model)

@router.get("/adicionarcupom")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/adicionarcupom.html", view_model)
