"""
________________________________________________________________________

:PROJECT: SiLA2_python

*pumpunitcontroller_server_simulation *

:details: pumpunitcontroller_server_simulation: Allows to control the currently used units for passing and retrieving flow rates and volumes to and from a pump.. 
           
:file:    pumpunitcontroller_server_simulation.py
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
import PumpUnitController_pb2 as pb2
import PumpUnitController_pb2_grpc as pb2_grpc


class PumpUnitController(pb2_grpc.PumpUnitControllerServicer):
    """ PumpUnitController - Allows to control the currently used units for passing and retrieving flow rates and volumes to and from a pump. """
    def __init__ (self):
        """ PumpUnitController class initialiser """
        logging.debug("init class: PumpUnitController ")

        # if self.implementation is set to None, it will use
        # the fallback simulation mode as default
        # if required, one could also create a simulation module and set this to the default implementation, like:
        #~ self.injectImplementation(GreetingProviderSimulation())

        self.implementation = None # this corresponds to the simple, fallback simulation mode

    # dependency injection - setter injection s. https://en.wikipedia.org/wiki/Dependency_injection
    def injectImplementation(self, implementation):
        self.implementation = implementation

    def SetFlowUnit(self, request, context):
        """Sets the flow unit for the pump. The flow unit defines the unit to be used for all flow values passed to or retrieved from the pump.
            :param request: gRPC request
            :param context: gRPC context
            :param request.FlowUnit: The flow unit to set. It has to something like "ml/s" or "µl/s", for instance.

        """
        logging.debug("SetFlowUnit - Mode: simulation ")

        if self.implementation is not None:
            return self.implementation.SetFlowUnit(request, context)
        else:
            pass #~ return_val = request.FlowUnit.value
            #~ return pb2.SetFlowUnit_Responses(  )

    def SetVolumeUnit(self, request, context):
        """Sets the default volume unit. The volume unit defines the unit to be used for all volume values passed to or retrieved from the pump.
            :param request: gRPC request
            :param context: gRPC context
            :param request.VolumeUnit: The volume unit to set. It has to be something like "ml" or "µl", for instance.

        """
        logging.debug("SetVolumeUnit - Mode: simulation ")

        if self.implementation is not None:
            return self.implementation.SetVolumeUnit(request, context)
        else:
            pass #~ return_val = request.VolumeUnit.value
            #~ return pb2.SetVolumeUnit_Responses(  )

    def Subscribe_FlowUnit(self, request, context):
        """The currently used flow unit.
            :param request: gRPC request
            :param context: gRPC context
            :param response.FlowUnit: The currently used flow unit.

        """
        logging.debug("Subscribe_FlowUnit - Mode: simulation ")

        if self.implementation is not None:
            self.implementation.Subscribe_FlowUnit(request, context)
        else:
            #~ yield_val = request.FlowUnit.value
            pass #~ yield pb2.Subscribe_FlowUnit_Responses( FlowUnit=fwpb2.String(value="DEFAULTstring" + yield_val) )

    def Subscribe_VolumeUnit(self, request, context):
        """The currently used volume unit.
            :param request: gRPC request
            :param context: gRPC context
            :param response.VolumeUnit: The currently used volume unit.

        """
        logging.debug("Subscribe_VolumeUnit - Mode: simulation ")

        if self.implementation is not None:
            self.implementation.Subscribe_VolumeUnit(request, context)
        else:
            #~ yield_val = request.VolumeUnit.value
            pass #~ yield pb2.Subscribe_VolumeUnit_Responses( VolumeUnit=fwpb2.String(value="DEFAULTstring" + yield_val) )




