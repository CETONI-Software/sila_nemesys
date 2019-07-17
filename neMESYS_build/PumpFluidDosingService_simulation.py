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

        self.SetFillLevel_UUID = ""
        self.DoseVolume_UUID = ""
        self.GenerateFlow_UUID = ""
        self.SyringeFillLevel_UUID = ""
        self.FlowRate_UUID = ""

    def SetFillLevel(self, request, context):
        """
                Pumps fluid with the given flow rate until the requested fill level is reached.
                Depending on the requested fill level given in the FillLevel parameter this function may cause aspiration or dispension of fluid.

            :param request: gRPC request
            :param context: gRPC context
            :param request.FillLevel:
                The requested fill level. A level of 0 indicates a completely empty syringe. The value has to be between 0 and MaxSyringeFillLevel or else the ValidationError RequestedFillLevelOutOfRange is thrown.
        """
        logging.debug("SetFillLevel - Mode: simulation ")

        if self.SetFillLevel_UUID:
            # return fwpb2.SiLAError(frameworkError=fwpb2.FrameworkError(errorType=fwpb2.FrameworkError.ErrorType.COMMAND_EXECUTION_NOT_ACCEPTED))
            return fwpb2.SiLAError(frameworkError=fwpb2.FrameworkError(errorType=fwpb2.FrameworkError.ErrorType.INVALID_COMMAND_EXECUTION_UUID))
        else:
            self.SetFillLevel_UUID = str(uuid.uuid4())
            logging.info("Started dosing with flow rate of {} until fill level of {} units is reached (UUID: {})".format(
                request.FlowRate, request.FillLevel, self.SetFillLevel_UUID))
            command_uuid = fwpb2.CommandExecutionUUID(
                commandId=self.SetFillLevel_UUID)
            return fwpb2.CommandConfirmation(commandId=command_uuid)

    def SetFillLevel_Info(self, request, context):
        """
                Pumps fluid with the given flow rate until the requested fill level is reached.
                Depending on the requested fill level given in the FillLevel parameter this function may cause aspiration or dispension of fluid.

            :param request: gRPC request
            :param context: gRPC context
            :param request.CommandExecutionUUID: identifies the command execution
        """
        logging.debug("SetFillLevel_Info - Mode: simulation ")

        if self.SetFillLevel_UUID == request.commandId:
            yield fwpb2.ExecutionInfo(commandStatus=fwpb2.ExecutionInfo.CommandStatus.waiting)
            for _ in range(10):
                yield fwpb2.ExecutionInfo(commandStatus=fwpb2.ExecutionInfo.CommandStatus.running)
                time.sleep(0.5)

            yield fwpb2.ExecutionInfo(commandStatus=fwpb2.ExecutionInfo.CommandStatus.finishedSuccessfully)
        else:
            yield fwpb2.SiLAError(frameworkError=fwpb2.FrameworkError(errorType=fwpb2.FrameworkError.ErrorType.INVALID_COMMAND_EXECUTION_UUID))

    def SetFillLevel_Result(self, request, context):
        """
                Pumps fluid with the given flow rate until the requested fill level is reached.
                Depending on the requested fill level given in the FillLevel parameter this function may cause aspiration or dispension of fluid.

            :param request: gRPC request
            :param context: gRPC context
            :param request.CommandExecutionUUID: identifies the command execution
        """
        logging.debug("SetFillLevel_Result - Mode: simulation ")

        if self.SetFillLevel_UUID == request.commandId:
            logging.info(f"Finished dosing! (UUID: {self.SetFillLevelUUID})")
            return pb2.SetFillLevel_Responses(Success=fwpb2.Boolean(value=True))
            self.SetFillLevel_UUID = str
        else:
            return fwpb2.SiLAError(frameworkError=fwpb2.FrameworkError(errorType=fwpb2.FrameworkError.ErrorType.INVALID_COMMAND_EXECUTION_UUID))

    def DoseVolume(self, request, context):
        """Dose a certain amount of volume with the given flow rate.
            :param request: gRPC request
            :param context: gRPC context
            :param request.Volume: The amount of volume to dose.

        """
        logging.debug("DoseVolume - Mode: simulation ")

        command_uuid = fwpb2.CommandExecutionUUID(commandId=str(uuid.uuid4()))
        return fwpb2.CommandConfirmation(commandId=command_uuid)

    def DoseVolume_Info(self, request, context):
        """Dose a certain amount of volume with the given flow rate.
            :param request: gRPC request
            :param context: gRPC context
            :param request.CommandExecutionUUID: identifies the command execution
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
            :param request.CommandExecutionUUID: identifies the command execution
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

        command_uuid = fwpb2.CommandExecutionUUID(commandId=str(uuid.uuid4()))
        return fwpb2.CommandConfirmation(commandId=command_uuid)

    def GenerateFlow_Intermediate(self, request, context):
        """
            Generate a continous flow with the given flow rate. Dosing continues until it gets stopped manually by calling StopDosage or until the pusher reached one of its limits.

            :param request: gRPC request
            :param context: gRPC context
            :param request.CommandExecutionUUID: identifies the command execution
        """
        logging.debug("GenerateFlow_Intermediate - Mode: simulation ")

        uuid = request.commandId
        yield pb2.GenerateFlow_Intermediate_IntermediateResponses(Success=fwpb2.String(value="DEFAULTstring" + return_val))

    def GenerateFlow_Info(self, request, context):
        """
            Generate a continous flow with the given flow rate. Dosing continues until it gets stopped manually by calling StopDosage or until the pusher reached one of its limits.

            :param request: gRPC request
            :param context: gRPC context
            :param request.CommandExecutionUUID: identifies the command execution
        """
        logging.debug("GenerateFlow_Info - Mode: simulation ")

        uuid = request.commandId
        yield fwpb2.ExecutionInfo(commandStatus=fwpb2.ExecutionInfo.CommandStatus.waiting)
        yield fwpb2.ExecutionInfo(commandStatus=fwpb2.ExecutionInfo.CommandStatus.running)
        yield fwpb2.ExecutionInfo(commandStatus=fwpb2.ExecutionInfo.CommandStatus.finishedSuccessfully)

    def GenerateFlow_Result(self, request, context):
        """
            Generate a continous flow with the given flow rate. Dosing continues until it gets stopped manually by calling StopDosage or until the pusher reached one of its limits.

            :param request: gRPC request
            :param context: gRPC context
            :param request.CommandExecutionUUID: identifies the command execution
        """
        logging.debug("GenerateFlow_Result - Mode: simulation ")

        uuid = request.commandId
        return pb2.GenerateFlow_Responses(Success=fwpb2.Boolean(value=False))

    def StopDosage(self, request, context):
        """Stops a currently running dosage immediately.
        empty parameter
        """
        logging.debug("StopDosage - Mode: simulation ")

        return_val = request.Void.value
        return pb2.StopDosage_Responses(Success=fwpb2.Boolean(value=False))

    def Get_MaxSyringeFillLevel(self, request, context):
        """The maximum amount of fluid that the syringe can hold.
            :param request: gRPC request
            :param context: gRPC context
            :param response.MaxSyringeFillLevel: The maximum amount of fluid that the syringe can hold.

        """
        logging.debug("Get_MaxSyringeFillLevel - Mode: simulation ")

        return_val = request.MaxSyringeFillLevel.value
        return pb2.Get_MaxSyringeFillLevel_Responses(MaxSyringeFillLevel=pb2.DataType_ValueWithUnit(ValueWithUnit=fwpb2.Real(value=0.0)))

    def Subscribe_SyringeFillLevel(self, request, context):
        """The current amount of fluid left in the syringe.
            :param request: gRPC request
            :param context: gRPC context
            :param response.SyringeFillLevel: The current amount of fluid left in the syringe.

        """
        logging.debug("Subscribe_SyringeFillLevel - Mode: simulation ")

        yield_val = request.SyringeFillLevel.value
        pb2.Subscribe_SyringeFillLevel_Responses(
            SyringeFillLevel=pb2.DataType_ValueWithUnit(ValueWithUnit=fwpb2.Real(value=0.0)))

    def Get_MaxFlowRate(self, request, context):
        """The maximum value of the flow rate at which this pump can dose a fluid.
            :param request: gRPC request
            :param context: gRPC context
            :param response.MaxFlowRate: The maximum value of the flow rate at which this pump can dose a fluid.

        """
        logging.debug("Get_MaxFlowRate - Mode: simulation ")

        return_val = request.MaxFlowRate.value
        return pb2.Get_MaxFlowRate_Responses(MaxFlowRate=pb2.DataType_ValueWithUnit(ValueWithUnit=fwpb2.Real(value=0.0)))

    def Get_MinFlowRate(self, request, context):
        """The minimum value of the flow rate at which this pump can dose a fluid.
            :param request: gRPC request
            :param context: gRPC context
            :param response.MinFlowRate: The minimum value of the flow rate at which this pump can dose a fluid.

        """
        logging.debug("Get_MinFlowRate - Mode: simulation ")

        return_val = request.MinFlowRate.value
        return pb2.Get_MinFlowRate_Responses(MinFlowRate=pb2.DataType_ValueWithUnit(ValueWithUnit=fwpb2.Real(value=0.0)))

    def Subscribe_FlowRate(self, request, context):
        """The current value of the flow rate. It is 0 if the pump does not dose any fluid.
            :param request: gRPC request
            :param context: gRPC context
            :param response.FlowRate: The current value of the flow rate. It is 0 if the pump does not dose any fluid.

        """
        logging.debug("Subscribe_FlowRate - Mode: simulation ")

        yield_val = request.FlowRate.value
        pb2.Subscribe_FlowRate_Responses(
            FlowRate=pb2.DataType_ValueWithUnit(ValueWithUnit=fwpb2.Real(value=0.0)))
