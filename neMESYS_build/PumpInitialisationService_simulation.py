"""
________________________________________________________________________

:PROJECT: SiLA2_python

*pumpinitialisationservice_server_simulation *

:details: pumpinitialisationservice_server_simulation: 
            Allows to initialise a pump by either executing a complete initialisation or by simply setting the pump's drive position counter. InitialisePumpDrive is mandatory if the last value of the drive position counter cannot be provided. Clients can query the DrivePositionCounter property to provide this at the next initialisation and then use RestoreDrivePositionCounter.
            The initialisation has to be successful in order for the pump to work correctly and dose fluids. If the initialisation fails, the StandardExecutionError InitialisationFailed is thrown.
    . 
           
:file:    pumpinitialisationservice_server_simulation.py
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
import PumpInitialisationService_pb2 as pb2
import PumpInitialisationService_pb2_grpc as pb2_grpc


class PumpInitialisationServiceSimulation():
    """ PumpInitialisationServiceSimulation - 
#            Allows to initialise a pump by either executing a complete initialisation or by simply setting the pump's drive position counter. InitialisePumpDrive is mandatory if the last value of the drive position counter cannot be provided. Clients can query the DrivePositionCounter property to provide this at the next initialisation and then use RestoreDrivePositionCounter.
#            The initialisation has to be successful in order for the pump to work correctly and dose fluids. If the initialisation fails, the StandardExecutionError InitialisationFailed is thrown.
#     """
    def __init__ (self):
        """ PumpInitialisationServiceSimulation class initialiser """
        logging.debug("init class: PumpInitialisationServiceSimulation ")



    def InitialisePumpDrive(self, request, context):
        """Initialize the pump drive (e.g. by executing a reference move).
        empty parameter
        """
        logging.debug("InitialisePumpDrive - Mode: simulation ")

        #~ return_val = request.Void.value
        #~ return pb2.InitialisePumpDrive_Responses(Success=fwpb2.Boolean(value=False))

    def RestoreDrivePositionCounter(self, request, context):
        """Restore the internal hardware position counter value of the pump drive.
                In many drives the actual position value is counted by a quadrature decoder. This internal position counter value will get lost, as soon as the device is switched off. In order to restore this position counter value after power on, a client can query the internal position counter value (DrivePositionCounter), store it persistently into a configuration file and restore it later by calling this function.
        
            :param request: gRPC request
            :param context: gRPC context
            :param request.DrivePositionCounter: The drive position counter to restore.

        """
        logging.debug("RestoreDrivePositionCounter - Mode: simulation ")

        #~ return_val = request.DrivePositionCounter.value
        #~ return pb2.RestoreDrivePositionCounter_Responses(Success=fwpb2.Boolean(value=False))

    def Subscribe_DrivePositionCounter(self, request, context):
        """The value of the internal drive position counter.
            :param request: gRPC request
            :param context: gRPC context
            :param response.DrivePositionCounter: The value of the internal drive position counter.

        """
        logging.debug("Subscribe_DrivePositionCounter - Mode: simulation ")

        #~ yield_val = request.DrivePositionCounter.value
        #~ pb2.Subscribe_DrivePositionCounter_Responses( DrivePositionCounter=fwpb2.Real(value=0.0) )




