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


def evaluate_prefix(prefix_string):
    """Converts the given prefix_string to a qmixpump.UnitPrefix
    """
    switcher = {
        "deci": qmixpump.UnitPrefix.deci,
        "centi": qmixpump.UnitPrefix.centi,
        "milli": qmixpump.UnitPrefix.milli,
        "micro": qmixpump.UnitPrefix.micro
    } # default = no prefix
    return switcher.get(prefix_string, qmixpump.UnitPrefix.unit)

# TODO: Handle wrong inputs properly
def evaluate_volume_unit(volume_unit_string):
    """ Converts a given volume_unit_string to a qmixpump.VolumeUnit
    """
    # if volume_unit_string == "litres":
    return qmixpump.VolumeUnit.litres

    # return fwpb2.SiLAError(validationError=fwpb2.ValidationError(
    #     param="VolumeUnit",
    #     cause="The given volume unit is not supported!"
    # ))

def evaluate_time_unit(time_unit_string):
    """Converts a given time_unit_string into a qmixpump.TimeUnit
    """
    switcher = {
        "per_hour": qmixpump.TimeUnit.per_hour,
        "per_min": qmixpump.TimeUnit.per_minute
    } # default = "per_second"
    return switcher.get(time_unit_string, qmixpump.TimeUnit.per_second)


def prefix_to_string(prefix):
    """Converts a given prefix to a human readable string
        :param prefix: qmixpump.UnitPrefix
    """
    switcher = {
        qmixpump.UnitPrefix.deci: "deci",
        qmixpump.UnitPrefix.centi: "centi",
        qmixpump.UnitPrefix.milli: "milli",
        qmixpump.UnitPrefix.micro: "micro"
    } # default = no prefix
    return switcher.get(prefix, "unit")

def time_unit_to_string(time_unit):
    """Converts a given time_unit to a human readable string
        :param time_unit: qmixpump.TimeUnit
    """
    switcher = {
        qmixpump.TimeUnit.per_hour: "per_hour",
        qmixpump.TimeUnit.per_minute: "per_min"
    } # default = "per_second"
    return switcher.get(time_unit, "per_second")

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
            :param request.Prefix: The prefix for the velocity unit.
            :param request.VolumeUnit: The volume unit (numerator) of the velocity unit.
            :param request.TimeUnit: The time unit (denominator) of the velocity unit.
        """
        logging.debug("SetFlowUnit - Mode: real ")

        prefix = evaluate_prefix(request.Prefix.value)
        volume_unit = evaluate_volume_unit(request.VolumeUnit.value)
        time_unit = evaluate_time_unit(request.TimeUnit.value)

        self.pump.set_flow_unit(prefix, volume_unit, time_unit)

        return pb2.SetFlowUnit_Responses()

    def SetVolumeUnit(self, request, context):
        """Sets the default volume unit. The volume unit defines the unit to be used for all volume values passed to or retrieved from the pump.
            :param request: gRPC request
            :param context: gRPC context
            :param request.Prefix: The prefix for the velocity unit.
            :param request.VolumeUnit: The volume unit identifier.
        """
        logging.debug("SetVolumeUnit - Mode: real ")

        prefix = evaluate_prefix(request.Prefix.value)
        volume_unit = evaluate_volume_unit(request.VolumeUnit.value)

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
        prefix_string = prefix_to_string(prefix)
        volume_unit_string = "litres"
        time_unit_string = time_unit_to_string(time_unit)

        yield pb2.Subscribe_FlowUnit_Responses(FlowUnit=fwpb2.String(value=prefix_string + " " + volume_unit_string + " " + time_unit_string))

    def Subscribe_VolumeUnit(self, request, context):
        """The currently used volume unit.
            :param request: gRPC request
            :param context: gRPC context
            :param response.VolumeUnit: The currently used volume unit.
        """
        logging.debug("Subscribe_VolumeUnit - Mode: simulation ")

        prefix, volume_unit = self.pump.get_volume_unit()
        prefix_string = prefix_to_string(prefix)
        volume_unit_string = "litres"

        yield pb2.Subscribe_VolumeUnit_Responses(VolumeUnit=fwpb2.String(value=prefix_string + " " + volume_unit_string))
