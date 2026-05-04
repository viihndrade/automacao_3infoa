import pyautogui
import time

def abrirChrome():
    #pressiona junto as teclas windows e d
    #win + d é o atalho para mostrar o desktop
    pyautogui.hotkey('win', 'd')
    #pressiona a tecla win
    pyautogui.press('win')
    #digita um texto
    pyautogui.write('edge', interval=0.2)
    #pressiona enter
    pyautogui.press('enter')
    #faz uma pausa de 1 seg
    time.sleep(1)
    #pressiona win + seta para cima - para maximizar a janela
    pyautogui.hotkey('win', 'up')

def pesquisarNoGPT():
    #abre um endereço
    pyautogui.write('http://www.chatgpt.com')
    pyautogui.press('enter')

    #faz uma pausa
    time.sleep(3)

    #faz uma pesquisa no chatgpt
    pyautogui.write(pesquisa)
    pyautogui.press('enter')

    #tenta clicar na imagem copia
    while True:
        time.sleep(2)
        try:
            xy = pyautogui.locateCenterOnScreen('aula8\\copiar.png', confidence=0.98)
            pyautogui.click(xy)
            break
        except:
            pyautogui.press('pagedown')

#criar função para enviar email
def enviarEmail():
    #atalho para abrir a nova guia
    pyautogui.hotkey('ctrl', 't')
    time.sleep(1)
    pyautogui.write('www.gmail.com')
    pyautogui.press('enter')
    time.sleep(3)

    xy = pyautogui.locateCenterOnScreen('aula8\\escrever.png', confidence = 0.95)
    pyautogui.click(xy)

    time.sleep(2)

    pyautogui.write('softip@gmail.com')
    pyautogui.press('enter')

    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.write('Assunto: Pesquisa automatizada')

    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')

    xy = pyautogui.locateCenterOnScreen('aula8\\enviar.png', confidence = 0.95)
    pyautogui.click(xy)


#Parte Principal do Programa

#abre uma janela parao usuario digitar um texto

pesquisa = pyautogui.prompt('O que você quer pesquisar hoje?')
abrirChrome()
pesquisarNoGPT()
enviarEmail()
D