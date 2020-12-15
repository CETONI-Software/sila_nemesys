"""
________________________________________________________________________

:PROJECT: SiLA2_python

*Axis System Control Service*

:details: AxisSystemControlService:
    Provides functionality to observe and control the state of an axis system

:file:    AxisSystemControlService_real.py
:authors: Florian Meinicke

:date: (creation)          2020-12-15T07:50:56.811849
:date: (last modification) 2020-12-15T07:50:56.811849

.. note:: Code generated by sila2codegenerator 0.2.0

________________________________________________________________________

**Copyright**:
  This file is provided "AS IS" with NO WARRANTY OF ANY KIND,
  INCLUDING THE WARRANTIES OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.

  For further Information see LICENSE file that comes with this distribution.
________________________________________________________________________
"""

__version__ = "0.1.0"

# import general packages
import logging
import time         # used for observables
import uuid         # used for observables
import grpc         # used for type hinting only

# import SiLA2 library
import sila2lib.framework.SiLAFramework_pb2 as silaFW_pb2

# import gRPC modules for this feature
from .gRPC import AxisSystemControlService_pb2 as AxisSystemControlService_pb2
# from .gRPC import AxisSystemControlService_pb2_grpc as AxisSystemControlService_pb2_grpc

# import default arguments
from .AxisSystemControlService_default_arguments import default_dict


