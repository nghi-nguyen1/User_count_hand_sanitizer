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

#with open('../config/config.json') as file: # open config file
# config = json.load(file)  # load config file and deserialize it to a dictionary

rtc = machine.RTC()
#print(rtc.memory())
button_pressed_numbers = 0

wake1 = Pin(14, mode = Pin.IN)
print("Button_pressed_number: " + str(button_pressed_numbers))
esp32.wake_on_ext0(pin = wake1, level = esp32.WAKEUP_ANY_HIGH)

if not rtc.memory() == b'':
    button_pressed_numbers = int(rtc.memory().decode("utf-8")[0]) + 1
    #print(f"button type: {type(button_pressed_numbers)}")
    print(f"button: {button_pressed_numbers}")
    #print(f"button: {button_pressed_numbers[0]}")

#if button_pressed_numbers == 0 or button_pressed_numbers == 5:
#    with open('../config/config.json') as file: # open config file
#      config = json.load(file)  # load config file and deserialize it to a dictionary
#    ssid = config.get("wifi", {}).get("ssid_2") # get ssid from config dictionary
#    password = config.get("wifi", {}).get("password_2") # get password from config dictionary
#    print(ssid, password)

#    sta_if = setup_wifi() # create wifi station interface
#    connect_wifi(sta_if=sta_if, ssid=ssid, password=password) # connect to wifi network
#    # disconnect_wifi(sta_if=sta_if) # disconnect from wifi network
#    status(sta_if=sta_if) # print status of wifi connection
    
    
if button_pressed_numbers == 0: # first url
    print('task1')
    time_press = calibrate_time()
    time_press = "".join(str(time_press[0:6])).replace(',','').replace(')','').replace('(','').replace(' ','')
    json_dict = {"facility" : "PlatformCalgary",}
    json_file = json.dumps(json_dict)
    res = send_post_request(url = "http://www.i4h22-hygienie.xyz/api/pump/initialize/", json = json_dict)
    #rtc.memory(str(button_pressed_numbers))
    #print(type(button_pressed_numbers))
    print(res.status_code)
    print(res.text)
    #print(type(res))
    pumpID = res.json().get("pumpID", {})
    pumpID_dict = {'pumpID': pumpID }
    with open('../config/pumpID.json', 'w') as file: # open config file
        json.dump(pumpID_dict, file)
    json_post_content = str(button_pressed_numbers) + str(pumpID)
    #print(type(json_post_content))
    #print(json_post_content)
    #print(type(json_post_content.encode()))
    #print(json_post_content.encode())
    rtc.memory(json_post_content.encode())
    # this command writes writedata into the RTC memory. Method .encode is to change data to bytearray.


sleep(2)

#pumpID = res.json().get("pumpID", {})
#if pumpID != None:
#    rtc.memory(str(pumpID))
#print (pumpID)

    
if button_pressed_numbers == 5: # second url
    with open('../config/config.json') as file: 
        config = json.load(file)  
    ssid = config.get("wifi", {}).get("ssid_1") 
    password = config.get("wifi", {}).get("password_1") 
    print(ssid, password)
    sta_if = setup_wifi() # create wifi station interface
    connect_wifi(sta_if = sta_if, ssid = ssid, password = password) # connect to wifi network
    # disconnect_wifi(sta_if=sta_if) # disconnect from wifi network
    status(sta_if=sta_if) # print status of wifi connection
    
    print("Sending post request at 10")
    print(str(rtc.memory()))
    json_dict = {"pumpID" : rtc.memory().decode("utf-8")[1:25], "uses(yyyy/m/d/hh/mm/ss)" : [rtc.memory().decode("utf-8")[25:]]}
    json_file = json.dumps(json_dict)
    res = send_post_request(url = "http://www.i4h22-hygienie.xyz/api/trigger/post-trigger", json = json_dict)
    print(res.status_code)
    print(json_file)
    print(type(rtc.memory()))
    print(res.text)
    machine.reset()
elif not button_pressed_numbers % 20 == 0:
    print('task2')
    existing_json_post_content = rtc.memory().decode("utf-8") # this command puts the RTC memory into readdata. Data is in string now
    print(existing_json_post_content)
    #with open('../config/pumpID.json') as file: # open config file
    #    pumpID = json.load(file).get("pumpID", {})
    time_press = calibrate_time()
    print("Pringting out" + str(time_press))
    print(time_press[0:6])
    time_press = "".join(str(time_press[0:6])).replace(',','').replace(')','').replace('(','').replace(' ','')
    json_post_content = str(button_pressed_numbers) + existing_json_post_content[1:] + time_press +'__'
    print(json_post_content.encode())
    rtc.memory(json_post_content.encode())
    #print ('y/m/d/h/m/s:' + str(time_press[0:6]))
    #rtc.memory(str(time_press[0:6]))
    #print("button_pressed: " + str(button_pressed_numbers) + " at y/m/d/h/m/s:" + str(time_press[0:6]))
    #json_dict = {"pumpID" : pumpID, "uses" : [str(time_press[0:6])]}
    #json_file = json.dumps(json_dict)
    #res = send_post_request(url = "http://www.i4h22-hygienie.xyz/api/trigger/post-trigger", json = json_dict)
    #rtc.memory(str(button_pressed_numbers))
    #print(res.status_code)
#else:
#    print('No button pressed')
#    print('I am going to sleep')
#    sleep(2)


print('Go to deep sleep')
deepsleep(1000000)
