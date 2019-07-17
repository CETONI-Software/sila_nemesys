"""
________________________________________________________________________

:PROJECT: SiLA2_python

*pumpdrivecontrolservice_server_real *

:details: pumpdrivecontrolservice_server_real:
        Functionality to control and maintain the drive that drives the pump.
        Allows to initialise a pump (e.g. by executing a reference move).
        The initialisation has to be successful in order for the pump to work correctly and dose fluids. If the initialisation fails, the StandardExecutionError InitialisationFailed is thrown.
        Obtain status information about the pump drive's current state (e.g. enabled/disabled or fault state).
    .

:file:    pumpdrivecontrolservice_server_real.py
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
from configparser import ConfigParser, NoSectionError, NoOptionError

# importing protobuf and gRPC handler/stubs
import sila2lib.SiLAFramework_pb2 as fwpb2
import PumpDriveControlService_pb2 as pb2
import PumpDriveControlService_pb2_grpc as pb2_grpc

# import qmixsdk
from qmixsdk import qmixbus
from qmixsdk import qmixpump


class PumpDriveControlServiceReal():
    """ PumpDriveControlServiceReal -
#        Functionality to control and maintain the drive that drives the pump.
#        Allows to initialise a pump (e.g. by executing a reference move).
#        The initialisation has to be successful in order for the pump to work correctly and dose fluids. If the initialisation fails, the StandardExecutionError InitialisationFailed is thrown.
#        Obtain status information about the pump drive's current state (e.g. enabled/disabled or fault state).
#     """
    def __init__ (self, pump, sila2_conf):
        """ PumpDriveControlServiceReal class initialiser """
        logging.debug("init class: PumpDriveControlServiceReal ")

        self.pump = pump
        self.sila2_conf = sila2_conf

        self.restore_last_drive_position_counter()

    def restore_last_drive_position_counter(self):
        """Reads the last drive position counter from the server's config file.
        """
        pump_name = self.pump.get_pump_name()
        try:
            drive_pos_counter = int(self.sila2_conf[pump_name]["drive_pos_counter"])
            logging.debug("Restoring drive position counter: %d", drive_pos_counter)
            self.pump.restore_position_counter_value(drive_pos_counter)
        except NoSectionError as err:
            logging.error("No section for %s in SiLA2 config file: %s", pump_name, err)
        except (NoOptionError, KeyError) as err:
            logging.error("Cannot read config file option in %s", err)
            logging.error("No drive position counter found! Reference move needed!")


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

    def EnablePumpDrive(self, request, context):
        """Set the pump into enabled state.
            :param request: gRPC request
            :param context: gRPC context
        """
        logging.debug("EnablePumpDrive - Mode: real ")

        if self.pump.is_in_fault_state():
            self.pump.clear_fault()
        self.pump.enable(True)

        return pb2.EnablePumpDrive_Responses()

    def DisablePumpDrive(self, request, context):
        """Set the pump into disabled state.
            :param request: gRPC request
            :param context: gRPC context
        """
        logging.debug("DisablePumpDrive - Mode: real ")

        self.pump.enable(False)

        return pb2.DisablePumpDrive_Responses()

    def Subscribe_PumpDriveState(self, request, context):
        """The current state of the pump. This is either enabled or disabled. Only if the sate is enabled, the pump can dose fluids.
            :param request: gRPC request
            :param context: gRPC context
            :param response.PumpDriveState: The current state of the pump. This is either enabled or disabled. Only if the sate is enabled, the pump can dose fluids.
        """
        logging.debug("Subscribe_PumpDriveState - Mode: real ")

        logging.debug("Pump is enabled: %s", self.pump.is_enabled())

        yield pb2.Subscribe_PumpDriveState_Responses(
            PumpDriveState=fwpb2.Boolean(value=self.pump.is_enabled())
        )

    def Subscribe_FaultState(self, request, context):
        """Returns if the pump is in fault state. If the value is true (i.e. the pump is in fault state), it can be cleared by calling ClearFaultState.
            :param request: gRPC request
            :param context: gRPC context
            :param response.FaultState: Returns if the pump is in fault state. If the value is true (i.e. the pump is in fault state), it can be cleared by calling ClearFaultState.
        """
        logging.debug("Subscribe_FaultState - Mode: real ")

        logging.debug("Pump is in fault state: %s", self.pump.is_in_fault_state())

        yield pb2.Subscribe_FaultState_Responses(
            FaultState=fwpb2.Boolean(value=self.pump.is_in_fault_state())
        )
