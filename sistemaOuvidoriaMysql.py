import manifestacaoController as controller


def mostrarInterface():
    print("1 - Listar manifestacoes\n"
          "2 - Cadastrar manifestacao\n"
          "3 - Excluir manifestacao por Id\n"
          "4 - Alterar manifestacao por Id\n"
          "5 - Pegar manifestacao por Id\n"
          "6 - sair\n"
          )


while True:
    mostrarInterface()
    opcao = int(input("Digite a opcao: "))
    print("-----------------------------------------------------------")

    match opcao:
        case 1:
            controller.listarManifestacoes()

        case 2:
            controller.cadastrarManifestacao()

        case 3:
            controller.excluirManifestacao()

        case 4:
            controller.atualizarManifestacao()

        case 5:
            controller.pegarManifestacaoPorId()

        case 6:
            print("Saindo...")
            break

        case _:
            print("Opcao invalida!!")
            print("-----------------------------------------------------------")
