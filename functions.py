import pyautogui

def findwhat(listy, item = ""):
    output = []
    for element in listy:
        titr = element.title
        if (titr.find(item) >= 0):
            bro = titr[:titr.find(item)] + titr[titr.find(item) + len(item):] 
            output.append(bro)
    return output

windows = pyautogui.getAllWindows()

window=findwhat(windows, " - Inkscape")