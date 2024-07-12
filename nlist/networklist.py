#!/usr/bin/python
"""
This tool can scan a given network range and list all available endpoints.
For a existing config file additional documentation can be made

Author: bau-steinchen
GitHub: https://github.com/bau-steinchen
"""
import os
import json

from gui.kivy import GUI

from helper.tool import Tool

##########################################################################
# main 
##########################################################################
def main():
    
    conf = Tool().get_config_location()
    # print(conf)

    # create an run gui loop
    GUI(default_config=conf).run()

###########################################################################
# entry point
###########################################################################
if __name__ == '__main__':
    main()
