from fastapi import FastAPI, HTTPException, Request, logger, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from util.mensagens import adicionar_mensagem_erro


templates = Jinja2Templates(directory="templates")



def configurar_excecoes(app: FastAPI):

    @app.exception_handler(401)
    async def unauthorized_exception_handler(request: Request, _):
        return_url = f"?return_url={request.url.path}"
        response = RedirectResponse(
            f"/login{return_url}", status_code=status.HTTP_302_FOUND
        )
        adicionar_mensagem_erro(
            response,
            f"A página <b>{request.url.path}</b> é restrita a usuários logados. Identifique-se para poder prosseguir.",
        )
        return response

    @app.exception_handler(403)
    async def forbidden_exception_handler(request: Request, _):
        return_url = f"/login?return_url={request.url.path}"
        usuario = request.state.usuario if hasattr(request.state, "usuario") else None

        if usuario:
            # match usuario.perfil:
            #     case 1:
            #         return_url = "/usuario"
            #     case 2:
            #         return_url = "/admin"
            response = RedirectResponse(return_url, status_code=status.HTTP_302_FOUND)
            adicionar_mensagem_erro(
                response,
                f"Você está logado como <b>{usuario.nome}</b> e seu perfil de usuário não tem autorização de acesso à página <b>{request.url.path}</b>. Saia de seu usuário e entre com um usuário do perfil adequado para poder acessar a página em questão.",
            )
            return response
        else:
            response = RedirectResponse(
                f"/login{return_url}", status_code=status.HTTP_302_FOUND
            )
            adicionar_mensagem_erro(
                response,
                f"Somente usuários autenticados possuem acesso à página <b>{request.url.path}</b>. Entre com um usuário do perfil adequado para poder acessar a página em questão.",
            )
            return response

    @app.exception_handler(404)
    async def page_not_found_exception_handler(request: Request, _):
        usuario = request.state.usuario if hasattr(request.state, "usuario") else None
        return templates.TemplateResponse(
            "shared/pages/404.html",
            {
                "request": request,
                "usuario": usuario,
            },
        )

    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, ex: HTTPException):
        #logger.error("Ocorreu uma exceção não tratada: %s", ex)
        usuario = request.state.usuario if hasattr(request.state, "usuario") else None
        view_model = {
            "request": request,
            "usuario": usuario,
            "detail": "Erro na requisição HTTP.",
        }
        return templates.TemplateResponse(
            "shared/pages/error.html",
            view_model,
            status_code=ex.status_code,
        )

    @app.exception_handler(Exception)
    async def general_exception_handler(request: Request, ex: Exception):
        #logger.error("Ocorreu uma exceção não tratada: %s", ex)
        usuario = request.state.usuario if hasattr(request.state, "usuario") else None
        view_model = {
            "request": request,
            "usuario": usuario,
            "detail": "Erro interno do servidor.",
        }
        return templates.TemplateResponse(
            "shared/pages/error.html",
            view_model,
            status_code=500,
        )
