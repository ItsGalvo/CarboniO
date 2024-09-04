from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from util.templates import obter_jinja_templates



router = APIRouter()
templates = obter_jinja_templates("templates/main")

@router.get("/")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/index.html", view_model)

@router.get("/juntepontos")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/juntepontos.html", view_model)

@router.get("/contato")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/contato.html", view_model)

@router.get("/ofertas")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/ofertas.html", view_model)

@router.get("/store")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/store.html", view_model)

@router.get("/paginaproduto")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/paginaproduto.html", view_model)

@router.get("/login")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/login.html", view_model)

@router.get("/loginusuario1")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/loginusuario1.html", view_model)

@router.get("/loginusuario2")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/loginusuario2.html", view_model)

@router.get("/loginusuario3")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/loginusuario3.html", view_model)

@router.get("/loginempresa1")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/loginempresa1.html", view_model)

@router.get("/loginempresa2")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/loginempresa2.html", view_model)

@router.get("/loginempresa3")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/loginempresa3.html", view_model)

@router.get("/carrinho")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/carrinho.html", view_model)

@router.get("/comeceaqui")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/comeceaqui.html", view_model)

@router.get("/perfil")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/perfil.html", view_model)

@router.get("/mensagens")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/mensagens.html", view_model)

@router.get("/editarperfil")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/editarperfil.html", view_model)

@router.get("/adicionarcupom")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/adicionarcupom.html", view_model)

@router.get("/cuponsusuario")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/cuponsusuario.html", view_model)

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

@router.get("/", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/index.html", {"request": request})