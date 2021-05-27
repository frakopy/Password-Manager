import pyperclip, time
import pyautogui as pg
import win32gui, win32con

#-------------------------------------------------------------
#Para esconder la consola de windows de forma automatica:
consola = win32gui.GetForegroundWindow()
win32gui.ShowWindow(consola , win32con.SW_HIDE)
#-------------------------------------------------------------

#Para copiar un texto al porta papeles, es decir que si luego usamos las combinaciones del teclado de
#ctrl + v ó click derecho y seleccionar pegar entonces este texto se pegara en la zona en la que se encuentre el cursor
#pyperclip.copy('Hola Mundo!!!')

pg.click()#Para que se active la pantalla en la que deseamos escribir el passowrd

#El texto que hayamos copiado con ctr+c o copy con las opciones de windows lo pegamos
#y lo guardamos en una variable
texto_copiado = pyperclip.paste() 

#Usando pyautogui entonces escribimos el texto que habiamos copiado
pg.typewrite(texto_copiado)
time.sleep(0.5)
pg.press('Enter')
#-------------------------------------------------------------
