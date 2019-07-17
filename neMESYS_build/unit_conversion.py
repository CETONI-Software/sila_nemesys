import logging

import sila2lib.SiLAFramework_pb2 as fwpb2

from qmixsdk import qmixpump

class UnitConversionError(Exception):
    """Error-class for all unit-conversion errors.
    """


def evaluate_units(requested_volume_unit, requested_time_unit=None):
    """
    Converts the given volume and time unit from strings to qmixpump units
    and returns a 2-tuple or a 3-tuple (if a time unit is provided).
    """
    prefix_string = requested_volume_unit[0] if len(requested_volume_unit) > 1 else " "
    volume_unit_string = requested_volume_unit[-1]

    prefix = evaluate_prefix(prefix_string)
    if isinstance(prefix, fwpb2.SiLAError):
        logging.error("Wrong prefix: '%s' not supported", prefix_string)
        raise UnitConversionError(prefix) # raise the error, if there was one

    volume_unit = evaluate_volume_unit(volume_unit_string)
    if isinstance(volume_unit, fwpb2.SiLAError):
        logging.error("Wrong volume unit: '%s' not supported", volume_unit_string)
        raise UnitConversionError(volume_unit) # raise the error, if there was one

    if requested_time_unit:
        time_unit = evaluate_time_unit(requested_time_unit)
        if isinstance(time_unit, fwpb2.SiLAError):
            logging.error("Wrong time unit: '%s' not supported", requested_time_unit)
            raise UnitConversionError(time_unit) # raise the error, if there was one

        return (prefix, volume_unit, time_unit)

    return (prefix, volume_unit)


def evaluate_prefix(prefix_string):
    """Converts the given prefix_string to a qmixpump.UnitPrefix
    """
    switcher = {
        " ": qmixpump.UnitPrefix.unit,
        "d": qmixpump.UnitPrefix.deci,
        "c": qmixpump.UnitPrefix.centi,
        "m": qmixpump.UnitPrefix.milli,
        "µ": qmixpump.UnitPrefix.micro
    }
    error = fwpb2.SiLAError(validationError=fwpb2.ValidationError(
        parameter="Prefix",
        cause="The given prefix is not supported!"
    ))
    return switcher.get(prefix_string, error)

def evaluate_volume_unit(volume_unit_string):
    """ Converts a given volume_unit_string to a qmixpump.VolumeUnit
    """
    if volume_unit_string == "l":
        return qmixpump.VolumeUnit.litres

    return fwpb2.SiLAError(validationError=fwpb2.ValidationError(
        parameter="VolumeUnit",
        cause="The given volume unit is not supported!"
    ))

def evaluate_time_unit(time_unit_string):
    """Converts a given time_unit_string into a qmixpump.TimeUnit
    """
    switcher = {
        "s"  : qmixpump.TimeUnit.per_second,
        "min": qmixpump.TimeUnit.per_minute,
        "h"  : qmixpump.TimeUnit.per_hour
    }
    error = fwpb2.SiLAError(validationError=fwpb2.ValidationError(
        parameter="TimeUnit",
        cause="The given time unit is not supported!"
    ))
    return switcher.get(time_unit_string, error)

def prefix_to_string(prefix):
    """Converts a given prefix to a human readable string
        :param prefix: qmixpump.UnitPrefix
    """
    switcher = {
        qmixpump.UnitPrefix.deci : "d",
        qmixpump.UnitPrefix.centi: "c",
        qmixpump.UnitPrefix.milli: "m",
        qmixpump.UnitPrefix.micro: "µ"
    } # default = no prefix
    return switcher.get(prefix, "")

def time_unit_to_string(time_unit):
    """Converts a given time_unit to a human readable string
        :param time_unit: qmixpump.TimeUnit
    """
    switcher = {
        qmixpump.TimeUnit.per_hour  : "h",
        qmixpump.TimeUnit.per_minute: "min"
    } # default = "per_second"
    return switcher.get(time_unit, "s")
