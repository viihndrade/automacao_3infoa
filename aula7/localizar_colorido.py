import pyautogui

while True:
    try:
        xy = pyautogui.locateCenterOnScreen(
        'aula7\\vermelhojogo.png', 
        confidence= 0.99, 
        grayscale= False)

        pyautogui.click(xy)

