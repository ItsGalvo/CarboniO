from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from util.templates import obter_jinja_templates



router = APIRouter()
templates = obter_jinja_templates("templates/main")

@router.get("/pages/")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/index.html", view_model)

@router.get("/pages/contato")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/contato.html", view_model)

@router.get("/pages/store")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/store.html", view_model)

@router.get("/pages/teste")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/teste.html", view_model)

@router.get("/pages/carrinho")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/carrinho.html", view_model)

@router.get("/", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/index.html", {"request": request})
