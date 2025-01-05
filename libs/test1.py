
with open('../config/config.json') as file:
    config = json.load(file)  
ssid = config.get("wifi", {}).get("ssid_1") 
password = config.get("wifi", {}).get("password_1") 
print(ssid, password)
sta_if = setup_wifi() # create wifi station interface
connect_wifi(sta_if = sta_if, ssid = ssid, password = password) # connect to wifi network
    # disconnect_wifi(sta_if=sta_if) # disconnect from wifi network
status(sta_if=sta_if) # print status of wifi connection