@router.post("/cadastrar")
async def post_cadastrar(request: Request):
    # capturar os dados do formulário de cadastro como um dicionário
    dados = dict(await request.form())
    # normalizar os dados para tipificar os valores corretamente
    dados["data_nascimento"] = date.fromisoformat(dados["data_nascimento"])
    dados["perfil"] = int(dados["perfil"])
    # validar dados do formulário
    erros = {}
    #validação da senha igual à confirmação senha
    if is_matching_fields(dados["senha"],"senha", "Senha", dados[confirmacao_senha], "Confirmação de Senha", erros):
        dados.pop("confirmacao_senha")
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