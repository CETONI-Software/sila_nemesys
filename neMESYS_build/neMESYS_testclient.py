#!/usr/bin/env python3
"""
________________________________________________________________________

:PROJECT: SiLA2_python

*neMESYS client *

:details: neMESYS client: This is a test service for neMESYS syringe pumps via SiLA2. 
           
:file:    neMESYS_client.py
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
import time

import grpc

import sila2lib.sila_client as s2client
from sila2lib.sila_service_detection import SiLA2ServiceDetection

from sila2lib import SiLAFramework_pb2 as fwpb2
from sila2lib.std_features import SiLAService_pb2 as spb2
from sila2lib.std_features import SiLAService_pb2_grpc as spb2g
from sila2lib.std_features import SimulationController_pb2 as scpb2
from sila2lib.std_features import SimulationController_pb2_grpc as scpb2g

import PumpFluidDosingService_pb2
import PumpFluidDosingService_pb2_grpc
import PumpUnitController_pb2
import PumpUnitController_pb2_grpc
import PumpInitialisationService_pb2
import PumpInitialisationService_pb2_grpc
import ValvePositionController_pb2
import ValvePositionController_pb2_grpc


class neMESYSClient(s2client.SiLA2Client):
    """ Class doc """
    def __init__ (self, name="neMESYSClient", service_name=None, sila_hostname="localhost", 
                  description="Description: This is a SiLA2 test client",
                  UUID = None, version="0.0", vendor_URL="lara.uni-greifswald.de",
                  ip='127.0.0.1', port=50051, key=None, cert=None):
        super().__init__(name=name,
                        service_name=service_name,
                        description=description,
                        UUID = UUID,
                        version=version,
                        sila_hostname=sila_hostname,
                        vendor_URL=vendor_URL,
                        ip=ip, port=port, 
                        key=key, cert=cert)
        
        """ Class initialiser 
            param cert=None: server certificate filename, e.g. 'sila_server.crt'  """
                
        self.PumpFluidDosingService_serv_stub = PumpFluidDosingService_pb2_grpc.PumpFluidDosingServiceStub(self.channel)
        self.PumpUnitController_serv_stub = PumpUnitController_pb2_grpc.PumpUnitControllerStub(self.channel)
        self.PumpInitialisationService_serv_stub = PumpInitialisationService_pb2_grpc.PumpInitialisationServiceStub(self.channel)
        self.ValvePositionController_serv_stub = ValvePositionController_pb2_grpc.ValvePositionControllerStub(self.channel)

    
    def run(self):
        try:
            print("SiLA client / client neMESYS -------- commands ------------")
            
            # --> put your remote calls here, e.g. (this is really only an example, please use the your corresponding calls)
            
            # calling SiLAService
            response = self.SiLAService_serv_stub.Get_ImplementedFeatures(spb2.ImplementedFeatures_Parameters() )
            for feature_id in response.ImplementedFeatures :
                logging.debug("implemented feature:{}".format(feature_id.FeatureIdentifier.value) )
            
            try:
                response = self.SiLAService_serv_stub.GetFeatureDefinition( 
                                spb2.GetFeatureDefinition_Parameters(
                                   QualifiedFeatureIdentifier=spb2.DataType_FeatureIdentifier(FeatureIdentifier=fwpb2.String(value="SiLAService") )) )
                logging.debug("get feat def-response:{}".format(response) )
            except grpc.RpcError as err:
                logging.debug("grpc/SiLA error: {}".format(err) )
            
            try: 
                response = self.SiLAService_serv_stub.GetFeatureDefinition( 
                                spb2.GetFeatureDefinition_Parameters(
                                    QualifiedFeatureIdentifier=spb2.DataType_FeatureIdentifier(FeatureIdentifier=fwpb2.String(value="NoFeature") )) )
                logging.debug("get feat def-response:{}".format(response) )
            except grpc.RpcError as err:
                logging.debug("grpc/SiLA error: {}".format(err) )
            
            response = self.SiLAService_serv_stub.Get_ServerName(spb2.ServerName_Parameters() )
            logging.debug("display name:{}".format(response.ServerName.value) )
            
            response = self.SiLAService_serv_stub.Get_ServerDescription(spb2.ServerDescription_Parameters())
            logging.debug("description:{}".format(response.ServerDescription.value) )
            
            response = self.SiLAService_serv_stub.Get_ServerVersion(spb2.ServerVersion_Parameters())
            logging.debug("version:{}".format(response.ServerVersion.value) )
            
            # testing commands --------------
            
            # --> calling PumpFluidDosingService
            try :
                pass #~ response = self.PumpFluidDosingService_serv_stub.SetFillLevel(PumpFluidDosingService_pb2.SetFillLevel_Parameters(FillLevel=fwpb2.Real(value=0.0)))
                #~ logging.debug("SetFillLevel response:{}".format(response.Success) )
            except grpc.RpcError as err:
                logging.error("grpc/SiLA error: {}".format(err) )
            try :
                pass #~ response = self.PumpFluidDosingService_serv_stub.DoseVolume(PumpFluidDosingService_pb2.DoseVolume_Parameters(Volume=fwpb2.Real(value=0.0)))
                #~ logging.debug("DoseVolume response:{}".format(response.Success) )
            except grpc.RpcError as err:
                logging.error("grpc/SiLA error: {}".format(err) )
            try :
                pass #~ response = self.PumpFluidDosingService_serv_stub.GenerateFlow(PumpFluidDosingService_pb2.GenerateFlow_Parameters(FlowRate=fwpb2.Real(value=0.0)))
                #~ logging.debug("GenerateFlow response:{}".format(response.Success) )
            except grpc.RpcError as err:
                logging.error("grpc/SiLA error: {}".format(err) )
            try :
                pass #~ response = self.PumpFluidDosingService_serv_stub.StopDosage(PumpFluidDosingService_pb2.StopDosage_Parameters())
                #~ logging.debug("StopDosage response:{}".format(response.Success) )
            except grpc.RpcError as err:
                logging.error("grpc/SiLA error: {}".format(err) )
            # --> calling PumpUnitController
            try :
                pass #~ response = self.PumpUnitController_serv_stub.SetFlowUnit(PumpUnitController_pb2.SetFlowUnit_Parameters(Prefix=fwpb2.String(value="DEFAULTstring" + return_val)))
                #~ logging.debug("SetFlowUnit response:{}".format(response.Void) )
            except grpc.RpcError as err:
                logging.error("grpc/SiLA error: {}".format(err) )
            try :
                pass #~ response = self.PumpUnitController_serv_stub.SetVolumeUnit(PumpUnitController_pb2.SetVolumeUnit_Parameters(Prefix=fwpb2.String(value="DEFAULTstring" + return_val)))
                #~ logging.debug("SetVolumeUnit response:{}".format(response.Void) )
            except grpc.RpcError as err:
                logging.error("grpc/SiLA error: {}".format(err) )
            # --> calling PumpInitialisationService
            try :
                pass #~ response = self.PumpInitialisationService_serv_stub.InitializePumpDrive(PumpInitialisationService_pb2.InitializePumpDrive_Parameters())
                #~ logging.debug("InitializePumpDrive response:{}".format(response.Success) )
            except grpc.RpcError as err:
                logging.error("grpc/SiLA error: {}".format(err) )
            try :
                pass #~ response = self.PumpInitialisationService_serv_stub.RestoreDrivePositionCounter(PumpInitialisationService_pb2.RestoreDrivePositionCounter_Parameters(DrivePositionCounter=fwpb2.Integer(value=0)))
                #~ logging.debug("RestoreDrivePositionCounter response:{}".format(response.Success) )
            except grpc.RpcError as err:
                logging.error("grpc/SiLA error: {}".format(err) )
            # --> calling ValvePositionController
            try :
                pass #~ response = self.ValvePositionController_serv_stub.SwitchToPosition(ValvePositionController_pb2.SwitchToPosition_Parameters(Position=fwpb2.Integer(value=0)))
                #~ logging.debug("SwitchToPosition response:{}".format(response.Success) )
            except grpc.RpcError as err:
                logging.error("grpc/SiLA error: {}".format(err) )
            try :
                pass #~ response = self.ValvePositionController_serv_stub.TogglePosition(ValvePositionController_pb2.TogglePosition_Parameters())
                #~ logging.debug("TogglePosition response:{}".format(response.Success) )
            except grpc.RpcError as err:
                logging.error("grpc/SiLA error: {}".format(err) )


            # testing properties ------------
            
            try :
                response = self.PumpFluidDosingService_serv_stub.Get_MaxSyringeFillLevel(PumpFluidDosingService_pb2.Get_MaxSyringeFillLevel_Parameters())
                #~ logging.debug("Get_MaxSyringeFillLevel response:{}".format(response.MaxSyringeFillLevel) )
            except grpc.RpcError as err:
                logging.error("grpc/SiLA error: {}".format(err) )
            try :
                response = next(self.PumpFluidDosingService_serv_stub.Subscribe_SyringeFillLevel(PumpFluidDosingService_pb2.Subscribe_SyringeFillLevel_Parameters()))
                #~ logging.debug("Subscribe_SyringeFillLevel response:{}".format(response.SyringeFillLevel) )
            except grpc.RpcError as err:
                logging.error("grpc/SiLA error: {}".format(err) )
            try :
                response = self.PumpFluidDosingService_serv_stub.Get_MaxFlowRate(PumpFluidDosingService_pb2.Get_MaxFlowRate_Parameters())
                #~ logging.debug("Get_MaxFlowRate response:{}".format(response.MaxFlowRate) )
            except grpc.RpcError as err:
                logging.error("grpc/SiLA error: {}".format(err) )
            try :
                response = next(self.PumpFluidDosingService_serv_stub.Subscribe_FlowRate(PumpFluidDosingService_pb2.Subscribe_FlowRate_Parameters()))
                #~ logging.debug("Subscribe_FlowRate response:{}".format(response.FlowRate) )
            except grpc.RpcError as err:
                logging.error("grpc/SiLA error: {}".format(err) )
            try :
                response = next(self.PumpUnitController_serv_stub.Subscribe_FlowUnit(PumpUnitController_pb2.Subscribe_FlowUnit_Parameters()))
                #~ logging.debug("Subscribe_FlowUnit response:{}".format(response.FlowUnit) )
            except grpc.RpcError as err:
                logging.error("grpc/SiLA error: {}".format(err) )
            try :
                response = next(self.PumpUnitController_serv_stub.Subscribe_VolumeUnit(PumpUnitController_pb2.Subscribe_VolumeUnit_Parameters()))
                #~ logging.debug("Subscribe_VolumeUnit response:{}".format(response.VolumeUnit) )
            except grpc.RpcError as err:
                logging.error("grpc/SiLA error: {}".format(err) )
            try :
                response = next(self.PumpInitialisationService_serv_stub.Subscribe_DrivePositionCounter(PumpInitialisationService_pb2.Subscribe_DrivePositionCounter_Parameters()))
                #~ logging.debug("Subscribe_DrivePositionCounter response:{}".format(response.DrivePositionCounter) )
            except grpc.RpcError as err:
                logging.error("grpc/SiLA error: {}".format(err) )
            try :
                response = self.ValvePositionController_serv_stub.Get_NumberOfPositions(ValvePositionController_pb2.Get_NumberOfPositions_Parameters())
                #~ logging.debug("Get_NumberOfPositions response:{}".format(response.NumberOfPositions) )
            except grpc.RpcError as err:
                logging.error("grpc/SiLA error: {}".format(err) )
            try :
                response = next(self.ValvePositionController_serv_stub.Subscribe_Position(ValvePositionController_pb2.Subscribe_Position_Parameters()))
                #~ logging.debug("Subscribe_Position response:{}".format(response.Position) )
            except grpc.RpcError as err:
                logging.error("grpc/SiLA error: {}".format(err) )

            
        except grpc._channel._Rendezvous as err :
            self.error_handler(err)

    def error_handler(self, errors):
        logging.error(errors._state)    

def parseCommandLine():
    """ just looking for command line arguments ...
       :param - : - """
    help = "SiLA2 service: neMESYS"
    parser = argparse.ArgumentParser(description="A SiLA2 client: neMESYS")
    parser.add_argument('-s','--server-name', action='store',
                         help='SiLA server to connect with [server-name]', default="neMESYS")
    parser.add_argument('-v','--version', action='version', version='%(prog)s ' + __version__)
    
    return parser.parse_args()
    
if __name__ == '__main__':
    """Main: """
    logging.basicConfig(format='%(levelname)s| %(module)s.%(funcName)s:%(message)s', level=logging.DEBUG)
    #~ logging.basicConfig(format='%(levelname)s|%(module)s.%(funcName)s:%(message)s', level=logging.ERROR)
    
    parsed_args = parseCommandLine()

    if parsed_args.server_name :
        # mv to class
        logging.info("starting SiLA2 client with service name: {servername}".format(servername=parsed_args.server_name))
        
        logging.info("starting SiLA2 client: neMESYS")
        sila_client = neMESYSClient(ip='127.0.0.1', port=50053 )
        sila_client.run()
