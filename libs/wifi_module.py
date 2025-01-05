import network
from time import sleep
def setup_wifi():
  sta_if = network.WLAN(network.STA_IF) # create station interface. STA_IF for station interface (use AP_IF for access point interface)
  return sta_if


def connect_wifi(sta_if, ssid, password):
  #"""
  #Create a network object and connect to wifi network with input ssid and password.
  
  #Example:
  #connect_wifi(ssid, password)
  #"""
  sta_if.active(True) # activate station interface
  if not sta_if.isconnected():
    print('connecting to network...')
    sta_if.connect(ssid, password) # connect to network with ssid and password
    counter = 0
    while not sta_if.isconnected():
      if counter < 10:
          print('.')
          counter += 1
          sleep(1)
      else:
          return
  else:
    print ('Connected')

def disconnect_wifi(sta_if):
  """_summary_
  Disconnect to the current wifi network
  
  Example:
  disconnect_wifi(sta_if)
  """
  sta_if.active(False) # deactivate station interface
  if not sta_if.isconnected():
    print('Already disconnected')

def status(sta_if):
  if sta_if.isconnected():
    print("Already connected")
    print(f"IP address: {sta_if.ifconfig()[0]}")
    print(f"Subnet mask: {sta_if.ifconfig()[1]}")
    print(f"Gateway: {sta_if.ifconfig()[2]}")
    print(f"DNS server: {sta_if.ifconfig()[3]}")
