from message_services.telegram.cron_jobs import startEventUpdater
from database.database import *
import sys, codecs
import threading


sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
chatBot = {
    "name": "Coddy",
}




threads = []
threads.append(threading.Thread(target=startEventUpdater))

for thread in threads:
    thread.daemon = True
    thread.start()
for thread in threads:
    thread.join()