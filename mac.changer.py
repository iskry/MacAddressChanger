#!/usr/bin/env python

import subprocess
import optparse

def getArguments(): 
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="newMac", help="new MAC address")
    return parser.parse_args()

def changeMac(interface, newMac):
    print("[+} Changing MAC addres for " + interface + " to " + newMac)
    subprocess.call("ifconfig " + interface + " down", shell=True)
    subprocess.call("ifconfig " + interface + " hw ether " + newMac, shell=True)
    subprocess.call("ifconfig " + interface + " up", shell=True)

(options, arguments) = getArguments()
changeMac(options.interface, options.newMac)

