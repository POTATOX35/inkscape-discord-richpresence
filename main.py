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
        buttons= [{"label": "GitHub", "url": "https://github.com/POTATOX35/pcstats-discrd-richpresence"}],
    )
    else:
        RPC.close()
        time.sleep(10)
    
    
    
    
    