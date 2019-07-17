"""
________________________________________________________________________

:PROJECT: SiLA2_python

*pumpunitcontroller_server_real *

:details: pumpunitcontroller_server_real: Allows to control the currently used units for passing and retrieving flow rates and volumes to and from a pump..

:file:    pumpunitcontroller_server_real.py
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

# import qmixsdk
from qmixsdk import qmixbus
from qmixsdk import qmixpump

class PumpUnitControllerReal():
    """ PumpUnitControllerReal - Allows to control the currently used units for passing and retrieving flow rates and volumes to and from a pump. """
    def __init__ (self, bus, pump):
        """ PumpUnitControllerReal class initialiser """
        logging.debug("init class: PumpUnitControllerReal ")

        self.bus = bus
        self.pump = pump



    def SetFlowUnit(self, request, context):
        """Sets the flow unit for the pump. The flow unit defines the unit to be used for all flow values passed to or retrieved from the pump.
            :param request: gRPC request
            :param context: gRPC context
            :param request.Prefix: The prefix for the velocity unit.
            :param request.VolumeUnit: The volume unit (numerator) of the velocity unit.
            :param request.TimeUnit: The time unit (denominator) of the velocity unit.

        """
        logging.debug("SetFlowUnit - Mode: real ")

        #~ return_val = request.Prefix.value
        #~ return pb2.SetFlowUnit_Responses()

    def SetVolumeUnit(self, request, context):
        """Sets the default volume unit. The volume unit defines the unit to be used for all volume values passed to or retrieved from the pump.
            :param request: gRPC request
            :param context: gRPC context
            :param request.Prefix: The prefix for the velocity unit.
            :param request.VolumeUnit: The volume unit identifier.

        """
        logging.debug("SetVolumeUnit - Mode: real ")

        #~ return_val = request.Prefix.value
        #~ return pb2.SetVolumeUnit_Responses()

    def Subscribe_FlowUnit(self, request, context):
        """The currently used flow unit.
            :param request: gRPC request
            :param context: gRPC context
            :param response.FlowUnit: The currently used flow unit.

        """
        logging.debug("Subscribe_FlowUnit - Mode: real ")

        #~ yield_val = request.FlowUnit.value
        #~ pb2.Subscribe_FlowUnit_Responses( FlowUnit=fwpb2.String(value="DEFAULTstring" + yield_val) )




