#!/usr/bin/env python3
"""
________________________________________________________________________

:PROJECT: SiLA2_python

*neMESYS *

:details: neMESYS: This is a test service for neMESYS syringe pumps via SiLA2.

:file:    neMESYS.py
:authors: Florian Meinicke

:date: (creation)          20190627
:date: (last modification) 20190627

.. note:: - 0.1.6
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
import argparse

import sila2lib.sila_server as slss

import PumpFluidDosingService_pb2
import PumpFluidDosingService_pb2_grpc
import PumpUnitController_pb2
import PumpUnitController_pb2_grpc
import PumpInitialisationService_pb2
import PumpInitialisationService_pb2_grpc
import ValvePositionController_pb2
import ValvePositionController_pb2_grpc


from PumpFluidDosingService_servicer import PumpFluidDosingService
from PumpFluidDosingService_simulation import PumpFluidDosingServiceSimulation
from PumpFluidDosingService_real import PumpFluidDosingServiceReal

from PumpUnitController_servicer import PumpUnitController
from PumpUnitController_simulation import PumpUnitControllerSimulation
from PumpUnitController_real import PumpUnitControllerReal

from PumpInitialisationService_servicer import PumpInitialisationService
from PumpInitialisationService_simulation import PumpInitialisationServiceSimulation
from PumpInitialisationService_real import PumpInitialisationServiceReal

from ValvePositionController_servicer import ValvePositionController
from ValvePositionController_simulation import ValvePositionControllerSimulation
from ValvePositionController_real import ValvePositionControllerReal

# import qmixsdk
from qmixsdk import qmixbus
from qmixsdk import qmixpump

class neMESYSServer(slss.SiLA2Server):
    """ Class doc """
    def __init__ (self, parsed_args):
        super().__init__(name=parsed_args.server_name,
                         description=parsed_args.description,
                         server_type=parsed_args.server_type,
                         version=__version__,
                         vendor_URL="cetoni.de")

        """ Class initialiser """
        # registering features
        self.PumpFluidDosingService_servicer = PumpFluidDosingService()
        PumpFluidDosingService_pb2_grpc.add_PumpFluidDosingServiceServicer_to_server(self.PumpFluidDosingService_servicer, self.grpc_server)
        self.addFeature('PumpFluidDosingService', '.')

        self.PumpUnitController_servicer = PumpUnitController()
        PumpUnitController_pb2_grpc.add_PumpUnitControllerServicer_to_server(self.PumpUnitController_servicer, self.grpc_server)
        self.addFeature('PumpUnitController', '.')

        self.PumpInitialisationService_servicer = PumpInitialisationService()
        PumpInitialisationService_pb2_grpc.add_PumpInitialisationServiceServicer_to_server(self.PumpInitialisationService_servicer, self.grpc_server)
        self.addFeature('PumpInitialisationService', '.')

        self.ValvePositionController_servicer = ValvePositionController()
        ValvePositionController_pb2_grpc.add_ValvePositionControllerServicer_to_server(self.ValvePositionController_servicer, self.grpc_server)
        self.addFeature('ValvePositionController', '.')

        self.connect_to_bus_and_enable_pump()

        self.switchToRealMode()

        # starting and running the gRPC/SiLA2 server
        self.run()

        self.stop_and_close_bus()


    def connect_to_bus_and_enable_pump(self):
        """
            Loads a valid Qmix configuration, connects to the bus,
            retrieves the pump and enables it.
        """
        logging.debug("Opening bus")

        self.bus = qmixbus.Bus()
        # let's see if that helps...
        try:
            self.bus.open("/mnt/hgfs/Win_Data/SiLA/NDM-SiLA", 0)
        except qmixbus.DeviceError as err:
            logging.error("qmixbus.open(): %s", err)
            logging.info("trying again...")
            self.bus.open("/mnt/hgfs/Win_Data/SiLA/NDM-SiLA", 0)

        self.pump = qmixpump.Pump()
        self.pump.lookup_by_name("neMESYS_Low_Pressure_1_Pump")

        # let's see if that helps...
        try:
            self.bus.start()
        except qmixbus.DeviceError as err:
            logging.error("qmixbus.start(): %s", err)
            logging.info("trying again...")
            self.bus.start()

        if self.pump.is_in_fault_state():
            self.pump.clear_fault()
        if not self.pump.is_enabled():
            self.pump.enable(True)


    def stop_and_close_bus(self):
        """ Stops and closes the bus communication.
        """
        print()
        logging.debug("Closing bus...")
        self.bus.stop()
        self.bus.close()


    def switchToSimMode(self):
        """overwriting base class method"""
        self.simulation_mode = True
        self.PumpFluidDosingService_servicer.injectImplementation(PumpFluidDosingServiceSimulation()) # or use 'None' for default simulation implementation
        self.PumpUnitController_servicer.injectImplementation(PumpUnitControllerSimulation()) # or use 'None' for default simulation implementation
        self.PumpInitialisationService_servicer.injectImplementation(PumpInitialisationServiceSimulation()) # or use 'None' for default simulation implementation
        self.ValvePositionController_servicer.injectImplementation(ValvePositionControllerSimulation()) # or use 'None' for default simulation implementation

        success = True
        logging.debug("switched to sim mode {}".format(success) )

    def switchToRealMode(self):
        """overwriting base class method"""
        self.simulation_mode = False
        self.PumpFluidDosingService_servicer.injectImplementation(PumpFluidDosingServiceReal(self.bus, self.pump))
        self.PumpUnitController_servicer.injectImplementation(PumpUnitControllerReal(self.bus, self.pump))
        self.PumpInitialisationService_servicer.injectImplementation(PumpInitialisationServiceReal(self.bus, self.pump))
        self.ValvePositionController_servicer.injectImplementation(ValvePositionControllerReal(self.bus, self.pump))

        success = True
        logging.debug("switched to real mode {}".format(success) )


def parseCommandLine():
    """ just looking for commandline arguments ...
       :param - : -"""
    help = "SiLA2 service: neMESYS"

    parser = argparse.ArgumentParser(description="A SiLA2 service: neMESYS")
    parser.add_argument('-s','--server-name', action='store',
                         default="neMESYS", help='start SiLA server with [server-name]' )
    parser.add_argument('-t','--server-type', action='store',
                         default="TestServer", help='start SiLA server with [server-type]' )
    parser.add_argument('-d','--description', action='store',
                         default="This is a test service for neMESYS syringe pumps via SiLA2", help='SiLA server description' )
    parser.add_argument('-v','--version', action='version', version='%(prog)s ' + __version__)
    return parser.parse_args()


if __name__ == '__main__':
    """Main: """
    logging.basicConfig(format='%(levelname)s| %(module)s.%(funcName)s: %(message)s', level=logging.DEBUG)
    #~ logging.basicConfig(format='%(levelname)s| %(module)s.%(funcName)s: %(message)s', level=logging.ERROR)

    parsed_args = parseCommandLine()

    if parsed_args.server_name :
        # mv to class
        logging.info("starting SiLA2 server with server name: {server_name}".format(server_name=parsed_args.server_name))

        # generate SiLAserver
        sila_server = neMESYSServer(parsed_args=parsed_args )

