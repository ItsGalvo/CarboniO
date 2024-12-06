import bcrypt
from fastapi import APIRouter, Form, Request, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from repositories.usuario_repo import UsuarioRepo
from util.mensagens import adicionar_mensagem_erro, adicionar_mensagem_sucesso

router = APIRouter(prefix="/centrodecoleta")
templates = Jinja2Templates("templates")

@router.get("/index")
def get_root(request: Request):
    centrocoleta = request.state.usuario
    dados = UsuarioRepo.obter_dados_por_email(centrocoleta.email)
    view_model = {"request": request, "dados": dados}
    return templates.TemplateResponse("main/pages/centrodecoleta/index.html", view_model)

@router.get("/politicaprivacidade")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/centrodecoleta/politicaprivacidade.html", view_model)

@router.get("/termosdeuso")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/centrodecoleta/termosdeuso.html", view_model)

@router.post("/alterar_senha")
async def post_alterarsenha(request: Request):
    dados = dict(await request.form())
    usuario = request.state.usuario
    id = usuario.id
    email = usuario.email
    senha = dados["senha"]
    novasenha = dados["novasenha"]
    confsenha = dados["confsenha"]
    senha_hash = UsuarioRepo.obter_senha_por_email(email)

    if not senha_hash:
        response = RedirectResponse("/centrodecoleta/index", status.HTTP_303_SEE_OTHER)
        adicionar_mensagem_erro(response, "Usuário/senha não encontrado em nossa base de dados.")
        return response
    
    if not bcrypt.checkpw(senha.encode(), senha_hash.encode()):
        response = RedirectResponse("/centrodecoleta/index", status.HTTP_303_SEE_OTHER)
        adicionar_mensagem_erro(response, "Senha atual não confere.")
        return response
    
    if novasenha != confsenha:
        response = RedirectResponse("/centrodecoleta/index", status.HTTP_303_SEE_OTHER)
        adicionar_mensagem_erro(response, "Nova senha não foi confirmada com sucesso.")
        return response
    
    senha_hash = bcrypt.hashpw(novasenha.encode(), bcrypt.gensalt())
    UsuarioRepo.atualizar_senha(id, senha_hash.decode())
    response = RedirectResponse("/centrodecoleta/index", status.HTTP_303_SEE_OTHER)
    adicionar_mensagem_sucesso(response, "Senha alterada com sucesso!")
    return response

@router.post("/adicionar_credito")
async def post_adicionar_credito(request : Request):
    dados = dict(await request.form())
    add_credito = int(dados['credito'])
    usuario = UsuarioRepo.obter_dados_por_email(dados['email'])
    if usuario:
        creditoatual = usuario.credito
        credito = creditoatual + add_credito
        UsuarioRepo.atualizar_credito(usuario.id, credito)
        response = RedirectResponse("/centrodecoleta/index", status.HTTP_303_SEE_OTHER)
        adicionar_mensagem_sucesso(response, "Crédito adicionado com sucesso!")
        return response
    
    response = RedirectResponse("/centrodecoleta/index", status.HTTP_303_SEE_OTHER)
    adicionar_mensagem_erro(response, "Ocorreu um erro, tente novamente.")
    return response
