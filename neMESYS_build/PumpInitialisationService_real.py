"""
________________________________________________________________________

:PROJECT: SiLA2_python

*pumpinitialisationservice_server_real *

:details: pumpinitialisationservice_server_real:
            Allows to initialise a pump (e.g. by executiong a reference move).
            The initialisation has to be successful in order for the pump to work correctly and dose fluids. If the initialisation fails, the StandardExecutionError InitialisationFailed is thrown.
    .

:file:    pumpinitialisationservice_server_real.py
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
import PumpInitialisationService_pb2 as pb2
import PumpInitialisationService_pb2_grpc as pb2_grpc

# import qmixsdk
from qmixsdk import qmixbus
from qmixsdk import qmixpump


class PumpInitialisationServiceReal():
    """ PumpInitialisationServiceReal -
#            Allows to initialise a pump (e.g. by executiong a reference move).
#            The initialisation has to be successful in order for the pump to work correctly and dose fluids. If the initialisation fails, the StandardExecutionError InitialisationFailed is thrown.
#     """
    def __init__ (self, bus, pump):
        """ PumpInitialisationServiceReal class initialiser """
        logging.debug("init class: PumpInitialisationServiceReal ")

        self.bus = bus
        self.pump = pump


    def wait_calibration_finished(self, timeout_sec):
        """
        The function waits until pump calibration has finished or
        until the timeout occurs.
        """
        timer = qmixbus.PollingTimer(timeout_sec * 1000)
        result = False
        while not (result or timer.is_expired()):
            time.sleep(0.1)
            result = self.pump.is_calibration_finished()
        return result

    def InitializePumpDrive(self, request, context):
        """Initialize the pump drive (e.g. by executing a reference move).
        empty parameter
        """
        logging.debug("InitializePumpDrive - Mode: real ")

        self.pump.calibrate()
        time.sleep(0.2)
        calibration_finished = self.wait_calibration_finished(30)
        logging.info("Pump calibrated: %s", calibration_finished)

        return pb2.InitializePumpDrive_Responses(Success=fwpb2.Boolean(value=calibration_finished))
