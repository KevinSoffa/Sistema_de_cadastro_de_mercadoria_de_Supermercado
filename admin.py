import pymysql.cursors
import time


class admin():
    def __init__(self):
        pass

    def conexao(self):
        try:
            self.banco = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                db='mercado',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
            print('Conectando ao Servidor...')
            time.sleep(1)
            print('\033[1;34mCONECTADO com sucesso\033[m')
            print('=-' * 15)
        except:
            print('\033[1;31mERRO ao conectar com o Banco de Dados\033[m')

    def login(self):
        self.conexao()
        time.sleep(2)
        print('\033[1;36;40m=== LOGIN ===\033[m')
        print('Para voltar ao Menu Principal digite 1')
        email = input('E-mail: ')
        senha = input('Senha: ')
        autenticado = False
        try:
            with self.banco.cursor() as cursos:
                cursos.execute('SELECT * FROM admin')
                resultados = cursos.fetchall()

        except:
            print('\033[1;31mAlgo deu ERRADO :(\033[m')
            print('\033[1;31mERRO ao conectar com o Banco de Dados - admin\033[m')
        for i in resultados:
            if email == i['email'] and senha == i['senha']:
                autenticado = True
                break
            else:
                pass
        if autenticado:
            time.sleep(0.5)
            self.menuAdmin()
        else:
            print('\033[1;31mAlgo deu ERRADO :(\033[m')
            print('\033[1;31mDados INCORRETOS! Tente novamente\033[m')
            self.login()

    def VerificaEmail(self, email):
        self.conexao()
        try:
            with self.banco.cursor() as cursos:
                cursos.execute('SELECT * FROM admin')
                resultados = cursos.fetchall()

        except:
            print('\033[1;31mAlgo deu ERRADO :(\033[m')
            print('\033[1;31mERRO ao conectar com o Banco de Dados - admin\033[m')
        for i in resultados:
            if email == i['email']:
                return 1
            else:
                pass
            return 0

    def cadastro(self):
        print('\033[1;36;40m=== CADASTRO DE ADM ===\033[m')
        cod = '123'  # Código de verificação
        codigo = input('Digite o código de verificação: ')
        if codigo == cod:
            nome = input('Digite seu nome de Usuário: ')
            email = input('Digite seu E-mail: ')
            senha = input('Crie sua Senha: ')
            confirmacao_senha = input('Confirme sua Senha: ')
            if senha == confirmacao_senha:
                dados = [nome, email, senha, 1]
                self.conexao()
                email_existente = self.VerificaEmail(email)
                if email_existente == 1:
                    print('E-mail existente. Faça o Login!')
                    self.login()
                else:
                    with self.banco.cursor() as cursos:
                        sql = "INSERT INTO admin (nome, email, senha, status) VALUES (%s, %s, %s, %s)"
                        cursos.execute(sql, dados)
                        self.banco.commit()
                        print('ADM Cadastrado!')
                        print('=-' * 15)
                        time.sleep(2)
                        self.login()
            else:
                print('\033[1;31mERRO. Senhas não conferem!!!\033[m')
                time.sleep(2)
                print('Tente NOVAMENTE')
                print('=-' * 15)
                self.cadastro()

    def menuAdmin(self):
        print('=-' * 15)
        print('\033[1;36;40m=== MENU ADM ===\033[m')
        print('1. Cadastrar novo Produto\n'
              '2. Alterar dados de um produto\n'
              '3. Deletar produto\n'
              '4. Listar produtos\n'
              '0. Digite 0 para \033[1;31mSAIR\033[m')
        print('=-' * 15)
        op = int(input('>> Digite o número da opção desejada: '))
        print('=-' * 15)
        if op == 0:
            return 0
        elif op == 1:
            nome_produto = input('Nome do produto: ')
            quantidade = int(input('Quantidade: '))

            print('\033[1;33m|Tipos de Produto|\033[m')
            print('(1. Alimento) | (2. Higiene) \n'
                  '(3. Limpeza   | (4. Outros)')
            tipo = int(input('Tipo do produto [número]:'))

            dadosProdutos = [nome_produto, quantidade, tipo]
            produtos(dadosProdutos).cadastrarProduto()


class produtos(admin):
    def __init__(self, dadosProdutos):
        self.dadosProdutos = dadosProdutos

    def cadastrarProduto(self):
        self.conexao()
        with self.banco.cursor() as cursos:
            sql = "INSERT INTO produtos (nomeProduto, quantidade, tipo) VALUES (%s, %s, %s)"
            cursos.execute(sql, self.dadosProdutos)
            self.banco.commit()
            print('\033[1;32mProduto Cadastrado!\033[m')
            time.sleep(1)
            self.menuAdmin()

