import time
import psutil
from pypresence import Presence
import keyboard

client_id ="842103064449253413"
RPC = Presence(client_id)
RPC.connect()

while True:
    if ("ShareX.exe" in (i.name() for i in psutil.process_iter()))== True:
        RPC.update(
            state= "ShareX Oynuyor",
        )
    issic= round(psutil.cpu_percent(),1)
    isram= round(psutil.virtual_memory().percent,1)
    RPC.update(
        details="CPU Usage= "+ str(issic)+"%",
        
        buttons= [{"label": "GitHub", "url": "https://github.com/POTATOX35/pcstats-discrd-richpresence"}],
         small_text="zort",
        start=int(time.time())
    )
    time.sleep(5)
    
    