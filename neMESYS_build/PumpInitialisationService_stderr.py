"""
________________________________________________________________________

:PROJECT: SiLA2_python

*pumpinitialisationservice_server_real *

:details: pumpinitialisationservice_server_real: 
            Allows to initialise a pump by either executing a complete initialisation or by simply setting the pump's drive position counter. InitialisePumpDrive is mandatory if the last value of the drive position counter cannot be provided. Clients can query the DrivePositionCounter property to provide this at the next initialisation and then use RestoreDrivePositionCounter.
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




# Std Errors ... 
