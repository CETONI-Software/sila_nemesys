"""
________________________________________________________________________

:PROJECT: SiLA2_python

*pumpfluiddosingservice_server_real *

:details: pumpfluiddosingservice_server_real:
        Allows to dose a specified fluid. There are commands for absolute dosing (SetFillLevel) and relative dosing (DoseVolume and GenerateFlow) available.

        The flow rate can be negative. In this case the pump aspirates the fluid instead of dispensing. The flow rate has to be a value between MaxFlowRate and MinFlowRate. If the value is not within this range (hence is invalid) a ValidationError will be thrown.
        At any time the property CurrentSyringeFillLevel can be queried to see how much fluid is left in the syringe. Similarly the property CurrentFlowRate can be queried to get the current flow rate at which the pump is dosing.
    .

:file:    pumpfluiddosingservice_server_real.py
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
import time
# importing protobuf and gRPC handler/stubs
import sila2lib.SiLAFramework_pb2 as fwpb2
import PumpFluidDosingService_pb2 as pb2
import PumpFluidDosingService_pb2_grpc as pb2_grpc

# import qmixsdk
from qmixsdk import qmixbus
from qmixsdk import qmixpump


def wait_dosage_finished(pump, timeout_seconds):
    """
    The function waits until the last dosage command has finished
    until the timeout occurs.
    """

    timer = qmixbus.PollingTimer(timeout_seconds * 1000) # msec
    message_timer = qmixbus.PollingTimer(500) # msec
    result = True
    while result and not timer.is_expired():
        time.sleep(0.1)
        if message_timer.is_expired():
            logging.info("Fill level: %s", pump.get_fill_level())
            yield fwpb2.ExecutionInfo(commandStatus=fwpb2.ExecutionInfo.CommandStatus.running)
            message_timer.restart()
        result = pump.is_pumping()

    if not result:
        yield fwpb2.ExecutionInfo(commandStatus=fwpb2.ExecutionInfo.CommandStatus.finishedSuccessfully)
    else:
        yield fwpb2.ExecutionInfo(commandStatus=fwpb2.ExecutionInfo.CommandStatus.finishedWithError)


class PumpFluidDosingServiceReal():
    """ PumpFluidDosingServiceReal -
