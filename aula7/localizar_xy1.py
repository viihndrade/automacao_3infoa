#importa a biblioteca(módulo) que controla o
#mouse e o teclado
import pyautogui

#localiza as coordenadas de um elemento na tela
#usando ma imagem
o = pyautogui.locateCenterOnScreen('aula7\\8.png', confidence=0.99)
print (o)
pyautogui.click (o, duration=1)

m = pyautogui.locateCenterOnScreen('aula7\\Multiplicar.png', confidence=0.99)
print (m)
pyautogui.click (m, duration=1)

t = pyautogui.locateCenterOnScreen('aula7\\3.png', confidence=0.99)
print (t)
pyautogui.click (t, duration=1)

i = pyautogui.locateCenterOnScreen('aula7\\Igual.png', confidence=0.99)
print (i)
pyautogui.click (i, duration=1)