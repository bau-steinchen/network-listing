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

##########################################################################
# main 
##########################################################################
def main():
    with open('nlist', 'r') as f:
        data = json.load(f)
    # print (data['config'])
    # handle config file
    conf = data['config']
    if not os.path.exists(conf):
        with open(conf, 'w') as datei:
            datei.write('') 


    # create an run gui loop
    GUI(default_config=conf).run()



###########################################################################
# entry point
###########################################################################
if __name__ == '__main__':
    main()
