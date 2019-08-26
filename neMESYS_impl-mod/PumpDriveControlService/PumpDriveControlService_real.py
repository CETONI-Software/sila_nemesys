"""
________________________________________________________________________

:PROJECT: SiLA2_python

*Pump Drive Control Service*

:details: PumpDriveControlService:
    Functionality to control and maintain the drive that drives the pump.
    Allows to initialize a pump (e.g. by executing a reference move) and obtain status information about the pump
    drive's current state (i.e. enabled/disabled).
    The initialization has to be successful in order for the pump to work correctly and dose fluids. If the
    initialization fails, the StandardExecutionError InitializationFailed is thrown.

:file:    PumpDriveControlService_real.py
:authors: Florian Meinicke

:date: (creation)          2019-07-16T11:11:31.282215
:date: (last modification) 2019-08-23T11:56:25.065599

.. note:: Code generated by SiLA2CodeGenerator 0.2.0

________________________________________________________________________

**Copyright**:
  This file is provided "AS IS" with NO WARRANTY OF ANY KIND,
  INCLUDING THE WARRANTIES OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.

  For further Information see LICENSE file that comes with this distribution.
________________________________________________________________________
"""

__version__ = "0.0.1"

# import general packages
import logging
import uuid
import time
from configparser import ConfigParser, NoSectionError, NoOptionError

# import qmixsdk
from qmixsdk import qmixbus
from qmixsdk import qmixpump

# import SiLA2 library
import sila2lib.SiLAFramework_pb2 as fwpb2

# import gRPC modules for this feature
from .gRPC import PumpDriveControlService_pb2 as pb2
from .gRPC import PumpDriveControlService_pb2_grpc as pb2_grpc

# import default arguments
from .PumpDriveControlService_default_arguments import default_dict


# noinspection PyPep8Naming
class PumpDriveControlServiceReal:
    """
    Implementation of the *Pump Drive Control Service* in *Real* mode
        This is a test service for neMESYS syringe pumps via SiLA2
    """

    def __init__(self, pump: qmixpump.Pump, sila2_conf: ConfigParser):
        """Class initialiser"""

        logging.debug('Started server in mode: {mode}'.format(mode='Real'))

        self.pump = pump
        self.sila2_conf = sila2_conf

        self._restore_last_drive_position_counter()

    def _restore_last_drive_position_counter(self):
        """
        Reads the last drive position counter from the server's config file.
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


    def _wait_calibration_finished(self, timeout_sec):
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


    def InitializePumpDrive(self, request, context) -> pb2.InitializePumpDrive_Responses:
        """
        Executes the unobservable command Initialize Pump Drive
            Initialize the pump drive (e.g. by executing a reference move).

        :param request: gRPC request containing the parameters passed:
            request.EmptyParameter (Empty Parameter): An empty parameter data type used if no parameter is required.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: The return object defined for the command with the following fields:
            request.EmptyResponse (Empty Response): An empty response data type used if no response is required.
        """

        self.pump.calibrate()
        time.sleep(0.2)
        calibration_finished = self._wait_calibration_finished(30)
        logging.info("Pump calibrated: %s", calibration_finished)

        return pb2.InitializePumpDrive_Responses()

    def EnablePumpDrive(self, request, context) -> pb2.EnablePumpDrive_Responses:
        """
        Executes the unobservable command Enable Pump Drive
            Set the pump into enabled state.

        :param request: gRPC request containing the parameters passed:
            request.EmptyParameter (Empty Parameter): An empty parameter data type used if no parameter is required.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: The return object defined for the command with the following fields:
            request.EmptyResponse (Empty Response): An empty response data type used if no response is required.
        """

        if self.pump.is_in_fault_state():
            self.pump.clear_fault()
        self.pump.enable(True)

        return pb2.EnablePumpDrive_Responses()

    def DisablePumpDrive(self, request, context) -> pb2.DisablePumpDrive_Responses:
        """
        Executes the unobservable command Disable Pump Drive
            Set the pump into disabled state.

        :param request: gRPC request containing the parameters passed:
            request.EmptyParameter (Empty Parameter): An empty parameter data type used if no parameter is required.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: The return object defined for the command with the following fields:
            request.EmptyResponse (Empty Response): An empty response data type used if no response is required.
        """

        self.pump.enable(False)

        return pb2.DisablePumpDrive_Responses()

    def Subscribe_PumpDriveState(self, request, context) -> pb2.Subscribe_PumpDriveState_Responses:
        """
        Requests the observable property Pump Drive State
            The current state of the pump. This is either enabled (true) or disabled (false). Only if the sate is enabled, the pump can dose fluids.

        :param request: An empty gRPC request object (properties have no parameters)
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A response object with the following fields:
            request.PumpDriveState (Pump Drive State): The current state of the pump. This is either enabled (true) or disabled (false). Only if the sate is enabled, the pump can dose fluids.
        """

        logging.debug("Pump is enabled: %s", self.pump.is_enabled())

        while True:
            yield pb2.Subscribe_PumpDriveState_Responses(
                PumpDriveState=fwpb2.Boolean(value=self.pump.is_enabled())
            )

            # we add a small delay to give the client a chance to keep up.
            time.sleep(0.5)


    def Subscribe_FaultState(self, request, context) -> pb2.Subscribe_FaultState_Responses:
        """
        Requests the observable property Fault State
            Returns if the pump is in fault state. If the value is true (i.e. the pump is in fault state), it can be cleared by calling EnablePumpDrive.

        :param request: An empty gRPC request object (properties have no parameters)
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A response object with the following fields:
            request.FaultState (Fault State): Returns if the pump is in fault state. If the value is true (i.e. the pump is in fault state), it can be cleared by calling EnablePumpDrive.
        """

        logging.debug("Pump is in fault state: %s", self.pump.is_in_fault_state())

        while True:
            yield pb2.Subscribe_FaultState_Responses(
                FaultState=fwpb2.Boolean(value=self.pump.is_in_fault_state())
            )

            # we add a small delay to give the client a chance to keep up.
            time.sleep(0.5)
