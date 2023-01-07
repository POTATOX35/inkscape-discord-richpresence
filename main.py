import time
import psutil
from pypresence import Presence
import keyboard

client_id ="842103064449253413"
RPC = Presence(client_id)
RPC.connect()

while True:
    if ("inkscape.exe" in (i.name() for i in psutil.process_iter())) == True:
        RPC.update(
        details="Çalışıyor",
        large_image="logo"
        )
    else:
        RPC.close()
        time.sleep(time.time)
    
    
    
    
    