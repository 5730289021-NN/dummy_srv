#! /usr/bin/env python
# Obtain from https://www.theconstructsim.com/ros-5-mins-029-create-ros-service-server/
import rospy                                      # the main module for ROS-python programs
from std_srvs.srv import Trigger, TriggerResponse # we are creating a 'Trigger service'...
                                                  # ...Other types are available, and you can create
                                                  # custom types
def trigger_response(request):
    ''' 
    Callback function used by the service server to process
    requests from clients. It returns a TriggerResponse
    '''
    return TriggerResponse(
        success=True,
        message="Hey, roger that; we'll be right there!"
    )

rospy.init_node('sos_service')                     # initialize a ROS node

rospy.loginfo('SOS Service Run')

my_service = rospy.Service(                        # create a service, specifying its name,
    '/fake_911', Trigger, trigger_response         # type, and callback
)
rospy.spin()                                       # Keep the program from exiting, until Ctrl + C is pressed