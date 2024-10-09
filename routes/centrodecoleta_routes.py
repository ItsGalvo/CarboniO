from fastapi import APIRouter, Form, Request, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from repositories.usuario_repo import UsuarioRepo

router = APIRouter(prefix="/centrodecoleta")
templates = Jinja2Templates("templates")

@router.get("/addcreditos")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/centrodecoleta/addcreditos.html", view_model)

#@router.post("/post_cadastrar_creditos")
#async def post_cadastrar_creditos(
#    nome: str = Form(...),
#    cpf: str = Form(...),
#    creditos = Form(...),):
#    confcpf = checar_credenciais_credito(nome, cpf)
#    if confcpf == None:
#        return RedirectResponse("/addcreditos", status_code=status.HTTP_303_SEE_OTHER)
#    addcredito = obter_credito(cpf) + creditos
#    UsuarioRepo.addcreditos(addcredito)
#    return RedirectResponse("/addcreditos", status_code=status.HTTP_303_SEE_OTHER)