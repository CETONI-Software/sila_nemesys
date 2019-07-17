"""
________________________________________________________________________

:PROJECT: SiLA2_python

*pumpdrivecontrolservice_server_simulation *

:details: pumpdrivecontrolservice_server_simulation:
        Functionality to control and maintain the drive that drives the pump.
        Allows to initialise a pump (e.g. by executing a reference move).
        The initialisation has to be successful in order for the pump to work correctly and dose fluids. If the initialisation fails, the StandardExecutionError InitialisationFailed is thrown.
        Obtain status information about the pump drive's current state (e.g. enabled/disabled or fault state).
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


class PumpDriveControlService(pb2_grpc.PumpDriveControlServiceServicer):
    """ PumpDriveControlService -
#        Functionality to control and maintain the drive that drives the pump.
#        Allows to initialise a pump (e.g. by executing a reference move).
#        The initialisation has to be successful in order for the pump to work correctly and dose fluids. If the initialisation fails, the StandardExecutionError InitialisationFailed is thrown.
#        Obtain status information about the pump drive's current state (e.g. enabled/disabled or fault state).
#     """
    def __init__ (self):
        """ PumpDriveControlService class initialiser """
        logging.debug("init class: PumpDriveControlService ")

        # if self.implementation is set to None, it will use
        # the fallback simulation mode as default
        # if required, one could also create a simulation module and set this to the default implementation, like:
        #~ self.injectImplementation(GreetingProviderSimulation())

        self.implementation = None # this corresponds to the simple, fallback simulation mode

    # dependency injection - setter injection s. https://en.wikipedia.org/wiki/Dependency_injection
    def injectImplementation(self, implementation):
        self.implementation = implementation

    def InitializePumpDrive(self, request, context):
        """Initialize the pump drive (e.g. by executing a reference move).
        empty parameter
        """
        logging.debug("InitializePumpDrive - Mode: simulation ")

        if self.implementation is not None:
            return self.implementation.InitializePumpDrive(request, context)
        else:
            pass #~ return_val = request.Void.value
            #~ return pb2.InitializePumpDrive_Responses( Success=fwpb2.Boolean(value=False) )

    def EnablePumpDrive(self, request, context):
        """Set the pump into enabled state.
            :param request: gRPC request
            :param context: gRPC context
        """
        logging.debug("EnablePumpDrive - Mode: simulation ")

        if self.implementation is not None:
            return self.implementation.EnablePumpDrive(request, context)
        else:
            pass #~ return_val = request.Void.value
            #~ return pb2.EnablePumpDrive_Responses()

    def DisablePumpDrive(self, request, context):
        """Set the pump into disabled state.
            :param request: gRPC request
            :param context: gRPC context
        """
        logging.debug("DisablePumpDrive - Mode: simulation ")

        if self.implementation is not None:
            return self.implementation.DisablePumpDrive(request, context)
        else:
            pass #~ return_val = request.Void.value
            #~ return pb2.DisablePumpDrive_Responses()

    def Subscribe_PumpDriveState(self, request, context):
        """The current state of the pump. This is either enabled or disabled. Only if the sate is enabled, the pump can dose fluids.
            :param request: gRPC request
            :param context: gRPC context
            :param response.PumpDriveState: The current state of the pump. This is either enabled or disabled. Only if the sate is enabled, the pump can dose fluids.

        """
        logging.debug("Subscribe_PumpDriveState - Mode: simulation ")

        if self.implementation is not None:
            return self.implementation.Subscribe_PumpDriveState(request, context)
        else:
            #~ yield_val = request.PumpDriveState.value
            pass #~ yield pb2.Subscribe_PumpDriveState_Responses( PumpDriveState=fwpb2.Boolean(value=False) )

    def Subscribe_FaultState(self, request, context):
        """Returns if the pump is in fault state. If the value is true (i.e. the pump is in fault state), it can be cleared by calling ClearFaultState.
            :param request: gRPC request
            :param context: gRPC context
            :param response.FaultState: Returns if the pump is in fault state. If the value is true (i.e. the pump is in fault state), it can be cleared by calling ClearFaultState.
        """
        logging.debug("Subscribe_FaultState - Mode: simulation ")

        if self.implementation is not None:
            return self.implementation.Subscribe_FaultState(request, context)
        else:
            #~ yield_val = request.FaultState.value
            pass #~ yield pb2.Subscribe_FaultState_Responses( FaultState=fwpb2.Boolean(value=False) )
