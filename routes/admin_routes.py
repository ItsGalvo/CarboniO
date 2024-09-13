from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from util.templates import obter_jinja_templates


router = APIRouter(prefix="/admin")
templates = obter_jinja_templates("templates/main")
