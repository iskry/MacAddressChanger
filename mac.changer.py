#!/usr/bin/env python

import subprocess
import optparse

def getArguments(): 
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="newMac", help="new MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.newMac:
        parser.error("[-] Please specify a new MAC, use --help for more info.")
    return options

def changeMac(interface, newMac):
    print("[+} Changing MAC addres for " + interface + " to " + newMac)
    subprocess.call("ifconfig " + interface + " down", shell=True)
    subprocess.call("ifconfig " + interface + " hw ether " + newMac, shell=True)
    subprocess.call("ifconfig " + interface + " up", shell=True)

options = getArguments()
changeMac(options.interface, options.newMac)

