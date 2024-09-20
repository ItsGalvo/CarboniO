from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/usuario")
templates = Jinja2Templates("templates/main")

@router.get("/estatisticas")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/estatisticas.html", view_model)

@router.get("/contato")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/contato.html", view_model)