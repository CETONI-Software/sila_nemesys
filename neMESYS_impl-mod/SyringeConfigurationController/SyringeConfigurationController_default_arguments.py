# This file contains default values that are used for the implementations to supply them with 
#   working, albeit mostly useless arguments.
#   You can also use this file as an example to create your custom responses. Feel free to remove
#   Once you have replaced every occurrence of the defaults with more reasonable values.
#   Or you continue using this file, supplying good defaults..

# import the required packages
import sila2lib.SiLAFramework_pb2 as fwpb2
from .gRPC import SyringeConfigurationController_pb2 as pb2

# initialise the default dictionary so we can add keys. 
#   We need to do this separately/add keys separately, so we can access keys already defined e.g.
#   for the use in data type identifiers
default_dict = dict()


default_dict['SetSyringeParameters_Parameters'] = {
    'InnerDiameter': fwpb2.Real(value=0.0),
    'MaxPistonStroke': fwpb2.Real(value=0.0)
}

default_dict['SetSyringeParameters_Responses'] = {
    
}

default_dict['Subscribe_InnerDiameter_Responses'] = {
    'InnerDiameter': fwpb2.Real(value=0.0)
}

default_dict['Subscribe_MaxPistonStroke_Responses'] = {
    'MaxPistonStroke': fwpb2.Real(value=0.0)
}
