from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/empresa")
templates = Jinja2Templates("templates")

@router.get("/editarperfilempresa")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/empresa/editarperfilempresa.html", view_model)

@router.get("/cuponsativos")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/empresa/cuponsativos.html", view_model)

@router.get("/perfilempresa")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/empresa/perfilempresa.html", view_model)

@router.get("/adicionarcupom")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/empresa/adicionarcupom.html", view_model)

@router.get("/estatisticas")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/empresa/estatisticas.html", view_model)