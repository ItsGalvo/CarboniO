from datetime import date
from fastapi import APIRouter, Request, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from models.usuario_model import Usuario
from repositories.usuario_repo import UsuarioRepo
from util.mensagens import adicionar_mensagem_erro, adicionar_mensagem_sucesso

templates = Jinja2Templates("templates")
router = APIRouter(prefix="/consumidor")

@router.get("/index")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/consumidor/index.html", view_model)

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
    usuario = request.state.usuario
    dados = UsuarioRepo.obter_dados_por_email(usuario.email)
    view_model = {"request": request, 'dados': dados}
    return templates.TemplateResponse("main/pages/consumidor/editarperfil.html", view_model)

@router.get("/cuponsusuario")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/consumidor/cuponsusuario.html", view_model)

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

@router.get("/estatisticas")
def get_root(request: Request):  
    options = [
        {"value": "2021", "label": "2021"},
        {"value": "2022", "label": "2022"},
        {"value": "2023", "label": "2023"},
        {"value": "2024", "label": "2024"},
    ]
    view_model = {"request": request, "options": options}
    return templates.TemplateResponse("main/pages/consumidor/estatisticas.html", view_model)

@router.get("/politicaprivacidade")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/consumidor/politicaprivacidade.html", view_model)

@router.get("/termosdeuso")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/consumidor/termosdeuso.html", view_model)

@router.get("/contato")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/consumidor/contato.html", view_model)

@router.post("/atualizar_dados")
async def post_dados(request: Request):
    dados = dict(await request.form())
    usuarioAutenticadoDto = (
        request.state.usuario if hasattr(request.state, "usuario") else None
    )
    dados["id"] = usuarioAutenticadoDto.id
    usuario = Usuario(**dados)
    if UsuarioRepo.atualizar_dados(usuario):
        response = RedirectResponse("/consumidor/perfil", status.HTTP_303_SEE_OTHER)
        adicionar_mensagem_sucesso(response, "Cadastro atualizado com sucesso!")
        return response
    else:
        response = RedirectResponse("/consumidor/editarperfil", status.HTTP_303_SEE_OTHER)
        adicionar_mensagem_erro(
            response,
            "Ocorreu um problema ao atualizar seu cadastro. Tente novamente mais tarde.",
        )
        return response