'''main executable for setting up UGV'''
import json
from util import setup_vehicle
from ugv import UGV

def main(configs):
    '''Configure vtol and ready for mission'''
    # pylint: disable=unused-variable
    vehicle = setup_vehicle(configs, UGV)
    vehicle.start_auto_mission()

if __name__ == '__main__':
    with open('../configs.json', 'r') as configs:
        main(json.load(configs))
        