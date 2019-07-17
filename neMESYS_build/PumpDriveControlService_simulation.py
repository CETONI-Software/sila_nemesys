"""
________________________________________________________________________

:PROJECT: SiLA2_python

*pumpdrivecontrolservice_server_simulation *

:details: pumpdrivecontrolservice_server_simulation: 
        Functionality to control and maintain the drive that drives the pump.
        Allows to initialize a pump (e.g. by executing a reference move) and obtain status information about the pump drive's current state (i.e. enabled/disabled).
        The initialization has to be successful in order for the pump to work correctly and dose fluids. If the initialization fails, the StandardExecutionError InitializationFailed is thrown.
    . 
           
:file:    pumpdrivecontrolservice_server_simulation.py
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
# importing protobuf and gRPC handler/stubs
import sila2lib.SiLAFramework_pb2 as fwpb2
import PumpDriveControlService_pb2 as pb2
import PumpDriveControlService_pb2_grpc as pb2_grpc


class PumpDriveControlServiceSimulation():
    """ PumpDriveControlServiceSimulation - 
#        Functionality to control and maintain the drive that drives the pump.
#        Allows to initialize a pump (e.g. by executing a reference move) and obtain status information about the pump drive's current state (i.e. enabled/disabled).
#        The initialization has to be successful in order for the pump to work correctly and dose fluids. If the initialization fails, the StandardExecutionError InitializationFailed is thrown.
#     """
    def __init__ (self):
        """ PumpDriveControlServiceSimulation class initialiser """
        logging.debug("init class: PumpDriveControlServiceSimulation ")



    def InitializePumpDrive(self, request, context):
        """Initialize the pump drive (e.g. by executing a reference move).
        empty parameter
        """
        logging.debug("InitializePumpDrive - Mode: simulation ")

        #~ return_val = request.Void.value
        #~ return pb2.InitializePumpDrive_Responses(Success=fwpb2.Boolean(value=False))

    def EnablePumpDrive(self, request, context):
        """Set the pump into enabled state.
        empty parameter
        """
        logging.debug("EnablePumpDrive - Mode: simulation ")

        #~ return_val = request.Void.value
        #~ return pb2.EnablePumpDrive_Responses()

    def DisablePumpDrive(self, request, context):
        """Set the pump into disabled state.
        empty parameter
        """
        logging.debug("DisablePumpDrive - Mode: simulation ")

        #~ return_val = request.Void.value
        #~ return pb2.DisablePumpDrive_Responses()

    def Subscribe_PumpDriveState(self, request, context):
        """The current state of the pump. This is either enabled or disabled. Only if the sate is enabled, the pump can dose fluids.
            :param request: gRPC request
            :param context: gRPC context
            :param response.PumpDriveState: The current state of the pump. This is either enabled or disabled. Only if the sate is enabled, the pump can dose fluids.

        """
        logging.debug("Subscribe_PumpDriveState - Mode: simulation ")

        #~ yield_val = request.PumpDriveState.value
        #~ pb2.Subscribe_PumpDriveState_Responses( PumpDriveState=fwpb2.Boolean(value=False) )

    def Subscribe_FaultState(self, request, context):
        """Returns if the pump is in fault state. If the value is true (i.e. the pump is in fault state), it can be cleared by calling EnablePumpDrive.
            :param request: gRPC request
            :param context: gRPC context
            :param response.FaultState: Returns if the pump is in fault state. If the value is true (i.e. the pump is in fault state), it can be cleared by calling EnablePumpDrive.

        """
        logging.debug("Subscribe_FaultState - Mode: simulation ")

        #~ yield_val = request.FaultState.value
        #~ pb2.Subscribe_FaultState_Responses( FaultState=fwpb2.Boolean(value=False) )




