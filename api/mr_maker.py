import matplotlib.pyplot as plt
from api import configure

plt.rcParams["figure.figsize"] = (20,10)

def convert_to_unit(x):
    return x/configure.G_data_unit

def line_graph_chunk_data(df,file_name):
    # Bytes_Time
    df_time = list(range(0,len(df["Date"])))
    df['Bytes'] = df['Bytes'].map(convert_to_unit)
    plt.plot(df_time,df["Bytes"])
    plt.title("Bytes over Time")
    plt.xlabel("Time")
    plt.ylabel(configure.G_string_data_unit)
    plt.savefig(f"./static/assets/img/temp_graphs/{file_name}_bytes_time.png")
    plt.close()
    # Records Time
    plt.plot(df_time,df["Records"])
    plt.title("Records over Time")
    plt.xlabel("Time")
    plt.ylabel(configure.G_string_data_unit)
    plt.savefig(f"./static/assets/img/temp_graphs/{file_name}_records_time.png")
    plt.close()
    # Packets Over Time
    plt.plot(df_time,df["Packets"])
    plt.title("Packets over Time")
    plt.xlabel("Time")
    plt.ylabel(configure.G_string_data_unit)
    plt.savefig(f"./static/assets/img/temp_graphs/{file_name}_records_time.png")
    plt.close()
    # Packets_Over_Bytes
    plt.scatter(df["Packets"],df["Bytes"])
    plt.xlabel("Bytes")
    plt.ylabel("Packetes")
    plt.title("Packets Over bytes")
    plt.savefig(f"./static/assets/img/temp_graphs/{file_name}_packets_bytes.png")
    plt.close()
    to_return ={"bytes_time":f"/assets/img/temp_graphs/{file_name}_bytes_time.png", "records_time": f"/assets/img/temp_graphs/{file_name}_records_time.png", "packets_bytes": f"/assets/img/temp_graphs/{file_name}_packets_bytes.png"} 
    return to_return