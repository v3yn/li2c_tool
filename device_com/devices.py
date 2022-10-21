from typing import Tuple  # type-checking

from pyftdi.ftdi import Ftdi
from pyftdi.serialext import serial_for_url
from serial import Serial

def get_device_port(device_url: str = "ftdi:///1") -> Serial:
    """
    Opens serial port on the FTDI device specified
    :param device_url: URL compliant to the PyFtdi URL scheme
        (default: access first available)
    :return: Serial object of open port
    """
    port = serial_for_url(device_url)
    return port


def list_devices() -> None:
    Ftdi.show_devices()
    Ftdi.list_devices()