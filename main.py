import time
import psutil
from pypresence import Presence

client_id ="842103064449253413"
RPC = Presence(client_id)
RPC.connect()

while True:
    issic= round(psutil.cpu_percent(),1)
   
    isram= round(psutil.virtual_memory().percent,1)
    RPC.update(
        details="CPU Usage= "+ str(issic)+"%",
        state= "RAM Usage= "+str(isram)+"%",
        buttons= [{"label": "GitHub", "url": "https://github.com/POTATOX35/pcstats-discrd-richpresence"}]
    )
    time.sleep(5)