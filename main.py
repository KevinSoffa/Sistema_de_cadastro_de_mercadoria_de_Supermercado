import time

import admin as adm


def main():
    print('=-' * 15)
    print('{:^40}'.format('\033[1;36;40m===> OPÇÕES <===\033[m'))
    print('=-' * 15)
    print("1. Para logar como Administrador\n"
          "2. Para Cadastrar\n"
          "3. Ver Produtos\n"
          "4. Digite 4 para \033[1;31mSAIR\033[m")
    print('=-'*15)
    op = int(input('>> Digite o número da opção desejada: '))
    if op == 1:
        adm.admin().login()  # Logar

    elif op == 2:
        adm.admin().cadastro()  # Cadastrar

    elif op == 3:
        pass  # Ver produtos

    else:
        print('FINALIZANDO SERVIDOR...')
        time.sleep(3)
        print('Até Logo!!!')


if __name__ == '__main__':
    main()
