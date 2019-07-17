"""
________________________________________________________________________

:PROJECT: SiLA2_python

*pumpfluiddosingservice_server_simulation *

:details: pumpfluiddosingservice_server_simulation: 
        Allows to dose a specified fluid. There are commands for absolute dosing (SetFillLevel) and relative dosing (DoseVolume and GenerateFlow) available.

        The flow rate can be negative. In this case the pump aspirates the fluid instead of dispensing. The flow rate has to be a value between MaxFlowRate and MinFlowRate. If the value is not within this range (hence is invalid) a ValidationError will be thrown.
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
# importing protobuf and gRPC handler/stubs
import sila2lib.SiLAFramework_pb2 as fwpb2
import PumpFluidDosingService_pb2 as pb2
import PumpFluidDosingService_pb2_grpc as pb2_grpc


class PumpFluidDosingService(pb2_grpc.PumpFluidDosingServiceServicer):
    """ PumpFluidDosingService - 
#        Allows to dose a specified fluid. There are commands for absolute dosing (SetFillLevel) and relative dosing (DoseVolume and GenerateFlow) available.
#
#        The flow rate can be negative. In this case the pump aspirates the fluid instead of dispensing. The flow rate has to be a value between MaxFlowRate and MinFlowRate. If the value is not within this range (hence is invalid) a ValidationError will be thrown.
#        At any time the property CurrentSyringeFillLevel can be queried to see how much fluid is left in the syringe. Similarly the property CurrentFlowRate can be queried to get the current flow rate at which the pump is dosing.
#     """
    def __init__ (self):
        """ PumpFluidDosingService class initialiser """
        logging.debug("init class: PumpFluidDosingService ")

        # if self.implementation is set to None, it will use
        # the fallback simulation mode as default
        # if required, one could also create a simulation module and set this to the default implementation, like:
        #~ self.injectImplementation(GreetingProviderSimulation())

        self.implementation = None # this corresponds to the simple, fallback simulation mode

    # dependency injection - setter injection s. https://en.wikipedia.org/wiki/Dependency_injection
    def injectImplementation(self, implementation):
        self.implementation = implementation

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
        logging.debug("SetFillLevel - Mode: simulation ")

        if self.implementation is not None:
            return self.implementation.SetFillLevel(request, context)
        else:
            pass #~ command_uuid = fwpb2.CommandExecutionUUID( str(uuid.uuid4()) )
            #~ return fwpb2.CommandConfirmation( commandId = command_uuid )

    def SetFillLevel_Info(self, request, context):
        """
                Pumps fluid with the given flow rate until the requested fill level is reached.
                Depending on the requested fill level given in the FillLevel parameter this function may cause aspiration or dispension of fluid.
        
            :param request: gRPC request
            :param context: gRPC context
            :param request.commandId: identifies the command execution
        """
        logging.debug("SetFillLevel_Info - Mode: simulation ")

        if self.implementation is not None:
            for info_resp in self.implementation.SetFillLevel_Info(request, context):
                yield info_resp 
        else:
            pass #~ uuid = request.commandId
            #~ yield fwpb2.ExecutionInfo( commandStatus=fwpb2.ExecutionInfo.CommandStatus.waiting)
            #~ yield fwpb2.ExecutionInfo( commandStatus=fwpb2.ExecutionInfo.CommandStatus.running)
            #~ yield fwpb2.ExecutionInfo( commandStatus=fwpb2.ExecutionInfo.CommandStatus.finishedSuccessfully)

    def SetFillLevel_Result(self, request, context):
        """
                Pumps fluid with the given flow rate until the requested fill level is reached.
                Depending on the requested fill level given in the FillLevel parameter this function may cause aspiration or dispension of fluid.
        
            :param request: gRPC request
            :param context: gRPC context
            :param request.commandId: identifies the command execution
        """
        logging.debug("SetFillLevel_Result - Mode: simulation ")

        if self.implementation is not None:
            return self.implementation.SetFillLevel_Result(request, context)
        else:
            pass #~ uuid = request.commandId
            #~ return pb2.SetFillLevel_Responses( Success=fwpb2.Boolean(value=False) )

    def DoseVolume(self, request, context):
        """Dose a certain amount of volume with the given flow rate.
            :param request: gRPC request
            :param context: gRPC context
            :param request.Volume: The amount of volume to dose.
            :param request.FlowRate: 
                The flow rate at which the pump should dose the fluid. This value can be negative. In that case the pump aspirates the fluid.
            

        """
        logging.debug("DoseVolume - Mode: simulation ")

        if self.implementation is not None:
            return self.implementation.DoseVolume(request, context)
        else:
            pass #~ command_uuid = fwpb2.CommandExecutionUUID( str(uuid.uuid4()) )
            #~ return fwpb2.CommandConfirmation( commandId = command_uuid )

    def DoseVolume_Info(self, request, context):
        """Dose a certain amount of volume with the given flow rate.
            :param request: gRPC request
            :param context: gRPC context
            :param request.commandId: identifies the command execution
        """
        logging.debug("DoseVolume_Info - Mode: simulation ")

        if self.implementation is not None:
            for info_resp in self.implementation.DoseVolume_Info(request, context):
                yield info_resp 
        else:
            pass #~ uuid = request.commandId
            #~ yield fwpb2.ExecutionInfo( commandStatus=fwpb2.ExecutionInfo.CommandStatus.waiting)
            #~ yield fwpb2.ExecutionInfo( commandStatus=fwpb2.ExecutionInfo.CommandStatus.running)
            #~ yield fwpb2.ExecutionInfo( commandStatus=fwpb2.ExecutionInfo.CommandStatus.finishedSuccessfully)

    def DoseVolume_Result(self, request, context):
        """Dose a certain amount of volume with the given flow rate.
            :param request: gRPC request
            :param context: gRPC context
            :param request.commandId: identifies the command execution
        """
        logging.debug("DoseVolume_Result - Mode: simulation ")

        if self.implementation is not None:
            return self.implementation.DoseVolume_Result(request, context)
        else:
            pass #~ uuid = request.commandId
            #~ return pb2.DoseVolume_Responses( Success=fwpb2.Boolean(value=False) )

    def GenerateFlow(self, request, context):
        """
            Generate a continous flow with the given flow rate. Dosing continues until it gets stopped manually by calling StopDosage or until the pusher reached one of its limits.
        
            :param request: gRPC request
            :param context: gRPC context
            :param request.FlowRate: 
                The flow rate at which the pump should dose the fluid. This value can be negative. In that case the pump aspirates the fluid.
            

        """
        logging.debug("GenerateFlow - Mode: simulation ")

        if self.implementation is not None:
            return self.implementation.GenerateFlow(request, context)
        else:
            pass #~ command_uuid = fwpb2.CommandExecutionUUID( str(uuid.uuid4()) )
            #~ return fwpb2.CommandConfirmation( commandId = command_uuid )

    def GenerateFlow_Info(self, request, context):
        """
            Generate a continous flow with the given flow rate. Dosing continues until it gets stopped manually by calling StopDosage or until the pusher reached one of its limits.
        
            :param request: gRPC request
            :param context: gRPC context
            :param request.commandId: identifies the command execution
        """
        logging.debug("GenerateFlow_Info - Mode: simulation ")

        if self.implementation is not None:
            for info_resp in self.implementation.GenerateFlow_Info(request, context):
                yield info_resp 
        else:
            pass #~ uuid = request.commandId
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
        logging.debug("GenerateFlow_Result - Mode: simulation ")

        if self.implementation is not None:
            return self.implementation.GenerateFlow_Result(request, context)
        else:
            pass #~ uuid = request.commandId
            #~ return pb2.GenerateFlow_Responses( Success=fwpb2.Boolean(value=False) )

    def StopDosage(self, request, context):
        """Stops a currently running dosage immediately.
        empty parameter
        """
        logging.debug("StopDosage - Mode: simulation ")

        if self.implementation is not None:
            return self.implementation.StopDosage(request, context)
        else:
            pass #~ return_val = request.Void.value
            #~ return pb2.StopDosage_Responses( Success=fwpb2.Boolean(value=False) )

    def Get_MaxSyringeFillLevel(self, request, context):
        """The maximum amount of fluid that the syringe can hold.
            :param request: gRPC request
            :param context: gRPC context
            :param response.MaxSyringeFillLevel: The maximum amount of fluid that the syringe can hold.

        """
        logging.debug("Get_MaxSyringeFillLevel - Mode: simulation ")

        if self.implementation is not None:
            return self.implementation.Get_MaxSyringeFillLevel(request, context)
        else:
            #~ return_val = request.MaxSyringeFillLevel.value
            pass #~ return pb2.Get_MaxSyringeFillLevel_Responses( MaxSyringeFillLevel=fwpb2.Real(value=0.0) )

    def Subscribe_SyringeFillLevel(self, request, context):
        """The current amount of fluid left in the syringe.
            :param request: gRPC request
            :param context: gRPC context
            :param response.SyringeFillLevel: The current amount of fluid left in the syringe.

        """
        logging.debug("Subscribe_SyringeFillLevel - Mode: simulation ")

        if self.implementation is not None:
            self.implementation.Subscribe_SyringeFillLevel(request, context)
        else:
            #~ yield_val = request.SyringeFillLevel.value
            pass #~ yield pb2.Subscribe_SyringeFillLevel_Responses( SyringeFillLevel=fwpb2.Real(value=0.0) )

    def Get_MaxFlowRate(self, request, context):
        """The maximum value of the flow rate at which this pump can dose a fluid.
            :param request: gRPC request
            :param context: gRPC context
            :param response.MaxFlowRate: The maximum value of the flow rate at which this pump can dose a fluid.

        """
        logging.debug("Get_MaxFlowRate - Mode: simulation ")

        if self.implementation is not None:
            return self.implementation.Get_MaxFlowRate(request, context)
        else:
            #~ return_val = request.MaxFlowRate.value
            pass #~ return pb2.Get_MaxFlowRate_Responses( MaxFlowRate=fwpb2.Real(value=0.0) )

    def Subscribe_FlowRate(self, request, context):
        """The current value of the flow rate. It is 0 if the pump does not dose any fluid.
            :param request: gRPC request
            :param context: gRPC context
            :param response.FlowRate: The current value of the flow rate. It is 0 if the pump does not dose any fluid.

        """
        logging.debug("Subscribe_FlowRate - Mode: simulation ")

        if self.implementation is not None:
            self.implementation.Subscribe_FlowRate(request, context)
        else:
            #~ yield_val = request.FlowRate.value
            pass #~ yield pb2.Subscribe_FlowRate_Responses( FlowRate=fwpb2.Real(value=0.0) )




