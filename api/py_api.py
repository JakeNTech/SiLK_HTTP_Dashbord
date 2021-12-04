#!/usr/bin/python3
"""
API for System interaction
JakeNTech
2021
"""
from datetime import datetime
import subprocess
import json
import pandas as pd
import random
import string
from api import mr_maker

def api(action):
    if action == "silk_status":
        #yaf_status = command_runner("echo Stopped").read()
        yaf_status = "Stopped"
        #rwflowpack_status = command_runner("echo Stopped").read()
        rwflowpack_status = "Stopped"
        to_return = {"rwflowpack": rwflowpack_status ,"yaf": yaf_status}
    elif action == "today_stats":
        to_return = chunk_stats(current_date(),current_date())
    else:
        to_return = {"Error":"400 Bad Request"}
    return to_return

def chunk_stats(s_date,e_date):
    #command = f"rwfilter --sensor={G_sensor} --start-date={s_date} --end-date{e_date} --type=all --all=stdout | rwcut --delim=','"
    #command = command.split(" ")
    #flow_data = subprocess.run(command, capture_output=True, text=True)
    #flow_data = (flow_data.stdout)
    #command_runner(f"rwfilter --sensor=S0 --start-date={s_date} --end-date{e_date} --type=all --all=stdout | rwcut --delim=',' > ./api/temp/csv_data/{data_path}.csv")
    # CODE FOR READING FROM TEST CSV
    data_path = "/mnt/c/Users/JakeNTech/Documents/GitHub/SiLK_HTTP_Dashbord/TestData/traffic_5minutes.csv"
    df = read_csv(data_path)
    packet_count = round((df["Packets"].sum()),2)
    record_count = round(df["Records"].sum())
    data_count = round((df["Bytes"].sum()/1000000),2)
    graph_paths = mr_maker.graph_chunk_data(df,random_string(10))
    to_return = {"packet_count":packet_count,"record_count":record_count,"data_count":data_count,"data_unit":"MB","current_date":current_date(), "graph_paths": graph_paths}
    return to_return

#Misc Functions
def current_date():
    return datetime.now().strftime("%Y/%m/%d")
def random_string(no):
    return ''.join(random.choice(string.ascii_letters) for i in range(no))
def read_csv(filename):
    return pd.read_csv(filename)