from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates("templates")
router = APIRouter(prefix="/consumidor")

@router.get("/index")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/consumidor/index.html", view_model)

@router.get("/carrinho")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/consumidor/carrinho.html", view_model)

@router.get("/comeceaqui")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/consumidor/comeceaqui.html", view_model)

@router.get("/perfil")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/consumidor/perfil.html", view_model)

@router.get("/mensagens")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/consumidor/mensagens.html", view_model)

@router.get("/reembolsos")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/consumidor/reembolsos.html", view_model)

@router.get("/editarperfil")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/consumidor/editarperfil.html", view_model)

@router.get("/cuponsusuario")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/consumidor/cuponsusuario.html", view_model)

@router.get("/store")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/consumidor/store.html", view_model)

@router.get("/juntepontos")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/consumidor/juntepontos.html", view_model)

@router.get("/paginaproduto")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/consumidor/paginaproduto.html", view_model)

@router.get("/estatisticas")
def get_root(request: Request):  
    options = [
        {"value": "2021", "label": "2021"},
        {"value": "2022", "label": "2022"},
        {"value": "2023", "label": "2023"},
        {"value": "2024", "label": "2024"},
    ]
    view_model = {"request": request, "options": options}
    return templates.TemplateResponse("main/pages/consumidor/estatisticas.html", view_model)

@router.get("/politicaprivacidade")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/consumidor/politicaprivacidade.html", view_model)

@router.get("/termosdeuso")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/consumidor/termosdeuso.html", view_model)

@router.get("/contato")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/consumidor/contato.html", view_model)