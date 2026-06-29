import pyautogui
import pandas as pd
import time

def preencher(imagem, deslocamentoY = 0, valor = None):
    campo = pyautogui.locateCenterOnScreen(imagem,confidence = 0.9)
    pyautogui.click(campo.x, campo.y + deslocamentoY)
    if valor:
        pyautogui.write(valor)
    pyautogui.scroll(-120)
    time.sleep(2)

planilha = pd.read_excel('dados_automacao.xlsx')
for indice, linha in planilha.iterrows():

    preencher('email.png')

    preencher('nome.png', 50, linha['nome'])

    preencher('matricula.png', 50, str(linha['matricula']))

    preencher('curso.png', 50, linha['curso'])

    preencher(f'{linha['genero']}.png')

    preencher('enviar.png')

    preencher('outra.png')





