#!/usr/bin/env python

import subprocess

interface = "wlan0"
newMac = "00:11:22:33:44:77"


print("[+} Changing MAC addres for " + interface + " to " + newMac)

#subprocess.call("ifconfig wlan0 down", shell=True)
#subprocess.call("ifconfig wlan0 hw ether 00:11:22:33:44:55", shell=True)
#subprocess.call("ifconfig wlan0 up", shell=True)

