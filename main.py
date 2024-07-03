from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

from ler_html import ler_html

app = FastAPI()

app.mount(path="/static", app=StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("index.html", view_model)

@app.get("/contato")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("contato.html", view_model)

@app.get("/store")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("store.html", view_model)

@app.get("/teste")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("teste.html", view_model)

@app.get("/carrinho")
def get_root(request: Request):
    view_model = {"request": request}
    return templates.TemplateResponse("teste.html", view_model)

if __name__ == "__main__":
    uvicorn.run(app="main:app", port=8000, reload=True)
