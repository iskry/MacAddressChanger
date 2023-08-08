# MAC Address Changer

This program allows users to change the MAC (Media Access Control) address of a specified network interface.

## Operating System Compatibility:

The program is designed for Unix-like operating systems, such as Linux and macOS. It will not work on Windows due to the usage of the `ifconfig` command.

## Features:

- Easily change the MAC address of a specific network interface.
- Check the current MAC address of the specified interface.
- Confirm whether the MAC address was successfully changed.

## Prerequisites:

- Python 2.x (due to the usage of `optparse`) (Will also work on Python 3.x)

## How to Use:

1. Clone the repository to your local machine.
2. Navigate to the directory containing the script.
3. Make the script executable:
    ```bash
    chmod +x <script_name>.py
    ```
4. Run the program with the following syntax:
    ```bash
    ./<script_name>.py -i <interface_name> -m <new_MAC_address>
    ```
    Replace `<script_name>` with the name of the Python script, `<interface_name>` with the name of your network interface (e.g., eth0, wlan0), and `<new_MAC_address>` with the desired MAC address.

   For example:
    ```bash
    ./mac_changer.py -i eth0 -m 00:11:22:33:44:55
    ```

## Help:

For more information about the available options, use:
```bash
./<script_name>.py --help

