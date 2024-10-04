from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates("templates")
router = APIRouter(prefix="/usuario")

@router.get("/contato")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/usuario/contato.html", view_model)

@router.get("/termosdeuso")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/usuario/termosdeuso.html", view_model)

@router.get("/politicaprivacidade")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/usuario/politicaprivacidade.html", view_model)