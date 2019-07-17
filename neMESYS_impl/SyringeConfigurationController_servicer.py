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


class SyringeConfigurationController(pb2_grpc.SyringeConfigurationControllerServicer):
    """ SyringeConfigurationController -
#            Syringe pump specific functions for configuration.
#     """
    def __init__ (self):
        """ SyringeConfigurationController class initialiser """
        logging.debug("init class: SyringeConfigurationController ")

        # if self.implementation is set to None, it will use
        # the fallback simulation mode as default
        # if required, one could also create a simulation module and set this to the default implementation, like:
        #~ self.injectImplementation(GreetingProviderSimulation())

        self.implementation = None # this corresponds to the simple, fallback simulation mode

    # dependency injection - setter injection s. https://en.wikipedia.org/wiki/Dependency_injection
    def injectImplementation(self, implementation):
        self.implementation = implementation

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

        if self.implementation is not None:
            return self.implementation.SetSyringeParameters(request, context)
        else:
            pass #~ return_val = request.InnerDiameter.value
            #~ return pb2.SetSyringeParameters_Responses(  )

    def Subscribe_InnerDiameter(self, request, context):
        """Inner diameter of the syringe tube in millimetres.
            :param request: gRPC request
            :param context: gRPC context
            :param response.InnerDiameter: Inner diameter of the syringe tube in millimetres.
        """
        logging.debug("Subscribe_InnerDiameter - Mode: simulation ")

        if self.implementation is not None:
            return self.implementation.Subscribe_InnerDiameter(request, context)
        else:
            #~ yield_val = request.InnerDiameter.value
            pass #~ yield pb2.Subscribe_InnerDiameter_Responses( InnerDiameter=fwpb2.Real(value=0.0) )

    def Subscribe_MaxPistonStroke(self, request, context):
        """The maximum piston stroke defines the maximum position the piston can be moved to before it slips out of the syringe tube. The maximum piston stroke limits the maximum travel range of the syringe pump pusher.
            :param request: gRPC request
            :param context: gRPC context
            :param response.MaxPistonStroke: The maximum piston stroke defines the maximum position the piston can be moved to before it slips out of the syringe tube. The maximum piston stroke limits the maximum travel range of the syringe pump pusher.
        """
        logging.debug("Subscribe_MaxPistonStroke - Mode: simulation ")

        if self.implementation is not None:
            return self.implementation.Subscribe_MaxPistonStroke(request, context)
        else:
            #~ yield_val = request.MaxPistonStroke.value
            pass #~ yield pb2.Subscribe_MaxPistonStroke_Responses( MaxPistonStroke=fwpb2.Real(value=0.0) )




