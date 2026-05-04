import pyautogui
import time

def abrirChrome():
    #pressiona junto as teclas windows e d
    #win + d é o atalho para mostrar o desktop
    pyautogui.hotkey('win', 'd')
    #pressiona a tecla win
    pyautogui.press('win')
    #digita um texto
    pyautogui.write('chrome', interval=0.2)
    #pressiona enter
    pyautogui.press('enter')
    
    #faz uma pausa de 1 seg
    time.sleep(1)
    pyautogui.press('tab')
    pyautogui.press('enter')                 
    #pressiona win + seta para cima - para maximizar a janela
    pyautogui.hotkey('win', 'up')

abrirChrome()
time.sleep(2)

pyautogui.write('chrome://dino')
pyautogui.press('enter')

while True:
    time.sleep(0.5)
    pyautogui.press('space')      