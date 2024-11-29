import datetime
from datetime import timedelta
import bcrypt
from fastapi import APIRouter, Form, Request, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from dtos.usuario_autenticado import UsuarioAutenticado
from models.usuario_model import Usuario
from repositories.usuario_repo import UsuarioRepo
from util.auth import NOME_COOKIE_AUTH, adicionar_token_jwt, criar_token_jwt
from util.mensagens import adicionar_mensagem_erro, adicionar_mensagem_sucesso
from util.validators import *


router = APIRouter()
templates = Jinja2Templates("templates")

@router.get("/")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/index.html", view_model)

@router.get("/login")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/login.html", view_model)

# @router.post("/post_entrar")
# async def post_entrar(
#     email: str = Form(...), 
#     senha: str = Form(...)):
#     usuario = UsuarioRepo.checar_credenciais(email, senha)
#     if usuario is None:
#         response = RedirectResponse("/login", status_code=status.HTTP_303_SEE_OTHER)
#         adicionar_mensagem_erro(response, "Credenciais inválidas! Cheque os valores digitados e tente novamente.")
#         return response
#     token = criar_token_jwt(UsuarioAutenticado)
#     nome_perfil = None
#     match (usuario[2]):
#         case 2: nome_perfil = "empresa"
#         case 3: nome_perfil = "admin"
#         case 4: nome_perfil = "centrodecoleta"
#         case 5: nome_perfil = "consumidor"
#         case _: nome_perfil = ""
#     response = RedirectResponse(f"/{nome_perfil}/index", status_code=status.HTTP_303_SEE_OTHER)  
#     adicionar_token_jwt(response, token)  
#     response.set_cookie(
#         key=NOME_COOKIE_AUTH,
#         value=token,
#         max_age=3600*24*365*10,
#         httponly=True,
#         samesite="lax"
#     )
#     adicionar_mensagem_sucesso(response, "Login realizado com sucesso!")
#     return response

@router.post("/post_entrar")
async def post_entrar(request: Request):
    dados = dict(await request.form())
    email = dados["email"]
    senha = dados["senha"]
    senha_hash = UsuarioRepo.obter_senha_por_email(email)
    if senha_hash and bcrypt.checkpw(senha.encode(), senha_hash.encode()):
        usuario = UsuarioRepo.obter_dados_por_email(email)
        usuarioAutenticadoDto = UsuarioAutenticado(
            id=usuario.id,
            nome=usuario.nome,
            email=usuario.email,
            perfil=usuario.perfil,
        )
        token = criar_token_jwt(usuarioAutenticadoDto)
        nome_perfil = None
        match(usuarioAutenticadoDto.perfil):
            case 2: nome_perfil = "empresa"
            case 3: nome_perfil = "admin"
            case 4: nome_perfil = "centrodecoleta"
            case 5: nome_perfil = "consumidor"
            case _: nome_perfil = ""
        response = RedirectResponse(f"/{nome_perfil}/index", status.HTTP_303_SEE_OTHER)
        adicionar_token_jwt(response, token)
        adicionar_mensagem_sucesso(response, "Login realizado com sucesso!")
        return response
    else:
        response = RedirectResponse("/login", status.HTTP_303_SEE_OTHER)
        adicionar_mensagem_erro(response, "Credenciais inválidas! Cheque os valores digitados e tente novamente.")
        return response
    
@router.get("/criarconta")
async def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("main/pages/criarconta.html", view_model)

# @router.post("/post_cadastrar")
# async def post_cadastrar(
#     nome: str = Form(...),
#     cpf: str = Form(...),
#     email: str = Form(...),
#     telefone: str = Form(...),
#     cep: str = Form(...),
#     senha: str = Form(...),
#     confsenha: str = Form(...)):
#     if senha != confsenha:
#         response = RedirectResponse("/criarconta", status_code=status.HTTP_303_SEE_OTHER)
#         adicionar_mensagem_erro(response, "Credenciais inválidas! Cheque os valores digitados e tente novamente.")
#         return response
#     senha_hash = obter_hash_senha(senha)
#     usuario = Usuario(
#         nome=nome, 
#         cpf=cpf, 
#         email=email, 
#         telefone=telefone,
#         cep=cep, 
#         senha=senha_hash,
#         perfil=5)
#     UsuarioRepo.inserir(usuario)
#     response = RedirectResponse("/login", status_code=status.HTTP_303_SEE_OTHER)
#     adicionar_mensagem_sucesso(response, "Cadastro realizado com sucesso!")
#     return response

@router.post("/post_cadastrar")
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
    data_minima = datetime.now() - timedelta(days=365 * 130)
    data_maxima = datetime.now() - timedelta(days=365 * 18)
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
    dados["perfil"] = 5
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