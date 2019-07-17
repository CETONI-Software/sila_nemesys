import logging

from qmixsdk import qmixpump

class UnitConversionError(Exception):
    """Error-class for all unit-conversion errors.
    """

    def __init__(self, param, message):
        """
            :param param: the parameter of the unit that failed the conversion
            :param message: a description of what went wrong
        """
        super().__init__(message)
        logging.error(message)
        self.param = param
        self.message = message

    @property
    def param(self):
        """the parameter of the unit that failed the conversion
        """
        return self.__param

    @param.setter
    def param(self, param):
        self.__param = param

    @property
    def message(self):
        """a description of what went wrong
        """
        return self.__message

    @message.setter
    def message(self, message):
        self.__message = message


def evaluate_units(requested_volume_unit, requested_time_unit=None):
    """
    Converts the given volume and time unit from strings to qmixpump units
    and returns a 2-tuple or a 3-tuple (if a time unit is provided).
    :param requested_volume_unit: the volume unit to convert to a string
    :param requested_time_unit: the time unit to convert to a string
    """
    prefix_string = requested_volume_unit[0] if len(requested_volume_unit) > 1 else " "
    volume_unit_string = requested_volume_unit[-1]

    prefix = evaluate_prefix(prefix_string)
    volume_unit = evaluate_volume_unit(volume_unit_string)

    if requested_time_unit:
        time_unit = evaluate_time_unit(requested_time_unit)

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
    prefix = switcher.get(prefix_string)
    if not prefix:
        raise UnitConversionError("prefix", f"Wrong prefix: '{prefix_string}' not supported")

    return prefix

def evaluate_volume_unit(volume_unit_string):
    """ Converts a given volume_unit_string to a qmixpump.VolumeUnit
    """
    if volume_unit_string == "l":
        return qmixpump.VolumeUnit.litres

    raise UnitConversionError("volume_unit", f"Wrong volume unit: '{volume_unit_string}' not supported")

def evaluate_time_unit(time_unit_string):
    """Converts a given time_unit_string into a qmixpump.TimeUnit
    """
    switcher = {
        "s"  : qmixpump.TimeUnit.per_second,
        "min": qmixpump.TimeUnit.per_minute,
        "h"  : qmixpump.TimeUnit.per_hour
    }

    time_unit = switcher.get(time_unit_string)
    if not time_unit:
        raise UnitConversionError("time_unit", f"Wrong time_unit: '{time_unit_string}' not supported")

    return time_unit

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
