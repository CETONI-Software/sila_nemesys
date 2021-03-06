# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import ContinuousFlowInitializationController_pb2 as ContinuousFlowInitializationController__pb2
import sila2lib.framework.SiLAFramework_pb2 as SiLAFramework__pb2


class ContinuousFlowInitializationControllerStub(object):
    """Feature: Continuous Flow Initialization Controller
    Allows to initialize a contiflow pump before starting the continuous flow.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.InitializeContiflow = channel.unary_unary(
                '/sila2.de.cetoni.pumps.contiflowpumps.continuousflowinitializationcontroller.v1.ContinuousFlowInitializationController/InitializeContiflow',
                request_serializer=ContinuousFlowInitializationController__pb2.InitializeContiflow_Parameters.SerializeToString,
                response_deserializer=SiLAFramework__pb2.CommandConfirmation.FromString,
                )
        self.InitializeContiflow_Info = channel.unary_stream(
                '/sila2.de.cetoni.pumps.contiflowpumps.continuousflowinitializationcontroller.v1.ContinuousFlowInitializationController/InitializeContiflow_Info',
                request_serializer=SiLAFramework__pb2.CommandExecutionUUID.SerializeToString,
                response_deserializer=SiLAFramework__pb2.ExecutionInfo.FromString,
                )
        self.InitializeContiflow_Result = channel.unary_unary(
                '/sila2.de.cetoni.pumps.contiflowpumps.continuousflowinitializationcontroller.v1.ContinuousFlowInitializationController/InitializeContiflow_Result',
                request_serializer=SiLAFramework__pb2.CommandExecutionUUID.SerializeToString,
                response_deserializer=ContinuousFlowInitializationController__pb2.InitializeContiflow_Responses.FromString,
                )
        self.Subscribe_IsInitialized = channel.unary_stream(
                '/sila2.de.cetoni.pumps.contiflowpumps.continuousflowinitializationcontroller.v1.ContinuousFlowInitializationController/Subscribe_IsInitialized',
                request_serializer=ContinuousFlowInitializationController__pb2.Subscribe_IsInitialized_Parameters.SerializeToString,
                response_deserializer=ContinuousFlowInitializationController__pb2.Subscribe_IsInitialized_Responses.FromString,
                )


class ContinuousFlowInitializationControllerServicer(object):
    """Feature: Continuous Flow Initialization Controller
    Allows to initialize a contiflow pump before starting the continuous flow.
    """

    def InitializeContiflow(self, request, context):
        """Initialize Contiflow
        Initialize the continuous flow pump.
        Call this command after all parameters have been set, to prepare the conti flow pump for the start of the continuous
        flow. The initialization procedure ensures, that the syringes are sufficiently filled to start the continuous flow. So
        calling this command may cause a syringe refill if the syringes are not sufficiently filled. So before calling this
        command you should ensure, that syringe refilling properly works an can be executed. If you have a certain syringe
        refill procedure, you can also manually refill the syringes with the normal syringe pump functions. If the syringes are
        sufficiently filled if you call this function, no refilling will take place.

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InitializeContiflow_Info(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InitializeContiflow_Result(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Subscribe_IsInitialized(self, request, context):
        """Is Initialized
        Returns true, if the conti fow pump is initialized and ready for continuous flow start.
        Use this function to check if the pump is initialized before you start a continuous flow. If you change and continuous
        flow parameter, like valve settings, cross flow duration and so on, the pump will leave the initialized state. That
        means, after each parameter change, an initialization is required. Changing the flow rate or the dosing volume does not
        require and initialization.

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ContinuousFlowInitializationControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'InitializeContiflow': grpc.unary_unary_rpc_method_handler(
                    servicer.InitializeContiflow,
                    request_deserializer=ContinuousFlowInitializationController__pb2.InitializeContiflow_Parameters.FromString,
                    response_serializer=SiLAFramework__pb2.CommandConfirmation.SerializeToString,
            ),
            'InitializeContiflow_Info': grpc.unary_stream_rpc_method_handler(
                    servicer.InitializeContiflow_Info,
                    request_deserializer=SiLAFramework__pb2.CommandExecutionUUID.FromString,
                    response_serializer=SiLAFramework__pb2.ExecutionInfo.SerializeToString,
            ),
            'InitializeContiflow_Result': grpc.unary_unary_rpc_method_handler(
                    servicer.InitializeContiflow_Result,
                    request_deserializer=SiLAFramework__pb2.CommandExecutionUUID.FromString,
                    response_serializer=ContinuousFlowInitializationController__pb2.InitializeContiflow_Responses.SerializeToString,
            ),
            'Subscribe_IsInitialized': grpc.unary_stream_rpc_method_handler(
                    servicer.Subscribe_IsInitialized,
                    request_deserializer=ContinuousFlowInitializationController__pb2.Subscribe_IsInitialized_Parameters.FromString,
                    response_serializer=ContinuousFlowInitializationController__pb2.Subscribe_IsInitialized_Responses.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'sila2.de.cetoni.pumps.contiflowpumps.continuousflowinitializationcontroller.v1.ContinuousFlowInitializationController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ContinuousFlowInitializationController(object):
    """Feature: Continuous Flow Initialization Controller
    Allows to initialize a contiflow pump before starting the continuous flow.
    """

    @staticmethod
    def InitializeContiflow(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sila2.de.cetoni.pumps.contiflowpumps.continuousflowinitializationcontroller.v1.ContinuousFlowInitializationController/InitializeContiflow',
            ContinuousFlowInitializationController__pb2.InitializeContiflow_Parameters.SerializeToString,
            SiLAFramework__pb2.CommandConfirmation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InitializeContiflow_Info(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/sila2.de.cetoni.pumps.contiflowpumps.continuousflowinitializationcontroller.v1.ContinuousFlowInitializationController/InitializeContiflow_Info',
            SiLAFramework__pb2.CommandExecutionUUID.SerializeToString,
            SiLAFramework__pb2.ExecutionInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InitializeContiflow_Result(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sila2.de.cetoni.pumps.contiflowpumps.continuousflowinitializationcontroller.v1.ContinuousFlowInitializationController/InitializeContiflow_Result',
            SiLAFramework__pb2.CommandExecutionUUID.SerializeToString,
            ContinuousFlowInitializationController__pb2.InitializeContiflow_Responses.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Subscribe_IsInitialized(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/sila2.de.cetoni.pumps.contiflowpumps.continuousflowinitializationcontroller.v1.ContinuousFlowInitializationController/Subscribe_IsInitialized',
            ContinuousFlowInitializationController__pb2.Subscribe_IsInitialized_Parameters.SerializeToString,
            ContinuousFlowInitializationController__pb2.Subscribe_IsInitialized_Responses.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
