#!/usr/bin/env python

import subprocess
import optparse
import re

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
    print("[+} Changing MAC address for " + interface + " to " + newMac)
    subprocess.call("ifconfig " + interface + " down", shell=True)
    subprocess.call("ifconfig " + interface + " hw ether " + newMac, shell=True)
    subprocess.call("ifconfig " + interface + " up", shell=True)
  

def getcurrentMac(interface):
    ifconfigResult = subprocess.check_output(["ifconfig", interface])

    macAddressSearch = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfigResult))

    if macAddressSearch:
        return macAddressSearch.group(0)
    else:
        print("[-] Could not read MAC address")

options = getArguments()

currentMac = getcurrentMac(options.interface)
print("Current MAC = " + str(currentMac))

changeMac(options.interface, options.newMac)

currentMac = getcurrentMac(options.interface)
if currentMac == options.newMac:
    print("[+] Mac address was successfully changed to " + currentMac)
else:
    print("[-] MAC address did not get changed.")
