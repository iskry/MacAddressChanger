#!/usr/bin/env python

import subprocess

interface = input("Interface > ")
newMac = input("New MAC address > ")


print("[+} Changing MAC addres for " + interface + " to " + newMac)

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + newMac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)

