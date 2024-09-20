from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/centro")
templates = Jinja2Templates("templates/main")

@router.get("/centrodecoleta")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/centrodecoleta.html", view_model)

@router.get("/addcreditos")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("pages/addcreditos.html", view_model)
