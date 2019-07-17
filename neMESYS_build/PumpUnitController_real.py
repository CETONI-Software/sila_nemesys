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

import sila2lib.sila_error_handling as sila_error

# importing protobuf and gRPC handler/stubs
import sila2lib.SiLAFramework_pb2 as fwpb2
import PumpUnitController_pb2 as pb2
import PumpUnitController_pb2_grpc as pb2_grpc

# import qmixsdk
from qmixsdk import qmixbus
from qmixsdk import qmixpump

import unit_conversion as uc


class PumpUnitControllerReal():
    """ PumpUnitControllerReal - Allows to control the currently used units for passing and retrieving flow rates and volumes to and from a pump. """

    def __init__(self, bus, pump):
        """ PumpUnitControllerReal class initialiser """
        logging.debug("init class: PumpUnitControllerReal ")

        self.bus = bus
        self.pump = pump

    def SetFlowUnit(self, request, context):
        """Sets the flow unit for the pump. The flow unit defines the unit to be used for all flow values passed to or retrieved from the pump.
            :param request: gRPC request
            :param context: gRPC context
            :param request.FlowUnit: The flow unit to set. It has to something like "ml/s" or "µl/s", for instance.
        """
        logging.debug("SetFlowUnit - Mode: real ")

        try:
            requested_volume_unit, requested_time_unit = request.FlowUnit.value.split("/")
            prefix, volume_unit, time_unit = uc.evaluate_units(requested_volume_unit,
                                                               requested_time_unit)
        except ValueError as err:
            sila_error.raiseRPCError(context, sila_error.getValidationError(
                parameter="FlowUnit",
                cause="The given flow unit is malformed. It has to be something like 'ml/s' for instance."
            ))
        except uc.UnitConversionError as err:
            sila_error.raiseRPCError(context, sila_error.getValidationError(
                parameter=err.param, cause=err.message
            ))
        else:
            self.pump.set_flow_unit(prefix, volume_unit, time_unit)
            return pb2.SetFlowUnit_Responses()

    def SetVolumeUnit(self, request, context):
        """Sets the default volume unit. The volume unit defines the unit to be used for all volume values passed to or retrieved from the pump.
            :param request: gRPC request
            :param context: gRPC context
            :param request.VolumeUnit: The volume unit to set. It has to be something like "ml" or "µl", for instance.
        """
        logging.debug("SetVolumeUnit - Mode: real ")

        try:
            prefix, volume_unit = uc.evaluate_units(request.VolumeUnit.value)
        except uc.UnitConversionError as err:
            sila_error.raiseRPCError(context, sila_error.getValidationError(
                parameter=err.param, cause=err.message
            ))
        else:
            self.pump.set_volume_unit(prefix, volume_unit)
            return pb2.SetVolumeUnit_Responses()

    def Subscribe_FlowUnit(self, request, context):
        """The currently used flow unit.
            :param request: gRPC request
            :param context: gRPC context
            :param response.FlowUnit: The currently used flow unit.
        """
        logging.debug("Subscribe_FlowUnit - Mode: real ")

        prefix, volume_unit, time_unit = self.pump.get_flow_unit()
        prefix_string = uc.prefix_to_string(prefix)
        volume_unit_string = "l"
        time_unit_string = uc.time_unit_to_string(time_unit)

        yield pb2.Subscribe_FlowUnit_Responses(FlowUnit=fwpb2.String(
                value=prefix_string + volume_unit_string + "/" + time_unit_string
        ))

    def Subscribe_VolumeUnit(self, request, context):
        """The currently used volume unit.
            :param request: gRPC request
            :param context: gRPC context
            :param response.VolumeUnit: The currently used volume unit.
        """
        logging.debug("Subscribe_VolumeUnit - Mode: simulation ")

        prefix, volume_unit = self.pump.get_volume_unit()
        prefix_string = uc.prefix_to_string(prefix)
        volume_unit_string = "l"

        yield pb2.Subscribe_VolumeUnit_Responses(
            VolumeUnit=fwpb2.String(value=prefix_string + volume_unit_string
        ))
