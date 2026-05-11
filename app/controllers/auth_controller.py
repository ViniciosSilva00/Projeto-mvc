from fastapi import APIRouter, Depends, Request, Form, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.usuario import Usuario
from app.auth import hash_senha, verificar_senha, criar_token

router =APIRouter(prefix="/auth", tags=["autenticação"])

templates = Jinja2Templates(directory="app/templates")

#Rota de cadastro
@router.get("/cadastro")
def tela_cadastro(request: Request):
    return templates.TemplateResponse(
        request,
          "auth/cadastro.html", 
          {"request": request}

    )
#Rota de cadastro
@router.post("/login")
def tela_login(request: Request):
    return templates.TemplateResponse(
        request,
          "auth/login.html", 
          {"request": request}
    )
# Criar usuario no banco - cadastrar usuario

novo_usuario = Usuario(
    nome=nome,
    email=email,
    senha_hash=hash_senha(senha), #Nunca salva a senha pura no db
)