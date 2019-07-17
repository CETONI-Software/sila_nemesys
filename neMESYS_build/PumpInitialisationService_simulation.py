"""
________________________________________________________________________

:PROJECT: SiLA2_python

*pumpinitialisationservice_server_simulation *

:details: pumpinitialisationservice_server_simulation:
            Allows to initialise a pump (e.g. by executiong a reference move).
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
#            Allows to initialise a pump (e.g. by executiong a reference move).
#            The initialisation has to be successful in order for the pump to work correctly and dose fluids. If the initialisation fails, the StandardExecutionError InitialisationFailed is thrown.
#     """
    def __init__ (self):
        """ PumpInitialisationServiceSimulation class initialiser """
        logging.debug("init class: PumpInitialisationServiceSimulation ")



    def InitializePumpDrive(self, request, context):
        """Initialize the pump drive (e.g. by executing a reference move).
        empty parameter
        """
        logging.debug("InitializePumpDrive - Mode: simulation ")

        #~ return_val = request.Void.value
        return pb2.InitializePumpDrive_Responses(Success=fwpb2.Boolean(value=True))




