from libs.wifi_module import setup_wifi, connect_wifi, disconnect_wifi, status
import json
import network
import os

from libs.time import calibrate_time
from libs.request_module import send_post_request
from machine import Pin, deepsleep, TouchPad, Pin
from time import sleep
import machine
import esp32
import json
import urequests as request

rtc = machine.RTC()
print(rtc.memory())


if rtc.memory() == b'':
    with open('../config/config.json') as file: # open config file
      config = json.load(file)  # load config file and deserialize it to a dictionary
    ssid = config.get("wifi", {}).get("ssid_1") # get ssid from config dictionary
    password = config.get("wifi", {}).get("password_1") # get password from config dictionary
    #print(ssid, password)

    sta_if = setup_wifi() # create wifi station interface
    connect_wifi(sta_if=sta_if, ssid=ssid, password=password) # connect to wifi network
    # disconnect_wifi(sta_if=sta_if) # disconnect from wifi network
    status(sta_if=sta_if) # print status of wifi connection


