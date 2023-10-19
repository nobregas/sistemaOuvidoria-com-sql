import manifestacaoController as controller
import manifestacaoService as service

def mostrarInterface():
    print("1 - Listar manifestacoes\n"
          "2 - Cadastrar manifestacao\n"
          "3 - Excluir manifestacao\n"
          "4 - Alterar manifestacao\n"
          "5 - sair\n")

def pegarOpcaoValida():
    while True:
        opcao = int(input("Digite a opcao: "))
        if opcao not in [1, 2, 3, 4, 5]:
            print("Opcao invalida!!")
        else:
            break

    return opcao

while True:
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

    mostrarInterface()
    opcao = pegarOpcaoValida()
    print("-------------------------------------------")

    if opcao == 5: #opcao 5
        print("Saindo...")
        break

    match opcao:
        case 1:
            controller.listarManifestacoes()

        case 2:
            controller.cadastrarManifestacao(manifestacao)

        case 3:
            controller.excluirManifestacao()

        case 4:
            controller.atualizarManifestacao()

service.conection.close()