# noinspection PyPep8Naming,PyUnusedLocal
class AxisSystemControlServiceReal:
    """
    Implementation of the *Axis System Control Service* in *Real* mode
        Allows to control motion systems like axis systems
    """

    def __init__(self):
        """Class initialiser"""

        logging.debug('Started server in mode: {mode}'.format(mode='Real'))

    def _get_command_state(self, command_uuid: str) -> silaFW_pb2.ExecutionInfo:
        """
        Method to fill an ExecutionInfo message from the SiLA server for observable commands

        :param command_uuid: The uuid of the command for which to return the current state

        :return: An execution info object with the current command state
        """

        #: Enumeration of silaFW_pb2.ExecutionInfo.CommandStatus
        command_status = silaFW_pb2.ExecutionInfo.CommandStatus.waiting
        #: Real silaFW_pb2.Real(0...1)
        command_progress = None
        #: Duration silaFW_pb2.Duration(seconds=<seconds>, nanos=<nanos>)
        command_estimated_remaining = None
        #: Duration silaFW_pb2.Duration(seconds=<seconds>, nanos=<nanos>)
        command_lifetime_of_execution = None

        # TODO: check the state of the command with the given uuid and return the correct information

        # just return a default in this example
        return silaFW_pb2.ExecutionInfo(
            commandStatus=command_status,
            progressInfo=(
                command_progress if command_progress is not None else None
            ),
            estimatedRemainingTime=(
                command_estimated_remaining if command_estimated_remaining is not None else None
            ),
            updatedLifetimeOfExecution=(
                command_lifetime_of_execution if command_lifetime_of_execution is not None else None
            )
        )

    def EnableAxisSystem(self, request, context: grpc.ServicerContext) \
            -> AxisSystemControlService_pb2.EnableAxisSystem_Responses:
        """
        Executes the unobservable command "Enable Axis System"
            Set all axes of the axis system into enabled state
    
        :param request: gRPC request containing the parameters passed:
            request.EmptyParameter (Empty Parameter): An empty parameter data type used if no parameter is required.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information
    
        :returns: The return object defined for the command with the following fields:
            EmptyResponse (Empty Response): An empty response data type used if no response is required.
        """
    
        # initialise the return value
        return_value = None
    
        # TODO:
        #   Add implementation of Real for command EnableAxisSystem here and write the resulting response
        #   in return_value
    
        # fallback to default
        if return_value is None:
            return_value = AxisSystemControlService_pb2.EnableAxisSystem_Responses(
                **default_dict['EnableAxisSystem_Responses']
            )
    
        return return_value
    
    
    def DisableAxisSystem(self, request, context: grpc.ServicerContext) \
            -> AxisSystemControlService_pb2.DisableAxisSystem_Responses:
        """
        Executes the unobservable command "Disable Axis System"
            Set all axes of the axis system into disabled state
    
        :param request: gRPC request containing the parameters passed:
            request.EmptyParameter (Empty Parameter): An empty parameter data type used if no parameter is required.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information
    
        :returns: The return object defined for the command with the following fields:
            EmptyResponse (Empty Response): An empty response data type used if no response is required.
        """
    
        # initialise the return value
        return_value = None
    
        # TODO:
        #   Add implementation of Real for command DisableAxisSystem here and write the resulting response
        #   in return_value
    
        # fallback to default
        if return_value is None:
            return_value = AxisSystemControlService_pb2.DisableAxisSystem_Responses(
                **default_dict['DisableAxisSystem_Responses']
            )
    
        return return_value
    
    
    def ClearAxisFaultState(self, request, context: grpc.ServicerContext) \
            -> AxisSystemControlService_pb2.ClearAxisFaultState_Responses:
        """
        Executes the unobservable command "Clear Axis Fault State"
            Clears the fault condition of a single axis. This is some kind of error acknowledge that clears the last fault and sets the device in an error-free state.
    
        :param request: gRPC request containing the parameters passed:
            request.EmptyParameter (Empty Parameter): An empty parameter data type used if no parameter is required.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information
    
        :returns: The return object defined for the command with the following fields:
            EmptyResponse (Empty Response): An empty response data type used if no response is required.
        """
    
        # initialise the return value
        return_value = None
    
        # TODO:
        #   Add implementation of Real for command ClearAxisFaultState here and write the resulting response
        #   in return_value
    
        # fallback to default
        if return_value is None:
            return_value = AxisSystemControlService_pb2.ClearAxisFaultState_Responses(
                **default_dict['ClearAxisFaultState_Responses']
            )
    
        return return_value
    

    def Get_AvailableAxes(self, request, context: grpc.ServicerContext) \
            -> AxisSystemControlService_pb2.Get_AvailableAxes_Responses:
        """
        Requests the unobservable property Available Axes
            The names of the individual axes of the axis system.
    
        :param request: An empty gRPC request object (properties have no parameters)
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information
    
        :returns: A response object with the following fields:
            AvailableAxes (Available Axes): The names of the individual axes of the axis system.
        """
    
        # initialise the return value
        return_value: AxisSystemControlService_pb2.Get_AvailableAxes_Responses = None
    
        # TODO:
        #   Add implementation of Simulation for property AvailableAxes here and write the resulting response
        #   in return_value
    
        # fallback to default
        if return_value is None:
            return_value = AxisSystemControlService_pb2.Get_AvailableAxes_Responses(
                **default_dict['Get_AvailableAxes_Responses']
            )
    
        return return_value
    
    def Subscribe_AxisSystemState(self, request, context: grpc.ServicerContext) \
            -> AxisSystemControlService_pb2.Subscribe_AxisSystemState_Responses:
        """
        Requests the observable property Axis System State
            The current state of the axis system. This is either 'Enabled' or 'Disabled'. Only if the state is 'Enabled', the axis system can move.
        :param request: An empty gRPC request object (properties have no parameters)
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information
    
        :returns: A response object with the following fields:
            AxisSystemState (Axis System State): The current state of the axis system. This is either 'Enabled' or 'Disabled'. Only if the sate is 'Enabled', the axis system can move.
        """
    
        # initialise the return value
        return_value: AxisSystemControlService_pb2.Subscribe_AxisSystemState_Responses = None
    
        # we could use a timeout here if we wanted
        while True:
            # TODO:
            #   Add implementation of Real for property AxisSystemState here and write the resulting
            #   response in return_value
    
            # create the default value
            if return_value is None:
                return_value = AxisSystemControlService_pb2.Subscribe_AxisSystemState_Responses(
                    **default_dict['Subscribe_AxisSystemState_Responses']
                )
    
    
            yield return_value
    
    
    def Subscribe_AxisFaultState(self, request, context: grpc.ServicerContext) \
            -> AxisSystemControlService_pb2.Subscribe_AxisFaultState_Responses:
        """
        Requests the observable property Axis Fault State
            Returns if a single axis of the system is in fault state. If the value is true (i.e. the axis is in fault state), it can be cleared by calling ClearAxisFaultState.
    
        :param request: An empty gRPC request object (properties have no parameters)
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information
    
        :returns: A response object with the following fields:
            AxisFaultState (Axis Fault State): Returns if a single axis of the system is in fault state. If the value is true (i.e. the axis is in fault state), it can be cleared by calling ClearAxisFaultState.
        """
    
        # initialise the return value
        return_value: AxisSystemControlService_pb2.Subscribe_AxisFaultState_Responses = None
    
        # we could use a timeout here if we wanted
        while True:
            # TODO:
            #   Add implementation of Real for property AxisFaultState here and write the resulting
            #   response in return_value
    
            # create the default value
            if return_value is None:
                return_value = AxisSystemControlService_pb2.Subscribe_AxisFaultState_Responses(
                    **default_dict['Subscribe_AxisFaultState_Responses']
                )
    
    
            yield return_value
    

    def Get_FCPAffectedByMetadata_AxisIdentifier(self, request, context: grpc.ServicerContext) \
            -> AxisSystemControlService_pb2.Get_FCPAffectedByMetadata_AxisIdentifier_Responses:
        """
        Requests the unobservable property FCPAffectedByMetadata Axis Identifier
            Specifies which Features/Commands/Properties of the SiLA server are affected by the Axis Identifier Metadata.
    
        :param request: An empty gRPC request object (properties have no parameters)
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information
    
        :returns: A response object with the following fields:
            AffectedCalls (AffectedCalls): A string containing a list of Fully Qualified Identifiers of Features, Commands and Properties for which the SiLA Client Metadata is expected as part of the respective RPCs.
        """
    
        # initialise the return value
        return_value: AxisSystemControlService_pb2.Get_FCPAffectedByMetadata_AxisIdentifier_Responses = None
    
        # TODO:
        #   Add implementation of Real for property FCPAffectedByMetadata_AxisIdentifier here and write the resulting response
        #   in return_value
    
        # fallback to default
        if return_value is None:
            return_value = AxisSystemControlService_pb2.Get_FCPAffectedByMetadata_AxisIdentifier_Responses(
                **default_dict['Get_FCPAffectedByMetadata_AxisIdentifier_Responses']
            )
    
        return return_value
