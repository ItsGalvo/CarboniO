from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/centro")
templates = Jinja2Templates("templates")

@router.get("/centrodecoleta")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/centrodecoleta/centrodecoleta.html", view_model)

@router.get("/addcreditos")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/centrodecoleta/addcreditos.html", view_model)
