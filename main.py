import dotenv
from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from repositories.usuario_repo import UsuarioRepo
from routes.main_routes import router as main_router
from routes.admin_routes import router as admin_router
from routes.consumidor_routes import router as consumidor_router
from routes.centrodecoleta_routes import router as centrodecoleta_router
from routes.empresa_routes import router as empresa_router
from routes.usuario_routes import router as usuario_router
from util.auth import checar_autenticacao, checar_autorizacao
from util.exceptions import configurar_excecoes

UsuarioRepo.criar_tabela()
dotenv.load_dotenv()
app = FastAPI(dependencies=[Depends(checar_autorizacao)])
app.mount(path="/static", app=StaticFiles(directory="static"), name="static")
app.middleware("http")(checar_autenticacao)
configurar_excecoes(app)
app.include_router(main_router)
app.include_router(admin_router)
app.include_router(centrodecoleta_router)
app.include_router(empresa_router)
app.include_router(consumidor_router)
app.include_router(usuario_router)

