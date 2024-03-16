import psutil
import time
from datetime import datetime

printed_executables = {}

def log_connected_executables():
    for process in psutil.process_iter(['exe']):
        try:
            connections = process.connections()
            if connections:
                executable = process.exe()
                if executable not in printed_executables:
                    if executable != "":
                        if executable.startswith("C:\Windows"):
                            print(datetime.now().strftime("%Hh%M") +" - "+ "\033[91m{}\033[00m".format(executable))
                            printed_executables[executable] = True
                        else:
                            print(datetime.now().strftime("%Hh%M") +" - "+ "\033[92m{}\033[00m".format(executable))
                            printed_executables[executable] = True                        
        except (psutil.AccessDenied, psutil.NoSuchProcess, psutil.ZombieProcess):
            pass

while True:
    log_connected_executables()
    time.sleep(5) 