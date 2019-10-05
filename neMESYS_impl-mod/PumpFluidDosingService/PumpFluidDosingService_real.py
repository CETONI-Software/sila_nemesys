"""
________________________________________________________________________

:PROJECT: SiLA2_python

*Pump Fluid Dosing Service*

:details: PumpFluidDosingService:
    Allows to dose a specified fluid. There are commands for absolute dosing (SetFillLevel) and relative dosing
    (DoseVolume and GenerateFlow) available.The flow rate can be negative. In this case the pump aspirates the fluid
    instead of dispensing. The flow rate has to be a value between MaxFlowRate and MinFlowRate. If the value is not
    within this range (hence is invalid) a ValidationError will be thrown.
    At any time the property CurrentSyringeFillLevel can be queried to see how much fluid is left in the syringe.
    Similarly the property CurrentFlowRate can be queried to get the current flow rate at which the pump is dosing.

:file:    PumpFluidDosingService_real.py
:authors: Florian Meinicke

:date: (creation)          2019-07-16T11:11:31.305142
:date: (last modification) 2019-10-05T11:53:30.844094

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
import time         # used for observables
import uuid         # used for observables
import grpc         # used for type hinting only

# import qmixsdk
from qmixsdk import qmixbus
from qmixsdk import qmixpump

# import SiLA2 library
import sila2lib.framework.SiLAFramework_pb2 as silaFW_pb2

# import gRPC modules for this feature
from .gRPC import PumpFluidDosingService_pb2 as PumpFluidDosingService_pb2
# from .gRPC import PumpFluidDosingService_pb2_grpc as PumpFluidDosingService_pb2_grpc

# import default arguments
from .PumpFluidDosingService_default_arguments import default_dict
# import SiLA errors
import neMESYS_errors

import PumpUnitController.unit_conversion as uc

# noinspection PyPep8Naming,PyUnusedLocal
class PumpFluidDosingServiceReal:
    """
    Implementation of the *Pump Fluid Dosing Service* in *Real* mode
        This is a sample service for controlling neMESYS syringe pumps via SiLA2
    """

    def __init__(self, pump: qmixpump.Pump):
        """Class initialiser"""

        logging.debug('Started server in mode: {mode}'.format(mode='Real'))

        self.pump = pump

        self.dosage_uuid = ""

    def _check_pre_dosage(self, context, flow_rate, fill_level=None, volume=None):
        """
        Checks if the given flow rate and fill level or volume are in the correct ranges for this pump
            :param context: gRPC context - used for issueing errors
            :param flow_rate: The flow rate to check, if it's in the bounds for this pump
            :param fill_level: The fill level to check, if it's in the bounds for this pump
            :param volume: The volume to check, if it's in the bounds for this pump
        """

        max_fill_level = self.pump.get_volume_max()
        max_flow_rate = self.pump.get_flow_rate_max()

        # We only allow one dosage at a time.
        # -> Stop the currently running dosage and after that start the new one.
        if self.dosage_uuid:
            self.StopDosage(0, 0)
            # wait for the currently running dosage to catch up
            time.sleep(0.1)

        msg = """
        The requested {param} ({requested_val} {unit}) is not in the range
        bewteen 0 {unit} and {max_val} {unit} for this pump.
        """
        if flow_rate < 0 or flow_rate > max_flow_rate:
            unit = uc.flow_unit_to_string(self.pump.get_flow_unit())
            raise neMESYS_errors.FlowRateOutOfRangeError(
                msg.format(param="flow rate", unit=unit, requested_val=flow_rate, max_val=max_flow_rate)
            )
        if fill_level is not None and (fill_level < 0 or fill_level > max_fill_level):
            unit = uc.volume_unit_to_string(self.pump.get_volume_unit())
            raise neMESYS_errors.FillLevelOutOfRangeError(
                msg.format(param="fill level", unit=unit, requested_val=fill_level, max_val=max_fill_level)
            )
        if volume is not None and (volume < 0 or volume > max_fill_level):
            unit = uc.volume_unit_to_string(self.pump.get_volume_unit())
            raise neMESYS_errors.VolumeOutOfRangeError(
                msg.format(param="volume", unit=unit, requested_val=volume, max_val=max_fill_level)
            )


    def _wait_dosage_finished(self):
        """
        The function waits until the last dosage command has finished or
        until a timeout occurs. The timeout is estimated from the dosage's flow
        and target volume
        """

        flow_in_sec = self.pump.get_flow_is() / self.pump.get_flow_unit().time_unitid.value
        max_wait_time = self.pump.get_target_volume() / flow_in_sec + 2 # +2 sec buffer
        logging.debug("target volume: %f", self.pump.get_target_volume())
        logging.debug("flow_in_sec: %f", flow_in_sec)
        logging.debug("max_wait_time: %fs", max_wait_time)

        timer = qmixbus.PollingTimer(max_wait_time * 1000) # msec
        message_timer = qmixbus.PollingTimer(500) # msec
        is_pumping = True
        while is_pumping and not timer.is_expired():
            time.sleep(0.1)
            if message_timer.is_expired():
                logging.info("Fill level: %s", self.pump.get_fill_level())
                yield silaFW_pb2.ExecutionInfo(
                    commandStatus=silaFW_pb2.ExecutionInfo.CommandStatus.running
                )
                message_timer.restart()
            is_pumping = self.pump.is_pumping()

        if not is_pumping and not self.pump.is_in_fault_state():
            yield silaFW_pb2.ExecutionInfo(
                commandStatus=silaFW_pb2.ExecutionInfo.CommandStatus.finishedSuccessfully
            )
        else:
            yield silaFW_pb2.ExecutionInfo(
                commandStatus=silaFW_pb2.ExecutionInfo.CommandStatus.finishedWithError
            )
            logging.error("An unexpected error occured: %s", self.pump.read_last_error())

    def SetFillLevel(self, request, context: grpc.ServicerContext) \
            -> silaFW_pb2.CommandConfirmation:
        """
        Executes the observable command "Set Fill Level"
            Pumps fluid with the given flow rate until the requested fill level is reached.
            Depending on the requested fill level given in the FillLevel parameter this function may cause aspiration or dispension of fluid.

        :param request: gRPC request containing the parameters passed:
            request.FillLevel (Fill Level):
            The requested fill level. A level of 0 indicates a completely empty syringe. The value has to be between 0 and MaxSyringeFillLevel or else a ValidationError will be thrown.
            request.FlowRate (Flow Rate):
            The flow rate at which the pump should dose the fluid. This value can be negative. In that case the pump aspirates the fluid.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A command confirmation object with the following information:
            commandId: A command id with which this observable command can be referenced in future calls
            lifetimeOfExecution: The (maximum) lifetime of this command call.
        """

        requested_fill_level = request.FillLevel.value
        requested_flow_rate = request.FlowRate.value

        self._check_pre_dosage(context, requested_flow_rate, fill_level=requested_fill_level)

        self.dosage_uuid = str(uuid.uuid4())
        command_uuid = silaFW_pb2.CommandExecutionUUID(commandId=self.dosage_uuid)

        self.pump.set_fill_level(requested_fill_level, requested_flow_rate)
        logging.info("Started dosing with flow rate of %5.2f until fill level of %5.2f is reached (UUID: %s)",
                     requested_flow_rate, requested_fill_level, self.dosage_uuid)

        # respond with UUID and lifetime of execution
        return silaFW_pb2.CommandConfirmation(commandId=command_uuid)

    def SetFillLevel_Info(self, request, context: grpc.ServicerContext) \
            -> silaFW_pb2.ExecutionInfo:
        """
        Returns execution information regarding the command call :meth:`~.SetFillLevel`.

        :param request: A request object with the following properties
            commandId: The UUID of the command executed.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: An ExecutionInfo response stream for the command with the following fields:
            commandStatus: Status of the command (enumeration)
            progressInfo: Information on the progress of the command (0 to 1)
            estimatedRemainingTime: Estimate of the remaining time required to run the command
            updatedLifetimeOfExecution: An update on the execution lifetime
        """
        # Get the UUID of the command
        command_uuid = request.commandId

        logging.info("Requested SetFillLevel_Info for dosage (UUID: %s)", command_uuid)
        logging.info("Current dosage is UUID: %s", self.dosage_uuid)

        # catch invalid CommandExecutionUUID:
        if not command_uuid or self.dosage_uuid != command_uuid:
            raise neMESYS_errors.SiLAFrameworkError(
                neMESYS_errors.SiLAFrameworkErrorType.INVALID_COMMAND_EXECUTION_UUID
            )

        return self._wait_dosage_finished()

    def SetFillLevel_Result(self, request, context: grpc.ServicerContext) \
            -> PumpFluidDosingService_pb2.SetFillLevel_Responses:
        """
        Returns the final result of the command call :meth:`~.SetFillLevel`.

        :param request: A request object with the following properties
            CommandExecutionUUID: The UUID of the command executed.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: The return object defined for the command with the following fields:
            request.EmptyResponse (Empty Response): An empty response data type used if no response is required.
        """

        # Get the UUID of the command
        command_uuid = request.commandId

        # catch invalid CommandExecutionUUID:
        if not command_uuid and self.dosage_uuid != command_uuid:
            raise neMESYS_errors.SiLAFrameworkError(
                neMESYS_errors.SiLAFrameworkErrorType.INVALID_COMMAND_EXECUTION_UUID
            )

        # catch premature command call
        if self.pump.is_pumping():
            raise neMESYS_errors.SiLAFrameworkError(
                neMESYS_errors.SiLAFrameworkErrorType.COMMAND_EXECUTION_NOT_FINISHED
            )

        logging.info("Finished dosing! (UUID: %s)", self.dosage_uuid)
        self.dosage_uuid = ""
        time.sleep(0.6)

        return PumpFluidDosingService_pb2.SetFillLevel_Responses()


    def DoseVolume(self, request, context: grpc.ServicerContext) \
            -> silaFW_pb2.CommandConfirmation:
        """
        Executes the observable command "Dose Volume"
            Dose a certain amount of volume with the given flow rate.

        :param request: gRPC request containing the parameters passed:
            request.Volume (Volume):
            The amount of volume to dose. This value can be negative. In that case the pump aspirates the fluid.
            request.FlowRate (Flow Rate): The flow rate at which the pump should dose the fluid.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A command confirmation object with the following information:
            commandId: A command id with which this observable command can be referenced in future calls
            lifetimeOfExecution: The (maximum) lifetime of this command call.
        """

        requested_volume = request.Volume.value
        requested_flow_rate = request.FlowRate.value

        # requested_volume is neagtive to indicate aspiration of fluid.
        # Since the pre dosage checks test against 0 and the max flow rate of
        # the pump, we pass the absolute value of the requested_flow_rate.
        self._check_pre_dosage(context, requested_flow_rate, volume=abs(requested_volume))

        # Give clearer error messages:
        # QmixSDK would just start and immediately stop dosing in case of dispense
        # from empty syringe or aspirate to full syringe.
        pump_fill_level = self.pump.get_fill_level()
        if requested_volume > pump_fill_level:
            raise neMESYS_errors.VolumeOutOfRangeError(
                msg="There is too less fluid in the syringe! Aspirate some fluid before dispensing!"
            )
        # negative to indicate that there is still space for mor fluid
        free_volume = pump_fill_level - self.pump.get_volume_max()
        if requested_volume < free_volume:
            raise neMESYS_errors.VolumeOutOfRangeError(
                msg="There is too much fluid in the syringe! Dispense some fluid before aspirating!"
            )

        self.dosage_uuid = str(uuid.uuid4())
        command_uuid = silaFW_pb2.CommandExecutionUUID(commandId=self.dosage_uuid)

        self.pump.pump_volume(requested_volume, requested_flow_rate)
        logging.info("Started dosing a volume of %s with a flow rate of %5.2f (UUID: %s)",
                     requested_volume, requested_flow_rate, self.dosage_uuid)
        return silaFW_pb2.CommandConfirmation(commandId=command_uuid)

    def DoseVolume_Info(self, request, context: grpc.ServicerContext) \
            -> silaFW_pb2.ExecutionInfo:
        """
        Returns execution information regarding the command call :meth:`~.DoseVolume`.

        :param request: A request object with the following properties
            commandId: The UUID of the command executed.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: An ExecutionInfo response stream for the command with the following fields:
            commandStatus: Status of the command (enumeration)
            progressInfo: Information on the progress of the command (0 to 1)
            estimatedRemainingTime: Estimate of the remaining time required to run the command
            updatedLifetimeOfExecution: An update on the execution lifetime
        """
        # Get the UUID of the command
        command_uuid = request.commandId

        logging.info("Requested DoseVolume_Info for dosage (UUID: %s)", command_uuid)
        logging.info("Current dosage is UUID: %s", self.dosage_uuid)

        # catch invalid CommandExecutionUUID:
        if not command_uuid or self.dosage_uuid != command_uuid:
            raise neMESYS_errors.SiLAFrameworkError(
                neMESYS_errors.SiLAFrameworkErrorType.INVALID_COMMAND_EXECUTION_UUID
            )

        return self._wait_dosage_finished()

    def DoseVolume_Result(self, request, context: grpc.ServicerContext) \
            -> PumpFluidDosingService_pb2.DoseVolume_Responses:
        """
        Returns the final result of the command call :meth:`~.DoseVolume`.

        :param request: A request object with the following properties
            CommandExecutionUUID: The UUID of the command executed.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: The return object defined for the command with the following fields:
            request.EmptyResponse (Empty Response): An empty response data type used if no response is required.
        """

        # Get the UUID of the command
        command_uuid = request.commandId

        # catch invalid CommandExecutionUUID:
        if not command_uuid and self.dosage_uuid != command_uuid:
            raise neMESYS_errors.SiLAFrameworkError(
                neMESYS_errors.SiLAFrameworkErrorType.INVALID_COMMAND_EXECUTION_UUID
            )

        # catch premature command call
        if self.pump.is_pumping():
            raise neMESYS_errors.SiLAFrameworkError(
                neMESYS_errors.SiLAFrameworkErrorType.COMMAND_EXECUTION_NOT_FINISHED
            )

        logging.info("Finished dosing! (UUID: %s)", self.dosage_uuid)
        self.dosage_uuid = ""
        return PumpFluidDosingService_pb2.DoseVolume_Responses()


    def GenerateFlow(self, request, context: grpc.ServicerContext) \
            -> silaFW_pb2.CommandConfirmation:
        """
        Executes the observable command "Generate Flow"
            Generate a continous flow with the given flow rate. Dosing continues until it gets stopped manually by calling StopDosage or until the pusher reached one of its limits.

        :param request: gRPC request containing the parameters passed:
            request.FlowRate (Flow Rate):
            The flow rate at which the pump should dose the fluid. This value can be negative. In that case the pump aspirates the fluid.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A command confirmation object with the following information:
            commandId: A command id with which this observable command can be referenced in future calls
            lifetimeOfExecution: The (maximum) lifetime of this command call.
        """

        requested_flow_rate = request.FlowRate.value

        # requested_flow_rate is neagtive to indicate aspiration of fluid.
        # Since the pre dosage checks test against 0 and the max flow rate of
        # the pump, we pass the absolute value of the requested_flow_rate.
        self._check_pre_dosage(context, abs(requested_flow_rate))

        # Give clearer error messages:
        # QmixSDK would just start and immediately stop dosing in case of dispense
        # from empty syringe or aspirate to full syringe.
        if requested_flow_rate > 0 and self.pump.get_fill_level() == 0:
            raise neMESYS_errors.FlowRateOutOfRangeError(
                msg="Cannot dispense from an empty syringe! Aspirate some fluid before dispensing!"
            )
        if requested_flow_rate < 0 and self.pump.get_fill_level() == self.pump.get_volume_max():
            raise neMESYS_errors.FlowRateOutOfRangeError(
                msg="Cannot aspirate to a full syringe! Dispense some fluid before aspirating!"
            )

        self.dosage_uuid = str(uuid.uuid4())
        command_uuid = silaFW_pb2.CommandExecutionUUID(commandId=self.dosage_uuid)

        self.pump.generate_flow(requested_flow_rate)
        logging.info("Started dosing with a flow rate of %5.2f (UUID: %s)",
                     requested_flow_rate, self.dosage_uuid)
        return silaFW_pb2.CommandConfirmation(commandId=command_uuid)

    def GenerateFlow_Info(self, request, context: grpc.ServicerContext) \
            -> silaFW_pb2.ExecutionInfo:
        """
        Returns execution information regarding the command call :meth:`~.GenerateFlow`.

        :param request: A request object with the following properties
            commandId: The UUID of the command executed.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: An ExecutionInfo response stream for the command with the following fields:
            commandStatus: Status of the command (enumeration)
            progressInfo: Information on the progress of the command (0 to 1)
            estimatedRemainingTime: Estimate of the remaining time required to run the command
            updatedLifetimeOfExecution: An update on the execution lifetime
        """
        # Get the UUID of the command
        command_uuid = request.commandId

        # catch invalid CommandExecutionUUID:
        if not command_uuid or self.dosage_uuid != command_uuid:
            raise neMESYS_errors.SiLAFrameworkError(
                neMESYS_errors.SiLAFrameworkErrorType.INVALID_COMMAND_EXECUTION_UUID
            )

        return self._wait_dosage_finished()

    def GenerateFlow_Result(self, request, context: grpc.ServicerContext) \
            -> PumpFluidDosingService_pb2.GenerateFlow_Responses:
        """
        Returns the final result of the command call :meth:`~.GenerateFlow`.

        :param request: A request object with the following properties
            CommandExecutionUUID: The UUID of the command executed.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: The return object defined for the command with the following fields:
            request.EmptyResponse (Empty Response): An empty response data type used if no response is required.
        """

        # Get the UUID of the command
        command_uuid = request.commandId

        # catch invalid CommandExecutionUUID:
        if not command_uuid and self.dosage_uuid != command_uuid:
            raise neMESYS_errors.SiLAFrameworkError(
                neMESYS_errors.SiLAFrameworkErrorType.INVALID_COMMAND_EXECUTION_UUID
            )

        # catch premature command call
        if self.pump.is_pumping():
            raise neMESYS_errors.SiLAFrameworkError(
                neMESYS_errors.SiLAFrameworkErrorType.COMMAND_EXECUTION_NOT_FINISHED
            )

        logging.info("Finished dosing! (UUID: %s)", self.dosage_uuid)
        self.dosage_uuid = ""
        return PumpFluidDosingService_pb2.GenerateFlow_Responses()


    def StopDosage(self, request, context: grpc.ServicerContext) \
            -> PumpFluidDosingService_pb2.StopDosage_Responses:
        """
        Executes the unobservable command "Stop Dosage"
            Stops a currently running dosage immediately.

        :param request: gRPC request containing the parameters passed:
            request.EmptyParameter (Empty Parameter): An empty parameter data type used if no parameter is required.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: The return object defined for the command with the following fields:
            request.EmptyResponse (Empty Response): An empty response data type used if no response is required.
        """

        self.pump.stop_pumping()
        return PumpFluidDosingService_pb2.StopDosage_Responses()

    def Subscribe_MaxSyringeFillLevel(self, request, context: grpc.ServicerContext) \
            -> PumpFluidDosingService_pb2.Subscribe_MaxSyringeFillLevel_Responses:
        """
        Requests the observable property Maximum Syringe Fill Level
            The maximum amount of fluid that the syringe can hold.

        :param request: An empty gRPC request object (properties have no parameters)
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A response object with the following fields:
            request.MaxSyringeFillLevel (Maximum Syringe Fill Level): The maximum amount of fluid that the syringe can hold.
        """
        while True:
            yield PumpFluidDosingService_pb2.Subscribe_MaxSyringeFillLevel_Responses(
                MaxSyringeFillLevel=silaFW_pb2.Real(value=self.pump.get_volume_max())
            )

            # we add a small delay to give the client a chance to keep up.
            time.sleep(0.5)


    def Subscribe_SyringeFillLevel(self, request, context: grpc.ServicerContext) \
            -> PumpFluidDosingService_pb2.Subscribe_SyringeFillLevel_Responses:
        """
        Requests the observable property Syringe Fill Level
            The current amount of fluid left in the syringe.

        :param request: An empty gRPC request object (properties have no parameters)
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A response object with the following fields:
            request.SyringeFillLevel (Syringe Fill Level): The current amount of fluid left in the syringe.
        """

        while True:
            yield PumpFluidDosingService_pb2.Subscribe_SyringeFillLevel_Responses(
                SyringeFillLevel=silaFW_pb2.Real(value=self.pump.get_fill_level())
            )

            # we add a small delay to give the client a chance to keep up.
            time.sleep(0.5)


    def Subscribe_MaxFlowRate(self, request, context: grpc.ServicerContext) \
            -> PumpFluidDosingService_pb2.Subscribe_MaxFlowRate_Responses:
        """
        Requests the observable property Maximum Flow Rate
            The maximum value of the flow rate at which this pump can dose a fluid.

        :param request: An empty gRPC request object (properties have no parameters)
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A response object with the following fields:
            request.MaxFlowRate (Maximum Flow Rate): The maximum value of the flow rate at which this pump can dose a fluid.
        """

        while True:
            yield PumpFluidDosingService_pb2.Subscribe_MaxFlowRate_Responses(
                MaxFlowRate=silaFW_pb2.Real(value=self.pump.get_flow_rate_max())
            )

            # we add a small delay to give the client a chance to keep up.
            time.sleep(0.5)


    def Subscribe_FlowRate(self, request, context: grpc.ServicerContext) \
            -> PumpFluidDosingService_pb2.Subscribe_FlowRate_Responses:
        """
        Requests the observable property Flow Rate
            The current value of the flow rate. It is 0 if the pump does not dose any fluid.

        :param request: An empty gRPC request object (properties have no parameters)
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A response object with the following fields:
            request.FlowRate (Flow Rate): The current value of the flow rate. It is 0 if the pump does not dose any fluid.
        """

        while True:
            yield PumpFluidDosingService_pb2.Subscribe_FlowRate_Responses(
                FlowRate=silaFW_pb2.Real(value=self.pump.get_flow_is())
            )

            # we add a small delay to give the client a chance to keep up.
            time.sleep(0.5)

