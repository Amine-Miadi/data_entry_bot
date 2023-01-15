import PySimpleGUI as sg
import pyautogui
import keyboard
import time
import sys
import os

text = []
exitProgram = False
working_directory = os.getcwd()



#setting exit conditions, set 'q' as the button to stop program
keyboard.add_hotkey('q', lambda: quit())

def quit():
    global exitProgram
    exitProgram=True



layout = [  
            [sg.Text("Choose a text file:")],
            [sg.InputText(key="-FILE_PATH-"), 
            sg.FileBrowse(initial_folder=working_directory, file_types=[("txt Files", "*.txt")])],
            [sg.Button('Submit'), sg.Exit()]
        ]

window = sg.Window("IDs Loader", layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == "Submit":
        path = values["-FILE_PATH-"]
        with open(path) as f:
            data = f.readlines()
        for id in data:
            text.append(id[:-1])
    break

time.sleep(5)
#loop as long as hotkey is not pressed
for line in text:
    if(exitProgram):
        sys.exit()
    pyautogui.typewrite(line)
    time.sleep(1)
    pyautogui.typewrite("\n")
    pyautogui.hotkey("ctrlleft", "a")
    pyautogui.hotkey('delete')

window.close()