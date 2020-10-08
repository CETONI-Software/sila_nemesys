"""
________________________________________________________________________

:PROJECT: SiLA2_python

*Valve Position Controller*

:details: ValvePositionController:
    Allows to specify a certain logical position for a valve. The Position property can be querried at any time to
    obtain the current valve position.

:file:    ValvePositionController_servicer.py
:authors: Florian Meinicke

:date: (creation)          2019-07-16T11:11:31.315160
:date: (last modification) 2019-10-05T11:53:30.855496

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
import grpc

# meta packages
from typing import Union

# import SiLA2 library
import sila2lib.framework.SiLAFramework_pb2 as silaFW_pb2

# import gRPC modules for this feature
from .gRPC import ValvePositionController_pb2 as ValvePositionController_pb2
from .gRPC import ValvePositionController_pb2_grpc as ValvePositionController_pb2_grpc

# import SiLA errors
from .. import neMESYS_errors

# import simulation and real implementation
from .ValvePositionController_simulation import ValvePositionControllerSimulation
from .ValvePositionController_real import ValvePositionControllerReal


class ValvePositionController(ValvePositionController_pb2_grpc.ValvePositionControllerServicer):
    """
    This is a sample service for controlling neMESYS syringe pumps via SiLA2
    """
    implementation: Union[ValvePositionControllerSimulation, ValvePositionControllerReal]
    simulation_mode: bool

    def __init__(self, pump, simulation_mode: bool = True):
        """
        Class initialiser.

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
                               implementation: Union[ValvePositionControllerSimulation,
                                                     ValvePositionControllerReal]
                               ) -> bool:
        """
        Dependency injection of the implementation used.
            Allows to set the class used for simulation/real mode.

        :param implementation: A valid implementation of the neMESYSServicer.
        """

        self.implementation = implementation
        return True

    def switch_to_simulation_mode(self):
        """Method that will automatically be called by the server when the simulation mode is requested."""
        self.simulation_mode = True
        self._inject_implementation(ValvePositionControllerSimulation())

    def switch_to_real_mode(self):
        """Method that will automatically be called by the server when the real mode is requested."""
        self.simulation_mode = False
        self._inject_implementation(ValvePositionControllerReal(self.pump))

    def SwitchToPosition(self, request, context: grpc.ServicerContext) \
            -> ValvePositionController_pb2.SwitchToPosition_Responses:
        """
        Executes the unobservable command "Switch To Position"
            Switches the valve to the specified position. The given position has to be less than the NumberOfPositions or else a ValidationError is thrown.

        :param request: gRPC request containing the parameters passed:
            request.Position (Position): The target position that the valve should be switched to.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: The return object defined for the command with the following fields:
            request.EmptyResponse (Empty Response): An empty response data type used if no response is required.
        """

        logging.debug(
            "SwitchToPosition called in {current_mode} mode".format(
                current_mode=('simulation' if self.simulation_mode else 'real')
            )
        )

        try:
            return self.implementation.SwitchToPosition(request, context)
        except (neMESYS_errors.ValvePositionOutOfRangeError, neMESYS_errors.DeviceError) as err:
            if isinstance(err, neMESYS_errors.DeviceError):
                err = neMESYS_errors.QmixSDKError(err)
            err.raise_rpc_error(context)
            return None


    def TogglePosition(self, request, context: grpc.ServicerContext) \
            -> ValvePositionController_pb2.TogglePosition_Responses:
        """
        Executes the unobservable command "Toogle Position"
            This command only applies for 2-way valves to toggle between its two different positions. If the command is called for any other valve type a ValveNotToggleable error is thrown.

        :param request: gRPC request containing the parameters passed:
            request.EmptyParameter (Empty Parameter): An empty parameter data type used if no parameter is required.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: The return object defined for the command with the following fields:
            request.EmptyResponse (Empty Response): An empty response data type used if no response is required.
        """

        logging.debug(
            "TogglePosition called in {current_mode} mode".format(
                current_mode=('simulation' if self.simulation_mode else 'real')
            )
        )

        try:
            return self.implementation.TogglePosition(request, context)
        except (neMESYS_errors.ValveNotToggleableError, neMESYS_errors.DeviceError) as err:
            if isinstance(err, neMESYS_errors.DeviceError):
                err = neMESYS_errors.QmixSDKError(err)
            err.raise_rpc_error(context)
            return None

    def Get_NumberOfPositions(self, request, context: grpc.ServicerContext) \
            -> ValvePositionController_pb2.Get_NumberOfPositions_Responses:
        """
        Requests the unobservable property Number Of Positions
            The number of the valve positions available.

        :param request: An empty gRPC request object (properties have no parameters)
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A response object with the following fields:
            request.NumberOfPositions (Number Of Positions): The number of the valve positions available.
        """

        logging.debug(
            "Property NumberOfPositions requested in {current_mode} mode".format(
                current_mode=('simulation' if self.simulation_mode else 'real')
            )
        )
        return self.implementation.Get_NumberOfPositions(request, context)

    def Subscribe_Position(self, request, context: grpc.ServicerContext) \
            -> ValvePositionController_pb2.Subscribe_Position_Responses:
        """
        Requests the observable property Position
            The current logical valve position. This is a value between 0 and NumberOfPositions - 1.

        :param request: An empty gRPC request object (properties have no parameters)
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A response stream with the following fields:
            request.Position (Position): The current logical valve position. This is a value between 0 and NumberOfPositions - 1.
        """

        logging.debug(
            "Property Position requested in {current_mode} mode".format(
                current_mode=('simulation' if self.simulation_mode else 'real')
            )
        )
        try:
            return self.implementation.Subscribe_Position(request, context)
        except neMESYS_errors.DeviceError as err:
            err = neMESYS_errors.QmixSDKError(err)
            err.raise_rpc_error(context)
            return None