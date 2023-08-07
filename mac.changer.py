#!/usr/bin/env python

import subprocess
import optparse

parser = optparse.OptionParser()
 
parser.add_input("-i", "--interface", dest="interface" help="interface to change its MAC address")
parser.add_input("-m", "--mac", dest="newMac", help="new MAC address")

parser.parse_args()


interface = input("Interface > ")
newMac = input("New MAC address > ")


print("[+} Changing MAC addres for " + interface + " to " + newMac)

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + newMac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)

