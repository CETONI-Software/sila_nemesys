# PumpFluidDosingService
Allows to dose a fluid by a given amount of volume or a given flow rate. There are commands for absolute dosing ([`SetFillLevel`](#SetFillLevel)) and relative dosing ([`DoseVolume`](#DoseVolume) and [`GenerateFlow`](#GenerateFlow)) available.

The flow rate can be negative. In this case the pump aspirates the fluid instead of dispensing. The flow rate has to be a value between [`MaxFlowRate`](#Properties) and [`MinFlowRate`](#Properties). If the value is not within this range (hence is invalid) a ValidationError will be thrown.  
At any time the property [`SyringeFillLevel`](#Properties) can be queried to see how much fluid is left in the syringe.
Similarly the property [`FlowRate`](#Properties) can be queried to get the current flow rate at which the pump is dosing.

## Commands
### `SetFillLevel`
Pumps fluid with the given flow rate until the requested fill level is reached. Depending on the requested fill level given in the `FillLevel` parameter this function may cause aspiration or dispension of fluid.

Parameters:
- `FillLevel`: The requested fill level. A level of 0 indicates a completely empty syringe. The value has to be between 0 and [`MaxSyringeFillLevel`](#Properties) or else a ValidationError will be thrown.
- `FlowRate`: The flow rate at which the pump should dose the fluid. This value can be negative. In that case the pump aspirates the fluid.

Response:
- `Success`: A boolean value where `false` means that the dosage failed and `true` meaning the dosage was finished properly.

observable: yes

### `DoseVolume`
Dose a certain amount of volume with the given flow rate.  

Parameters:
- `Volume`: The amount of volume to dose.
- `FlowRate`: The flow rate at which the pump should dose the fluid. This value can be negative. In that case the pump aspirates the fluid.

Response:
- `Success`: A boolean value where `false` means that the dosage failed and `true` meaning the dosage was finished properly.

observable: yes

### `GenerateFlow`
Generate a continous flow with the given flow rate. Dosing continues until it gets stopped manually by calling [`StopDosage`](#StopDosage) or until the pusher reached one of its limits.

Parameters:
- `FlowRate`: The flow rate at which the pump should dose the fluid. This value can be negative. In that case the pump aspirates the fluid.

Response:
- `Success`: A boolean value where `false` means that the dosage failed and `true` meaning the dosage was finished properly.

observable: yes

### `StopDosage`
Stops a currently running dosage immediately. 

Parameters:
- none

Response:
- `Success`: A boolean value where `false` means that stopping the dosage failed and `true` meaning the dosage was stopped properly.

observable: no

## Properties
- `MaxSyringeFillLevel`: The maximum amount of fluid that the syringe can hold.
    * observable: no
- `SyringeFillLevel`: The current amount of fluid left in the syringe.
    * observable: yes
- `MaxFlowRate`: The maximum value of the flow rate at which this pump can dose a fluid.
    * observable: no
- `MinFlowRate`: The minimum value of the flow rate at which this pump can dose a fluid.
    * observable: no
- `FlowRate`: The current value of the flow rate. It is 0 if the pump does not dose any fluid.
    * observable: yes

## Errors
### DefinedExecutionErrors
- `DosageFinishedUnexpectedly`: The dosage could not be finished properly due to an error.

### UndefinedExecutionErrors
- none





# PumpUnitController
Allows to control the currently used units for passing and retrieving flow rates and volumes to and from a pump.

## Commands
### `SetFlowUnit`
Sets the flow unit for the pump.
The flow unit defines the unit to be used for all flow values passed to or retrieved from the pump.

Parameters:
- `Prefix`: The prefix for the velocity unit.
- `VolumeUnit`: The volume unit (numerator) of the velocity unit.
- `TimeUnit`: The time unit (denominator) of the velocity unit.

Response:
- none

observable: no

### `SetVolumeUnit`
Sets the default volume unit.
The volume unit defines the unit to be used for all volume values passed to or retrieved from the pump.

Parameters:
- `Prefix`: The prefix of the SI unit.
- `VolumeUnit`: The volume unit identifier.

Response:
- none

observable: no

## Properties
- `FlowUnit`: The currently used flow unit.
    * observable: yes
- `VolumeUnit`: The currently used volume unit.
    * observable: yes

## Errors
### DefinedExecutionErrors
- none

### UndefinedExecutionErrors
- none

# PumpInitialisationService
Allows to initialise a pump by either executing a complete initialisation or by simply setting the pump's drive position counter. 
`InitialisePumpDrive` is mandatory if the last value of the drive position counter cannot be provided.
Clients can query the [`DrivePositionCounter`](#Properties-1) property to provide this at the next initialisation and then use [`RestoreDrivePositionCounter`](#RestoreDrivePositionCounter).  
The initialisation has to be successful in order for the pump to work correctly and dose fluids. If the initialisation fails, the DefinedExecutionError [`InitialisationFailed`](#DefinedExecutionErrors-1) is thrown.

## Commands
### `InitialisePumpDrive`
Initialize the pump drive (e.g. by executing a reference move).

Parameters:
- none

Response:
- `Success`: A boolean value where `false` represents a failed initialisation and `true` represents a successful initialisation.

observable: no

### `RestoreDrivePositionCounter`
Restore the internal hardware position counter value of the pump drive.  
In many drives the actual position value is counted by a quadrature decoder.
This internal position counter value will get lost, as soon as the device is switched off.
In order to restore this position counter value after power on, a client can query the internal position counter value ([`DrivePositionCounter`](#Properties-1)), store it persistently into a configuration file and restore it later by calling this function.

Parameters:
- `DrivePositionCounter`: The drive position counter to restore.

Response:
- `Success`: A boolean value where `false` represents a failed initialisation and `true` represents a successful initialisation.

observable: no

## Properties
- `DrivePositionCounter`: The value of the internal drive position counter.
    * observable: yes

## Errors
### DefinedExecutionErrors
- `InitialisationFailed`: The initialisation did not end properly.

### UndefinedExecutionErrors
- none


# ValvePositionController
Allows to specify a certain logical position for a valve. The [`CurrentPosition`](#Properties-2) property can be querried at any time to obtain the current valve position.  

## Commands
### `SwitchToPosition`
Switches the valve to the specified position. The given position has to be less than the [`NumberOfPositions`](#NumberOfPositions) or else a ValidationError will be thrown.

Parameters:
- `Position`: The target position that the valve should be switched to.

Response:
- `Success`: A boolean value where `false` represents a failed command execution and `true` represents a successful command execution.

observable: no

### `TooglePosition`
This command only applies for 2-way valves to toggle between its two different positions. If the command is called for any other valve type a `ValveNotToggleable` error is thrown.

Parameters:
- none

Response:
- `Success`: A boolean value where `false` represents a failed command execution and `true` represents a successful command execution.

observable: no

## Properties
- `NumberOfPositions`: The number of valve positions available.
    * observable: no
- `CurrentPosition`: The current logic valve position. This is a value between 0 and `NumberOfPositions` - 1.
    * observable: yes

## Errors
### DefinedExecutionErrors
- `ValveNotToggleable`: The current valve does not support toggling because it has more than only two possible positions.

### UndefinedExecutionErrors
- none

