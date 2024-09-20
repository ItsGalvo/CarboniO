from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/admin")
templates = Jinja2Templates("templates")


@router.get("/index_adm")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/admin/index_adm.html", view_model)

@router.get("/addempresa")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/admin/addempresa.html", view_model)

@router.get("/login_admin")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/admin/login_admin.html", view_model)
