#!/usr/bin/env python

import subprocess
import optparse

def changeMac(interface, newMac):
    print("[+} Changing MAC addres for " + interface + " to " + newMac)

    subprocess.call("ifconfig " + interface + " down", shell=True)
    subprocess.call("ifconfig " + interface + " hw ether " + newMac, shell=True)
    subprocess.call("ifconfig " + interface + " up", shell=True)


parser = optparse.OptionParser()
 
parser.add_option("-i", "--interface", dest="interface", help="interface to change its MAC address")
parser.add_option("-m", "--mac", dest="newMac", help="new MAC address")

(options, arguments) = parser.parse_args()

changeMac(options.interface, options.newMac)
