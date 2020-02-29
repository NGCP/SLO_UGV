"""Autonomous UGV"""
from dronekit import VehicleMode, Vehicle, LocationGlobalRelative
class UGV(Vehicle):
    def __init__(self, *args):
        super(UGV, self).__init__(*args)
    
    def setup(self):
        #TODO
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

