"""
________________________________________________________________________

:PROJECT: SiLA2_python

*syringeconfigurationcontroller_server_simulation *

:details: syringeconfigurationcontroller_server_simulation: 
            Syringe pump specific functions for configuration.
    . 
           
:file:    syringeconfigurationcontroller_server_simulation.py
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
import SyringeConfigurationController_pb2 as pb2
import SyringeConfigurationController_pb2_grpc as pb2_grpc


class SyringeConfigurationControllerSimulation():
    """ SyringeConfigurationControllerSimulation - 
#            Syringe pump specific functions for configuration.
#     """
    def __init__ (self):
        """ SyringeConfigurationControllerSimulation class initialiser """
        logging.debug("init class: SyringeConfigurationControllerSimulation ")



    def SetSyringeParameters(self, request, context):
        """
            Set syringe parameters.
            If you change the syringe in one device, you need to setup the new syringe parameters to get proper conversion of flow rate und volume units.
        
            :param request: gRPC request
            :param context: gRPC context
            :param request.InnerDiameter: Inner diameter of the syringe tube in millimetres.
            :param request.MaxPistonStroke: The maximum piston stroke defines the maximum position the piston can be moved to before it slips out of the syringe tube. The maximum piston stroke limits the maximum travel range of the syringe pump pusher.

        """
        logging.debug("SetSyringeParameters - Mode: simulation ")

        #~ return_val = request.InnerDiameter.value
        #~ return pb2.SetSyringeParameters_Responses()

    def Subscribe_InnerDiameter(self, request, context):
        """Inner diameter of the syringe tube in millimetres.
            :param request: gRPC request
            :param context: gRPC context
            :param response.InnerDiameter: Inner diameter of the syringe tube in millimetres.

        """
        logging.debug("Subscribe_InnerDiameter - Mode: simulation ")

        #~ yield_val = request.InnerDiameter.value
        #~ pb2.Subscribe_InnerDiameter_Responses( InnerDiameter=fwpb2.Real(value=0.0) )

    def Subscribe_MaxPistonStroke(self, request, context):
        """The maximum piston stroke defines the maximum position the piston can be moved to before it slips out of the syringe tube. The maximum piston stroke limits the maximum travel range of the syringe pump pusher.
            :param request: gRPC request
            :param context: gRPC context
            :param response.MaxPistonStroke: The maximum piston stroke defines the maximum position the piston can be moved to before it slips out of the syringe tube. The maximum piston stroke limits the maximum travel range of the syringe pump pusher.

        """
        logging.debug("Subscribe_MaxPistonStroke - Mode: simulation ")

        #~ yield_val = request.MaxPistonStroke.value
        #~ pb2.Subscribe_MaxPistonStroke_Responses( MaxPistonStroke=fwpb2.Real(value=0.0) )




