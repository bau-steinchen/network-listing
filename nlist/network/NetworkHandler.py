#!/usr/bin/python

import os
import platform

class NetworkHandler():
    def __init__(self) -> None:
        pass

    def check_device_status(self, device_ip):
        # "-c 1" means to send only one packet of data
        if platform.system().lower() == "windows":
            response = os.system(f"ping -n 1 {device_ip}")
        else:
            response = os.system(f"ping -c 1 {device_ip}")
        # Check the response
        if response == 0:
            return True
        else:
            return False
