import easygui
import os
msg = f"""Processo Muva Animation
1 Blender (importa o FBX)
2 Maya
3 Max
"""
title="MUVA ANIMATION"
choices = ["Blender","Maya","3D Max"]
reply = easygui.buttonbox(msg, title , choices=choices)
if reply == "Blender":
    os.startfile(r"C:\Program Files\Blender Foundation\Blender 3.4\blender.exe")
elif reply == "Maya":
    os.startfile(r"C:\Program Files\Autodesk\Maya2023\bin\maya.exe")
elif reply == "3D Max":
    os.startfile(r"C:\Program Files\Autodesk\3ds Max 2023\3dsmax.exe")
else:
    print("Done")
    
import pyautogui
pyautogui.PAUSE = 5

pyautogui.click(x=867, y=127)

pyautogui.PAUSE = 1

pyautogui.press("enter")
pyautogui.hotkey("ctrl","o")
pyautogui.click(x=1271, y=823)
pyautogui.click(x=1701, y=166)
pyautogui.click(x=1271, y=823)
pyautogui.hotkey("g","z")
pyautogui.write("3")
pyautogui.hotkey("enter")
pyautogui.hotkey("esc")

# pyautogui.hotkey("a")
# pyautogui.hotkey("clear")




## intervalo de pausa
# import pyautogui
# time.sleep(15)

# pyautogui.press("enter")
# pyautogui.hotkey('ctrl', 'a', interval=30) # Press the Ctrl-C hotkey combination.    
# pyautogui.hotkey('a')
# pyautogui.hotkey('del')

# # # POSICAO DO MOUSE
# import time
# time.sleep(3)
# pyautogui.position()


