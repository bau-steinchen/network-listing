#!/usr/bin/python

import json
from pathlib import Path

FILENAME = 'nlist.json'

class Tool:
    def __init__(self):
        if not Path(FILENAME).exists():
            data = {'config': 'network.json'}
            with open(FILENAME, 'w') as f:
                json.dump(data, f)
            
    def get_config_location(self):
        with open(FILENAME, 'r') as f:
            data = json.load(f)
        return data['config']
    
    def set_config_location(self, filepath):
        data = { 'config': filepath}
        with open(FILENAME, 'w') as f:
            json.dump(data, f)