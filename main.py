import time
import psutil
from pypresence import Presence
import pyautogui
from functions import *

client_id ="842103064449253413"
RPC = Presence(client_id)
RPC.connect()
lastname = ''
while True:
    windows = pyautogui.getAllWindows()

    window=findwhat(windows, " - Inkscape")
    if  window[0] != None:
        project_name=window[0]
    if ("inkscape.exe" in (i.name() for i in psutil.process_iter())) == True:
        if (lastname != project_name):
            RPC.connect()
            lastname = project_name
            RPC.update(
            state="Editing " + project_name,
            large_image="logo1",
            large_text="Playing Inkscape",
            start=int(time.time())
        )
    else:
        RPC.close()
    time.sleep(5)
    
    
    
    
    