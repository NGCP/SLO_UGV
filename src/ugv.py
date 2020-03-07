"""Autonomous UGV"""
import time
from math import radians
from dronekit import VehicleMode, Vehicle, LocationGlobalRelative
from pymavlink import mavutil
from coms import Coms
from util import get_distance_metres, to_quaternion


class UGV(Vehicle):
    def __init__(self, *args):
        super(UGV, self).__init__(*args)
    
    def setup(self):
        print('Initializing Coms')
        self.coms = Coms(self.configs, self.coms_callback)
        
        msg = {
        "type": "connect",
        "time": 0, # This field is currently not used
        "sid": self.configs['vehicle_id'],
        "tid": 0, # The ID of GCS
        "id": 0, # The ID of this message
        }
        
        self.coms.send_till_ack(self.configs["mission_control_MAC"], msg, msg['id'])
        return None
        
    configs = None

    def start_auto_mission(self):
        '''Arms and starts an AUTO mission loaded onto the vehicle'''
        while not self.is_armable:
            print(" Waiting for vehicle to initialise...")
            time.sleep(1)

        self.mode = VehicleMode("GUIDED")
        self.armed = True

        while not self.armed:
            print(" Waiting for arming...")
            time.sleep(1)

        self.commands.next = 0
        self.mode = VehicleMode("AUTO")

        msg = self.message_factory.command_long_encode(
            0, 0,    # target_system, target_component
            mavutil.mavlink.MAV_CMD_DO_SET_SERVO, #command
            0, #confirmation
            3, 1500, 0, 0, 0, 0, 0)    # param 1 ~ 7 not used
        # send command to vehicle
        self.send_mavlink(msg)

        self.commands.next = 0

    # def locate_vehicle(self):
    #     while True:
    #         self.rotate_vehicle()
    #         if ultraSonicDistance < 1:
    #             break
    #     return gyroValue

    # def goto_vehicle(self):
    #     while ultraSonicDistance > 1:

    def coms_callback(self, command):
        '''callback for radio messages'''

        #tuple of commands that can be executed
        valid_commands = ("start", "load", "go_to", "return", "stop", "manual")
        #gives us the specific command we want the drone to executre

        #checking for valid command
        if command["Type"] not in valid_commands:
            raise Exception("Error: Unsupported status for vehicle")

        #executes takeoff command to drone
        if command["Type"] == 'start':
            #TODO
            pass
        #executes land command to drone
        
        elif command["Type"] == 'load':
            #TODO
            pass
        
        elif command["Type"] == 'go_to':
            #TODO
            pass
            self.go_to(LocationGlobalRelative(command["Body"]["Lat"], \
                command["Body"]["Lon"], command["Body"]["Alt"]))
        
        elif command["Type"] == 'stop':
            #TODO
            pass
        
        elif command["Type"] == 'manual':
            #TODO
            pass