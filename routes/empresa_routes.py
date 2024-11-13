from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/empresa")
templates = Jinja2Templates("templates")

@router.get("/cuponsativos")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/empresa/cuponsativos.html", view_model)

@router.get("/index")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/empresa/index.html", view_model)

@router.get("/editarperfilempresa")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/empresa/editarperfilempresa.html", view_model)

@router.get("/adicionarcupom")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/empresa/adicionarcupom.html", view_model)

@router.get("/estatisticas")
def get_root(request: Request):
    options = [
        {"value": "2021", "label": "2021"},
        {"value": "2022", "label": "2022"},
        {"value": "2023", "label": "2023"},
        {"value": "2024", "label": "2024"},
    ]
    view_model = {"request": request, "options": options}
    return templates.TemplateResponse("main/pages/empresa/estatisticas.html", view_model)

@router.get("/mensagens")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/empresa/mensagens.html", view_model)

@router.get("/politicaprivacidade")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/empresa/politicaprivacidade.html", view_model)

@router.get("/termosdeuso")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/empresa/termosdeuso.html", view_model)

@router.get("/contato")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/empresa/contato.html", view_model)