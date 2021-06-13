#!/usr/bin/python3
"""
API for System interaction
JakeNTech
2021
"""
from datetime import datetime
from os import popen as command_runner
from flask import jsonify

def request(action):
    # if action == "current_time":
    #    to_return = {"current_time": current_time()}
    # elif action == "echo_system":
    #     to_return = {"echo_system": run_os_command("ls -a")}
    if action == "silk_status":
        # Actual comands commented out as SiLK isn't installed in dev enviroment
        #yaf_status = run_os_command("service yaf status")
        #rwflowpack_status = run_os_command("service rwflowpack status")
        yaf_status = command_runner("echo Stopped").read()
        rwflowpack_status = command_runner("echo Stopped").read()
        to_return = {"rwflowpack": rwflowpack_status ,"yaf": yaf_status}
    else:
        to_return = {"Error":"400 Bad Request"}
    return jsonify(to_return)

def current_time():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")