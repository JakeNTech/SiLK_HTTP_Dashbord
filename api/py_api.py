#!/usr/bin/python3
"""
API for System interaction
JakeNTech
2021
"""
from datetime import datetime
import subprocess
"""
API for Getting Data out of SiLK
"""
def api(action):
    if action == "current_time":
        to_return = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    elif action == "echo_system":
        result = subprocess.run(["ls","-a"], capture_output=True, text=True)
        to_return = result.stdout
    else:
        to_return = "400 Bad Request."
    return(to_return)
