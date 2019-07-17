"""
________________________________________________________________________

:PROJECT: SiLA2_python

*Pump Unit Controller*

:details: PumpUnitController:
    Allows to control the currently used units for passing and retrieving flow rates and volumes to and from a pump.

:file:    PumpUnitController_servicer.py
:authors: Florian Meinicke

:date: (creation)          2019-07-16T11:11:31.287651
:date: (last modification) 2019-07-16T11:11:31.287651

.. note:: Code generated by SiLA2CodeGenerator 0.2.0

________________________________________________________________________

**Copyright**:
  This file is provided "AS IS" with NO WARRANTY OF ANY KIND,
  INCLUDING THE WARRANTIES OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.

  For further Information see LICENSE file that comes with this distribution.
________________________________________________________________________
"""

__version__ = "0.0.1"

# import general packages
import logging

# meta packages
from typing import Union

# import SiLA2 library
import sila2lib.SiLAFramework_pb2 as fwpb2

# import gRPC modules for this feature
from .gRPC import PumpUnitController_pb2 as pb2
from .gRPC import PumpUnitController_pb2_grpc as pb2_grpc

# import simulation and real implementation
from .PumpUnitController_simulation import PumpUnitControllerSimulation
from .PumpUnitController_real import PumpUnitControllerReal


class PumpUnitController(pb2_grpc.PumpUnitControllerServicer):
    """
    This is a test service for neMESYS syringe pumps via SiLA2
    """
    implementation: Union[PumpUnitControllerSimulation, PumpUnitControllerReal]
    simulation_mode: bool

    def __init__(self, pump, simulation_mode: bool = True):
        """
        Class initialiser

        :param pump: A valid `qxmixpump` for this service to use
        :param simulation_mode: Sets whether at initialisation the simulation mode is active or the real mode
        """

        self.pump = pump

        self.simulation_mode = simulation_mode
        if simulation_mode:
            self.switch_to_simulation_mode()
        else:
            self.switch_to_real_mode()

    def _inject_implementation(self,
                               implementation: Union[PumpUnitControllerSimulation,
                                                     PumpUnitControllerReal]
                               ) -> bool:
        """
        Dependency injection of the implementation used.
            Allows to set the class used for simulation/real mode

        :param implementation: A valid implementation of the neMESYSServicer
        """

        self.implementation = implementation
        return True

    def switch_to_simulation_mode(self):
        self.simulation_mode = True
        self._inject_implementation(PumpUnitControllerSimulation())

    def switch_to_real_mode(self):
        self.simulation_mode = False
        self._inject_implementation(PumpUnitControllerReal(self.pump))

    def SetFlowUnit(self, request, context) -> pb2.SetFlowUnit_Responses:
        """
        Executes the unobservable command Set Flow Unit
            Sets the flow unit for the pump. The flow unit defines the unit to be used for all flow values passed to or retrieved from the pump.

        :param request: gRPC request containing the parameters passed:
            request.FlowUnit (FlowUnit): The flow unit to set. It has to something like "ml/s" or "µl/s", for instance.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: The return object defined for the command with the following fields:
            request.EmptyResponse (Empty Response): An empty response data type used if no response is required.
        """

        logging.debug(
            "SetFlowUnit called in {current_mode} mode".format(
                current_mode=('simulation' if self.simulation_mode else 'real')
            )
        )
        return self.implementation.SetFlowUnit(request, context)

    def SetVolumeUnit(self, request, context) -> pb2.SetVolumeUnit_Responses:
        """
        Executes the unobservable command Set Volume Unit
            Sets the default volume unit. The volume unit defines the unit to be used for all volume values passed to or retrieved from the pump.

        :param request: gRPC request containing the parameters passed:
            request.VolumeUnit (Volume Unit): The volume unit to set. It has to be something like "ml" or "µl", for instance.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: The return object defined for the command with the following fields:
            request.EmptyResponse (Empty Response): An empty response data type used if no response is required.
        """

        logging.debug(
            "SetVolumeUnit called in {current_mode} mode".format(
                current_mode=('simulation' if self.simulation_mode else 'real')
            )
        )
        return self.implementation.SetVolumeUnit(request, context)

    def Subscribe_FlowUnit(self, request, context) -> pb2.Subscribe_FlowUnit_Responses:
        """
        Requests the observable property Flow Unit
            The currently used flow unit.

        :param request: An empty gRPC request object (properties have no parameters)
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A response stream with the following fields:
            request.FlowUnit (Flow Unit): The currently used flow unit.
        """

        logging.debug(
            "Property FlowUnit requested in {current_mode} mode".format(
                current_mode=('simulation' if self.simulation_mode else 'real')
            )
        )
        return self.implementation.Subscribe_FlowUnit(request, context)


    def Subscribe_VolumeUnit(self, request, context) -> pb2.Subscribe_VolumeUnit_Responses:
        """
        Requests the observable property Volume Unit
            The currently used volume unit.

        :param request: An empty gRPC request object (properties have no parameters)
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A response stream with the following fields:
            request.VolumeUnit (Volume Unit): The currently used volume unit.
        """

        logging.debug(
            "Property VolumeUnit requested in {current_mode} mode".format(
                current_mode=('simulation' if self.simulation_mode else 'real')
            )
        )
        return self.implementation.Subscribe_VolumeUnit(request, context)

