#!/usr/bin/env python

# Import necessary libraries
import subprocess
import optparse
import re

# Define a function to get command-line arguments from the user
def getArguments(): 
    # Create an OptionParser object to handle parsing of command-line options
    parser = optparse.OptionParser()

    # Add options for the interface and new MAC address
    parser.add_option("-i", "--interface", dest="interface", help="interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="newMac", help="new MAC address")

    # Parse the command-line arguments
    (options, arguments) = parser.parse_args()

    # Check if user provided both interface and MAC address, else display error
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.newMac:
        parser.error("[-] Please specify a new MAC, use --help for more info.")

    # Return the parsed options
    return options

# Define a function to change the MAC address for the provided interface
def changeMac(interface, newMac):
    print("[+} Changing MAC address for " + interface + " to " + newMac)
    # Bring the network interface down
    subprocess.call("ifconfig " + interface + " down", shell=True)
    # Set the new MAC address
    subprocess.call("ifconfig " + interface + " hw ether " + newMac, shell=True)
    # Bring the network interface back up
    subprocess.call("ifconfig " + interface + " up", shell=True)

# Define a function to get the current MAC address for the provided interface
def getcurrentMac(interface):
    # Execute the ifconfig command for the provided interface
    ifconfigResult = subprocess.check_output(["ifconfig", interface])

    # Use regex to search for MAC address pattern in the ifconfig output
    macAddressSearch = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfigResult))

    # Return the MAC address if found, else display error
    if macAddressSearch:
        return macAddressSearch.group(0)
    else:
        print("[-] Could not read MAC address")

# Get the command-line arguments
options = getArguments()

# Fetch and print the current MAC address
currentMac = getcurrentMac(options.interface)
print("Current MAC = " + str(currentMac))

# Change the MAC address using the provided arguments
changeMac(options.interface, options.newMac)

# Fetch and compare the updated MAC address with the intended MAC address
currentMac = getcurrentMac(options.interface)
if currentMac == options.newMac:
    print("[+] Mac address was successfully changed to " + currentMac)
else:
    print("[-] MAC address did not get changed.")

