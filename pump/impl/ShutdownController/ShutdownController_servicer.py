"""
________________________________________________________________________

:PROJECT: SiLA2_python

*Shutdown Controller*

:details: ShutdownController:
    Provides a generic way of telling a SiLA2 server that it is about to be shut down. The server implements a routine
    to be executed before the hardware is shut down (e.g. saving device paramters or bringing the device into a safe
    position).

:file:    ShutdownController_servicer.py
:authors: Florian Meinicke

:date: (creation)          2019-07-17T09:54:01.896624
:date: (last modification) 2019-10-05T11:53:30.862736

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
from .gRPC import ShutdownController_pb2 as ShutdownController_pb2
from .gRPC import ShutdownController_pb2_grpc as ShutdownController_pb2_grpc

# import SiLA errors
from .. import neMESYS_errors

# import simulation and real implementation
from .ShutdownController_simulation import ShutdownControllerSimulation
from .ShutdownController_real import ShutdownControllerReal


class ShutdownController(ShutdownController_pb2_grpc.ShutdownControllerServicer):
    """
    This is a sample service for controlling neMESYS syringe pumps via SiLA2
    """
    implementation: Union[ShutdownControllerSimulation, ShutdownControllerReal]
    simulation_mode: bool

    def __init__(self, pump, server_name, sila2_conf, simulation_mode: bool = True):
        """
        Class initialiser.

        :param bus: A valid `qxmixbus` for this service to use
        :param server_name: The name of the SiLA server
        :param sila2_conf: The config of the server
        :param simulation_mode: Sets whether at initialisation the simulation mode is active or the real mode
        """

        self.pump = pump
        self.server_name = server_name
        self.sila2_conf = sila2_conf

        self.simulation_mode = simulation_mode
        if simulation_mode:
            self.switch_to_simulation_mode()
        else:
            self.switch_to_real_mode()

    def _inject_implementation(self,
                               implementation: Union[ShutdownControllerSimulation,
                                                     ShutdownControllerReal]
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
        self._inject_implementation(ShutdownControllerSimulation())

    def switch_to_real_mode(self):
        """Method that will automatically be called by the server when the real mode is requested."""
        self.simulation_mode = False
        self._inject_implementation(ShutdownControllerReal(
            pump=self.pump,
            server_name=self.server_name,
            sila2_conf=self.sila2_conf
        ))

    def Shutdown(self, request, context: grpc.ServicerContext) \
            -> silaFW_pb2.CommandConfirmation:
        """
        Executes the observable command "Shutdown"
            Initiates the shutdown routine. If no errors occured during the shutdown process the server should be considered ready to be physically shutdown (i.e. the device can be shut down/powered off).

        :param request: gRPC request containing the parameters passed:
            request.EmptyParameter (Empty Parameter): An empty parameter data type used if no parameter is required.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A command confirmation object with the following information:
            commandId: A command id with which this observable command can be referenced in future calls
            lifetimeOfExecution: The (maximum) lifetime of this command call.
        """

        logging.debug(
            "Shutdown called in {current_mode} mode".format(
                current_mode=('simulation' if self.simulation_mode else 'real')
            )
        )
        return self.implementation.Shutdown(request, context)

    def Shutdown_Info(self, request, context: grpc.ServicerContext) \
            -> silaFW_pb2.ExecutionInfo:
        """
        Returns execution information regarding the command call :meth:`~.Shutdown`.

        :param request: A request object with the following properties
            CommandExecutionUUID: The UUID of the command executed.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: An ExecutionInfo response stream for the command with the following fields:
            commandStatus: Status of the command (enumeration)
            progressInfo: Information on the progress of the command (0 to 1)
            estimatedRemainingTime: Estimate of the remaining time required to run the command
            updatedLifetimeOfExecution: An update on the execution lifetime
        """

        logging.debug(
            "Shutdown_Info called in {current_mode} mode".format(
                current_mode=('simulation' if self.simulation_mode else 'real')
            )
        )

        try:
            return self.implementation.Shutdown_Info(request, context)
        except (neMESYS_errors.SiLAFrameworkError, neMESYS_errors.DeviceError) as err:
            if isinstance(err, neMESYS_errors.DeviceError):
                err = neMESYS_errors.QmixSDKError(err)
            err.raise_rpc_error(context)
            return None

    def Shutdown_Result(self, request, context: grpc.ServicerContext) \
            -> ShutdownController_pb2.Shutdown_Responses:
        """
        Returns the final result of the command call :meth:`~.Shutdown`.

        :param request: A request object with the following properties
            CommandExecutionUUID: The UUID of the command executed.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: The return object defined for the command with the following fields:
            request.EmptyResponse (Empty Response): An empty response data type used if no response is required.
        """

        logging.debug(
            "Shutdown_Result called in {current_mode} mode".format(
                current_mode=('simulation' if self.simulation_mode else 'real')
            )
        )
        return self.implementation.Shutdown_Result(request, context)
