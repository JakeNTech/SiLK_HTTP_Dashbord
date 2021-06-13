#!/usr/bin/python3
"""
API for System interaction
JakeNTech
2021
"""
from datetime import datetime
from os import popen as command_runner
import json
import pandas as pd
import random
import string

def configure(config_file_path):
    config_file = open(config_file_path,"r").read()
    config_file = json.loads(config_file)
    # Define the devision to convert Bytes from or to leave them as Bytes
    global G_data_unit
    global G_string_data_unit
    G_data_unit = 1
    G_string_data_unit = "B"
    if config_file["data_unit"] == "kilobytes":
        G_data_unit = 1000
        G_string_data_unit = "KB"
    elif config_file["data_unit"] == "megabytes":
        G_data_unit = 1000000
        G_string_data_unit = "MB"
    elif config_file["data_unit"] == "gigabytes":
        G_data_unit = 1000000000
        G_string_data_unit = "GB"
    elif config_file["data_unit"] == "terabytes":
        G_data_unit = 1000000000000
        G_string_data_unit = "TB"
    else:
        G_data_unit = 1
        G_string_data_unit = "B"
    global G_decimal_places
    G_decimal_places = config_file["decimal_places"]

def api(action):
    if action == "silk_status":
        yaf_status = command_runner("echo Stopped").read()
        rwflowpack_status = command_runner("echo Stopped").read()
        to_return = {"rwflowpack": rwflowpack_status ,"yaf": yaf_status}
    elif action == "today_stats":
        to_return = chunk_stats(current_date(),current_date())
    else:
        to_return = {"Error":"400 Bad Request"}
    return to_return

def chunk_stats(s_data,e_date):
    #data_path = random_string()
    data_path = "/mnt/c/Users/JakeNTech/Documents/GitHub/SiLK_HTTP_Dashbord/TestData/traffic_5minutes.csv"
    #command = f"rwfilter --sensor=S0 --start-date={s_date} --end-date{e_date} --type=all --all=stdout | rwcut --delim=',' > ./temp/csv_data/{data_path}.csv"
    #command_runner(command)
    df = pd.read_csv(data_path)
    packet_count = round((df["Packets"].sum()),G_decimal_places)
    record_count = round(df["Records"].sum())
    data_count = round((df["Bytes"].sum()/G_data_unit),G_decimal_places)
    to_return = {"packet_count":packet_count,"record_count":record_count,"data_count":data_count,"data_unit":G_string_data_unit,"current_date":current_date()}
    return to_return

#Misc Functions
def current_date():
    return datetime.now().strftime("%Y/%m/%d")
def random_string():
    return ''.join(random.choice(string.ascii_letters) for i in range(10))