#        Allows to dose a specified fluid. There are commands for absolute dosing (SetFillLevel) and relative dosing (DoseVolume and GenerateFlow) available.
#
#        The flow rate can be negative. In this case the pump aspirates the fluid instead of dispensing. The flow rate has to be a value between MaxFlowRate and MinFlowRate. If the value is not within this range (hence is invalid) a ValidationError will be thrown.
#        At any time the property CurrentSyringeFillLevel can be queried to see how much fluid is left in the syringe. Similarly the property CurrentFlowRate can be queried to get the current flow rate at which the pump is dosing.
#     """
    def __init__ (self, bus, pump):
        """ PumpFluidDosingServiceReal class initialiser """
        logging.debug("init class: PumpFluidDosingServiceReal ")

        self.bus = bus
        self.pump = pump

        self.max_fill_level = self.pump.get_volume_max()
        self.dosage_uuid = ""

    def check_pre_dosage(self, flow_rate, fill_level=None, volume=None):
        """Checks if the given flow rate and fill level or volume are in the correct ranges for this pump
        """
        # We only allow one dosage at a time.
        # -> Throw an error if another dosage should be started when there already is one.
        if self.dosage_uuid:
            # return fwpb2.SiLAError(frameworkError=fwpb2.FrameworkError(errorType=fwpb2.FrameworkError.ErrorType.COMMAND_EXECUTION_NOT_ACCEPTED))
            return fwpb2.SiLAError(frameworkError=fwpb2.FrameworkError(
                errorType=fwpb2.FrameworkError.ErrorType.INVALID_COMMAND_EXECUTION_UUID))
        if flow_rate < 0 or flow_rate > self.pump.get_flow_rate_max():
            logging.error("Requested Flow Rate Out Of Range - FlowRate: %5.2f", flow_rate)
            return fwpb2.SiLAError(validationError=fwpb2.ValidationError(
                parameter="FlowRate",
                cause="The specified flow rate is not in the range bewteen 0 and MaxFlowRate for this pump."))
        if fill_level is not None and (fill_level < 0 or fill_level > self.max_fill_level):
            logging.error("Requested Fill Level Out Of Range - FillLevel: %5.2f", fill_level)
            return fwpb2.SiLAError(validationError=fwpb2.ValidationError(
                parameter="FillLevel",
                cause="The fill level requested in SetFillLevel is greater than MaxSyringeFillLevel or less than 0.",
                action="Adjust the FillLevel parameter to fit in the specified range."))
        if volume is not None and (volume < 0 or volume > self.max_fill_level):
            logging.error("Requested Volume Out Of Range - Volume: %5.2f", volume)
            return fwpb2.SiLAError(validationError=fwpb2.ValidationError(
                parameter="Volume",
                cause="The volume requested in DoseVolume is greater than MaxSyringeFillLevel or less than 0.",
                action="Adjust the Volume parameter to fit in the specified range."))

    def SetFillLevel(self, request, context):
        """
                Pumps fluid with the given flow rate until the requested fill level is reached.
                Depending on the requested fill level given in the FillLevel parameter this function may cause aspiration or dispension of fluid.

            :param request: gRPC request
            :param context: gRPC context
            :param request.FillLevel:
                The requested fill level. A level of 0 indicates a completely empty syringe. The value has to be between 0 and MaxSyringeFillLevel or else a ValidationError will be thrown.

            :param request.FlowRate:
                    The flow rate at which the pump should dose the fluid. This value can be negative. In that case the pump aspirates the fluid.
        """
        logging.debug("SetFillLevel - Mode: real ")

        requested_fill_level = request.FillLevel.value
        requested_flow_rate = request.FlowRate.value

        check_result = self.check_pre_dosage(requested_flow_rate,
                                             fill_level=requested_fill_level)
        if check_result:
            return check_result

        self.dosage_uuid = str(uuid.uuid4())
        logging.info("Started dosing with flow rate of %5.2f until fill level of %5.2f is reached (UUID: %s)",
                     requested_flow_rate, requested_fill_level, self.dosage_uuid)
        command_uuid = fwpb2.CommandExecutionUUID(
            commandId=self.dosage_uuid)

        try:
            self.pump.set_fill_level(requested_fill_level, requested_flow_rate)
        except qmixbus.DeviceError as err:
            logging.error("QmixSDK Error: %s", err)
            return fwpb2.SiLAError(executionError=fwpb2.ExecutionError(
                errorIdentifier="DosageFinishedUnexpectedly", cause="self.pump.set_fill_level()"))
        return fwpb2.CommandConfirmation(commandId=command_uuid)

    def SetFillLevel_Info(self, request, context):
        """
                Pumps fluid with the given flow rate until the requested fill level is reached.
                Depending on the requested fill level given in the FillLevel parameter this function may cause aspiration or dispension of fluid.

            :param request: gRPC request
            :param context: gRPC context
            :param request.commandId: identifies the command execution
        """
        logging.debug("SetFillLevel_Info - Mode: real ")

        logging.info("Requested SetFillLevel_Info for dosage (UUID: %s)", request.commandId)
        logging.info("Current dosage is UUID: %s", self.dosage_uuid)

        yield fwpb2.ExecutionInfo(commandStatus=fwpb2.ExecutionInfo.CommandStatus.waiting)

        # catch invalid CommandExecutionUUID:
        if not request.commandId or self.dosage_uuid != request.commandId:
            yield fwpb2.SiLAError(frameworkError=fwpb2.FrameworkError(
                errorType=fwpb2.FrameworkError.ErrorType.INVALID_COMMAND_EXECUTION_UUID))
        else:
            for info in wait_dosage_finished(self.pump, 30):
                yield info

    def SetFillLevel_Result(self, request, context):
        """
                Pumps fluid with the given flow rate until the requested fill level is reached.
                Depending on the requested fill level given in the FillLevel parameter this function may cause aspiration or dispension of fluid.

            :param request: gRPC request
            :param context: gRPC context
            :param request.commandId: identifies the command execution
        """
        logging.debug("SetFillLevel_Result - Mode: real ")

        if request.commandId and self.dosage_uuid == request.commandId:
            logging.info(f"Finished dosing! (UUID: {self.dosage_uuid})")
            self.dosage_uuid = ""
            return pb2.SetFillLevel_Responses(Success=fwpb2.Boolean(value=True))

        return fwpb2.SiLAError(frameworkError=fwpb2.FrameworkError(
            errorType=fwpb2.FrameworkError.ErrorType.INVALID_COMMAND_EXECUTION_UUID))


    def DoseVolume(self, request, context):
        """Dose a certain amount of volume with the given flow rate.
            :param request: gRPC request
            :param context: gRPC context
            :param request.Volume: The amount of volume to dose.
            :param request.FlowRate:
                The flow rate at which the pump should dose the fluid. This value can be negative. In that case the pump aspirates the fluid.
        """
        logging.debug("DoseVolume - Mode: real ")

        requested_volume = request.Volume.value
        requested_flow_rate = request.FlowRate.value

        check_result = self.check_pre_dosage(requested_flow_rate,
                                             volume=requested_volume)
        if check_result:
            return check_result

        self.dosage_uuid = str(uuid.uuid4())
        logging.info("Started dosing a volume of %s with a flow rate of %5.2f (UUID: %s)",
                     requested_volume, requested_flow_rate, self.dosage_uuid)
        command_uuid = fwpb2.CommandExecutionUUID(
            commandId=self.dosage_uuid)

        try:
            self.pump.pump_volume(requested_volume, requested_flow_rate)
        except qmixbus.DeviceError as err:
            logging.error("QmixSDK Error: %s", err)
            return fwpb2.SiLAError(executionError=fwpb2.ExecutionError(
                errorIdentifier="DosageFinishedUnexpectedly", cause="self.pump.apsirate()"))
        return fwpb2.CommandConfirmation(commandId=command_uuid)

    def DoseVolume_Info(self, request, context):
        """Dose a certain amount of volume with the given flow rate.
            :param request: gRPC request
            :param context: gRPC context
            :param request.commandId: identifies the command execution
        """
        logging.debug("DoseVolume_Info - Mode: real ")

        #~ uuid = request.commandId
        #~ yield fwpb2.ExecutionInfo( commandStatus=fwpb2.ExecutionInfo.CommandStatus.waiting)
        #~ yield fwpb2.ExecutionInfo( commandStatus=fwpb2.ExecutionInfo.CommandStatus.running)
        #~ yield fwpb2.ExecutionInfo( commandStatus=fwpb2.ExecutionInfo.CommandStatus.finishedSuccessfully)

    def DoseVolume_Result(self, request, context):
        """Dose a certain amount of volume with the given flow rate.
            :param request: gRPC request
            :param context: gRPC context
            :param request.commandId: identifies the command execution
        """
        logging.debug("DoseVolume_Result - Mode: real ")

        #~ uuid = request.commandId
        #~ return pb2.DoseVolume_Responses(Success=fwpb2.Boolean(value=False))

    def GenerateFlow(self, request, context):
        """
            Generate a continous flow with the given flow rate. Dosing continues until it gets stopped manually by calling StopDosage or until the pusher reached one of its limits.

            :param request: gRPC request
            :param context: gRPC context
            :param request.FlowRate:
                The flow rate at which the pump should dose the fluid. This value can be negative. In that case the pump aspirates the fluid.
        """
        logging.debug("GenerateFlow - Mode: real ")

        #~ command_uuid = fwpb2.CommandExecutionUUID( commandId = str(uuid.uuid4()) )
        #~ return fwpb2.CommandConfirmation( commandId = command_uuid )

    def GenerateFlow_Intermediate(self, request, context):
        """
            Generate a continous flow with the given flow rate. Dosing continues until it gets stopped manually by calling StopDosage or until the pusher reached one of its limits.

            :param request: gRPC request
            :param context: gRPC context
            :param request.commandId: identifies the command execution
        """
        logging.debug("GenerateFlow_Intermediate - Mode: real ")

        #~ uuid = request.commandId
        #~ yield pb2.GenerateFlow_IntermediateResponses( Success=fwpb2.String(value="DEFAULTstring" + return_val) )

    def GenerateFlow_Info(self, request, context):
        """
            Generate a continous flow with the given flow rate. Dosing continues until it gets stopped manually by calling StopDosage or until the pusher reached one of its limits.

            :param request: gRPC request
            :param context: gRPC context
            :param request.commandId: identifies the command execution
        """
        logging.debug("GenerateFlow_Info - Mode: real ")

        #~ uuid = request.commandId
        #~ yield fwpb2.ExecutionInfo( commandStatus=fwpb2.ExecutionInfo.CommandStatus.waiting)
        #~ yield fwpb2.ExecutionInfo( commandStatus=fwpb2.ExecutionInfo.CommandStatus.running)
        #~ yield fwpb2.ExecutionInfo( commandStatus=fwpb2.ExecutionInfo.CommandStatus.finishedSuccessfully)

    def GenerateFlow_Result(self, request, context):
        """
            Generate a continous flow with the given flow rate. Dosing continues until it gets stopped manually by calling StopDosage or until the pusher reached one of its limits.

            :param request: gRPC request
            :param context: gRPC context
            :param request.commandId: identifies the command execution
        """
        logging.debug("GenerateFlow_Result - Mode: real ")

        #~ uuid = request.commandId
        #~ return pb2.GenerateFlow_Responses(Success=fwpb2.Boolean(value=False))

    def StopDosage(self, request, context):
        """Stops a currently running dosage immediately.
        empty parameter
        """
        logging.debug("StopDosage - Mode: real ")

        self.pump.stop_pumping()
        return pb2.StopDosage_Responses(Success=fwpb2.Boolean(value=True))

    def Get_MaxSyringeFillLevel(self, request, context):
        """The maximum amount of fluid that the syringe can hold.
            :param request: gRPC request
            :param context: gRPC context
            :param response.MaxSyringeFillLevel: The maximum amount of fluid that the syringe can hold.
        """
        logging.debug("Get_MaxSyringeFillLevel - Mode: real ")

        return pb2.Get_MaxSyringeFillLevel_Responses(
            MaxSyringeFillLevel=fwpb2.Real(value=self.max_fill_level))

    def Subscribe_SyringeFillLevel(self, request, context):
        """The current amount of fluid left in the syringe.
            :param request: gRPC request
            :param context: gRPC context
            :param response.SyringeFillLevel: The current amount of fluid left in the syringe.
        """
        logging.debug("Subscribe_SyringeFillLevel - Mode: real ")

        yield pb2.Subscribe_SyringeFillLevel_Responses(
            SyringeFillLevel=fwpb2.Real(value=self.pump.get_fill_level()))

    def Get_MaxFlowRate(self, request, context):
        """The maximum value of the flow rate at which this pump can dose a fluid.
            :param request: gRPC request
            :param context: gRPC context
            :param response.MaxFlowRate: The maximum value of the flow rate at which this pump can dose a fluid.
        """
        logging.debug("Get_MaxFlowRate - Mode: real ")

        return pb2.Get_MaxFlowRate_Responses(
            MaxFlowRate=fwpb2.Real(value=self.pump.get_flow_rate_max()))

    def Subscribe_FlowRate(self, request, context):
        """The current value of the flow rate. It is 0 if the pump does not dose any fluid.
            :param request: gRPC request
            :param context: gRPC context
            :param response.FlowRate: The current value of the flow rate. It is 0 if the pump does not dose any fluid.
        """
        logging.debug("Subscribe_FlowRate - Mode: real ")

        yield pb2.Subscribe_FlowRate_Responses(
            FlowRate=fwpb2.Real(value=self.pump.get_flow_is()))
