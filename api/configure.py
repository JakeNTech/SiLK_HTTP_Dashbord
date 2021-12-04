import json
def init(path):
    global G_decimal_places
    global G_data_unit
    global G_string_data_unit
    config_file = open(path,"r").read()
    config_file = json.loads(config_file)
    # Use Try incase it's not in the config file
    try:
        # Define the devision to convert Bytes from or to leave them as Bytes.
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
    except:
        G_data_unit = 1
        G_string_data_unit = "B"
    # Set the number of decimal places
    try:
        G_decimal_places = config_file["decimal_places"]
    except:
        G_decimal_places = 3
    # Sensor Name
    try:
        G_Sensor_name = config_file["sensor_name"]
    except:
        G_Sensor_name = "S0"