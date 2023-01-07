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
    if ("inkscape.exe" in (i.name() for i in psutil.process_iter())) == True:
        if (lastname != project_name):
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
    
    
    
    
    