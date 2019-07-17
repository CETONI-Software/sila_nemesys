"""
________________________________________________________________________

:PROJECT: SiLA2_python

*valvepositioncontroller_server_real *

:details: valvepositioncontroller_server_real: Allows to specify a certain logical position for a valve. The CurrentPosition property can be querried at any time to obtain the current valve position..

:file:    valvepositioncontroller_server_real.py
:authors: Florian Meinicke

:date: (creation)          20190627
:date: (last modification) 20190627

.. note:: Code generated automatically by SiLA2codegenerator v0.1.9!


           - 0.1.6
.. todo:: -
________________________________________________________________________

**Copyright**:
  This file is provided "AS IS" with NO WARRANTY OF ANY KIND,
  INCLUDING THE WARRANTIES OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.

  For further Information see LICENSE file that comes with this distribution.
________________________________________________________________________
"""
__version__ = "0.0.1"


import logging
import uuid
import time

import sila2lib.sila_error_handling as sila_error

# importing protobuf and gRPC handler/stubs
import sila2lib.SiLAFramework_pb2 as fwpb2
import ValvePositionController_pb2 as pb2
import ValvePositionController_pb2_grpc as pb2_grpc

# import qmixsdk
from qmixsdk import qmixbus
from qmixsdk import qmixpump
from qmixsdk import qmixvalve

class ValvePositionControllerReal():
    """ ValvePositionControllerReal - Allows to specify a certain logical position for a valve. The CurrentPosition property can be querried at any time to obtain the current valve position. """
    def __init__ (self, pump):
        """ ValvePositionControllerReal class initialiser """
        logging.debug("init class: ValvePositionControllerReal ")

        self.valve = pump.get_valve()
        self.num_of_valve_pos = self.valve.number_of_valve_positions()


    def SwitchToPosition(self, request, context):
        """Switches the valve to the specified position. The given position has to be less than the NumberOfPositions or else a ValidationError is thrown.
            :param request: gRPC request
            :param context: gRPC context
            :param request.Position: The target position that the valve should be switched to.

        """
        logging.debug("SwitchToPosition - Mode: real ")

        requested_valve_pos = request.Position.value
        if requested_valve_pos < 0 or requested_valve_pos >= self.num_of_valve_pos:
            sila_error.raiseRPCError(context, sila_error.getValidationError(
                parameter="Position",
                cause="The given position is not in the range for this valve.",
                action="Adjust the valve position to fit in the range between 0 and NumberOfPositions!"
            ))

        try:
            self.valve.switch_valve_to_position(requested_valve_pos)
        except qmixbus.DeviceError as err:
            logging.error("QmixSDK Error: %s", err)
            sila_error.raiseRPCError(context, sila_error.getStandardExecutionError(
                errorIdentifier="QmixSDKError", cause=str(err)
            ))

        return pb2.SwitchToPosition_Responses(Success=fwpb2.Boolean(value=True))


    def TogglePosition(self, request, context):
        """This command only applies for 2-way valves to toggle between its two different positions. If the command is called for any other valve type a ValveNotToggleable error is thrown.
        empty parameter
        """
        logging.debug("TogglePosition - Mode: real ")

        try:
            curr_pos = self.valve.actual_valve_position()
            self.valve.switch_valve_to_position((curr_pos + 1) % 2)
        except qmixbus.DeviceError as err:
            logging.error("QmixSDK Error: %s", err)
            sila_error.raiseRPCError(context, sila_error.getStandardExecutionError(
                errorIdentifier="QmixSDKError", cause=str(err)
            ))

        return pb2.TogglePosition_Responses(Success=fwpb2.Boolean(value=True))

    def Get_NumberOfPositions(self, request, context):
        """The number of the valve positions available.
            :param request: gRPC request
            :param context: gRPC context
            :param response.NumberOfPositions: The number of the valve positions available.

        """
        logging.debug("Get_NumberOfPositions - Mode: real ")

        return pb2.Get_NumberOfPositions_Responses(
            NumberOfPositions=fwpb2.Integer(value=self.num_of_valve_pos)
        )

    def Subscribe_Position(self, request, context):
        """The current logic valve position. This is a value between 0 and NumberOfPositions - 1.
            :param request: gRPC request
            :param context: gRPC context
            :param response.Position: The current logic valve position. This is a value between 0 and NumberOfPositions - 1.

        """
        logging.debug("Subscribe_Position - Mode: real ")

        while True:
            yield pb2.Subscribe_Position_Responses(
                Position=fwpb2.Integer(value=self.valve.actual_valve_position())
            )

            # we add a small delay to give the client a chance to keep up.
            time.sleep(0.5)



