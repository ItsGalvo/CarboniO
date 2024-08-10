from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from util.templates import obter_jinja_templates



router = APIRouter()
templates = obter_jinja_templates("templates/main")

@router.get("/")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/index.html", view_model)

@router.get("/contato")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/contato.html", view_model)

@router.get("/store")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/store.html", view_model)

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

@router.get("/carrinho")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/carrinho.html", view_model)


@router.get("/perfil")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/perfil.html", view_model)

@router.get("/perfil empresa")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/perfil empresa.html", view_model)

@router.get("/", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/index.html", {"request": request})

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from util.templates import obter_jinja_templates



router = APIRouter()
templates = obter_jinja_templates("templates/main")

@router.get("/")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/index.html", view_model)

@router.get("/contato")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/contato.html", view_model)

@router.get("/store")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/store.html", view_model)

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

@router.get("/carrinho")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/carrinho.html", view_model)


@router.get("/perfil")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/perfil.html", view_model)

@router.get("/perfil empresa")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/perfil empresa.html", view_model)

@router.get("/", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/index.html", {"request": request})
