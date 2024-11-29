import datetime
from urllib import response
import bcrypt
from fastapi import APIRouter, Form, Request, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from models.usuario_model import Usuario
from repositories.usuario_repo import UsuarioRepo
from util.mensagens import adicionar_mensagem_erro, adicionar_mensagem_sucesso
from util.validators import *

router = APIRouter(prefix="/admin")
templates = Jinja2Templates("templates")

@router.get("/index")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/admin/index.html", view_model)

@router.get("/addempresa")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/admin/addempresa.html", view_model)

@router.get("/addcentrocoleta")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/admin/addcentrocoleta.html", view_model)

@router.post("/post_cadastrar_empresa")
async def post_cadastrar(request: Request):
    # capturar os dados do formulário de cadastro como um dicionário
    dados = dict(await request.form())
    # normalizar os dados para tipificar os valores corretamente
    dados["data_nascimento"] = date.fromisoformat(dados["data_nascimento"])
    # validar dados do formulário
    erros = {}
    #validação da senha igual à confirmação senha
    if is_matching_fields(dados["senha"],"senha", "Senha", dados["confsenha"], "Confirmar senha", erros):
        dados.pop("confsenha")
    #validação do nome
    is_person_fullname(dados["nome"], "nome", "Nome", erros)
    is_size_between(dados["nome"], "nome", "Nome", erros)
    #validação de data de nascimento
    data_minima = datetime.now() - datetime.timedelta(days=365 * 130)
    data_maxima = datetime.now() - datetime.timedelta(days=365 * 18)
    is_date_between(dados["data_nascimento"], "data_nascimento", "Data de nasciemnto", data_minima, data_maxima, erros)
    #validação do email
    is_email(dados["email"], "email", "E-mail", erros)
    #validação do telefone
    is_size_between(dados["telefone"], "telefone", "Telefone", 14, 15, erros)
    #validção da senha
    is_password(dados["senha"], "senha", "Senha", erros)

    #montagem da exibição da senha
    if erros:
        response = templates.TemplatesResponse(
            "pages/cadastrar.html",
            {"request": request, "dados": dados, "erros": erros},
        )
        adicionar_mensagem_erro(response, "Há erros no formulário. corrija-os e tente novamente.")
        return response
    # criptografar a senha com bcrypt
    senha_hash = bcrypt.hashpw(dados["senha"].encode(), bcrypt.gensalt())
    dados["senha"] = senha_hash.decode()
    # criar um objeto Usuario com os dados do dicionário
    dados["perfil"] = 2
    usuario = Usuario(**dados)
    # inserir o objeto Usuario no banco de dados usando o repositório
    usuario = UsuarioRepo.inserir(usuario)
    # se inseriu com sucesso, redirecionar para a página de login
    if usuario:
        response = RedirectResponse("/entrar", status.HTTP_303_SEE_OTHER)
        adicionar_mensagem_sucesso(response, "Cadastro realizado com sucesso!")
        return response
    # se não inseriu, redirecionar para a página de cadastro com mensagem de erro
    else:
        response = RedirectResponse("/cadastrar", status.HTTP_303_SEE_OTHER)
        adicionar_mensagem_erro(
            response,
            "Ocorreu um problema ao realizar seu cadastro. Tente novamente mais tarde.",
        )
        return response

@router.post("/post_cadastrar_centrocoleta")
async def post_cadastrar(request: Request):
    # capturar os dados do formulário de cadastro como um dicionário
    dados = dict(await request.form())
    # normalizar os dados para tipificar os valores corretamente
    dados["data_nascimento"] = date.fromisoformat(dados["data_nascimento"])
    # validar dados do formulário
    erros = {}
    #validação da senha igual à confirmação senha
    if is_matching_fields(dados["senha"],"senha", "Senha", dados["confsenha"], "Confirmar senha", erros):
        dados.pop("confsenha")
    #validação do nome
    is_person_fullname(dados["nome"], "nome", "Nome", erros)
    is_size_between(dados["nome"], "nome", "Nome", erros)
    #validação de data de nascimento
    data_minima = datetime.now() - datetime.timedelta(days=365 * 130)
    data_maxima = datetime.now() - datetime.timedelta(days=365 * 18)
    is_date_between(dados["data_nascimento"], "data_nascimento", "Data de nasciemnto", data_minima, data_maxima, erros)
    #validação do email
    is_email(dados["email"], "email", "E-mail", erros)
    #validação do telefone
    is_size_between(dados["telefone"], "telefone", "Telefone", 14, 15, erros)
    #validção da senha
    is_password(dados["senha"], "senha", "Senha", erros)

    #montagem da exibição da senha
    if erros:
        response = templates.TemplatesResponse(
            "pages/cadastrar.html",
            {"request": request, "dados": dados, "erros": erros},
        )
        adicionar_mensagem_erro(response, "Há erros no formulário. corrija-os e tente novamente.")
        return response
    # criptografar a senha com bcrypt
    senha_hash = bcrypt.hashpw(dados["senha"].encode(), bcrypt.gensalt())
    dados["senha"] = senha_hash.decode()
    # criar um objeto Usuario com os dados do dicionário
    dados["perfil"] = 4
    usuario = Usuario(**dados)
    # inserir o objeto Usuario no banco de dados usando o repositório
    usuario = UsuarioRepo.inserir(usuario)
    # se inseriu com sucesso, redirecionar para a página de login
    if usuario:
        response = RedirectResponse("/entrar", status.HTTP_303_SEE_OTHER)
        adicionar_mensagem_sucesso(response, "Cadastro realizado com sucesso!")
        return response
    # se não inseriu, redirecionar para a página de cadastro com mensagem de erro
    else:
        response = RedirectResponse("/cadastrar", status.HTTP_303_SEE_OTHER)
        adicionar_mensagem_erro(
            response,
            "Ocorreu um problema ao realizar seu cadastro. Tente novamente mais tarde.",
        )
        return response