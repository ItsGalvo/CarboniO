from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates("templates")
router = APIRouter(prefix="/consumidor")

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

@router.get("/ofertas")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/consumidor/ofertas.html", view_model)

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
