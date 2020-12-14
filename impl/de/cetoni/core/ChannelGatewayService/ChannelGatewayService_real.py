"""
________________________________________________________________________

:PROJECT: SiLA2_python

*I/O Channel Gateway Service*

:details: ChannelGatewayService:
    This feature provides gateway functionality for the other I/O Features.

:file:    ChannelGatewayService_real.py
:authors: Florian Meinicke

:date: (creation)          2020-12-10T10:35:05.402420
:date: (last modification) 2020-12-10T10:35:05.402420

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

# meta packages
from typing import List, Tuple, Union

# import SiLA2 library
import sila2lib.framework.SiLAFramework_pb2 as silaFW_pb2
from sila2lib.sila_server import SiLA2Server

# import SiLA errors
from impl.common.qmix_errors import SiLAFrameworkError, SiLAFrameworkErrorType

# import gRPC modules for this feature
from .gRPC import ChannelGatewayService_pb2 as ChannelGatewayService_pb2
# from .gRPC import ChannelGatewayService_pb2_grpc as ChannelGatewayService_pb2_grpc

# import default arguments
from .ChannelGatewayService_default_arguments import default_dict

from qmixsdk.qmixcontroller import ControllerChannel
from qmixsdk.qmixanalogio import AnalogInChannel, AnalogOutChannel
from qmixsdk.qmixdigio import DigitalInChannel, DigitalOutChannel

# noinspection PyPep8Naming,PyUnusedLocal
class ChannelGatewayServiceReal:
    """
    Implementation of the *I/O Channel Gateway Service* in *Real* mode
        The SiLA 2 driver for Qmix I/O Devices
    """

    def __init__(self,
                 channels: List[Union[ControllerChannel,
                                      AnalogInChannel, AnalogOutChannel,
                                      DigitalInChannel, DigitalOutChannel]]):
        """
        Class initialiser

        :param channels: All channels of all devices with channels that are connected to the bus
        """

        self.METADATA_CHANNEL_IDENTIFIER = 'sila-de.cetoni-core-channelgatewayservice-v1-metadata-channelidentifier-bin'

        self.channels = channels
        self.feature_to_channel = {
            'ControlLoopService': ControllerChannel,
            'AnalogInChannelProvider': AnalogInChannel,
            'AnalogOutChannelController': AnalogOutChannel,
            'DigitalInChannelProvider': DigitalInChannel,
            'DigitalOutChannelController': DigitalOutChannel
        }

        logging.debug('Started server in mode: {mode}'.format(mode='Real'))

    def _get_channel_name(self, metadata: Tuple[Tuple[str, str]]) -> str:
        """
        Get the requested channel name from the given `metadata`

        :param metdata: The metadata of the call. It should contain the requested channel name
        :return: The channel name if it can be obtained, otherwise a SiLAFrameworkError will be raised
        """

        invocation_metadata = {key: value for key, value in metadata}
        logging.debug(f"Received invocation metadata: {invocation_metadata}")
        try:
            return invocation_metadata[self.METADATA_CHANNEL_IDENTIFIER].decode('utf-8')
        except KeyError:
            raise SiLAFrameworkError(SiLAFrameworkErrorType.INVALID_METADATA,
                                     'This Command requires the ChannelIdentifier metadata!')

    def get_channel(self, metadata: Tuple[Tuple[str, str]]):
        """
        Get the channel that is identified by the channel name given in `metadata`

        :param metdata: The metadata of the call. It should contain the requested channel name
        :return: A valid channel object if the channel can be identified, otherwise a SiLAFrameworkError will be raised
        """

        channel_name = self._get_channel_name(metadata)

        logging.debug(f"Requested channel: {channel_name}")

        for channel in self.channels:
            if channel.get_name() == channel_name:
                return channel
        return None

    def GetChannelIdentifiers(self, request, context: grpc.ServicerContext) \
            -> ChannelGatewayService_pb2.GetChannelIdentifiers_Responses:
        """
        Executes the unobservable command "Get Channel Identifiers"
            Get all possible channel names (identifiers) that the given Feature can use.

        :param request: gRPC request containing the parameters passed:
            request.FeatureIdentifier (Feature Identifier): A Fully Qualified Feature Identifier.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: The return object defined for the command with the following fields:
            ChannelIdentifiers (Channel Identifiers): A list of channel names (identifiers) that the given Feature can use.
        """

        requested_feature = request.FeatureIdentifier.value

        logging.debug(f"Requested channel identifiers for feature {requested_feature}")

        if requested_feature not in self.feature_to_channel:
            raise SiLAExecutionError(
                'ChannelIdentifierNotNecessary',
                f'The Feature {requested_feature} does not need the ChannelIdentifier metadata.'
            )

        channel_names = [silaFW_pb2.String(value=channel.get_name())
                         for channel in self.channels
                         if isinstance(channel, self.feature_to_channel[requested_feature])]

        return ChannelGatewayService_pb2.GetChannelIdentifiers_Responses(ChannelIdentifiers=channel_names)

    def Get_FCPAffectedByMetadata_ChannelIdentifier(self, request, context: grpc.ServicerContext) \
            -> ChannelGatewayService_pb2.Get_FCPAffectedByMetadata_ChannelIdentifier_Responses:
        """
        Requests the unobservable property FCPAffectedByMetadata Channel Identifier
            Specifies which Features/Commands/Properties of the SiLA server are affected by the Channel Identifier Metadata.

        :param request: An empty gRPC request object (properties have no parameters)
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A response object with the following fields:
            AffectedCalls (AffectedCalls): A string containing a list of Fully Qualified Identifiers of Features, Commands and Properties for which the SiLA Client Metadata is expected as part of the respective RPCs.
        """

        return ChannelGatewayService_pb2.Get_FCPAffectedByMetadata_ChannelIdentifier_Responses(
            AffectedCalls=[
                silaFW_pb2.String(value="ControlLoopService"),
                silaFW_pb2.String(value="AnalogInChannelProvider"),
                silaFW_pb2.String(value="AnalogOutChannelController"),
                silaFW_pb2.String(value="DigitalInChannelProvider"),
                silaFW_pb2.String(value="DigitalOutChannelController")
            ]
        )