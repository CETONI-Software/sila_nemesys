# This file contains default values that are used for the implementations to supply them with 
#   working, albeit mostly useless arguments.
#   You can also use this file as an example to create your custom responses. Feel free to remove
#   Once you have replaced every occurrence of the defaults with more reasonable values.
#   Or you continue using this file, supplying good defaults..

# import the required packages
import sila2lib.SiLAFramework_pb2 as fwpb2
from .gRPC import PumpFluidDosingService_pb2 as pb2

# initialise the default dictionary so we can add keys. 
#   We need to do this separately/add keys separately, so we can access keys already defined e.g.
#   for the use in data type identifiers
default_dict = dict()


default_dict['SetFillLevel_Parameters'] = {
    'FillLevel': fwpb2.Real(value=0.0),
    'FlowRate': fwpb2.Real(value=0.0)
}

default_dict['SetFillLevel_Responses'] = {
    'Success': fwpb2.Boolean(value=False)
}

default_dict['DoseVolume_Parameters'] = {
    'Volume': fwpb2.Real(value=0.0),
    'FlowRate': fwpb2.Real(value=0.0)
}

default_dict['DoseVolume_Responses'] = {
    'Success': fwpb2.Boolean(value=False)
}

default_dict['GenerateFlow_Parameters'] = {
    'FlowRate': fwpb2.Real(value=0.0)
}

default_dict['GenerateFlow_Responses'] = {
    'Success': fwpb2.Boolean(value=False)
}

default_dict['StopDosage_Parameters'] = {
    
}

default_dict['StopDosage_Responses'] = {
    'Success': fwpb2.Boolean(value=False)
}

default_dict['Subscribe_MaxSyringeFillLevel_Responses'] = {
    'MaxSyringeFillLevel': fwpb2.Real(value=0.0)
}

default_dict['Subscribe_SyringeFillLevel_Responses'] = {
    'SyringeFillLevel': fwpb2.Real(value=0.0)
}

default_dict['Subscribe_MaxFlowRate_Responses'] = {
    'MaxFlowRate': fwpb2.Real(value=0.0)
}

default_dict['Subscribe_FlowRate_Responses'] = {
    'FlowRate': fwpb2.Real(value=0.0)
}
