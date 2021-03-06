# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import SyringeConfigurationController_pb2 as SyringeConfigurationController__pb2


class SyringeConfigurationControllerStub(object):
  """Feature: Syringe Configuration Controller

  Provides syringe pump specific functions for configuration (i.e. the configuration of the syringe itself).

  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SetSyringeParameters = channel.unary_unary(
        '/sila2.de.cetoni.pumps.syringepumps.syringeconfigurationcontroller.v1.SyringeConfigurationController/SetSyringeParameters',
        request_serializer=SyringeConfigurationController__pb2.SetSyringeParameters_Parameters.SerializeToString,
        response_deserializer=SyringeConfigurationController__pb2.SetSyringeParameters_Responses.FromString,
        )
    self.Subscribe_InnerDiameter = channel.unary_stream(
        '/sila2.de.cetoni.pumps.syringepumps.syringeconfigurationcontroller.v1.SyringeConfigurationController/Subscribe_InnerDiameter',
        request_serializer=SyringeConfigurationController__pb2.Subscribe_InnerDiameter_Parameters.SerializeToString,
        response_deserializer=SyringeConfigurationController__pb2.Subscribe_InnerDiameter_Responses.FromString,
        )
    self.Subscribe_MaxPistonStroke = channel.unary_stream(
        '/sila2.de.cetoni.pumps.syringepumps.syringeconfigurationcontroller.v1.SyringeConfigurationController/Subscribe_MaxPistonStroke',
        request_serializer=SyringeConfigurationController__pb2.Subscribe_MaxPistonStroke_Parameters.SerializeToString,
        response_deserializer=SyringeConfigurationController__pb2.Subscribe_MaxPistonStroke_Responses.FromString,
        )


class SyringeConfigurationControllerServicer(object):
  """Feature: Syringe Configuration Controller

  Provides syringe pump specific functions for configuration (i.e. the configuration of the syringe itself).

  """

  def SetSyringeParameters(self, request, context):
    """Set Syringe Parameters

    Set syringe parameters.
    If you change the syringe in one device, you need to setup the new syringe parameters to get proper
    conversion of flow rate und volume units.

    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Subscribe_InnerDiameter(self, request, context):
    """Inner Diameter
    Inner diameter of the syringe tube in millimetres.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Subscribe_MaxPistonStroke(self, request, context):
    """Max Piston Stroke
    The maximum piston stroke defines the maximum position the piston can be moved to before it slips out of the syringe
    tube. The maximum piston stroke limits the maximum travel range of the syringe pump pusher.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SyringeConfigurationControllerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SetSyringeParameters': grpc.unary_unary_rpc_method_handler(
          servicer.SetSyringeParameters,
          request_deserializer=SyringeConfigurationController__pb2.SetSyringeParameters_Parameters.FromString,
          response_serializer=SyringeConfigurationController__pb2.SetSyringeParameters_Responses.SerializeToString,
      ),
      'Subscribe_InnerDiameter': grpc.unary_stream_rpc_method_handler(
          servicer.Subscribe_InnerDiameter,
          request_deserializer=SyringeConfigurationController__pb2.Subscribe_InnerDiameter_Parameters.FromString,
          response_serializer=SyringeConfigurationController__pb2.Subscribe_InnerDiameter_Responses.SerializeToString,
      ),
      'Subscribe_MaxPistonStroke': grpc.unary_stream_rpc_method_handler(
          servicer.Subscribe_MaxPistonStroke,
          request_deserializer=SyringeConfigurationController__pb2.Subscribe_MaxPistonStroke_Parameters.FromString,
          response_serializer=SyringeConfigurationController__pb2.Subscribe_MaxPistonStroke_Responses.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'sila2.de.cetoni.pumps.syringepumps.syringeconfigurationcontroller.v1.SyringeConfigurationController', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
