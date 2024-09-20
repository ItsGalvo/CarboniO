from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from util.templates import obter_jinja_templates

router = APIRouter(prefix="/consumidor")
templates = obter_jinja_templates("templates")

@router.get("/loginusuario")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/consumidor/loginusuario.html", view_model)

@router.get("/criarconta1")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/consumidor/criarconta1.html", view_model)

@router.get("/criarconta2")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/consumidor/criarconta2.html", view_model)

@router.get("/criarconta3")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/consumidor/criarconta3.html", view_model)

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

@router.get("/", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/consumidor/index.html", {"request": request})