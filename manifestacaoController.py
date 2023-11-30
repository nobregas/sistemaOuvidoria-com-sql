import manifestacaoService as service

manifestacao = {
    "nome": "",
    "email_manifestante": "",
    "descricao": "",
    "status": "",
    "responsavel": "",
    "prioridade": "",
    "categoria": "",
    "atribuido_a": ""
}


def pegarDados(manifestacao, pegarid=False):
    manifestacao["nome"] = input("Digite o nome da manifestacao: ")
    manifestacao["email_manifestante"] = input("Digite o email do manifestante: ")
    manifestacao["descricao"] = input("Digite a descricao da manifestacao: ")
    manifestacao["status"] = input("Digite o status da manifestacao: ")
    manifestacao["responsavel"] = input("Digite o responsavel da manifestacao: ")
    manifestacao["prioridade"] = input("Digite a prioridade da manifestacao: ")
    manifestacao["categoria"] = input("Digite a categoria da manifestacao: ")
    manifestacao["atribuido_a"] = input("Digite a quem esta atribuido a manifestacao: ")
    if pegarid:
        id = int(input("Digite o id da manifestacao: "))
        return id


def printJustificadoManifestacao(manifestacao):
    print(f"Manifestacao {manifestacao[0]}\n"
          f"nome: {manifestacao[1]}\n"
          f"email: {manifestacao[2]}\n"
          f"descricao: {manifestacao[3]}\n"
          f"status: {manifestacao[4]}\n"
          f"responsavel: {manifestacao[5]}\n"
          f"prioridade: {manifestacao[6]}\n"
          f"categoria: {manifestacao[7]}\n"
          f"atribuido a: {manifestacao[8]}\n")


def listarManifestacoes():
    print("-------------------Lista manifestacoes---------------------")
    manifestacoes = service.listar()
    for manifestacao in manifestacoes:
        printJustificadoManifestacao(manifestacao)
    print("-----------------------------------------------------------")


def pegarManifestacaoPorId():
    print("-----------------------Manifestacao------------------------")
    id = int(input("Digite o id da manifestacao: "))
    print()
    manifestacao_ = service.pegarPorId(id)
    printJustificadoManifestacao(manifestacao_)
    print("-----------------------------------------------------------")


def cadastrarManifestacao():
    print("------------------Cadastrando manifestacao-----------------")
    pegarDados(manifestacao)
    service.cadastrar(manifestacao)
    print("-----------------------------------------------------------")


def excluirManifestacao():
    print("------------------Excluindo manifestacao-------------------")
    listarManifestacoes()
    id = int(input("Digite o id da manifestacao: "))
    service.excluir(id)
    print("-----------------------------------------------------------")


def atualizarManifestacao():
    print("-----------------atualizando manifestacao------------------")
    listarManifestacoes()
    pegarDados(manifestacao, True)
    service.atualizar(manifestacao, id)
    print("-----------------------------------------------------------")
