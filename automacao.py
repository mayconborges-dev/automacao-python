# Passo a Passa do Projeto de Automação 
# Passo 1: Entrar no sistema da empresa
# Passo 2: Fazer Login
# Passo 3: Importar a base de produtos para cadastrar
# Passo 4: Cadastrar um produto
# Passo 5: Repetir o processo de cadastro até o fim.

import pyautogui
import time
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas

pyautogui.PAUSE = 0.3

# Abrir o navegador
pyautogui.press('Win')
pyautogui.write('Opera')
pyautogui.press('Enter')
time.sleep(2)

# Digitar e abrir o link
pyautogui.write(link)
pyautogui.press('Enter')
time.sleep(2)

# Login e senha
pyautogui.press('Tab')
pyautogui.write('PythoneTudodeBom')
pyautogui.press('Tab')
pyautogui.write('senha1234')
pyautogui.click(x=973, y=555)
time.sleep(3)

# Importe as informações dos produtos
import pandas as pd

tabela = pd.read_csv('produtos.csv')

print(tabela)

# Cadastrar o primeiro produto
for linha in tabela.index:
    # Clicar no campo código
    pyautogui.click(x=740, y=282)
    # Pegar da tabela o valor do campo que queremos preencher 
    codigo = tabela.loc[linha, 'codigo']
    # Preencher o campo
    pyautogui.write(str(codigo))
    # Proximo campo
    pyautogui.press('Tab')
    # Preencher o campo
    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press('Tab')
    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press('Tab')
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('Tab')
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('Tab')
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('Tab')
    obs = tabela.loc[linha, 'obs']
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, 'obs']))
    # Cadastra o produto no botão "Enviar"
    pyautogui.press('Enter')

    # Scroll para cima
    pyautogui.scroll(5000)

    # O Processo será repetido até o fim da tabela.