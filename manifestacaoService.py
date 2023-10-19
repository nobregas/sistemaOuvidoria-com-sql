import mysql.connector as bd
import propriedades as sql

conection = bd.connect(user=sql.dados["USER"],
                       password=sql.dados["PASSWORD"],
                       host=sql.dados["HOST"],
                       database=sql.dados["DATABASE"])
cursor = conection.cursor()

query = """CREATE TABLE IF NOT EXISTS manifestacoes(
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100),
        email_manifestante VARCHAR(100),
        descricao VARCHAR(100),
        status VARCHAR(100),
        responsavel VARCHAR(100),
        prioridade VARCHAR(100),
        categoria VARCHAR(100),
        atribuido_a VARCHAR(100)
    )"""
cursor.execute(query)

def checarId(id):
    try:
        checar_query = "SELECT id FROM manifestacoes WHERE id = %s"
        cursor.execute(checar_query, (id,))
        resultado = cursor.fetchone()
        return resultado is not None
    except bd.Error as e:
        print(f"Erro ao listar as manifestacoes: {e}")

def listar():
    try:
        listar_query = "SELECT * FROM manifestacoes"
        cursor.execute(listar_query)
        resultado = cursor.fetchall()
        if not resultado:
            print("Nao há manifestacoes no momento.")

        return resultado
    except bd.Error as e:
        print(f"Erro ao listar as manifestacoes: {e}")

def cadastrar(manifestacao):
    try:
        cadastro_query = """
                INSERT INTO manifestacoes (
                    nome, email_manifestante, descricao, status,
                     responsavel, prioridade, categoria, atribuido_a
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
        values = (manifestacao["nome"], manifestacao["email_manifestante"],
                  manifestacao["descricao"], manifestacao["status"],
                  manifestacao["responsavel"], manifestacao["prioridade"],
                  manifestacao["categoria"], manifestacao["atribuido_a"])

        cursor.execute(cadastro_query, values)
        conection.commit()
        print(f"Cadastro da manifestacao {manifestacao['nome']} bem sucedido!")
    except bd.Error as e:
        print(f"Erro ao cadastrar a manifestacao: {e}")


def excluir(id):
    if checarId(id):
        try:
            excluir_query = "DELETE FROM manifestacoes WHERE id = %s"
            cursor.execute(excluir_query, (id,))
            conection.commit()
            print(f"Sucesso ao excluir manifestacao de id {id}")

        except bd.Error as e:
            print(f"Erro ao excluir a manifestacao: {e}")
    else:
        print("Id invalido!")
def atualizar(valores_novos, id):
    if checarId(id):
        try:
            atualizar_query = """
                UPDATE manifestacoes
                SET
                    nome = %s,
                    email_manifestante = %s,
                    descricao = %s,
                    status = %s,
                    responsavel = %s,
                    prioridade = %s,
                    categoria = %s,
                    atribuido_a = %s
                WHERE id = %s
            """

            valores = [valores_novos["nome"], valores_novos["email_manifestante"],
                       valores_novos["descricao"], valores_novos["status"],
                       valores_novos["responsavel"], valores_novos["prioridade"],
                       valores_novos["categoria"], valores_novos["atribuido_a"],
                       id]

            cursor.execute(atualizar_query, valores)
            conection.commit()
            print(f"Sucesso ao atualizar os dados da manifestacao {id}")
        except bd.Error as e:
            print(f"Erro ao atualizar a manifestacao: {e}")
    else:
        print("Id invalido!")
