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
            print('=-' * 15)
            print('Conectando ao Servidor...')
            time.sleep(2)
            print('\033[1;34mCONECTADO com sucesso\033[m')
            print('=-' * 15)
        except:
            print('\033[1;31mERRO ao conectar com o Banco de Dados')


    def login(self):
        self.conexao()
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
            self.menuAdmin()
        else:
            print('\033[1;31mAlgo deu ERRADO :(\033[m')
            print('\033[1;31mDados INCORRETOS! Tente novamente\033[m')
            self.login()

    def cadastro(self, dados):
        pass

    def menuAdmin(self):
        print('\033[1;34mLOGADO COM SUCESSO!!!\033[m')
