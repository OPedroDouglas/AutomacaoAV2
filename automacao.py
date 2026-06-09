import pyautogui  # Biblioteca de automação
import time  # Biblioteca de tempo

pyautogui.PAUSE = 1 # Pausa para linha de comando

pyautogui.press('Win') # Abrir o Windows
pyautogui.write('Chrome') # Abrir o Google Chrome
pyautogui.press('enter') # Apertar a tecla Enter
pyautogui.write('https://www.tinkercad.com/dashboard') # Abrir o TInkerCad
pyautogui.press('enter') # Apertar a tecla Enter

time.sleep(5) # Tempo de espera pra entrar no site de 5 segundos

pyautogui.PAUSE = 1 # Pausa para linha de comando

pyautogui.click(x=169, y=647) # Abre a pasta de coleção
pyautogui.click(x=575, y=448) # Escolhe o projeto
pyautogui.click(x=549, y=625) # Abre o resumo do projeto 
pyautogui.click(x=1304, y=738) # Abre o projeto

time.sleep(4)

pyautogui.click(x=1657, y=230) # Inicia o sistema

time.sleep(2)

pyautogui.click(x=1505, y=236) # Mostra o codígo

time.sleep(2)

pyautogui.click(x=1261, y=1001) # Mostra o Serial Monitor

time.sleep(6)

pyautogui.click(x=1657, y=230) # Para o sistema

time.sleep(1)

pyautogui.click(x=1505, y=236) # Oculta o codígo