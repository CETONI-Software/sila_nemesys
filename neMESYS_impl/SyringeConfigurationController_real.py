"""
________________________________________________________________________

:PROJECT: SiLA2_python

*syringeconfigurationcontroller_server_real *

:details: syringeconfigurationcontroller_server_real:
            Syringe pump specific functions for configuration.
    .

:file:    syringeconfigurationcontroller_server_real.py
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

import sila2lib.sila_error_handling as sila_error

# importing protobuf and gRPC handler/stubs
import sila2lib.SiLAFramework_pb2 as fwpb2
import SyringeConfigurationController_pb2 as pb2
import SyringeConfigurationController_pb2_grpc as pb2_grpc

# import qmixsdk
from qmixsdk import qmixbus
from qmixsdk import qmixpump

class SyringeConfigurationControllerReal():
    """ SyringeConfigurationControllerReal -
#            Syringe pump specific functions for configuration.
#     """
    def __init__(self, pump):
        """ SyringeConfigurationControllerReal class initialiser """
        logging.debug("init class: SyringeConfigurationControllerReal ")

        self.pump = pump


    def SetSyringeParameters(self, request, context):
        """
            Set syringe parameters.
            If you change the syringe in one device, you need to setup the new syringe parameters to get proper conversion of flow rate und volume units.

            :param request: gRPC request
            :param context: gRPC context
            :param request.InnerDiameter: Inner diameter of the syringe tube in millimetres.
            :param request.MaxPistonStroke: The maximum piston stroke defines the maximum position the piston can be moved to before it slips out of the syringe tube. The maximum piston stroke limits the maximum travel range of the syringe pump pusher.
        """
        logging.debug("SetSyringeParameters - Mode: real ")

        def check_less_than_zero(param, param_str: str):
            """
            Checks if the given param is less than zero. If this is the case,
            an appropriate validation error is raised indicating to the client
            which parameter should be adjusted.

            :param param: The parameter to check against zero
            :param param_str: A string description of the given param
            """
            if param < 0:
                sila_error.raiseRPCError(context, sila_error.getValidationError(
                    param_str,
                    cause="The " + param_str + " cannot be less than 0",
                    action="Adjust the " + param_str + " to be greater than 0."
                ))

        requested_inner_diameter = request.InnerDiameter.value
        check_less_than_zero(requested_inner_diameter, "InnerDiameter")
        requested_piston_stroke = request.MaxPistonStroke.value
        check_less_than_zero(requested_piston_stroke, "MaxPistonStroke")

        try:
            self.pump.set_syringe_param(requested_inner_diameter, requested_piston_stroke)
        except qmixbus.DeviceError as err:
            logging.error("QmixSDK error: %s", err)
            # sila_error.raiseRPCError(context, sila_error.getStandardExecutionError())
        else:
            return pb2.SetSyringeParameters_Responses()

    def Subscribe_InnerDiameter(self, request, context):
        """Inner diameter of the syringe tube in millimetres.
            :param request: gRPC request
            :param context: gRPC context
            :param response.InnerDiameter: Inner diameter of the syringe tube in millimetres.
        """
        logging.debug("Subscribe_InnerDiameter - Mode: real ")

        while True:
            yield pb2.Subscribe_InnerDiameter_Responses(InnerDiameter=fwpb2.Real(
                value=self.pump.get_syringe_param().inner_diameter_mm
            ))

            # we add a small delay to give the client a chance to keep up.
            time.sleep(0.5)

    def Subscribe_MaxPistonStroke(self, request, context):
        """The maximum piston stroke defines the maximum position the piston can be moved to before it slips out of the syringe tube. The maximum piston stroke limits the maximum travel range of the syringe pump pusher.
            :param request: gRPC request
            :param context: gRPC context
            :param response.MaxPistonStroke: The maximum piston stroke defines the maximum position the piston can be moved to before it slips out of the syringe tube. The maximum piston stroke limits the maximum travel range of the syringe pump pusher.
        """
        logging.debug("Subscribe_MaxPistonStroke - Mode: real ")

        while True:
            yield pb2.Subscribe_MaxPistonStroke_Responses(MaxPistonStroke=fwpb2.Real(
                value=self.pump.get_syringe_param().max_piston_stroke_mm
            ))

            # we add a small delay to give the client a chance to keep up.
            time.sleep(0.5)




