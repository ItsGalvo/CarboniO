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
    empresas = UsuarioRepo.selecionar_por_perfil(2)
    centroscoleta = UsuarioRepo.selecionar_por_perfil(4)
    view_model = {"request": request, "empresas": empresas, "centroscoleta": centroscoleta}
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
    # validar dados do formulário
    erros = {}
    #validação da senha igual à confirmação senha
    if is_matching_fields(dados["senha"],"senha", "Senha", dados["confsenha"], "Confirmar senha", erros):
        dados.pop("confsenha")
    #validação do email
    is_email(dados["email"], "email", "E-mail", erros)
    #validação do telefone
    is_size_between(dados["telefone"], "telefone", "Telefone", 14, 15, erros)

    #montagem da exibição da senha
    if erros:
        response = templates.TemplateResponse(
            "main/pages/admin/addempresa.html",
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
        response = RedirectResponse("/admin/index", status.HTTP_303_SEE_OTHER)
        adicionar_mensagem_sucesso(response, "Cadastro da empresa realizado com sucesso!")
        return response
    # se não inseriu, redirecionar para a página de cadastro com mensagem de erro
    else:
        response = RedirectResponse("/admin/addempresa", status.HTTP_303_SEE_OTHER)
        adicionar_mensagem_erro(
            response,
            "Ocorreu um problema ao realizar seu cadastro. Tente novamente mais tarde.",
        )
        return response

@router.post("/post_cadastrar_centrocoleta")
async def post_cadastrar(request: Request):
    # capturar os dados do formulário de cadastro como um dicionário
    dados = dict(await request.form())
    # validar dados do formulário
    erros = {}
    #validação da senha igual à confirmação senha
    if is_matching_fields(dados["senha"],"senha", "Senha", dados["confsenha"], "Confirmar senha", erros):
        dados.pop("confsenha")
    #validação do email
    is_email(dados["email"], "email", "E-mail", erros)
    #validação do telefone
    is_size_between(dados["telefone"], "telefone", "Telefone", 14, 15, erros)

    #montagem da exibição da senha
    if erros:
        response = templates.TemplateResponse(
            "main/pages/admin/addcentrocoleta.html",
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
        response = RedirectResponse("/admin/index", status.HTTP_303_SEE_OTHER)
        adicionar_mensagem_sucesso(response, "Cadastro do centro de coleta realizado com sucesso!")
        return response
    # se não inseriu, redirecionar para a página de cadastro com mensagem de erro
    else:
        response = RedirectResponse("/admin/addcentrocoleta", status.HTTP_303_SEE_OTHER)
        adicionar_mensagem_erro(
            response,
            "Ocorreu um problema ao realizar seu cadastro. Tente novamente mais tarde.",
        )
        return response