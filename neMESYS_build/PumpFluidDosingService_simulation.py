"""
________________________________________________________________________

:PROJECT: SiLA2_python

*pumpfluiddosingservice_server_simulation *

:details: pumpfluiddosingservice_server_simulation:
        Allows to dose a specified fluid. There are commands for absolute dosing (SetFillLevel) and relative dosing (StartDoseVolume and StartGenerateFlow) available.

        The flow rate can be negative. In this case the pump aspirates the fluid instead of dispensing. The flow rate has to be a value between MaxFlowRate and MinFlowRate. If the value is not within this range (hence is invalid) the ValidationError FlowRateOutOfRange is thrown.
        At any time the property CurrentSyringeFillLevel can be queried to see how much fluid is left in the syringe. Similarly the property CurrentFlowRate can be queried to get the current flow rate at which the pump is dosing.
    .

:file:    pumpfluiddosingservice_server_simulation.py
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


class PumpFluidDosingServiceSimulation():
    """ PumpFluidDosingServiceSimulation -
#        Allows to dose a specified fluid. There are commands for absolute dosing (SetFillLevel) and relative dosing (StartDoseVolume and StartGenerateFlow) available.
#
#        The flow rate can be negative. In this case the pump aspirates the fluid instead of dispensing. The flow rate has to be a value between MaxFlowRate and MinFlowRate. If the value is not within this range (hence is invalid) the ValidationError FlowRateOutOfRange is thrown.
#        At any time the property CurrentSyringeFillLevel can be queried to see how much fluid is left in the syringe. Similarly the property CurrentFlowRate can be queried to get the current flow rate at which the pump is dosing.
#     """

    def __init__(self):
        """ PumpFluidDosingServiceSimulation class initialiser """
        logging.debug("init class: PumpFluidDosingServiceSimulation ")

        self.dosage_uuid = ""

        self.max_fill_level = 60.0  # ml
        self.fill_level = self.max_fill_level
        self.target_fill_level = 0.0 # ml
        self.max_flow_rate = 100.0  # ml
        self.min_flow_rate = -100.0  # ml
        self.flow_rate = 0.0  # ml/s
        # indicates whether we are currently dosing or if we have been stopped by a call to StopDosage
        self.dosing = False

    def SetFillLevel(self, request, context):
        """
                Pumps fluid with the given flow rate until the requested fill level is reached.
                Depending on the requested fill level given in the FillLevel parameter this function may cause aspiration or dispension of fluid.

            :param request: gRPC request
            :param context: gRPC context
            :param request.FillLevel:
                The requested fill level. A level of 0 indicates a completely empty syringe. The value has to be between 0 and MaxSyringeFillLevel or else the ValidationError RequestedFillLevelOutOfRange is thrown.
            :param request.FlowRate:
                    The flow rate at which the pump should dose the fluid. This value can be negative. In that case the pump aspirates the fluid.
        """
        logging.debug("SetFillLevel - Mode: simulation ")

        requested_fill_level = request.FillLevel.value
        requested_flow_rate = request.FlowRate.value

        # We only allow one dosage at a time.
        # -> Throw an error if another dosage should be started when there already is one.
        if self.dosage_uuid:
            # return fwpb2.SiLAError(frameworkError=fwpb2.FrameworkError(errorType=fwpb2.FrameworkError.ErrorType.COMMAND_EXECUTION_NOT_ACCEPTED))
            return fwpb2.SiLAError(frameworkError=fwpb2.FrameworkError(
                errorType=fwpb2.FrameworkError.ErrorType.INVALID_COMMAND_EXECUTION_UUID))
        elif requested_fill_level < 0 or requested_fill_level > self.max_fill_level:
            logging.error(f"Requested Fill Level Out Of Range - FillLevel: {requested_fill_level}ml")
            return fwpb2.SiLAError(validationError=fwpb2.ValidationError(
                parameter="FillLevel",
                cause="The fill level requested in SetFillLevel is greater than MaxSyringeFillLevel or less than 0.",
                action="Adjust the FillLevel parameter to fit in the specified range."))
        elif requested_flow_rate < self.min_flow_rate or requested_flow_rate > self.max_flow_rate:
            logging.error(f"Requested Flow Rate Out Of Range - FlowRate: {requested_flow_rate}ml/s")
            return fwpb2.SiLAError(validationError=fwpb2.ValidationError(
                parameter="FlowRate",
                cause="The specified flow rate is not in the range bewteen MaxFlowRate and MinFlowRate for this pump."))
        elif (requested_flow_rate > 0 and self.fill_level <= 0):
            logging.error("Cannot dispense from an empty syringe (self.FillLevel: {}ml, FlowRate: {}ml/s)".format(
                self.fill_level, requested_flow_rate))
            return fwpb2.SiLAError(validationError=fwpb2.ValidationError(
                parameter="FlowRate",
                cause="Cannot dispense any more fluid due to already empty syringe."))
        elif (requested_flow_rate < 0 and self.fill_level >= self.max_fill_level):
            logging.error("Cannot aspirate to a filled syringe (self.FillLevel: {}ml, FlowRate: {}ml/s)".format(
                self.fill_level, requested_flow_rate))
            return fwpb2.SiLAError(validationError=fwpb2.ValidationError(
                parameter="FlowRate",
                cause="Cannot aspirate any more fluid due to already filled syringe."))
        else:
            self.dosage_uuid = str(uuid.uuid4())
            logging.info("Started dosing with flow rate of {}ml/s until fill level of {}ml is reached (UUID: {})".format(
                requested_flow_rate, requested_fill_level, self.dosage_uuid))
            command_uuid = fwpb2.CommandExecutionUUID(
                commandId=self.dosage_uuid)

            self.target_fill_level = requested_fill_level # ml
            self.flow_rate = requested_flow_rate # ml/s
            self.dosing = True

            return fwpb2.CommandConfirmation(commandId=command_uuid)

    def SetFillLevel_Info(self, request, context):
        """
                Pumps fluid with the given flow rate until the requested fill level is reached.
                Depending on the requested fill level given in the FillLevel parameter this function may cause aspiration or dispension of fluid.

            :param request: gRPC request
            :param context: gRPC context
            :param request.commandId: identifies the command execution
        """
        logging.debug("SetFillLevel_Info - Mode: simulation ")
        logging.info(
            f"Requested SetFillLevel_Info for dosage (UUID: {request.commandId})")
        logging.info(f"Current dosage is UUID: {self.dosage_uuid}")

        yield fwpb2.ExecutionInfo(commandStatus=fwpb2.ExecutionInfo.CommandStatus.waiting)

        # catch invalid CommandExecutionUUID:
        if not request.commandId or self.dosage_uuid != request.commandId:
            yield fwpb2.SiLAError(frameworkError=fwpb2.FrameworkError(
                errorType=fwpb2.FrameworkError.ErrorType.INVALID_COMMAND_EXECUTION_UUID))
        else:
            Volume = abs(int(self.fill_level - self.target_fill_level))
            for i in range(Volume):
                time.sleep(0.5)
                progress = i / Volume * 100 * abs(self.flow_rate)
                logging.info("Dosage progress: {0:5.2f}% done - {1:5.2f}ml".format(progress, self.fill_level))

                if not self.dosing or (self.flow_rate > 0 and self.fill_level <= self.target_fill_level) or (self.flow_rate < 0 and self.fill_level >= self.target_fill_level):
                    break

                self.fill_level -= self.flow_rate

                yield fwpb2.ExecutionInfo(commandStatus=fwpb2.ExecutionInfo.CommandStatus.running,
                                          progressInfo=fwpb2.Real(value=progress))

            yield fwpb2.ExecutionInfo(commandStatus=fwpb2.ExecutionInfo.CommandStatus.finishedSuccessfully)


    def SetFillLevel_Result(self, request, context):
        """
                Pumps fluid with the given flow rate until the requested fill level is reached.
                Depending on the requested fill level given in the FillLevel parameter this function may cause aspiration or dispension of fluid.

            :param request: gRPC request
            :param context: gRPC context
            :param request.commandId: identifies the command execution
        """
        logging.debug("SetFillLevel_Result - Mode: simulation ")

        if request.commandId and self.dosage_uuid == request.commandId:
            logging.info(f"Finished dosing! (UUID: {self.dosage_uuid})")
            self.dosage_uuid = ""
            self.flow_rate = 0.0
            self.dosing = False
            return pb2.SetFillLevel_Responses(Success=fwpb2.Boolean(value=True))
        else:
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
        logging.debug("DoseVolume - Mode: simulation ")

        # We only allow one dosage at a time.
        # -> Throw an error if another dosage should be started when there already is one.
        if self.dosage_uuid:
            # return fwpb2.SiLAError(frameworkError=fwpb2.FrameworkError(errorType=fwpb2.FrameworkError.ErrorType.COMMAND_EXECUTION_NOT_ACCEPTED))
            return fwpb2.SiLAError(frameworkError=fwpb2.FrameworkError(
                errorType=fwpb2.FrameworkError.ErrorType.INVALID_COMMAND_EXECUTION_UUID))
        else:
            self.dosage_uuid = str(uuid.uuid4())
            logging.info("Started dosing a volume of {} with a flow rate of {} (UUID: {})".format(
                request.Volume.value, request.FlowRate.value, self.dosage_uuid))
            command_uuid = fwpb2.CommandExecutionUUID(
                commandId=self.dosage_uuid)
            return fwpb2.CommandConfirmation(commandId=command_uuid)

    def DoseVolume_Info(self, request, context):
        """Dose a certain amount of volume with the given flow rate.
            :param request: gRPC request
            :param context: gRPC context
            :param request.commandId: identifies the command execution
        """
        logging.debug("DoseVolume_Info - Mode: simulation ")

        uuid = request.commandId
        yield fwpb2.ExecutionInfo(commandStatus=fwpb2.ExecutionInfo.CommandStatus.waiting)
        yield fwpb2.ExecutionInfo(commandStatus=fwpb2.ExecutionInfo.CommandStatus.running)
        yield fwpb2.ExecutionInfo(commandStatus=fwpb2.ExecutionInfo.CommandStatus.finishedSuccessfully)

    def DoseVolume_Result(self, request, context):
        """Dose a certain amount of volume with the given flow rate.
            :param request: gRPC request
            :param context: gRPC context
            :param request.commandId: identifies the command execution
        """
        logging.debug("DoseVolume_Result - Mode: simulation ")

        uuid = request.commandId
        return pb2.DoseVolume_Responses(Success=fwpb2.Boolean(value=False))

    def GenerateFlow(self, request, context):
        """
            Generate a continous flow with the given flow rate. Dosing continues until it gets stopped manually by calling StopDosage or until the pusher reached one of its limits.

            :param request: gRPC request
            :param context: gRPC context
            :param request.FlowRate:
                The flow rate at which the pump should dose the fluid. This value can be negative. In that case the pump aspirates the fluid.
        """
        logging.debug("GenerateFlow - Mode: simulation ")

        requested_flow_rate = request.FlowRate.value
        # We only allow one dosage at a time.
        # -> Throw an error if another dosage should be started when there already is one.
        if self.dosage_uuid:
            # return fwpb2.SiLAError(frameworkError=fwpb2.FrameworkError(errorType=fwpb2.FrameworkError.ErrorType.COMMAND_EXECUTION_NOT_ACCEPTED))
            return fwpb2.SiLAError(frameworkError=fwpb2.FrameworkError(
                errorType=fwpb2.FrameworkError.ErrorType.INVALID_COMMAND_EXECUTION_UUID))
        elif requested_flow_rate < self.min_flow_rate or requested_flow_rate > self.max_flow_rate:
            logging.error(f"Requested Flow Rate Out Of Range - FlowRate: {requested_flow_rate}ml/s")
            return fwpb2.SiLAError(validationError=fwpb2.ValidationError(
                parameter="FlowRate",
                cause="The specified flow rate is not in the range bewteen MaxFlowRate and MinFlowRate for this pump."))
        elif (requested_flow_rate > 0 and self.fill_level <= 0):
            logging.error("Cannot dispense from an empty syringe (self.FillLevel: {}ml, FlowRate: {}ml/s)".format(
                self.fill_level, requested_flow_rate))
            return fwpb2.SiLAError(validationError=fwpb2.ValidationError(
                parameter="FlowRate",
                cause="Cannot dispense any more fluid due to already empty syringe."))
        elif (requested_flow_rate < 0 and self.fill_level >= self.max_fill_level):
            logging.error("Cannot aspirate to a filled syringe (self.FillLevel: {}ml, FlowRate: {}ml/s)".format(
                self.fill_level, requested_flow_rate))
            return fwpb2.SiLAError(validationError=fwpb2.ValidationError(
                parameter="FlowRate",
                cause="Cannot aspirate any more fluid due to already filled syringe."))
        else:
            self.dosage_uuid = str(uuid.uuid4())
            logging.info("Started dosing with flow rate of {}ml/s (UUID: {})".format(
                request.FlowRate.value, self.dosage_uuid))
            command_uuid = fwpb2.CommandExecutionUUID(
                commandId=self.dosage_uuid)

            self.flow_rate = requested_flow_rate # ml/s
            self.dosing = True

            return fwpb2.CommandConfirmation(commandId=command_uuid)


    def GenerateFlow_Intermediate(self, request, context):
        """
            Generate a continous flow with the given flow rate. Dosing continues until it gets stopped manually by calling StopDosage or until the pusher reached one of its limits.

            :param request: gRPC request
            :param context: gRPC context
            :param request.commandId: identifies the command execution
        """
        logging.debug("GenerateFlow_Intermediate - Mode: simulation ")

        uuid = request.commandId
        yield pb2.GenerateFlow_IntermediateResponses(
            Test=fwpb2.String(value="intermediate"))

    def GenerateFlow_Info(self, request, context):
        """
            Generate a continous flow with the given flow rate. Dosing continues until it gets stopped manually by calling StopDosage or until the pusher reached one of its limits.

            :param request: gRPC request
            :param context: gRPC context
            :param request.commandId: identifies the command execution
        """
        logging.debug("GenerateFlow_Info - Mode: simulation ")
        logging.info(
            f"Requested GenerateFlow_Info for dosage (UUID: {request.commandId})")
        logging.info(f"Current dosage is UUID: {self.dosage_uuid}")

        yield fwpb2.ExecutionInfo(commandStatus=fwpb2.ExecutionInfo.CommandStatus.waiting)

        # catch invalid CommandExecutionUUID:
        if not request.commandId or self.dosage_uuid != request.commandId:
            yield fwpb2.SiLAError(frameworkError=fwpb2.FrameworkError(
                errorType=fwpb2.FrameworkError.ErrorType.INVALID_COMMAND_EXECUTION_UUID))
        else:
            while self.dosing and (
                (self.flow_rate > 0 and self.fill_level >= 0) or (self.flow_rate < 0 and self.fill_level <= self.max_fill_level)
                ):
                self.fill_level -= self.flow_rate
                time.sleep(0.5)
                logging.info("Dosage progress: currently at {0:5.2f}ml".format(self.fill_level))

                yield fwpb2.ExecutionInfo(commandStatus=fwpb2.ExecutionInfo.CommandStatus.running)

            yield fwpb2.ExecutionInfo(commandStatus=fwpb2.ExecutionInfo.CommandStatus.finishedSuccessfully)


    def GenerateFlow_Result(self, request, context):
        """
            Generate a continous flow with the given flow rate. Dosing continues until it gets stopped manually by calling StopDosage or until the pusher reached one of its limits.

            :param request: gRPC request
            :param context: gRPC context
            :param request.commandId: identifies the command execution
        """
        logging.debug("GenerateFlow_Result - Mode: simulation ")

        logging.debug("request.commandId {}".format(request.commandId))

        # if dosage was stopped by a call to StopDosage AND we get a valid UUID
        # OR if we get a valid UUID AND it is the current dosage -> stop dosing and return result
        if (not self.dosing and request.commandId) or (request.commandId and self.dosage_uuid == request.commandId):
            logging.info(f"Finished dosing! (UUID: {self.dosage_uuid})")
            self.dosage_uuid = ""
            self.flow_rate = 0.0
            self.dosing = False
            return pb2.GenerateFlow_Responses(Success=fwpb2.Boolean(value=True))
        else:
            return fwpb2.SiLAError(frameworkError=fwpb2.FrameworkError(
                errorType=fwpb2.FrameworkError.ErrorType.INVALID_COMMAND_EXECUTION_UUID))

    def StopDosage(self, request, context):
        """Stops a currently running dosage immediately.
        empty parameter
        """
        logging.debug("StopDosage - Mode: simulation ")

        self.dosage_uuid = ""
        self.flow_rate = 0.0
        self.dosing = False
        return pb2.StopDosage_Responses(Success=fwpb2.Boolean(value=True))

    def Get_MaxSyringeFillLevel(self, request, context):
        """The maximum amount of fluid that the syringe can hold.
            :param request: gRPC request
            :param context: gRPC context
            :param response.MaxSyringeFillLevel: The maximum amount of fluid that the syringe can hold.
        """
        logging.debug("Get_MaxSyringeFillLevel - Mode: simulation ")

        return pb2.Get_MaxSyringeFillLevel_Responses(MaxSyringeFillLevel=fwpb2.Real(value=self.max_fill_level))

    def Subscribe_SyringeFillLevel(self, request, context):
        """The current amount of fluid left in the syringe.
            :param request: gRPC request
            :param context: gRPC context
            :param response.SyringeFillLevel: The current amount of fluid left in the syringe.
        """
        logging.debug("Subscribe_SyringeFillLevel - Mode: simulation ")

        yield pb2.Subscribe_SyringeFillLevel_Responses(SyringeFillLevel=fwpb2.Real(value=self.fill_level))

    def Get_MaxFlowRate(self, request, context):
        """The maximum value of the flow rate at which this pump can dose a fluid.
            :param request: gRPC request
            :param context: gRPC context
            :param response.MaxFlowRate: The maximum value of the flow rate at which this pump can dose a fluid.
        """
        logging.debug("Get_MaxFlowRate - Mode: simulation ")

        return pb2.Get_MaxFlowRate_Responses(MaxFlowRate=fwpb2.Real(value=self.max_flow_rate))

    def Subscribe_FlowRate(self, request, context):
        """The current value of the flow rate. It is 0 if the pump does not dose any fluid.
            :param request: gRPC request
            :param context: gRPC context
            :param response.FlowRate: The current value of the flow rate. It is 0 if the pump does not dose any fluid.
        """
        logging.debug("Subscribe_FlowRate - Mode: simulation ")

        yield pb2.Subscribe_FlowRate_Responses(FlowRate=fwpb2.Real(value=self.flow_rate))
