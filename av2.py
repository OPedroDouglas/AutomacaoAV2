import pyautogui  # Biblioteca de automação
import time  # Biblioteca de tempo
import pandas  # Biblioteca de arquivos

pyautogui.PAUSE = 1 # Pausa para linha de comando

pyautogui.press('Win') # Abrir o Windows
pyautogui.write('Chrome') # Abrir o Google Chrome
pyautogui.press('enter') # Apertar a tecla Enter
pyautogui.write('https://www.tinkercad.com/dashboard') # Abrir o Youtube
pyautogui.press('enter') # Apertar a tecla Enter

time.sleep(5) # Tempo de espera pra entrar no site de 3 segundos

pyautogui.PAUSE = 1

pyautogui.click(x=169, y=647) # Posição do mouse
pyautogui.click(x=639, y=447) # Posição do mouse
pyautogui.click(x=549, y=601) # Posição do mouse
pyautogui.click(x=1301, y=499) # Posição do mouse

time.sleep(4)

pyautogui.click(x=1657, y=230) # Posição do mouse

time.sleep(6)

pyautogui.click(x=1657, y=230) # Posição do mouse

time.sleep(1)

pyautogui.click(x=1505, y=236) # Posição do mouse
