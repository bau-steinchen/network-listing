#!/usr/bin/python

import json
from pathlib import Path

class Network:
    def __init__(self, configfile):
        if not Path(configfile).exists():
            data =  {   
                        'network': {
                            "ip": "192.168.178.0",
                            "mask": 24
                        },
                        'devices': []
                    }
            with open(configfile, 'w') as f:
                json.dump(data, f, indent=4)
        with open(configfile, 'r') as f:
            self.network = json.load(f)

    def dump_config(self):
        print(json.dumps(self.network, indent=4))

    def get_network_config(self):
        return self.network['network']
    
    def get_devices(self):
        return self.network['devices']