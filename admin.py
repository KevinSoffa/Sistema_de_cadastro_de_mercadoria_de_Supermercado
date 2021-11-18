import pymysql.cursors
import main
import time

import main


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
        global autenticado
        self.conexao()
        time.sleep(2)
        print('\033[1;36;40m=== LOGIN ===\033[m')
        print('Para voltar ao Menu Principal digite 1')
        email = input('E-mail: ')
        senha = input('Senha: ')
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
                autenticado = False
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
            produtos().cadastrarProduto(dadosProdutos)
        elif op == 2:
            produtos().alterarDados()

        elif op == 3:
            produtos().deletarProdutos()

        elif op == 4:
            produtos().listarProdutos()

        elif op == 0:
            print('FINALIZANDO SERVIDOR...')
            time.sleep(3)
            print('Até Logo!!!')


class produtos(admin):
    def __init__(self,):
        pass

    def cadastrarProduto(self, dadosProdutos):
        self.conexao()
        with self.banco.cursor() as cursos:
            sql = "INSERT INTO produtos (nomeProduto, quantidade, tipo) VALUES (%s, %s, %s)"
            cursos.execute(sql, dadosProdutos)
            self.banco.commit()
            print('\033[1;32mProduto Cadastrado!\033[m')
            time.sleep(1)
            self.menuAdmin()

    def listarProdutos(self):
        self.conexao()
        try:
            with self.banco.cursor() as cursos:
                cursos.execute('SELECT * FROM produtos')
                produtos = cursos.fetchall()

        except:
            print('\033[1;31mAlgo deu ERRADO :(\033[m')
            print('\033[1;31mERRO ao conectar com o Banco de Dados - produtos\033[m')
        print('=-' * 15)
        print('\033[1;36;40m=== LISTA DE PRODUTOS ===\033[m')
        print('(1. Alimento) | (2. Higiene) \n'
              '(3. Limpeza   | (4. Outros)')
        print('--' * 40)
        for i in produtos:
            if i['tipo'] == '1':
                tipo = "ALIMENTO"
            elif i['tipo'] == '2':
                tipo = "HIGIENE"
            elif i['tipo'] == '3':
                tipo = "LIMPEZA"
            else:
                tipo = "OUTROS"
            print('\033[1mID\033[m: {} | \033[1mProduto\033[m: {} | \033[1mQuantidade\033[m: {} | \033[1mTipo\033[m: {}'
                  ' '.format(i['idProdutos'], i['nomeProduto'], i['quantidade'], i['tipo']))
            print('--' * 40)
            time.sleep(0.5)
        try:
            if autenticado:
                self.menuAdmin()
        except:
            main.main()

    def deletarProdutos(self):
        self.conexao()
        id = int(input('Digite o ID do produto a ser EXCLUIDO: '))
        confirmacao = input(f'Tem certeza que deseja \033[1;31mEXCLUIR\033[m o produto de ID: {id}?[S|N]:').upper().strip()[0]
        if confirmacao == 'S':
            with self.banco.cursor() as cursos:
                cursos.execute(f"DELETE FROM produtos WHERE idProdutos={id}")
                self.banco.commit()
                print('Produto DELETADO')
                self.menuAdmin()
        else:
            self.deletarProdutos()

    def alterarDados(self):
        self.conexao()
        id = int(input('Digite o ID do produto a ser alterado: '))
        try:
            with self.banco.cursor() as cursos:
                cursos.execute('SELECT * FROM produtos WHERE idProdutos={}'.format(id))
                produto = cursos.fetchall()

        except:
            print('\033[1;31mAlgo deu ERRADO :(\033[m')
            print('\033[1;31mERRO ao conectar com o Banco de Dados - produtos\033[m')

        nomeProduto = input('Novo nome do Produto ({}): '.format(produto[0]['nomeProduto']))
        quantidade = int(input('Quantidade em estoque ({}): '.format(produto[0]['quantidade'])))
        print('(1. Alimento) | (2. Higiene) \n'
              '(3. Limpeza   | (4. Outros)')
        categoria = int(input('Digite o Tipo ATUAL do produto: '))
        if categoria == 1:
            print(f'{nomeProduto} | 1. Alimento')
        elif categoria == 2:
            print(f'{nomeProduto} | 2. Higiene')
        elif categoria == 3:
            print(f'{nomeProduto} | 3. Limpeza')
        elif categoria == 4:
            print(f'{nomeProduto} | 4. Outros')
        tipo = int(input('Digite o Novo tipo do produto: '))
        with self.banco.cursor() as cursos:
            cursos.execute("UPDATE produtos SET nomeProduto='{}', quantidade={}, tipo={} WHERE idProdutos={}".format(nomeProduto, quantidade, tipo, id))
            self.banco.commit()
            print(f'Produto:{nomeProduto} | Quantidade: {quantidade} | Tipo: {tipo}')
            print('\033[1;32mProduto ALTERADO!\033[m')
            time.sleep(1.5)
            self.menuAdmin()



