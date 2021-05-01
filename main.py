from pynput.mouse import Button, Controller
import keyboard
import PySimpleGUI as sg
import threading
import time

mouse = Controller()

layout = [[sg.Text("Click Speed (ms):", size=(15, 1)), sg.InputText()],
          [sg.Text("HotKey:", size=(15, 1)), sg.InputText()],
          [sg.Button("Start")],
          [sg.Button("Reset")]]
window = sg.Window(title="PyClicker", layout=layout, margins=(35, 40))


def input_values():
    while True:
        event, values = window.read()

        if event == "Start":
            interval = float(values[0]) * 0.001
            hotkey = values[1]
            break

    return interval, hotkey


def auto_click():
    while True:
        while keyboard.is_pressed(hotkey):
            mouse.click(Button.left, 1)
            time.sleep(interval)


interval, hotkey = input_values()

clicker = threading.Thread(target=auto_click,  daemon=True)
clicker.start()

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event == "Reset":
        interval, hotkey = input_values()

window.close()
