import time
import psutil
from pypresence import Presence
import pyautogui
from functions import *

client_id ="842103064449253413"
RPC = Presence(client_id)
RPC.connect()
lastname = ''
project_name = '   '
while True:
    windows = pyautogui.getAllWindows()

    window=findwhat(windows, " - Inkscape")
    if  len(window) >=  1:
         project_name=window[0]
    mayso = project_name
    if project_name == "" or project_name == "   ":
        mayso = "Idling..."
    else:
        mayso = "Editing " + project_name

    if ("inkscape.exe" in (i.name() for i in psutil.process_iter())) == True:
        if (lastname != project_name):

            RPC.connect()
            lastname = project_name
            RPC.update(
            state=mayso,
            large_image="logo1",
            large_text="Playing Inkscape",
            start=int(time.time())
        )
    else:
        RPC.close()
    time.sleep(5)
    
    
    
    
    