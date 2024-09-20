from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/admin")
templates = Jinja2Templates("templates/main")


@router.get("/index_adm")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/index_adm.html", view_model)

@router.get("/addempresa")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/addempresa.html", view_model)

@router.get("/login_admin")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/login_admin.html", view_model)
